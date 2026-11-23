#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按「用途 → 人 → 来源类型」给 distill-sources 建索引。

配置在仓库根目录 people.yaml。新增一个人：改配置、建目录、加人物卡，然后重跑本脚本。

不移动、不改名、不改写任何原始材料。可重复运行，覆盖生成：
  INDEX.md
  index/classification.csv
  people/<slug>.md 中 <!-- BEGIN MATERIAL LIST --> 与 <!-- END MATERIAL LIST --> 之间的清单
  （人物卡其余手写部分不改）

时间一律用北京时间（UTC+8）。

用法：
  python3 scripts/classify.py
"""

from __future__ import annotations

import csv
import datetime as dt
import fnmatch
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "people.yaml"
INDEX_MD = ROOT / "INDEX.md"
INDEX_DIR = ROOT / "index"
CSV_PATH = INDEX_DIR / "classification.csv"
PEOPLE_DIR = ROOT / "people"

BEIJING = dt.timezone(dt.timedelta(hours=8))
SOURCE_TYPES = ("wechat", "group-chat", "x", "github", "notes", "feishu")
VISIBILITIES = ("public", "member")
BEGIN_MARK = "<!-- BEGIN MATERIAL LIST -->"
END_MARK = "<!-- END MATERIAL LIST -->"

SKIP_DIR_NAMES = {".git", ".github", ".obsidian", ".agents", "node_modules", "__pycache__"}

DATE_IN_NAME = re.compile(
    r"(?:^|/)((?:20\d{2})[-_]?(?:0[1-9]|1[0-2])[-_]?(?:0[1-9]|[12]\d|3[01]))"
)
DATE_FIELD = re.compile(
    r"(?:发布时间|日期|时间)[：:\s]*((?:20\d{2})[-年](?:0[1-9]|1[0-2])[-月](?:0[1-9]|[12]\d|3[01]))"
)
ISO_DATE = re.compile(r"(20\d{2})[-年_]?(\d{2})[-月_]?(\d{2})")


def now_beijing() -> str:
    return dt.datetime.now(BEIJING).strftime("%Y-%m-%d %H:%M")


# ---------- 极简 YAML 子集（无第三方依赖） ----------

def load_yaml(path: Path) -> dict:
    try:
        import yaml  # type: ignore
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except ImportError:
        return load_simple_yaml(path.read_text(encoding="utf-8"))


def load_simple_yaml(text: str):
    """解析本仓 people.yaml 用到的子集：注释、映射、列表、标量。"""
    lines: list[tuple[int, str]] = []
    for raw in text.splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        lines.append((indent, raw.strip()))

    def parse_scalar(s: str):
        if s in ("null", "~", ""):
            return None
        if s in ("true", "True"):
            return True
        if s in ("false", "False"):
            return False
        if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
            return s[1:-1]
        if re.fullmatch(r"-?\d+", s):
            return int(s)
        return s

    def parse_flow(s: str):
        s = s.strip()
        if s.startswith("[") and s.endswith("]"):
            inner = s[1:-1].strip()
            if not inner:
                return []
            return [parse_scalar(p.strip()) for p in inner.split(",")]
        return parse_scalar(s)

    def parse_block(idx: int, indent: int):
        # peek
        if idx >= len(lines):
            return None, idx
        i, content = lines[idx]
        if i < indent:
            return None, idx
        if content.startswith("- "):
            return parse_list(idx, indent)
        return parse_map(idx, indent)

    def parse_map(idx: int, indent: int):
        result = {}
        while idx < len(lines):
            i, content = lines[idx]
            if i < indent:
                break
            if i > indent:
                raise ValueError(f"YAML 缩进异常: {content}")
            if content.startswith("- "):
                break
            if ":" not in content:
                raise ValueError(f"YAML 行缺少冒号: {content}")
            key, _, rest = content.partition(":")
            key = key.strip()
            rest = rest.strip()
            idx += 1
            if rest:
                result[key] = parse_flow(rest)
            else:
                if idx < len(lines) and lines[idx][0] > indent:
                    child, idx = parse_block(idx, lines[idx][0])
                    result[key] = child
                else:
                    result[key] = None
        return result, idx

    def parse_list(idx: int, indent: int):
        result = []
        while idx < len(lines):
            i, content = lines[idx]
            if i < indent:
                break
            if i > indent:
                raise ValueError(f"YAML 列表缩进异常: {content}")
            if not content.startswith("- "):
                break
            item = content[2:].strip()
            idx += 1
            if not item:
                if idx < len(lines) and lines[idx][0] > indent:
                    child, idx = parse_block(idx, lines[idx][0])
                    result.append(child)
                else:
                    result.append(None)
            elif item.endswith(":") and (idx >= len(lines) or lines[idx][0] > indent or (idx < len(lines) and lines[idx][1].startswith("- "))):
                # "- key:" with nested body, or just empty
                key = item[:-1].strip()
                if idx < len(lines) and lines[idx][0] > indent:
                    child, idx = parse_block(idx, lines[idx][0])
                    result.append({key: child})
                else:
                    result.append({key: None})
            elif ":" in item and not item.startswith("[") and not item.startswith("'") and not item.startswith('"'):
                key, _, rest = item.partition(":")
                obj = {key.strip(): parse_flow(rest.strip())}
                # following indented keys belong to this list dict
                if idx < len(lines) and lines[idx][0] > indent and not lines[idx][1].startswith("- "):
                    more, idx = parse_map(idx, lines[idx][0])
                    obj.update(more)
                result.append(obj)
            else:
                result.append(parse_flow(item))
        return result, idx

    doc, idx = parse_map(0, lines[0][0] if lines else 0)
    if idx != len(lines):
        raise ValueError(f"YAML 未解析完，停在: {lines[idx]}")
    return doc


# ---------- 文本与日期 ----------

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


def walk_files(path: Path):
    import os
    for dirpath, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_DIR_NAMES]
        yield dirpath, dirs, files


def read_upstream_url(repo: Path) -> str:
    p = repo / "UPSTREAM.md"
    if not p.is_file():
        return ""
    text = read_text_head(p, 2000)
    m = re.search(r"origin：\s*(\S+)", text)
    return m.group(1).rstrip("。") if m else ""


# ---------- 扫描 ----------

def rec(person: dict, src: dict, path_str: str, title: str, date: str, collection: str) -> dict:
    purposes = person.get("purposes") or [person["primary_purpose"]]
    vis = src.get("visibility") or "member"
    if vis not in VISIBILITIES:
        vis = "member"
    st = src.get("source_type") or ""
    return {
        "path": path_str,
        "source_person": person["name"],
        "person_slug": person["slug"],
        "source_type": st,
        "visibility": vis,
        "primary_purpose": person["primary_purpose"],
        "purposes": ";".join(purposes),
        "title": title,
        "date": date,
        "collection": collection,
    }


def add_file(records: list, person: dict, src: dict, path: Path, collection: str) -> None:
    text = read_text_head(path)
    title, date = extract_title_and_date(path, text)
    records.append(rec(person, src, rel_posix(path), title, date, collection))


def add_dir(records: list, person: dict, src: dict, path: Path, title: str, collection: str) -> None:
    records.append(rec(person, src, rel_posix(path) + "/", title, "", collection))


def scan_files(records: list, person: dict, src: dict, base: Path) -> None:
    if not base.exists():
        print(f"警告: 路径不存在 {src['path']}", file=sys.stderr)
        return
    collection = src["path"].rstrip("/")
    pattern = src.get("glob") or "*.md"
    if base.is_file():
        add_file(records, person, src, base, collection)
        return
    for p in sorted(base.glob(pattern)):
        if p.is_file():
            add_file(records, person, src, p, collection)
    for unit in src.get("dir_units") or []:
        rel = unit.get("rel") or unit.get("path")
        if not rel:
            continue
        d = base / rel
        if d.is_dir():
            n = len([x for x in d.iterdir() if x.is_file()])
            title = unit.get("title") or d.name
            add_dir(records, person, src, d, f"{title}（{n} 个文件）", collection)


def scan_github_seed(records: list, person: dict, src: dict, base: Path) -> None:
    collection = src["path"].rstrip("/")
    if not base.is_dir():
        print(f"警告: 路径不存在 {src['path']}", file=sys.stderr)
        return
    for p in sorted(base.glob("*.md")) + sorted(base.glob("*.py")):
        add_file(records, person, src, p, collection)
    pub = base / "公众号"
    if pub.is_dir():
        for p in sorted(pub.iterdir()):
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
                add_file(records, person, src, p, collection)
        imgs = [p for p in pub.iterdir() if p.suffix.lower() in {".jpg", ".jpeg", ".png"}]
        if imgs:
            records.append(rec(
                person, src, rel_posix(pub) + "/（封面图）",
                f"公众号目录封面图（{len(imgs)} 张）", "", collection,
            ))
    gf = base / "哥飞"
    if gf.is_dir():
        for p in sorted(gf.iterdir()):
            if p.is_file() and p.suffix.lower() in {".md", ".txt"}:
                add_file(records, person, src, p, collection)
        cover = gf / "封面"
        if cover.is_dir():
            n = len([x for x in cover.iterdir() if x.is_file()])
            add_dir(records, person, src, cover, f"哥飞文章封面图（{n} 张）", collection)


def scan_repos(records: list, person: dict, src: dict, base: Path) -> None:
    collection = src["path"].rstrip("/")
    if not base.is_dir():
        print(f"警告: 路径不存在 {src['path']}", file=sys.stderr)
        return
    for repo in sorted(base.iterdir()):
        if not repo.is_dir() or repo.name in SKIP_DIR_NAMES:
            continue
        url = read_upstream_url(repo)
        n = sum(len(files) for _, _, files in walk_files(repo))
        title = f"{repo.name}（{n} 个文件）"
        if url:
            title = f"{title} {url}"
        add_dir(records, person, src, repo, title, collection)


def scan_x_archive(records: list, person: dict, src: dict, base: Path) -> None:
    collection = src["path"].rstrip("/")
    if not base.is_dir():
        print(f"警告: 路径不存在 {src['path']}", file=sys.stderr)
        return
    for name in ("index.md", "all.md"):
        p = base / name
        if p.is_file():
            add_file(records, person, src, p, collection)
    arts = base / "articles"
    if arts.is_dir():
        for p in sorted(arts.glob("*.md")):
            add_file(records, person, src, p, collection)
    raw = base / "raw"
    if raw.is_dir():
        n = len([x for x in raw.iterdir() if x.is_file()])
        add_dir(records, person, src, raw, f"X 归档原始 JSON（{n} 个文件）", collection)


SCANNERS = {
    "files": scan_files,
    "github-seed": scan_github_seed,
    "repos": scan_repos,
    "x-archive": scan_x_archive,
    "notes": scan_files,
}


def scan_all(config: dict) -> list[dict]:
    records: list[dict] = []
    for person in config.get("people") or []:
        for src in person.get("sources") or []:
            st = src.get("source_type")
            if st not in SOURCE_TYPES:
                print(f"警告: 未知 source_type {st!r}（{person.get('slug')} {src.get('path')}），仍写入", file=sys.stderr)
            vis = src.get("visibility") or "member"
            if vis not in VISIBILITIES:
                print(f"警告: 可见性 {vis!r} 非法，改标 member", file=sys.stderr)
                src = {**src, "visibility": "member"}
            scanner = src.get("scanner") or "files"
            fn = SCANNERS.get(scanner)
            if not fn:
                print(f"警告: 未知 scanner {scanner!r}，改用 files", file=sys.stderr)
                fn = scan_files
            fn(records, person, src, ROOT / src["path"])
    return records


# ---------- 写出 ----------

CSV_FIELDS = [
    "path", "source_person", "source_type", "visibility",
    "primary_purpose", "purposes", "title", "date", "collection",
]


def write_csv(records: list[dict]) -> None:
    INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=CSV_FIELDS, extrasaction="ignore")
        w.writeheader()
        for rec_ in sorted(records, key=lambda r: r["path"]):
            w.writerow(rec_)


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def link_from_people(path_str: str) -> str:
    target = path_str
    if target.endswith("（封面图）"):
        target = target.replace("（封面图）", "/")
    return "../" + target


def sort_recs(rows: list[dict]) -> list[dict]:
    return sorted(rows, key=lambda r: (r["date"] != "", r["date"], r["path"]), reverse=True)


def source_type_label(st: str) -> str:
    return {
        "wechat": "wechat（公众号）",
        "group-chat": "group-chat（会员群）",
        "x": "x（公开帖/长文）",
        "github": "github",
        "notes": "notes（笔记）",
        "feishu": "feishu（飞书知识库）",
    }.get(st, st)


def coverage_of(rows: list[dict]) -> str:
    dates = [r["date"] for r in rows if r["date"]]
    return max(dates) if dates else ""


def render_material_list(person: dict, rows: list[dict]) -> str:
    n_pub = sum(1 for r in rows if r["visibility"] == "public")
    n_mem = sum(1 for r in rows if r["visibility"] == "member")
    cov = coverage_of(rows)
    purposes = person.get("purposes") or [person["primary_purpose"]]
    lines = [
        f"共 {len(rows)} 条；public {n_pub}，member {n_mem}。",
        f"主用途：{person['primary_purpose']}。全部用途：{'、'.join(purposes)}。",
    ]
    if cov:
        lines.append(f"材料日期覆盖至：{cov}。")
    lines += ["", "由 `scripts/classify.py` 根据 `people.yaml` 生成。原文件未移动。", ""]

    by_col: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for r in rows:
        by_col[(r["collection"], r["source_type"])].append(r)
    for collection, st in sorted(by_col):
        items = by_col[(collection, st)]
        vis = items[0]["visibility"] if items else ""
        lines += [
            f"## `{collection}`",
            "",
            f"来源类型：{source_type_label(st)}。可见性：{vis}。{len(items)} 条。",
            "",
            "| 日期 | 标题 | 路径 |",
            "|---|---|---|",
        ]
        for r in sort_recs(items):
            title = md_escape(r["title"])
            href = link_from_people(r["path"])
            date = r["date"] or "—"
            lines.append(f"| {date} | [{title}]({href}) | `{md_escape(r['path'])}` |")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def update_person_card(person: dict, rows: list[dict]) -> None:
    slug = person["slug"]
    card = PEOPLE_DIR / f"{slug}.md"
    if not card.is_file():
        print(f"警告: 缺少人物卡 {card.relative_to(ROOT)}，跳过（请从 templates/person-card.md 复制）", file=sys.stderr)
        return
    text = card.read_text(encoding="utf-8")
    block = BEGIN_MARK + "\n" + render_material_list(person, rows) + END_MARK
    if BEGIN_MARK in text and END_MARK in text:
        text = re.sub(
            re.escape(BEGIN_MARK) + r".*?" + re.escape(END_MARK),
            block,
            text,
            count=1,
            flags=re.S,
        )
    else:
        text = text.rstrip() + "\n\n## 材料清单\n\n" + block + "\n"

    cov = coverage_of(rows)
    if cov:
        text2, n = re.subn(
            r"^coverage_until:.*$",
            f'coverage_until: "{cov}"',
            text,
            count=1,
            flags=re.M,
        )
        if n:
            text = text2
    # 按材料汇总更新人物级可见性
    vis_set = {r["visibility"] for r in rows}
    if vis_set == {"public"}:
        pvis = "public"
    elif vis_set == {"member"}:
        pvis = "member"
    elif vis_set:
        pvis = "mixed"
    else:
        pvis = "待补"
    text2, n = re.subn(r"^visibility:.*$", f"visibility: {pvis}", text, count=1, flags=re.M)
    if n:
        text = text2
    card.write_text(text, encoding="utf-8")


def write_index(config: dict, records: list[dict], generated_at: str) -> None:
    people = config.get("people") or []
    by_slug: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_slug[r["person_slug"]].append(r)
    known = list(config.get("known_purposes") or [])
    # 按主用途分组；若某人有多个用途，在每个用途下都出现，并注明是否主用途
    by_purpose: dict[str, list[dict]] = defaultdict(list)
    seen_purposes = []
    for person in people:
        purposes = person.get("purposes") or [person["primary_purpose"]]
        for pu in purposes:
            by_purpose[pu].append(person)
            if pu not in seen_purposes:
                seen_purposes.append(pu)
    order = [p for p in known if p in by_purpose] + [p for p in seen_purposes if p not in known]

    lines = [
        "# 蒸馏原料索引",
        "",
        "三层结构：**用途 → 人 → 来源类型**。",
        "",
        "- **用途**：这种知识能帮着蒸馏出哪类 skill。每人一个主用途，可以有多个用途。已用：出海、产品、AI 工具。可扩展（例如 IP、具身智能）。",
        "- **人**：每人一张人物卡，见 `people/<slug>.md`。",
        "- **来源类型**：`wechat`（公众号）/ `group-chat`（会员群）/ `x` / `github` / `notes`（笔记）/ `feishu`（飞书知识库）。",
        "",
        "原文件不移动、不改名、不改内容。本文件与 `index/classification.csv`、人物卡里的材料清单由 [`scripts/classify.py`](scripts/classify.py) 根据 [`people.yaml`](people.yaml) 生成，可重跑。",
        "",
        f"生成时间：{generated_at}（北京时间）。合计条目：{len(records)}。",
        "",
    ]

    for pu in order:
        persons = by_purpose[pu]
        # 去重但保持配置顺序
        uniq = []
        seen = set()
        for p in persons:
            if p["slug"] in seen:
                continue
            seen.add(p["slug"])
            uniq.append(p)
        n_items = sum(len(by_slug.get(p["slug"], [])) for p in uniq)
        lines += [
            f"## 用途：{pu}",
            "",
            f"这类知识用来蒸馏「{pu}」相关 skill。{len(uniq)} 人，{n_items} 条。",
            "",
            "| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |",
            "|---|---|---|---:|---:|---:|---|",
        ]
        for p in uniq:
            rows = by_slug.get(p["slug"], [])
            n_pub = sum(1 for r in rows if r["visibility"] == "public")
            n_mem = sum(1 for r in rows if r["visibility"] == "member")
            all_pu = "、".join(p.get("purposes") or [p["primary_purpose"]])
            mark = p["name"]
            if p["primary_purpose"] != pu:
                mark = f"{p['name']}（兼）"
            lines.append(
                f"| {mark} | {p['primary_purpose']} | {all_pu} | {len(rows)} | {n_pub} | {n_mem} | [{p['slug']}.md](people/{p['slug']}.md) |"
            )
        lines.append("")

    # 可见性合计
    n_pub = sum(1 for r in records if r["visibility"] == "public")
    n_mem = sum(1 for r in records if r["visibility"] == "member")
    lines += [
        "## 可见性",
        "",
        f"合计 public {n_pub}，member {n_mem}。",
        "",
        "- `public`：公开公众号文章、公开 X 帖、公开的开源仓库，以及上游已公开的 GitHub 整理资料。",
        "- `member`：来源为会员群转录/截图，或仓主整理的非公开出处笔记。本仓现已公开；这些条目经仓主决定一并收入，标签只说明来源，不表示禁止公开。",
        "",
        "细目来源见 [SOURCES.md](SOURCES.md)。新增一个人的步骤见 [README.md](README.md)。",
        "",
        "## 重跑",
        "",
        "```bash",
        "python3 scripts/classify.py",
        "```",
        "",
    ]
    INDEX_MD.write_text("\n".join(lines), encoding="utf-8")


def print_report(records: list[dict]) -> None:
    by = defaultdict(lambda: {"n": 0, "public": 0, "member": 0, "types": defaultdict(int), "primary": "", "purposes": ""})
    for r in records:
        b = by[r["source_person"]]
        b["n"] += 1
        b[r["visibility"]] += 1
        b["types"][r["source_type"]] += 1
        b["primary"] = r["primary_purpose"]
        b["purposes"] = r["purposes"]
    print("=== 按人 ===")
    for name, b in by.items():
        types = ", ".join(f"{k}:{v}" for k, v in sorted(b["types"].items()))
        print(f"  {name}  主用途={b['primary']} 用途={b['purposes']}  条目={b['n']}  public={b['public']} member={b['member']}  ({types})")
    print("=== 可见性 ===")
    print(f"  public: {sum(1 for r in records if r['visibility']=='public')}")
    print(f"  member: {sum(1 for r in records if r['visibility']=='member')}")
    print(f"  合计: {len(records)}")


def main() -> int:
    if not CONFIG_PATH.is_file():
        print(f"缺少 {CONFIG_PATH}", file=sys.stderr)
        return 2
    config = load_yaml(CONFIG_PATH)
    if not config or not config.get("people"):
        print("people.yaml 里没有 people", file=sys.stderr)
        return 2

    records = scan_all(config)
    generated_at = now_beijing()
    write_csv(records)
    write_index(config, records, generated_at)

    by_slug: dict[str, list[dict]] = defaultdict(list)
    for r in records:
        by_slug[r["person_slug"]].append(r)
    for person in config["people"]:
        update_person_card(person, by_slug.get(person["slug"], []))

    # 校验 yaml 解析是否把 sources 吃全
    expected_people = {p["name"] for p in config["people"]}
    seen = {r["source_person"] for r in records}
    missing = expected_people - seen
    if missing:
        print(f"警告: 配置了但没有扫到材料的人: {missing}", file=sys.stderr)

    print_report(records)
    print(f"wrote {INDEX_MD.relative_to(ROOT)}, {CSV_PATH.relative_to(ROOT)}, people/* 材料清单")
    print(f"beijing time: {generated_at}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
