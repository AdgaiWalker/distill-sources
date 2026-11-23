#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 distill-sources 的原始数据，生成或增量更新 manifest.jsonl。

不移动、不改名、不改写任何原料。默认增量：同一 id 且 sha256 未变时，
保留已有条目里可能被人工改过的 kind、context_tags、license_status。

用法（在仓库根目录）：

    python3 tools/build_manifest.py
    python3 tools/build_manifest.py --full
    python3 tools/build_manifest.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpusutil import (
    HOLDOUT_DIR_REL,
    KINDS,
    LICENSE_STATUSES,
    MANIFEST_PATH,
    PEOPLE_YAML,
    ROOT,
    SEALED_MD,
    X_POSTS_CSV,
    X_POST_TYPE_KIND,
    date_from_mdy_prefix,
    extract_date_from_text_or_name,
    extract_source_url,
    fetched_to_beijing,
    license_from_visibility,
    load_manifest,
    load_yaml,
    make_record,
    now_beijing,
    parse_sealed_files,
    read_text_head,
    rel_posix,
    sealed_window,
    sha256_file,
    sha256_json,
    tree_hash,
    validate_manifest,
    write_manifest,
)

PRESERVE_FIELDS = ("kind", "context_tags", "license_status")


def x_archives_from_people(config: dict) -> dict[str, dict]:
    """slug -> {name, path, visibility} for x-archive sources."""
    out = {}
    for person in config.get("people") or []:
        for src in person.get("sources") or []:
            if src.get("source_type") == "x" or src.get("scanner") == "x-archive":
                out[person["slug"]] = {
                    "name": person["name"],
                    "path": src["path"],
                    "visibility": src.get("visibility") or "public",
                }
    return out


def load_all_posts(archive_dir: Path) -> tuple[dict, str]:
    raw = archive_dir / "raw" / "all_posts.json"
    if not raw.is_file():
        return {}, ""
    data = json.loads(raw.read_text(encoding="utf-8"))
    posts = {}
    for p in data.get("data") or []:
        if isinstance(p, dict) and p.get("id"):
            posts[str(p["id"])] = p
    fetched = ""
    for key in ("fetched_at_bj", "fetched_at_beijing", "fetched_at_et", "fetched_at"):
        if data.get(key):
            fetched = fetched_to_beijing(str(data[key]))
            if fetched:
                break
    return posts, fetched


def scan_x(config: dict) -> list[dict]:
    if not X_POSTS_CSV.is_file():
        print(f"警告: 找不到 {X_POSTS_CSV}，跳过 X 帖。请先跑 python3 scripts/tag_x.py", file=sys.stderr)
        return []
    archives = x_archives_from_people(config)
    # name or slug -> slug
    name_to_slug = {}
    for person in config.get("people") or []:
        name_to_slug[person["name"]] = person["slug"]
        name_to_slug[person["slug"]] = person["slug"]

    posts_cache: dict[str, tuple[dict, str]] = {}
    rows = []
    with X_POSTS_CSV.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            who = row.get("人") or ""
            slug = name_to_slug.get(who)
            if not slug:
                print(f"警告: x-posts.csv 中未识别的人 {who!r}，跳过 id={row.get('id')}", file=sys.stderr)
                continue
            info = archives.get(slug) or {"path": f"{slug}/x-archive", "visibility": "public"}
            archive_dir = ROOT / info["path"]
            if slug not in posts_cache:
                posts_cache[slug] = load_all_posts(archive_dir)
            posts, fetched_at = posts_cache[slug]
            pid = str(row.get("id") or "")
            post = posts.get(pid) or {}
            post_type = row.get("post_type") or ""
            kind = X_POST_TYPE_KIND.get(post_type, "unknown")
            source_url = row.get("链接") or post.get("url") or ""
            date = row.get("日期") or ""
            raw_path = (archive_dir / "raw" / "all_posts.json")
            path = rel_posix(raw_path) if raw_path.is_file() else (row.get("文件") or rel_posix(archive_dir))
            if post:
                digest = sha256_json(post)
            elif raw_path.is_file():
                digest = sha256_file(raw_path)
            else:
                digest = sha256_json({"id": pid, "row": row})
            tags = ["platform:x"]
            if post_type:
                tags.append(f"post_type:{post_type}")
            rows.append(
                make_record(
                    id=f"{slug}:x:{pid}",
                    person=slug,
                    platform="x",
                    kind=kind,
                    date=date,
                    source_url=source_url,
                    path=path,
                    sha256=digest,
                    license_status=license_from_visibility(info.get("visibility")),
                    context_tags=tags,
                    fetched_at=fetched_at,
                    holdout=False,
                )
            )
    return rows


