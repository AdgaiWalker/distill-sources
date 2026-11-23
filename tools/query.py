#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检索原文。在仓库根目录运行：

    python3 tools/query.py 新词 --person gefei              # 标题命中在前，本人原文在前
    python3 tools/query.py 新词 判断 --person gefei --brief  # 多个词同时命中；只看日期、来源、标题、路径
    python3 tools/query.py 个人IP --person bbkirstry --json  # 给 Agent 用
    python3 tools/query.py --person gefei --since 2026-01-01 --platform wechat

排序：标题命中 > 只有正文命中；本人原文 > 转述他人 > 多人对话/说话人待定 > 他人汇编 > 他人内容；同档按日期从新到旧。
没有命中或人名写错时退出码非 0，并给出 ls / rg 兜底命令。
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpusutil import MANIFEST_PATH, ORIGIN_LABELS, PEOPLE_YAML, ROOT, load_manifest, load_yaml

ORIGIN_RANK = {"self": 0, "quoted": 1, "mixed": 2, "uncertain": 2, "compiled": 3, "other": 4}
SNIPPET_CHARS = 240
_post_cache: dict[str, dict[str, str]] = {}


def post_texts(path: Path) -> dict[str, str]:
    key = str(path)
    if key not in _post_cache:
        out: dict[str, str] = {}
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            data = {}
        for p in data.get("data") or []:
            if not isinstance(p, dict) or not p.get("id"):
                continue
            art = p.get("article") or {}
            note = p.get("note_tweet") or p.get("note_post") or {}
            if isinstance(art, dict) and art.get("plain_text"):
                txt = f"{art.get('title') or ''}\n{art['plain_text']}"
            elif isinstance(note, dict) and note.get("text"):
                txt = note["text"]
            else:
                txt = p.get("text") or ""
            out[str(p["id"])] = txt
        _post_cache[key] = out
    return _post_cache[key]


def body_of(rec: dict) -> str:
    full = ROOT / (rec.get("path") or "").rstrip("/")
    if rec.get("platform") == "x" and full.suffix == ".json":
        return post_texts(full).get(rec["id"].rsplit(":", 1)[-1], "")
    if full.is_dir():
        for name in ("README.md", "readme.md", "UPSTREAM.md"):
            if (full / name).is_file():
                full = full / name
                break
    if full.is_file() and full.suffix.lower() in {".md", ".txt", ".csv", ".py"}:
        try:
            return full.read_text(encoding="utf-8", errors="replace")
        except OSError:
            return ""
    return ""


def snippet(text: str, terms: list[str]) -> str:
    flat = " ".join(text.split())
    if not flat:
        return ""
    idx = -1
    low = flat.lower()
    for t in terms:
        idx = low.find(t.lower())
        if idx >= 0:
            break
    start = max(0, idx - 60) if idx >= 0 else 0
    chunk = flat[start : start + SNIPPET_CHARS]
    return ("…" if start else "") + chunk + ("…" if start + SNIPPET_CHARS < len(flat) else "")


def norm_title(s: str | None) -> str:
    import re

    return re.sub(r"[\W_\d]+", "", s or "")


