#!/usr/bin/env python3
"""给 X 归档帖子打类型标签。不删除任何原料。

用法（在仓库根目录）：

    python3 tools/tag_x.py

读取各人 x-archive/raw 的原始 JSON（优先 raw/all_posts.json），
按 referenced_tweets / in_reply_to_user_id / 作者 id 判断类型，
写出 index/x-posts.csv，并更新各人 x-archive/index.md 中
<!-- BEGIN X TYPE TAGS --> 与 <!-- END X TYPE TAGS --> 之间的统计。
不改 raw、all.md、articles/，也不删除 other.md。

每条帖只打一个 post_type，优先级：
  retweet > article > long > quote > self-thread > reply > original

含义：
  original     本人独立帖（无引用 / 回复 / 转帖）
  article      X Article
  long         长帖（note_tweet / note_post）
  self-thread  回复自己的线程续帖
  reply        回复别人
  quote        引用帖（含引用并回复）
  retweet      转帖

定时更新收录新帖后也应再跑本脚本。
也可 import 后调用 classify_post() / is_main_material()。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

BJ = timezone(timedelta(hours=8))

REPO_ROOT = Path(__file__).resolve().parent.parent

# slug -> (仓内 x-archive 相对路径, X 用户名, 显示名, 本机原路径)
ARCHIVES = [
    {
        "slug": "poteto",
        "name": "土豆姐（lauren）",
        "username": "poteto",
        "repo_dir": "poteto/x-archive",
    },
    {
        "slug": "bbkirstry",
        "name": "小晚不在",
        "username": "bbkirstry",
        "repo_dir": "bbkirstry/x-archive",
    },
    {
        "slug": "gengdaj",
        "name": "逸尘",
        "username": "gengdaJ",
        "repo_dir": "gengdaj/x-archive",
    },
    {
        "slug": "liuxiaopai",
        "name": "刘小排",
        "username": "bourneliu66",
        "repo_dir": "liuxiaopai/x-archive",
    },
]

TYPE_ORDER = ("original", "article", "long", "self-thread", "reply", "quote", "retweet")
TYPE_LABEL_ZH = {
    "original": "独立原创",
    "article": "X Article",
    "long": "长帖",
    "self-thread": "自回复线程",
    "reply": "回复别人",
    "quote": "引用帖",
    "retweet": "转帖",
}

# 蒸馏时的粗分（打标签脚本本身不筛帖）
MAIN_TYPES = {"original", "article", "long", "self-thread"}
SECONDARY_TYPES = {"reply", "quote"}
SKIP_READ_TYPES = {"retweet"}

BEGIN = "<!-- BEGIN X TYPE TAGS -->"
END = "<!-- END X TYPE TAGS -->"


def parse_utc(s: str | None) -> datetime | None:
    if not s:
        return None
    s = s.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(s).astimezone(timezone.utc)
    except ValueError:
        return None


def bj_date(p: dict) -> str:
    dt = parse_utc(p.get("created_at"))
    if dt is None:
        return ""
    return dt.astimezone(BJ).strftime("%Y-%m-%d")


def refs(p: dict) -> list[dict]:
    return p.get("referenced_tweets") or p.get("referenced_posts") or []


def ref_types(p: dict) -> set[str]:
    return {r.get("type") for r in refs(p) if r.get("type")}


def is_article(p: dict) -> bool:
    if p.get("article_title"):
        return True
    art = p.get("article")
    return isinstance(art, dict) and bool(art.get("title") or art.get("plain_text"))


def note_text(p: dict) -> str:
    nt = p.get("note_tweet") or p.get("note_post") or {}
    if isinstance(nt, dict):
        return nt.get("text") or ""
    return ""


def is_long_post(p: dict) -> bool:
    return bool(note_text(p))


def is_self_reply(p: dict, user_id: str, by_id: dict[str, dict], inc_tweets: dict[str, dict]) -> bool:
    types = ref_types(p)
    if "replied_to" not in types:
        return False
    author = p.get("author_id") or user_id
    irt = p.get("in_reply_to_user_id")
    if irt:
        return irt == author
    for r in refs(p):
        if r.get("type") != "replied_to":
            continue
        parent = by_id.get(r.get("id")) or inc_tweets.get(r.get("id"))
        if not parent:
            continue
        paid = parent.get("author_id")
        if paid:
            return paid == author
    return False


def classify_post(
    p: dict,
    user_id: str = "",
    by_id: dict[str, dict] | None = None,
    inc_tweets: dict[str, dict] | None = None,
) -> str:
    """返回单一 post_type。优先级：retweet > article > long > quote > self-thread > reply > original。"""
    by_id = by_id or {}
    inc_tweets = inc_tweets or {}
    types = ref_types(p)
    if "retweeted" in types:
        return "retweet"
    if is_article(p):
        return "article"
    if is_long_post(p):
        return "long"
    if "quoted" in types:
        return "quote"
    if "replied_to" in types:
        if is_self_reply(p, user_id, by_id, inc_tweets):
            return "self-thread"
        return "reply"
    return "original"


def is_main_material(post_type: str) -> bool:
    return post_type in MAIN_TYPES


def is_secondary_material(post_type: str) -> bool:
    return post_type in SECONDARY_TYPES


def load_posts(raw_dir: Path) -> tuple[dict, list[dict], dict[str, dict]]:
    all_path = raw_dir / "all_posts.json"
    inc_tweets: dict[str, dict] = {}
    user: dict = {}
    posts: list[dict] = []

    if all_path.is_file():
        obj = json.loads(all_path.read_text(encoding="utf-8"))
        if isinstance(obj, dict):
            user = obj.get("user") or {}
            posts = list(obj.get("data") or [])
            inc = obj.get("includes") or {}
            for t in inc.get("tweets") or inc.get("posts") or []:
                if t.get("id"):
                    inc_tweets[t["id"]] = t
        elif isinstance(obj, list):
            posts = obj

    # 补 includes，并在没有 all_posts 时从分页组装
    by_id: dict[str, dict] = {p["id"]: p for p in posts if p.get("id")}
    for f in sorted(raw_dir.glob("*.json")):
        if f.name in {"user.json", "all_posts.json"}:
            continue
        try:
            obj = json.loads(f.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if not isinstance(obj, dict):
            continue
        inc = obj.get("includes") or {}
        for t in inc.get("tweets") or inc.get("posts") or []:
            if t.get("id"):
                inc_tweets[t["id"]] = t
        if not posts:
            for p in obj.get("data") or []:
                pid = p.get("id")
                if pid and pid not in by_id:
                    by_id[pid] = p
    if not posts:
        posts = list(by_id.values())
    if not user and (raw_dir / "user.json").is_file():
        user = json.loads((raw_dir / "user.json").read_text(encoding="utf-8"))
    return user, posts, inc_tweets


def extract_ids_from_md(text: str) -> set[str]:
    ids = set(re.findall(r"status/(\d{10,})", text))
    ids.update(re.findall(r"帖子 ID[：:]\s*(\d{10,})", text))
    return ids


def map_post_files(archive_dir: Path, repo_dir: str) -> dict[str, str]:
    """帖子 id -> 仓内相对路径。优先单篇 markdown，其次 other.md，最后 all.md。"""
    mapping: dict[str, str] = {}
    arts = archive_dir / "articles"
    if arts.is_dir():
        for p in sorted(arts.glob("*.md")):
            rel = f"{repo_dir}/articles/{p.name}"
            for pid in extract_ids_from_md(p.read_text(encoding="utf-8")):
                mapping.setdefault(pid, rel)
    other = archive_dir / "other.md"
    if other.is_file():
        rel = f"{repo_dir}/other.md"
        for pid in extract_ids_from_md(other.read_text(encoding="utf-8")):
            mapping.setdefault(pid, rel)
    all_md = archive_dir / "all.md"
    if all_md.is_file():
        rel = f"{repo_dir}/all.md"
        # all.md 可能含全部相关帖；未单独成篇的都落到这里
        default = rel
    else:
        default = repo_dir
    mapping["_default"] = default
    return mapping


def post_url(p: dict, username: str) -> str:
    return p.get("url") or f"https://x.com/{username}/status/{p['id']}"


def render_index_section(slug: str, username: str, counts: Counter, total: int) -> str:
    lines = [
        BEGIN,
        "",
        "## 类型标签",
        "",
        "原料全收，只打类型标签，不按类型删除（哆啦 2026-11-22 定）。",
        "由 `tools/tag_x.py` 生成；每条一个 `post_type`，优先级：retweet > article > long > quote > self-thread > reply > original。",
        "完整表见仓库根目录 [index/x-posts.csv](../../index/x-posts.csv)。",
        "",
        "蒸馏时：主料是原创（original、self-thread）和长文（article、long）；",
        "辅料是有方法或观点的回复（reply）和引用（quote），由 agy 按「有没有可执行方法」筛；",
        "纯寒暄和转帖（retweet）不读。",
        "",
        f"- 合计：{total}",
    ]
    for t in TYPE_ORDER:
        lines.append(f"- `{t}`（{TYPE_LABEL_ZH[t]}）：{counts.get(t, 0)}")
    lines += [
        f"- 主料（original + article + long + self-thread）：{sum(counts[t] for t in MAIN_TYPES)}",
        f"- 辅料候选（reply + quote）：{sum(counts[t] for t in SECONDARY_TYPES)}",
        f"- 蒸馏时默认不读（retweet）：{counts.get('retweet', 0)}",
        "",
        END,
        "",
    ]
    return "\n".join(lines) + "\n"


def upsert_index_section(index_path: Path, section: str) -> None:
    text = index_path.read_text(encoding="utf-8") if index_path.is_file() else ""
    if BEGIN in text and END in text:
        pre, rest = text.split(BEGIN, 1)
        _, post = rest.split(END, 1)
        # 去掉 END 后多余空行，由 section 自带结尾空行
        post = post.lstrip("\n")
        new = pre.rstrip() + "\n\n" + section + post
    else:
        marker = "## 文件"
        if marker in text:
            pre, post = text.split(marker, 1)
            new = pre.rstrip() + "\n\n" + section + marker + post
        else:
            new = text.rstrip() + "\n\n" + section
    index_path.write_text(new, encoding="utf-8")


def tag_archive(root: Path, cfg: dict) -> list[dict]:
    archive = root / cfg["repo_dir"]
    raw = archive / "raw"
    if not raw.is_dir():
        print(f"警告: 找不到 {cfg['repo_dir']}/raw，跳过 {cfg['slug']}", file=sys.stderr)
        return []
    user, posts, inc_tweets = load_posts(raw)
    user_id = user.get("id") or ""
    by_id = {p["id"]: p for p in posts if p.get("id")}
    file_map = map_post_files(archive, cfg["repo_dir"])
    default_file = file_map.get("_default", cfg["repo_dir"])
    rows = []
    counts: Counter = Counter()
    for p in posts:
        pid = p.get("id")
        if not pid:
            continue
        ptype = classify_post(p, user_id, by_id, inc_tweets)
        counts[ptype] += 1
        rows.append({
            "人": cfg["slug"],
            "id": pid,
            "日期": bj_date(p),
            "post_type": ptype,
            "链接": post_url(p, cfg["username"]),
            "文件": file_map.get(pid, default_file),
        })
    rows.sort(key=lambda r: (r["日期"], r["id"]), reverse=True)
    section = render_index_section(cfg["slug"], cfg["username"], counts, len(rows))
    index_path = archive / "index.md"
    if index_path.is_file() or True:
        upsert_index_section(index_path, section)
    print(f"{cfg['slug']}: {len(rows)}  " + "  ".join(f"{t}={counts[t]}" for t in TYPE_ORDER))
    return rows


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = ["人", "id", "日期", "post_type", "链接", "文件"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    root = REPO_ROOT
    if argv is None:
        argv = sys.argv[1:]
    # 可选：只跑指定 slug
    wanted = set(argv) if argv else None
    all_rows: list[dict] = []
    for cfg in ARCHIVES:
        if wanted and cfg["slug"] not in wanted and cfg["username"] not in wanted:
            continue
        all_rows.extend(tag_archive(root, cfg))
    out = root / "index" / "x-posts.csv"
    write_csv(out, all_rows)
    print(f"wrote {out} ({len(all_rows)} rows)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