def scan_wechat(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    if not base.is_dir():
        return []
    vis = license_from_visibility(src.get("visibility"))
    rows = []
    for p in sorted(base.glob("*.md")):
        if not p.is_file():
            continue
        text = read_text_head(p, 3000)
        date = extract_date_from_text_or_name(p, text)
        url = extract_source_url(text)
        rows.append(
            make_record(
                id=f"{person['slug']}:wechat:{p.stem}",
                person=person["slug"],
                platform="wechat",
                kind="said",
                date=date,
                source_url=url,
                path=rel_posix(p),
                sha256=sha256_file(p),
                license_status=vis,
                context_tags=["platform:wechat"],
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def scan_group_chat(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    if not base.exists():
        return []
    vis = license_from_visibility(src.get("visibility"))
    rows = []
    for p in sorted(base.glob("*.md")):
        if not p.is_file():
            continue
        text = read_text_head(p, 3000)
        date = extract_date_from_text_or_name(p, text)
        rows.append(
            make_record(
                id=f"{person['slug']}:group-chat:{p.stem}",
                person=person["slug"],
                platform="group-chat",
                kind="said",
                date=date,
                source_url="",
                path=rel_posix(p),
                sha256=sha256_file(p),
                license_status=vis,
                context_tags=["platform:group-chat", "stage:会员群现场发言"],
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def scan_notes(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    if not base.exists():
        return []
    vis = license_from_visibility(src.get("visibility"))
    pattern = src.get("glob") or "*.md"
    rows = []
    files = [base] if base.is_file() else sorted(base.glob(pattern))
    for p in files:
        if not p.is_file():
            continue
        text = read_text_head(p, 3000)
        date = extract_date_from_text_or_name(p, text)
        rows.append(
            make_record(
                id=f"{person['slug']}:notes:{p.stem}",
                person=person["slug"],
                platform="notes",
                kind="said",
                date=date,
                source_url=extract_source_url(text),
                path=rel_posix(p),
                sha256=sha256_file(p),
                license_status=vis,
                context_tags=["platform:notes"],
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def scan_feishu(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    md_dir = base / "md"
    if not md_dir.is_dir():
        return []
    vis = license_from_visibility(src.get("visibility"))
    rows = []
    skip_names = {"README.md", "目录.md"}
    for p in sorted(md_dir.iterdir()):
        if not p.is_file() or p.name in skip_names:
            continue
        if p.suffix.lower() not in {".md", ".csv"}:
            continue
        text = read_text_head(p, 4000) if p.suffix.lower() == ".md" else ""
        # 文件名 MM-DD 的 9 篇，封存说明写明年份是 2026。
        date = date_from_mdy_prefix(p.name, 2026) or extract_date_from_text_or_name(p, text)
        # 仅当文件是工具表 csv，或标题用「工具｜」标明是表单/清单时，才标 did。
        # 标题里偶尔出现「工具」一词的文章仍是 said，不准扩大推断。
        if p.suffix.lower() == ".csv" or "工具｜" in p.name:
            kind = "did"
            tags = ["platform:feishu", "kind-hint:工具表"]
        else:
            kind = "said"
            tags = ["platform:feishu"]
        url = extract_source_url(text) if text else ""
        rows.append(
            make_record(
                id=f"{person['slug']}:feishu:{p.stem}",
                person=person["slug"],
                platform="feishu",
                kind=kind,
                date=date,
                source_url=url,
                path=rel_posix(p),
                sha256=sha256_file(p),
                license_status=vis,
                context_tags=tags,
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def scan_github_seed(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    if not base.is_dir():
        return []
    vis = license_from_visibility(src.get("visibility"))
    files: list[Path] = sorted(base.glob("*.md")) + sorted(base.glob("*.py"))
    for sub in ("公众号", "哥飞"):
        d = base / sub
        if d.is_dir():
            files.extend(sorted(p for p in d.iterdir() if p.is_file() and p.suffix.lower() in {".md", ".txt"}))
    rows = []
    for p in files:
        text = read_text_head(p, 3000)
        date = extract_date_from_text_or_name(p, text)
        if p.suffix == ".py":
            kind = "did"
            tags = ["platform:github", "github-seed", "kind-hint:脚本"]
        else:
            kind = "said"
            tags = ["platform:github", "github-seed"]
        rel = rel_posix(p)
        rows.append(
            make_record(
                id=f"{person['slug']}:github:{rel}",
                person=person["slug"],
                platform="github",
                kind=kind,
                date=date,
                source_url=extract_source_url(text),
                path=rel,
                sha256=sha256_file(p),
                license_status=vis,
                context_tags=tags,
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def read_upstream_url(repo: Path) -> str:
    p = repo / "UPSTREAM.md"
    if not p.is_file():
        return ""
    text = read_text_head(p, 2000)
    import re

    m = re.search(r"origin：\s*(\S+)", text)
    return m.group(1).rstrip("。") if m else ""


def scan_github_repos(person: dict, src: dict) -> list[dict]:
    base = ROOT / src["path"]
    if not base.is_dir():
        return []
    vis = license_from_visibility(src.get("visibility"))
    rows = []
    for repo in sorted(base.iterdir()):
        if not repo.is_dir() or repo.name.startswith("."):
            continue
        url = read_upstream_url(repo)
        rel = rel_posix(repo)
        rows.append(
            make_record(
                id=f"{person['slug']}:github-repo:{repo.name}",
                person=person["slug"],
                platform="github",
                kind="other",  # 他人整理的资料仓，不是本人一手表述或产物
                date="",
                source_url=url,
                path=rel + "/",
                sha256=tree_hash(repo),
                license_status=vis,
                context_tags=["platform:github", "github-member-repo"],
                fetched_at="",
                holdout=False,
            )
        )
    return rows


def scan_source(person: dict, src: dict) -> list[dict]:
    st = src.get("source_type") or ""
    scanner = src.get("scanner") or "files"
    if scanner == "x-archive" or st == "x":
        return []  # 统一由 scan_x 处理
    if st == "wechat":
        return scan_wechat(person, src)
    if st == "group-chat":
        return scan_group_chat(person, src)
    if st == "feishu":
        return scan_feishu(person, src)
    if st == "notes":
        return scan_notes(person, src)
    if scanner == "github-seed":
        return scan_github_seed(person, src)
    if scanner == "repos":
        return scan_github_repos(person, src)
    if scanner == "files":
        # 未单独分类的 files：按笔记处理
        return scan_notes(person, src)
    print(f"警告: 未处理的来源 {person.get('slug')} {src.get('path')} scanner={scanner} type={st}", file=sys.stderr)
    return []


def merge_incremental(old_rows: list[dict], new_rows: list[dict], full: bool) -> list[dict]:
    if full or not old_rows:
        return new_rows
    old_by_id = {r["id"]: r for r in old_rows if r.get("id")}
    merged = []
    for rec in new_rows:
        prev = old_by_id.get(rec["id"])
        if prev and prev.get("sha256") == rec.get("sha256"):
            keep = dict(rec)
            for field in PRESERVE_FIELDS:
                if field in prev and prev[field] not in (None, "", [], "unknown", "未知"):
                    # 仅当旧值看起来像人工改过、或至少有值时保留。
                    # holdout 以本次计算结果为准。
                    if prev[field] != rec.get(field):
                        keep[field] = prev[field]
            merged.append(keep)
        else:
            merged.append(rec)
    return merged


def main() -> int:
    parser = argparse.ArgumentParser(description="生成或增量更新 manifest.jsonl")
    parser.add_argument("--full", action="store_true", help="忽略已有清单，全量重建")
    parser.add_argument("--dry-run", action="store_true", help="只打印统计，不写文件")
    args = parser.parse_args()

    if not PEOPLE_YAML.is_file():
        raise SystemExit(f"找不到 {PEOPLE_YAML}")
    config = load_yaml(PEOPLE_YAML)

    rows: list[dict] = []
    for person in config.get("people") or []:
        for src in person.get("sources") or []:
            rows.extend(scan_source(person, src))
    rows.extend(scan_x(config))

    # 去重（同一 id 不应出现两次）
    by_id: dict[str, dict] = {}
    for rec in rows:
        if rec["id"] in by_id:
            print(f"警告: 重复 id，后写覆盖前写: {rec['id']}", file=sys.stderr)
        by_id[rec["id"]] = rec
    rows = list(by_id.values())

    old = [] if args.full else load_manifest()
    rows = merge_incremental(old, rows, full=args.full)

    errors = validate_manifest(rows)
    if errors:
        print(f"jsonschema 校验失败 {len(errors)} 条：", file=sys.stderr)
        for e in errors[:20]:
            print("  ", e, file=sys.stderr)
        return 1

    from collections import Counter

    kinds = Counter(r["kind"] for r in rows)
    unknown = kinds.get("unknown", 0)
    holdout_n = sum(1 for r in rows if r.get("holdout"))
    print(f"manifest 条目 {len(rows)}；holdout {holdout_n}；kind 分布 {dict(kinds)}；unknown {unknown}（{unknown / len(rows):.1%}）")
    if not args.dry_run:
        write_manifest(rows)
        print(f"wrote {MANIFEST_PATH.relative_to(ROOT)}  {now_beijing()} 北京时间")
    else:
        print("dry-run，未写入")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
