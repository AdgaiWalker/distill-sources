#!/usr/bin/env python3
"""生成 README「原料统计」一节，并刷新标题下的「最近抓取时间」。

用法（在仓库根目录）：

    python3 scripts/stats.py

读取 index/x-posts.csv 与 index/classification.csv，以及 people.yaml 的人名顺序，
替换 README.md 中 <!-- BEGIN STATS --> 与 <!-- END STATS --> 之间的内容。
只写统计数字，不把会员内容原文写入 README。

「最近抓取时间」读自 index/last-fetch.txt（由 scripts/record_fetch.py 在成功抓取后写入），
写入 README 主标题下 <!-- BEGIN FETCH META --> 与 <!-- END FETCH META --> 之间。
不要用本脚本运行时刻冒充抓取时间。

定时更新：成功抓取后先跑 record_fetch.py，再跑 tag_x.py、classify.py，最后跑本脚本。
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
README = ROOT / "README.md"
PEOPLE_YAML = ROOT / "people.yaml"
X_POSTS_CSV = ROOT / "index" / "x-posts.csv"
CLASSIFICATION_CSV = ROOT / "index" / "classification.csv"
LAST_FETCH = ROOT / "index" / "last-fetch.txt"

BJ = dt.timezone(dt.timedelta(hours=8))
BEGIN = "<!-- BEGIN STATS -->"
END = "<!-- END STATS -->"
FETCH_BEGIN = "<!-- BEGIN FETCH META -->"
FETCH_END = "<!-- END FETCH META -->"
TITLE_LINE = "# distill-sources（每四天抓取一次）"
TIME_RE = re.compile(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}")

# 与 classify.py 的来源类型一致
SOURCE_TYPES = ("wechat", "group-chat", "github", "x", "notes", "feishu")
SOURCE_ZH = {
    "wechat": "公众号文章",
    "group-chat": "会员群",
    "github": "GitHub 资料",
    "x": "X",
    "notes": "笔记",
    "feishu": "飞书知识库",
}

X_TYPES = ("original", "article", "long", "self-thread", "reply", "quote", "retweet")
X_ZH = {
    "original": "原创",
    "article": "文章",
    "long": "长帖",
    "self-thread": "自己的连续帖",
    "reply": "回复",
    "quote": "引用",
    "retweet": "转帖",
}

# 若 README 里还没有标记，插到这个标题之前
INSERT_BEFORE = "## 可见性规则"


def now_beijing() -> str:
    return dt.datetime.now(BJ).strftime("%Y-%m-%d %H:%M")


def read_last_fetch() -> tuple[str | None, str | None]:
    """返回 (北京时间 YYYY-MM-DD HH:MM, 数据来源说明)。文件不存在或无法解析则 (None, None)。"""
    if not LAST_FETCH.is_file():
        return None, None
    time_str = None
    source = None
    for raw in LAST_FETCH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("source:"):
            source = line.split(":", 1)[1].strip()
            continue
        if line.lower().startswith("timezone:"):
            continue
        if line.lower().startswith("time:"):
            line = line.split(":", 1)[1].strip()
        m = TIME_RE.search(line)
        if m and time_str is None:
            time_str = m.group(0)
    return time_str, source


def render_fetch_meta(time_str: str | None) -> str:
    if time_str:
        body = f"最近抓取时间：{time_str} 北京时间"
    else:
        body = "最近抓取时间：尚无记录（成功抓取后请先跑 `python3 scripts/record_fetch.py`）"
    return f"{FETCH_BEGIN}\n{body}\n{FETCH_END}\n"


def upsert_fetch_meta(text: str) -> str:
    """把「最近抓取时间」写到主标题正下方；主标题统一为每四天抓取一次。

    只处理文件开头、紧挨主标题的那一块，避免误伤后文说明里碰巧出现的标记文字。
    """
    time_str, _source = read_last_fetch()
    block = render_fetch_meta(time_str)
    lines = text.splitlines(keepends=True)
    if lines and lines[0].startswith("# distill-sources"):
        lines[0] = TITLE_LINE + "\n"
        text = "".join(lines)
    elif not text.startswith(TITLE_LINE):
        text = TITLE_LINE + "\n\n" + text

    # 若开头已有 FETCH META 块（主标题后、第一段正文前），只替换这一块
    prefix = text[:800]
    if FETCH_BEGIN in prefix and FETCH_END in prefix:
        pre, rest = text.split(FETCH_BEGIN, 1)
        # 标记必须紧挨标题（中间只允许空行）
        if pre.strip() == TITLE_LINE:
            _, post = rest.split(FETCH_END, 1)
            post = post.lstrip("\n")
            return TITLE_LINE + "\n\n" + block + "\n" + post

    # 否则插入标题后；若标题下已有旧块残片，先去掉紧随其后的一块
    rest = text[len(TITLE_LINE):].lstrip("\n") if text.startswith(TITLE_LINE) else text
    return TITLE_LINE + "\n\n" + block + "\n" + rest


def load_people_order() -> list[tuple[str, str]]:
    """返回 [(slug, name), ...]，顺序与 people.yaml 一致。不引入 PyYAML。"""
    text = PEOPLE_YAML.read_text(encoding="utf-8")
    people: list[tuple[str, str]] = []
    slug = None
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith("- slug:"):
            slug = line.split(":", 1)[1].strip().strip("\"'")
        elif line.startswith("name:") and slug is not None:
            name = line.split(":", 1)[1].strip().strip("\"'")
            people.append((slug, name))
            slug = None
    if not people:
        raise SystemExit("people.yaml 里没有读到人物")
    return people


def md_row(cells: list, aligns: list[str]) -> str:
    out = []
    for c, a in zip(cells, aligns):
        s = str(c)
        out.append(s)
    return "| " + " | ".join(out) + " |"


def md_sep(aligns: list[str]) -> str:
    parts = []
    for a in aligns:
        if a == "right":
            parts.append("---:")
        else:
            parts.append("---")
    return "| " + " | ".join(parts) + " |"


def md_table(headers: list[str], rows: list[list], aligns: list[str]) -> str:
    lines = [md_row(headers, aligns), md_sep(aligns)]
    for r in rows:
        lines.append(md_row(r, aligns))
    return "\n".join(lines)


def x_type_table(people: list[tuple[str, str]]) -> tuple[str, int]:
    if not X_POSTS_CSV.is_file():
        raise SystemExit(f"找不到 {X_POSTS_CSV}，请先运行 python3 scripts/tag_x.py")
    rows = list(csv.DictReader(X_POSTS_CSV.open(encoding="utf-8")))
    by_slug: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        ptype = r.get("post_type") or ""
        slug = r.get("人") or ""
        by_slug[slug][ptype] += 1
        by_slug[slug]["__total"] += 1

    slug_to_name = {s: n for s, n in people}
    # 只列出仓库里有 X 归档的人，顺序跟 people.yaml
    x_people = [(s, n) for s, n in people if s in by_slug]
    # 若 csv 里有 yaml 未登记的 slug，附在后面
    known = {s for s, _ in people}
    for s in by_slug:
        if s not in known:
            x_people.append((s, s))

    headers = ["人"] + [X_ZH[t] for t in X_TYPES] + ["合计"]
    aligns = ["left"] + ["right"] * (len(X_TYPES) + 1)
    table_rows = []
    col_tot = Counter()
    for slug, name in x_people:
        c = by_slug[slug]
        vals = [c.get(t, 0) for t in X_TYPES]
        total = c.get("__total", sum(vals))
        for t, v in zip(X_TYPES, vals):
            col_tot[t] += v
        col_tot["__total"] += total
        table_rows.append([name] + vals + [total])
    table_rows.append(["合计"] + [col_tot[t] for t in X_TYPES] + [col_tot["__total"]])

    if col_tot["__total"] != len(rows):
        print(f"警告: 表内合计 {col_tot['__total']} 与 x-posts.csv 行数 {len(rows)} 不一致", file=sys.stderr)

    return md_table(headers, table_rows, aligns), col_tot["__total"]


def source_table(people: list[tuple[str, str]]) -> tuple[str, int, int, int]:
    if not CLASSIFICATION_CSV.is_file():
        raise SystemExit(f"找不到 {CLASSIFICATION_CSV}，请先运行 python3 scripts/classify.py")
    rows = list(csv.DictReader(CLASSIFICATION_CSV.open(encoding="utf-8")))
    name_to_slug = {n: s for s, n in people}
    slug_of = {}
    for r in rows:
        person = r.get("source_person") or ""
        slug_of[person] = name_to_slug.get(person, person)

    counts: dict[str, Counter] = defaultdict(Counter)
    vis: dict[str, Counter] = defaultdict(Counter)
    for r in rows:
        person = r.get("source_person") or ""
        st = r.get("source_type") or ""
        counts[person][st] += 1
        vis[person][r.get("visibility") or ""] += 1
        counts[person]["__total"] += 1

    # 按 yaml 顺序，未登记的人附后
    yaml_names = [n for _, n in people]
    extra = [p for p in counts if p not in yaml_names]
    ordered = [n for n in yaml_names if n in counts] + extra

    headers = ["人"] + [SOURCE_ZH[t] for t in SOURCE_TYPES] + ["合计", "public", "member"]
    aligns = ["left"] + ["right"] * (len(SOURCE_TYPES) + 3)
    table_rows = []
    col = Counter()
    for name in ordered:
        c = counts[name]
        vals = [c.get(t, 0) for t in SOURCE_TYPES]
        total = c.get("__total", sum(vals))
        pub = vis[name].get("public", 0)
        mem = vis[name].get("member", 0)
        for t, v in zip(SOURCE_TYPES, vals):
            col[t] += v
        col["__total"] += total
        col["public"] += pub
        col["member"] += mem
        table_rows.append([name] + vals + [total, pub, mem])
    table_rows.append(
        ["合计"] + [col[t] for t in SOURCE_TYPES] + [col["__total"], col["public"], col["member"]]
    )

    if col["__total"] != len(rows):
        print(f"警告: 表内合计 {col['__total']} 与 classification.csv 行数 {len(rows)} 不一致", file=sys.stderr)

    return md_table(headers, table_rows, aligns), col["__total"], col["public"], col["member"]


def render(people: list[tuple[str, str]]) -> str:
    x_md, x_total = x_type_table(people)
    src_md, src_total, src_pub, src_mem = source_table(people)
    ts = now_beijing()
    parts = [
        BEGIN,
        "",
        "## 原料统计",
        "",
        f"由 [`scripts/stats.py`](scripts/stats.py) 根据 [`index/x-posts.csv`](index/x-posts.csv) 与 [`index/classification.csv`](index/classification.csv) 生成（{ts} 北京时间）。只列统计数字，不含会员内容原文。成功抓取后请依次跑 `record_fetch.py`、`tag_x.py`、`classify.py`、`stats.py`。",
        "",
        "### X 帖子类型",
        "",
        f"单位：帖。每条一个 `post_type`（优先级见「X 材料收录与蒸馏规则」）。合计 {x_total} 条。",
        "",
        x_md,
        "",
        "### 按人 × 来源类型",
        "",
        f"单位：索引条目，与 [INDEX.md](INDEX.md) 合计一致。本表合计 {src_total} 条（public {src_pub}，member {src_mem}）。",
        "X 列是归档文件条目（`index.md` / `all.md` / `articles/` / `raw/`），不是帖子数；帖子见上表。",
        "会员 GitHub 仓按仓计 1 条；会员群只记条目数量（记录与截图目录），不写入原文。",
        "",
        src_md,
        "",
        END,
        "",
    ]
    return "\n".join(parts) + "\n"


def upsert_readme(section: str) -> None:
    text = README.read_text(encoding="utf-8") if README.is_file() else ""
    if BEGIN in text and END in text:
        pre, rest = text.split(BEGIN, 1)
        _, post = rest.split(END, 1)
        post = post.lstrip("\n")
        new = pre.rstrip() + "\n\n" + section + post
    elif INSERT_BEFORE in text:
        pre, post = text.split(INSERT_BEFORE, 1)
        new = pre.rstrip() + "\n\n" + section + INSERT_BEFORE + post
    else:
        new = text.rstrip() + "\n\n" + section
    new = upsert_fetch_meta(new)
    README.write_text(new, encoding="utf-8")


def main() -> int:
    people = load_people_order()
    section = render(people)
    upsert_readme(section)
    # 打印两张表，方便核对
    body = section.split(BEGIN, 1)[1].split(END, 1)[0].strip()
    print(body)
    print(f"updated {README.relative_to(ROOT)}", file=sys.stderr)
    _run_corpus_tools()
    return 0


def _run_corpus_tools() -> None:
    """追加调用：重建 manifest 与覆盖率。失败只打印警告，不改变本脚本退出码。"""
    import subprocess

    for script in ("tools/build_manifest.py", "tools/coverage.py"):
        r = subprocess.run([sys.executable, str(ROOT / script)], cwd=ROOT)
        if r.returncode != 0:
            print(f"警告: {script} 退出码 {r.returncode}（不影响 stats.py）", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
