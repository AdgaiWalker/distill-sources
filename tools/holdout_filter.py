#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把封存窗口内的原文从公开仓移除（只按日期和文件名判断，不读正文）。

封存原文在私有仓 AdgaiWalker/distill-lab，考完后再公开。抓取同步可能把封存帖带回来，
所以 refresh 每次都会先跑本脚本。可重复运行；没有要移除的内容时什么都不改。

    python3 tools/holdout_filter.py            # 执行
    python3 tools/holdout_filter.py --dry-run  # 只统计
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BJ = dt.timezone(dt.timedelta(hours=8))

# 每批封存一项。窗口为北京时间，含起止日。规则与哈希见 HOLDOUT.md。
HOLDOUTS = [
    {
        "person": "bbkirstry",
        "user_id": "1923981862273417222",
        "window": ("2026-09-23", "2026-11-23"),
        "x_archive": "bbkirstry/x-archive",
        "feishu_kb": "bbkirstry/feishu-kb",
        "feishu_stems": [
            "09-23 重新理解「组局」和线下社交",
            "09-25 生财有术 杨涛线下答疑分享会｜小晚分享版",
            "09-25 生财有术 杨涛线下答疑分享会｜知识库版",
            "09-27 和前辈的内容、AI 与个人 IP交流",
            "10-10 商业价值创造与增长的底层逻辑",
            "11-16 写给所有正在 AI 时代寻找自己的人",
            "11-17 我开始觉得，AI 时代的一人公司，真的要来了",
            "11-18 ChatGPT保姆级写作教程｜很多人根本没搞懂 AI 写作这件事",
            "11-20 为什么别人的 ChatGPT 越聊越聪明，你的却总是听不懂人话？",
        ],
    }
]

DATE_RE = re.compile(r"(20\d{2}-\d{2}-\d{2})")


def in_window(day: str, win: tuple[str, str]) -> bool:
    return bool(day) and win[0] <= day <= win[1]


def bj_day(created_at: str) -> str:
    try:
        t = dt.datetime.fromisoformat(created_at.replace("Z", "+00:00"))
    except ValueError:
        return ""
    return t.astimezone(BJ).date().isoformat()


def is_sealed_tweet(t, h) -> bool:
    return (
        isinstance(t, dict)
        and str(t.get("author_id", "")) == h["user_id"]
        and in_window(bj_day(str(t.get("created_at", ""))), h["window"])
    )


def filter_json(path: Path, h, dry: bool) -> int:
    raw = path.read_text(encoding="utf-8")
    try:
        obj = json.loads(raw)
    except json.JSONDecodeError:
        return 0
    removed = 0

    def walk(o):
        nonlocal removed
        if isinstance(o, dict):
            for k, v in list(o.items()):
                if k in ("data", "tweets") and isinstance(v, list):
                    keep = [t for t in v if not is_sealed_tweet(t, h)]
                    removed += len(v) - len(keep)
                    o[k] = keep
                    for t in keep:
                        walk(t)
                else:
                    walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(obj)
    if removed and not dry:
        indent = 2 if raw.startswith("{\n  ") or raw.startswith("[\n  ") else None
        path.write_text(json.dumps(obj, ensure_ascii=False, indent=indent) + ("\n" if raw.endswith("\n") else ""), encoding="utf-8")
    return removed


def filter_md_blocks(path: Path, h, dry: bool) -> int:
    """all.md：按「## YYYY-MM-DD」分块，删掉窗口内的块。"""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out, removed, skipping = [], 0, False
    for ln in lines:
        if ln.startswith("## "):
            m = DATE_RE.match(ln[3:])
            skipping = bool(m and in_window(m.group(1), h["window"]))
            removed += skipping
        if not skipping:
            out.append(ln)
    if removed and not dry:
        path.write_text("".join(out), encoding="utf-8")
    return removed


def filter_index_table(path: Path, h, dry: bool) -> int:
    """index.md：删掉表格里日期落在窗口内的行。"""
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    out, removed = [], 0
    for ln in lines:
        m = DATE_RE.match(ln[2:]) if ln.startswith("| ") else None
        if m and in_window(m.group(1), h["window"]):
            removed += 1
            continue
        out.append(ln)
    if removed and not dry:
        path.write_text("".join(out), encoding="utf-8")
    return removed


def remove(path: Path, dry: bool) -> int:
    if not path.exists():
        return 0
    if not dry:
        shutil.rmtree(path) if path.is_dir() else path.unlink()
    return 1


def run(dry: bool = False) -> dict:
    stats = {"x_posts": 0, "all_md_blocks": 0, "index_rows": 0, "articles": 0, "feishu_files": 0}
    for h in HOLDOUTS:
        xa = ROOT / h["x_archive"]
        if xa.is_dir():
            for f in sorted((xa / "raw").glob("*.json")):
                n = filter_json(f, h, dry)
                if f.name == "all_posts.json":
                    stats["x_posts"] += n
            if (xa / "all.md").is_file():
                stats["all_md_blocks"] += filter_md_blocks(xa / "all.md", h, dry)
            if (xa / "index.md").is_file():
                stats["index_rows"] += filter_index_table(xa / "index.md", h, dry)
            for f in sorted((xa / "articles").glob("*.md")):
                m = DATE_RE.match(f.name)
                if m and in_window(m.group(1), h["window"]):
                    stats["articles"] += remove(f, dry)
        kb = ROOT / h["feishu_kb"]
        for stem in h["feishu_stems"]:
            for p in (kb / f"{stem}.docx", kb / f"{stem}.md", kb / "md" / f"{stem}.md", kb / "md" / "media" / stem):
                stats["feishu_files"] += remove(p, dry)
    return stats


def main() -> int:
    ap = argparse.ArgumentParser(description="从公开仓移除封存窗口内的原文")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    stats = run(args.dry_run)
    print(json.dumps(stats, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
