#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按人、时间、类型、平台、关键词检索原料。默认排除封存验证区。

用法（在仓库根目录）：

    python3 tools/query.py --person bbkirstry --kind said --q 定位
    python3 tools/query.py --person gefei --since 2026-01-01 --until 2026-03-31 --platform wechat
    python3 tools/query.py --person bbkirstry --q 个人IP --json
    python3 tools/query.py --include-holdout --person bbkirstry --since 2026-09-23 --limit 5
"""

from __future__ import annotations

import argparse
import json
import sys
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpusutil import (
    HOLDOUT_DIR_REL,
    MANIFEST_PATH,
    ROOT,
    load_manifest,
)

DEFAULT_LIMIT = 20
SNIPPET_CHARS = 400


def in_date_range(date: str, since: str | None, until: str | None) -> bool:
    if since and (not date or date < since):
        return False
    if until and (not date or date > until):
        return False
    return True


@lru_cache(maxsize=8)
def load_posts(json_path: str) -> dict[str, dict]:
    data = json.loads(Path(json_path).read_text(encoding="utf-8"))
    posts = {}
    for p in data.get("data") or []:
        if isinstance(p, dict) and p.get("id"):
            posts[str(p["id"])] = p
    return posts


def post_text(post: dict) -> str:
    article = post.get("article") or {}
    if isinstance(article, dict) and article.get("plain_text"):
        title = article.get("title") or post.get("article_title") or ""
        body = article["plain_text"]
        return f"{title}\n{body}".strip() if title else body
    note = post.get("note_tweet") or post.get("note_post") or {}
    if isinstance(note, dict) and note.get("text"):
        return note["text"]
    return post.get("text") or ""


def is_holdout_path(path: str) -> bool:
    return path.replace("\\", "/").startswith(HOLDOUT_DIR_REL + "/") or path.replace("\\", "/") == HOLDOUT_DIR_REL


def extract_text(rec: dict, include_holdout: bool) -> str:
    path = rec.get("path") or ""
    # 默认不读取封存目录里的正文
    if is_holdout_path(path) and not include_holdout:
        return ""
    full = ROOT / path.rstrip("/")
    # X 帖：从 all_posts.json 按 id 取正文
    if rec.get("platform") == "x" and rec.get("id", "").count(":") >= 2 and full.suffix == ".json":
        # id 形如 slug:x:tweetid；封存副本 posts_enriched 不在这里拆
        if full.name == "all_posts.json" and full.is_file():
            pid = rec["id"].rsplit(":", 1)[-1]
            post = load_posts(str(full)).get(pid)
            if post:
                return post_text(post)
        if full.name == "posts_enriched.json":
            return ""  # 即使 include-holdout，也不在检索里展开整个封存 JSON
    if full.is_file() and full.suffix.lower() in {".md", ".txt", ".csv", ".py"}:
        try:
            return full.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
    if full.is_dir():
        for name in ("README.md", "readme.md", "UPSTREAM.md"):
            p = full / name
            if p.is_file():
                try:
                    return p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    return ""
    return ""


def snippet(text: str, query: str | None, limit: int = SNIPPET_CHARS) -> str:
    if not text:
        return ""
    compact = " ".join(text.split())
    if not query:
        return compact[:limit] + ("…" if len(compact) > limit else "")
    # 取第一次命中附近
    lower = text.lower()
    q = query.lower()
    idx = lower.find(q)
    if idx < 0:
        return compact[:limit] + ("…" if len(compact) > limit else "")
    start = max(0, idx - 80)
    chunk = text[start : start + limit + 80]
    chunk = " ".join(chunk.split())
    prefix = "…" if start > 0 else ""
    suffix = "…" if start + limit + 80 < len(text) else ""
    return prefix + chunk[:limit] + (suffix if len(chunk) > limit else "")


def matches_query(text: str, rec: dict, query: str) -> bool:
    q = query.lower()
    hay = " ".join(
        [
            rec.get("id") or "",
            rec.get("path") or "",
            rec.get("source_url") or "",
            " ".join(rec.get("context_tags") or []),
            text or "",
        ]
    ).lower()
    return q in hay


def search(rows: list[dict], args) -> list[dict]:
    out = []
    for rec in rows:
        if not args.include_holdout and rec.get("holdout"):
            continue
        if args.person and rec.get("person") != args.person:
            continue
        if args.kind and rec.get("kind") != args.kind:
            continue
        if args.platform and rec.get("platform") != args.platform:
            continue
        if not in_date_range(rec.get("date") or "", args.since, args.until):
            continue
        text = extract_text(rec, include_holdout=args.include_holdout)
        if args.q and not matches_query(text, rec, args.q):
            continue
        out.append((rec, text))
        if args.limit and len(out) >= args.limit:
            break
    return out


def format_human(pairs: list[tuple[dict, str]], query: str | None) -> str:
    blocks = []
    for rec, text in pairs:
        lines = [
            f"--- {rec.get('id')}",
            f"{rec.get('person')}  {rec.get('platform')}  {rec.get('kind')}  {rec.get('date') or '（无日期）'}"
            + ("  [holdout]" if rec.get("holdout") else ""),
            f"路径: {rec.get('path')}",
        ]
        if rec.get("source_url"):
            lines.append(f"链接: {rec.get('source_url')}")
        snip = snippet(text, query)
        if snip:
            lines.append(snip)
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks) + ("\n" if blocks else "")


def format_json(pairs: list[tuple[dict, str]], query: str | None) -> str:
    items = []
    for rec, text in pairs:
        items.append(
            {
                "id": rec.get("id"),
                "person": rec.get("person"),
                "platform": rec.get("platform"),
                "kind": rec.get("kind"),
                "date": rec.get("date"),
                "source_url": rec.get("source_url"),
                "path": rec.get("path"),
                "holdout": bool(rec.get("holdout")),
                "snippet": snippet(text, query),
            }
        )
    return json.dumps(items, ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="检索原料清单，默认排除 holdout")
    parser.add_argument("--person", help="人物 slug，如 bbkirstry、gefei")
    parser.add_argument("--since", help="起始日期 YYYY-MM-DD（含）")
    parser.add_argument("--until", help="截止日期 YYYY-MM-DD（含）")
    parser.add_argument("--kind", help="said / did / corrected / rejected / other / unknown")
    parser.add_argument("--platform", help="wechat / x / feishu / group-chat / github / notes")
    parser.add_argument("--q", help="关键词，匹配正文、路径、链接、标签")
    parser.add_argument("--json", action="store_true", dest="as_json", help="输出 JSON，供 Agent 调用")
    parser.add_argument("--include-holdout", action="store_true", help="包含封存验证区（默认排除）")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help=f"最多返回条数，默认 {DEFAULT_LIMIT}；0 表示不限制")
    parser.add_argument("--manifest", default=str(MANIFEST_PATH))
    args = parser.parse_args()

    manifest = Path(args.manifest)
    if not manifest.is_file():
        raise SystemExit(f"找不到 {manifest}，请先跑 python3 tools/build_manifest.py")
    rows = load_manifest(manifest)
    pairs = search(rows, args)
    if args.as_json:
        sys.stdout.write(format_json(pairs, args.q))
    else:
        if not pairs:
            print("没有匹配的条目。", file=sys.stderr)
        else:
            sys.stdout.write(format_human(pairs, args.q))
        print(f"# {len(pairs)} 条（默认已排除 holdout）" if not args.include_holdout else f"# {len(pairs)} 条", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
