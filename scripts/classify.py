#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按「哪些人、拿来做什么用」给 distill-sources 建索引。

口径：
  哥飞、西门 → 用途：出海
  刘小排     → 用途：产品

不移动、不改名、不改写任何原始材料。可重复运行，每次覆盖生成：
  INDEX.md
  people/gefei.md
  people/ximen.md
  people/liuxiaopai.md
  people/other.md（仅当有「其他」时）
  index/classification.csv

用法：
  python3 scripts/classify.py
"""

from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PEOPLE_DIR = ROOT / "people"
INDEX_DIR = ROOT / "index"
CSV_PATH = INDEX_DIR / "classification.csv"
INDEX_MD = ROOT / "INDEX.md"

# 人 → 默认用途。用途只允许：出海 / 产品 / 未分类
PERSON_PURPOSE = {
    "哥飞": "出海",
    "西门": "出海",
    "刘小排": "产品",
}

PERSON_SLUG = {
    "哥飞": "gefei",
    "西门": "ximen",
    "刘小排": "liuxiaopai",
    "其他": "other",
}

PERSON_BLURB = {
    "哥飞": "哥飞的公众号、会员群、会员整理的哥飞相关仓库，以及 GitHub 种子仓。用来做出海。",
    "西门": "哆啦整理的西门笔记。用来做出海。",
    "刘小排": "刘小排（@bourneliu66）的 X 归档。用来做产品。",
    "其他": "无法归到哥飞、西门或刘小排的材料。",
}

DATE_IN_NAME = re.compile(
    r"(?:^|/)((?:20\d{2})[-_]?(?:0[1-9]|1[0-2])[-_]?(?:0[1-9]|[12]\d|3[01]))"
)
DATE_FIELD = re.compile(
    r"(?:发布时间|日期|时间)[：:\s]*((?:20\d{2})[-年](?:0[1-9]|1[0-2])[-月](?:0[1-9]|[12]\d|3[01]))"
)
ISO_DATE = re.compile(r"(20\d{2})[-年_]?(\d{2})[-月_]?(\d{2})")

SKIP_DIR_NAMES = {".git", ".github", ".obsidian", ".agents", "node_modules", "__pycache__"}


def norm_date(s: str | None) -> str:
    if not s:
        return ""
    m = ISO_DATE.search(s.replace(" ", ""))
    if not m:
        return ""
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3))).isoformat()
    except ValueError:
        return ""


def read_text_head(path: Path, limit: int = 4000) -> str:
    try:
        data = path.read_bytes()[: limit * 2]
    except OSError:
        return ""
    if b"\x00" in data[:1024]:
        return ""
    return data.decode("utf-8", errors="replace")[:limit]


def extract_title_and_date(path: Path, text: str = "", is_dir: bool = False) -> tuple[str, str]:
    title = ""
    date = ""
    if text:
        m = re.search(r"^#\s+(.+)$", text, re.M)
        if m:
            title = re.sub(r"\s+", " ", m.group(1).strip())
        m = DATE_FIELD.search(text)
        if m:
            date = norm_date(m.group(1))
    if not date:
        m = DATE_IN_NAME.search(path.name) or DATE_IN_NAME.search(str(path))
        if m:
            date = norm_date(m.group(1))
    if not title:
        if is_dir:
            title = path.name
        else:
            stem = path.stem
            stem = re.sub(r"^(20\d{6}|20\d{2}-\d{2}-\d{2})_?", "", stem)
            title = stem or path.name
    if len(title) > 120:
        title = title[:117] + "…"
    return title, date


def rel_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def count_files(path: Path) -> int:
    n = 0
    for dirpath, dirs, files in path.walk() if hasattr(path, "walk") else []:
        dirs[:] = [d for d in dirs if d not in SKIP_DIR_NAMES]
        n += len(files)
    if n == 0:
        for dirpath, dirs, files in _walk(path):
            n += len(files)
    return n


def _walk(path: Path):
    for dirpath, dirs, files in __import__("os").walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIR_NAMES]
        yield dirpath, dirs, files


def add(records: list[dict], path_str: str, person: str, title: str, date: str, collection: str) -> None:
    purpose = PERSON_PURPOSE.get(person, "未分类")
    records.append({
        "path": path_str,
        "source_person": person,
        "purpose": purpose,
        "title": title,
        "date": date,
        "collection": collection,
    })


def add_file(records: list[dict], path: Path, person: str, collection: str) -> None:
    text = read_text_head(path)
    title, date = extract_title_and_date(path, text)
    add(records, rel_posix(path), person, title, date, collection)


def add_dir(records: list[dict], path: Path, person: str, collection: str, title: str) -> None:
    add(records, rel_posix(path) + "/", person, title, "", collection)


def read_upstream_url(repo: Path) -> str:
    p = repo / "UPSTREAM.md"
    if not p.is_file():
        return ""
    text = read_text_head(p, 2000)
    m = re.search(r"origin：\s*(\S+)", text)
    return m.group(1).rstrip("。") if m else ""


def assign_member_repo_person(repo: Path, url: str) -> str:
    """会员仓按 UPSTREAM / 仓库名归人。当前这批都是哥飞相关整理。"""
    blob = f"{repo.name} {url}".lower()
    if "liuxiaopai" in blob or "bourneliu" in blob or "刘小排" in blob:
        return "刘小排"
    if "ximen" in blob or "西门" in blob:
        return "西门"
    # gefei / 哥飞 / OpenGeFei / 其余会员整理的哥飞资料
    if "gefei" in blob or "哥飞" in repo.name or "opengefei" in blob:
        return "哥飞"
    # 默认：放在 gefei/github-member-repos 下、且名称或上游指向哥飞方法论的，归哥飞
    return "哥飞"


def scan(records: list[dict]) -> None:
    # 哥飞公众号
    d = ROOT / "gefei/wechat-articles"
    for p in sorted(d.glob("*.md")):
        add_file(records, p, "哥飞", "gefei/wechat-articles")

    # 会员群
    d = ROOT / "gefei/group-chat"
    for p in sorted(d.glob("*.md")):
        add_file(records, p, "哥飞", "gefei/group-chat")
    shots = d / "screenshots"
    if shots.is_dir():
        n = len(list(shots.glob("*")))
        add_dir(records, shots, "哥飞", "gefei/group-chat", f"会员群截图（{n} 张，转录附件）")

    # 西门笔记
    d = ROOT / "gefei/ximen-notes"
    for p in sorted(d.glob("*.md")):
        add_file(records, p, "西门", "gefei/ximen-notes")

    # GitHub 种子仓 → 哥飞
    d = ROOT / "gefei/github-seed"
    for p in sorted(d.glob("*.md")) + sorted(d.glob("*.py")):
        add_file(records, p, "哥飞", "gefei/github-seed")
    pub = d / "公众号"
    if pub.is_dir():
        for p in sorted(pub.iterdir()):
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
                add_file(records, p, "哥飞", "gefei/github-seed")
        imgs = [p for p in pub.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
        if imgs:
            add(records, rel_posix(pub) + "/（封面图）", "哥飞", f"公众号目录封面图（{len(imgs)} 张）", "", "gefei/github-seed")
    gf = d / "哥飞"
    if gf.is_dir():
        for p in sorted(gf.iterdir()):
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
                add_file(records, p, "哥飞", "gefei/github-seed")
        cover = gf / "封面"
        if cover.is_dir():
            n = len(list(cover.glob("*")))
            add_dir(records, cover, "哥飞", "gefei/github-seed", f"哥飞文章封面图（{n} 张）")

    # 会员 GitHub 仓：按仓归人，不逐文件打标签
    base = ROOT / "gefei/github-member-repos"
    for repo in sorted(base.iterdir()):
        if not repo.is_dir():
            continue
        url = read_upstream_url(repo)
        person = assign_member_repo_person(repo, url)
        n = sum(len(files) for _, _, files in _walk(repo))
        title = f"{repo.name}（{n} 个文件）"
        if url:
            title = f"{title} {url}"
        add_dir(records, repo, person, "gefei/github-member-repos", title)

    # 刘小排 X 归档
    d = ROOT / "liuxiaopai/x-archive"
    for name in ("index.md", "all.md"):
        p = d / name
        if p.is_file():
            add_file(records, p, "刘小排", "liuxiaopai/x-archive")
    arts = d / "articles"
    if arts.is_dir():
        for p in sorted(arts.glob("*.md")):
            add_file(records, p, "刘小排", "liuxiaopai/x-archive")
    raw = d / "raw"
    if raw.is_dir():
        n = len(list(raw.glob("*")))
        add_dir(records, raw, "刘小排", "liuxiaopai/x-archive", f"X 归档原始 JSON（{n} 个文件）")


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def link_from_people(path_str: str) -> str:
    target = path_str
    if target.endswith("（封面图）"):
        target = target.replace("（封面图）", "/")
    return "../" + target


def sort_recs(rows: list[dict]) -> list[dict]:
    # 有日期的倒序在前，无日期的放最后
    return sorted(rows, key=lambda r: (r["date"] != "", r["date"], r["path"]), reverse=True)


def write_csv(records: list[dict]) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    fields = ["path", "source_person", "purpose", "title", "date", "collection"]
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for rec in sorted(records, key=lambda r: r["path"]):
            w.writerow(rec)


def write_people_pages(records: list[dict]) -> None:
    if PEOPLE_DIR.exists():
        for old in PEOPLE_DIR.glob("*.md"):
            old.unlink()
    else:
        PEOPLE_DIR.mkdir(parents=True, exist_ok=True)

    by_person: dict[str, list[dict]] = defaultdict(list)
    for rec in records:
        by_person[rec["source_person"]].append(rec)

    # 只写有条目的人；「其他」没有就不写
    order = ["哥飞", "西门", "刘小排", "其他"]
    for person in order:
        rows = by_person.get(person, [])
        if person == "其他" and not rows:
            continue
        slug = PERSON_SLUG[person]
        purpose = PERSON_PURPOSE.get(person, "未分类")
        parts = [
            f"# {person}",
            "",
            PERSON_BLURB[person],
            "",
            f"- 人：{person}",
            f"- 用途：{purpose}",
            f"- 条目：{len(rows)}",
            "",
            "由 `scripts/classify.py` 生成。原文件未移动。",
            "",
        ]
        # 按收藏夹分组
        by_col: dict[str, list[dict]] = defaultdict(list)
        for r in rows:
            by_col[r["collection"]].append(r)
        for col in sorted(by_col):
            items = by_col[col]
            parts += [f"## `{col}`", "", f"{len(items)} 条。", ""]
            parts += [
                "| 日期 | 标题 | 路径 |",
                "|---|---|---|",
            ]
            for r in sort_recs(items):
                title = md_escape(r["title"])
                href = link_from_people(r["path"])
                date = r["date"] or "—"
                parts.append(f"| {date} | [{title}]({href}) | `{md_escape(r['path'])}` |")
            parts.append("")
        (PEOPLE_DIR / f"{slug}.md").write_text("\n".join(parts), encoding="utf-8")


def write_index(records: list[dict], generated_at: str) -> None:
    by_person: dict[str, list[dict]] = defaultdict(list)
    by_purpose: dict[str, int] = defaultdict(int)
    by_person_purpose: dict[tuple[str, str], int] = defaultdict(int)
    unclassified = []
    for rec in records:
        by_person[rec["source_person"]].append(rec)
        by_purpose[rec["purpose"]] += 1
        by_person_purpose[(rec["source_person"], rec["purpose"])] += 1
        if rec["purpose"] == "未分类" or rec["source_person"] == "其他":
            unclassified.append(rec)

    lines = [
        "# 人物与用途索引",
        "",
        "分类口径：**哪些人的材料，拿来做什么用。**",
        "",
        "- 哥飞、西门 → **出海**",
        "- 刘小排 → **产品**",
        "",
        "不是按 SEO、外链、需求挖掘等主题分类。",
        "",
        "- **原文件不移动、不改名、不改内容**。本文件与 `people/`、`index/classification.csv` 都是新增索引。",
        "- 由 [`scripts/classify.py`](scripts/classify.py) 生成，可重跑。",
        "- 会员 GitHub 仓按 `UPSTREAM.md` / 仓库名归到对应的人，只记到仓，不逐文件列出。`github-seed` 归哥飞。",
        f"- 生成时间：{generated_at}（北京时间）。",
        "",
        "## 一览",
        "",
        "| 人 | 用途 | 条目 | 清单 |",
        "|---|---|---:|---|",
    ]
    for person in ("哥飞", "西门", "刘小排", "其他"):
        rows = by_person.get(person, [])
        if person == "其他" and not rows:
            continue
        purpose = PERSON_PURPOSE.get(person, "未分类")
        slug = PERSON_SLUG[person]
        lines.append(f"| {person} | {purpose} | {len(rows)} | [{slug}.md](people/{slug}.md) |")

    lines += [
        "",
        f"合计条目：{len(records)}。",
        "",
        "## 用途对照",
        "",
        "| 用途 | 对应的人 | 条目 |",
        "|---|---|---:|",
        f"| 出海 | 哥飞、西门 | {by_purpose.get('出海', 0)} |",
        f"| 产品 | 刘小排 | {by_purpose.get('产品', 0)} |",
        f"| 未分类 | — | {by_purpose.get('未分类', 0)} |",
        "",
        "细目来源见 [SOURCES.md](SOURCES.md)。",
        "",
        "## 覆盖范围",
        "",
        "- `gefei/wechat-articles/` → 哥飞 / 出海（逐篇）",
        "- `gefei/group-chat/` → 哥飞 / 出海（转录逐篇，截图按目录）",
        "- `gefei/github-seed/` → 哥飞 / 出海（文本逐篇，封面图按目录）",
        "- `gefei/github-member-repos/` → 按仓归人（这批均为哥飞相关整理，出海）",
        "- `gefei/ximen-notes/` → 西门 / 出海（逐篇）",
        "- `liuxiaopai/x-archive/` → 刘小排 / 产品（长文/长帖逐篇，索引与 raw JSON 按条/目录）",
        "",
        "## 重跑",
        "",
        "```bash",
        "python3 scripts/classify.py",
        "```",
        "",
    ]
    if unclassified:
        lines += ["## 未分类 / 其他", "", "下列条目需要人工再看：", ""]
        for r in unclassified:
            lines.append(f"- `{r['path']}` 人={r['source_person']} 用途={r['purpose']} {r['title']}")
        lines.append("")

    INDEX_MD.write_text("\n".join(lines), encoding="utf-8")


def print_report(records: list[dict]) -> None:
    by_person = defaultdict(int)
    by_purpose = defaultdict(int)
    by_col = defaultdict(int)
    unc = []
    for r in records:
        by_person[r["source_person"]] += 1
        by_purpose[r["purpose"]] += 1
        by_col[(r["source_person"], r["collection"])] += 1
        if r["purpose"] == "未分类" or r["source_person"] == "其他":
            unc.append(r)
    print("=== 按人 ===")
    for person in ("哥飞", "西门", "刘小排", "其他"):
        if person == "其他" and by_person.get(person, 0) == 0:
            continue
        print(f"  {person}（{PERSON_PURPOSE.get(person, '未分类')}）: {by_person.get(person, 0)}")
        cols = [(col, n) for (p, col), n in by_col.items() if p == person]
        for col, n in sorted(cols):
            print(f"      {col}: {n}")
    print("=== 用途 ===")
    for k in ("出海", "产品", "未分类"):
        print(f"  {k}: {by_purpose.get(k, 0)}")
    print(f"  合计: {len(records)}")
    if unc:
        print("=== 未分类/其他 ===")
        for r in unc:
            print(f"  {r['path']} {r['source_person']} {r['purpose']} {r['title']}")
    else:
        print("未分类: 0")


def main() -> int:
    if not (ROOT / "gefei").is_dir() or not (ROOT / "liuxiaopai").is_dir():
        print(f"仓库结构不对，ROOT={ROOT}", file=sys.stderr)
        return 2

    # 清掉旧的按主题索引，避免错误口径留在仓里
    stale_topics = ROOT / "TOPICS.md"
    stale_dir = ROOT / "topics"
    if stale_topics.exists():
        stale_topics.unlink()
        print("removed stale TOPICS.md")
    if stale_dir.is_dir():
        for p in stale_dir.glob("*.md"):
            p.unlink()
        try:
            stale_dir.rmdir()
            print("removed stale topics/")
        except OSError:
            pass

    records: list[dict] = []
    scan(records)
    generated_at = dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M")
    write_csv(records)
    write_people_pages(records)
    write_index(records, generated_at)
    print_report(records)
    print(f"wrote {INDEX_MD.relative_to(ROOT)}, {PEOPLE_DIR.relative_to(ROOT)}/, {CSV_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
