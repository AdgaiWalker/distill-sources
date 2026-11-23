#!/usr/bin/env python3
"""在成功抓取新原料后记录最近抓取时间（北京时间）。

用法（在仓库根目录）：

    python3 scripts/record_fetch.py
    python3 scripts/record_fetch.py --source "本次抓取说明"
    python3 scripts/record_fetch.py --time "2026-11-23 04:01" --source "历史记录说明"

写出 [index/last-fetch.txt](../index/last-fetch.txt)。不要把当前时间手写进 README；
随后请跑 `tag_x.py`、`classify.py`、`stats.py`，由 `stats.py` 把本文件中的时间
写到 README 标题下的「最近抓取时间」。

四天一次的定时更新在成功抓取（公众号、X 或 GitHub 资料有新内容入库）后
应先跑本脚本，再生成统计。无新内容时不要刷新时间。
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAST_FETCH = ROOT / "index" / "last-fetch.txt"
BJ = dt.timezone(dt.timedelta(hours=8))
TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")


def now_beijing() -> str:
    return dt.datetime.now(BJ).strftime("%Y-%m-%d %H:%M")


def write_last_fetch(time_str: str, source: str) -> None:
    if not TIME_RE.match(time_str):
        raise SystemExit(f"时间格式应为 YYYY-MM-DD HH:MM，收到：{time_str}")
    LAST_FETCH.parent.mkdir(parents=True, exist_ok=True)
    source_line = source.strip() or "scripts/record_fetch.py 在成功抓取后写入"
    text = (
        f"{time_str}\n"
        f"timezone: Asia/Shanghai\n"
        f"source: {source_line}\n"
    )
    LAST_FETCH.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="记录最近抓取时间（北京时间）")
    parser.add_argument(
        "--time",
        help="北京时间 YYYY-MM-DD HH:MM；缺省则用当前北京时间",
    )
    parser.add_argument(
        "--source",
        default="scripts/record_fetch.py 在成功抓取后写入",
        help="时间数据来源说明，写入 last-fetch.txt",
    )
    args = parser.parse_args()
    time_str = args.time or now_beijing()
    write_last_fetch(time_str, args.source)
    print(f"wrote {LAST_FETCH.relative_to(ROOT)}: {time_str} 北京时间")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