def fallback_hint(args, people: list[str]) -> str:
    word = " ".join(args.terms) or "关键词"
    w = word.split()[0]
    ls_scope, rg_scope = (f"{args.person}/*/", f"{args.person}/") if args.person else ("*/*/", ".")
    return (
        f"兜底：ls {ls_scope} | grep {w}   （文件名就是标题）\n"
        f"      rg -l {w} {rg_scope}   （全文搜索）\n"
        f"合法人名：{', '.join(people)}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="检索原文：标题命中在前，本人原文在前")
    ap.add_argument("terms", nargs="*", help="关键词，可写多个（需全部命中）")
    ap.add_argument("--q", action="append", default=[], help="关键词（同位置参数，兼容旧用法）")
    ap.add_argument("--person", help="人物 slug，如 gefei、bbkirstry")
    ap.add_argument("--platform", help="wechat / x / feishu / group-chat / github / notes")
    ap.add_argument("--kind", help="said / did / corrected / rejected / other / unknown")
    ap.add_argument("--origin", help="self / quoted / mixed / compiled / other / uncertain")
    ap.add_argument("--since", help="起始日期 YYYY-MM-DD（含）")
    ap.add_argument("--until", help="截止日期 YYYY-MM-DD（含）")
    ap.add_argument("--brief", action="store_true", help="每条一行：日期、来源、标题、路径")
    ap.add_argument("--json", action="store_true", help="输出 JSON")
    ap.add_argument("--limit", type=int, default=20, help="最多显示条数，默认 20；0 表示全部")
    ap.add_argument("--manifest", default=str(MANIFEST_PATH))
    args = ap.parse_args()
    args.terms = [t for t in args.terms + args.q if t.strip()]

    manifest = Path(args.manifest)
    rows = load_manifest(manifest)
    people = [p["slug"] for p in (load_yaml(PEOPLE_YAML).get("people") or [])] if PEOPLE_YAML.is_file() else []
    if not rows:
        print(f"找不到清单 {manifest}。先跑：python3 tools/refresh.py", file=sys.stderr)
        print(fallback_hint(args, people), file=sys.stderr)
        return 2
    if args.person and args.person not in people:
        print(f"没有这个人：{args.person}", file=sys.stderr)
        print(fallback_hint(argparse.Namespace(terms=args.terms, person=None), people), file=sys.stderr)
        return 2

    hits = []
    for rec in rows:
        if args.person and rec.get("person") != args.person:
            continue
        if args.platform and rec.get("platform") != args.platform:
            continue
        if args.kind and rec.get("kind") != args.kind:
            continue
        if args.origin and rec.get("origin") != args.origin:
            continue
        d = rec.get("date") or ""
        if (args.since and (not d or d < args.since)) or (args.until and (not d or d > args.until)):
            continue
        title = rec.get("title") or ""
        body = ""
        if args.terms:
            tl = title.lower()
            in_title = [t for t in args.terms if t.lower() in tl]
            if len(in_title) < len(args.terms):
                body = body_of(rec)
                hay = (title + "\n" + body + "\n" + (rec.get("path") or "")).lower()
                if not all(t.lower() in hay for t in args.terms):
                    continue
            score = 0 if len(in_title) == len(args.terms) else (1 if in_title else 2)
        else:
            score = 0
        hits.append((score, ORIGIN_RANK.get(rec.get("origin"), 2), d, rec, body))

    hits.sort(key=lambda h: (h[0], h[1], "" if h[2] else "~", -int(h[2].replace("-", "") or 0)))
    # 他人汇编里与本人原文同名的副本（如 github-seed 里的公众号导出）折叠掉
    own_titles = {norm_title(h[3].get("title")) for h in hits if h[3].get("origin") == "self"}
    folded = [h for h in hits if h[3].get("origin") == "compiled" and norm_title(h[3].get("title")) in own_titles]
    if folded:
        fold_ids = {id(h) for h in folded}
        hits = [h for h in hits if id(h) not in fold_ids]
    total = len(hits)
    shown = hits if args.limit == 0 else hits[: args.limit]

    if total == 0:
        print("没有命中。", file=sys.stderr)
        print(fallback_hint(args, people), file=sys.stderr)
        if args.json:
            print("[]")
        return 1

    if args.json:
        out = []
        for _, _, _, rec, body in shown:
            item = {k: rec.get(k) for k in ("id", "person", "platform", "kind", "origin", "date", "title", "path", "source_url")}
            item["origin_label"] = ORIGIN_LABELS.get(rec.get("origin"), "")
            if not args.brief:
                item["snippet"] = snippet(body or body_of(rec), args.terms)
            out.append(item)
        print(json.dumps({"total": total, "shown": len(out), "folded_copies": len(folded), "results": out}, ensure_ascii=False, indent=1))
        return 0

    print(
        f"# 共 {total} 条，显示 {len(shown)} 条"
        + ("（--limit 0 看全部）" if len(shown) < total else "")
        + (f"；另有 {len(folded)} 条他人汇编副本与原文同名，已折叠" if folded else "")
    )
    for _, _, d, rec, body in shown:
        label = ORIGIN_LABELS.get(rec.get("origin"), "")
        if args.brief:
            print(f"{d or '无日期'}  {rec.get('platform')}  [{label}]  {rec.get('title')}  {rec.get('path')}")
            continue
        print(f"\n--- {rec.get('title')}")
        print(f"{rec.get('person')} · {rec.get('platform')} · {label} · {d or '无日期'}")
        print(f"路径: {rec.get('path')}")
        if rec.get("source_url"):
            print(f"链接: {rec.get('source_url')}")
        sn = snippet(body or body_of(rec), args.terms)
        if sn:
            print(sn)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
