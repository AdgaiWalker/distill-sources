#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""按人统计原料覆盖率，写出 COVERAGE.md；超阈值时以非 0 退出码报警。

用法（在仓库根目录）：

    python3 tools/coverage.py
    python3 tools/coverage.py --manifest manifest.jsonl --output COVERAGE.md
"""

from __future__ import annotations

import argparse
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from corpusutil import (
    BEIJING,
    KINDS,
    MANIFEST_PATH,
    PEOPLE_YAML,
    ROOT,
    load_manifest,
    load_yaml,
    now_beijing,
)

OUTPUT_PATH = ROOT / "COVERAGE.md"

# 报警阈值
GAP_DAYS = 30  # 相邻两条有日期的数据间隔，或距今超过这个天数，视为断档
MISSING_FIELD_RATIO = 0.20  # date 或 source_url 空缺比例超过此值报警
UNKNOWN_KIND_RATIO = 0.30  # kind=unknown 比例超过此值报警

PRIORITY_GAPS = (
    "现场问答的追问往返",
    "对新手的纠正",
    "带时间戳的产物数据",
)


def people_order(config: dict) -> list[tuple[str, str]]:
    return [(p["slug"], p["name"]) for p in config.get("people") or []]


def dated(rows: list[dict]) -> list[dt.date]:
    out = []
    for r in rows:
        d = r.get("date") or ""
        if d:
            try:
                out.append(dt.date.fromisoformat(d))
            except ValueError:
                pass
    return sorted(out)


def find_gaps(dates: list[dt.date], today: dt.date, gap_days: int = GAP_DAYS) -> list[tuple[dt.date, dt.date, int]]:
    """返回 (start, end, days) 断档。包含内部间隔，以及最后一条到今天。"""
    gaps = []
    if not dates:
        return gaps
    for a, b in zip(dates, dates[1:]):
        delta = (b - a).days
        if delta > gap_days:
            gaps.append((a, b, delta))
    trailing = (today - dates[-1]).days
    if trailing > gap_days:
        gaps.append((dates[-1], today, trailing))
    return gaps


def field_missing_ratio(rows: list[dict], field: str) -> float:
    if not rows:
        return 0.0
    n = sum(1 for r in rows if not r.get(field))
    return n / len(rows)


def kind_counts(rows: list[dict]) -> dict[str, int]:
    c = {k: 0 for k in KINDS}
    for r in rows:
        k = r.get("kind") or "unknown"
        c[k] = c.get(k, 0) + 1
    return c


def suggestions(slug: str, name: str, rows: list[dict], counts: dict[str, int]) -> list[str]:
    """按人列出该补哪类素材，优先三类。只根据数量与平台，不编造内容判断。"""
    tips: list[str] = []
    platforms = {r.get("platform") for r in rows}
    # 1. 现场问答的追问往返
    has_live = any(r.get("platform") == "group-chat" for r in rows)
    live_n = sum(1 for r in rows if r.get("platform") == "group-chat")
    if not has_live:
        tips.append("现场问答的追问往返：目前没有会员群、答疑现场的往返记录，只有事后写成的文章或帖子。建议补原始问答记录（含追问）。")
    elif live_n < 5:
        tips.append(f"现场问答的追问往返：现有会员群记录仅 {live_n} 条，覆盖很薄。建议补更多答疑往返，而不是再堆公开长文。")
    # 2. 对新手的纠正
    if counts.get("corrected", 0) == 0:
        tips.append("对新手的纠正：现有标签无法把这类条目标出来（回复一律记为 said，未再细分）。建议补带纠正对象的原始回复，或在增量更新时人工把能确定的条目标为 corrected。")
    # 3. 带时间戳的产物数据
    did_n = counts.get("did", 0)
    has_product_metrics = any(
        "产物" in " ".join(r.get("context_tags") or []) or "metrics" in " ".join(r.get("context_tags") or [])
        for r in rows
    )
    if did_n == 0 and not has_product_metrics:
        tips.append("带时间戳的产物数据：没有站点快照、排名或互动随时间变化的记录，也没有 kind=did 的产物。建议补带日期的产物与数据，而不是再收一轮表述类原文。")
    elif did_n and not has_product_metrics:
        tips.append(f"带时间戳的产物数据：有 {did_n} 条 kind=did（多为工具表或脚本），但缺少带时间戳的站点/排名/互动数据。建议补这一类，而不是再增加工具清单。")
    # 补充：rejected 也几乎必然为空，但不挤占优先三类的位置；可作附注
    if counts.get("rejected", 0) == 0:
        tips.append("（附）放弃或否定的内容：目前没有 kind=rejected 的条目。有依据时再标，不要事后猜测。")
    return tips


def md_escape(s: str) -> str:
    return (s or "").replace("|", "\\|").replace("\n", " ")


def render(config: dict, rows: list[dict], today: dt.date) -> tuple[str, list[str]]:
    by_person: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        by_person[r.get("person") or "?"].append(r)

    alarms: list[str] = []
    lines = [
        "# 原料覆盖率",
        "",
        f"由 [`tools/coverage.py`](tools/coverage.py) 根据 [`manifest.jsonl`](manifest.jsonl) 生成（{now_beijing()} 北京时间）。",
        "原文件未移动、未改内容。本报告只统计清单，不含会员内容原文。",
        "",
        "报警阈值：",
        "",
        f"- 断档：相邻两条有日期的数据间隔，或最后一条距今天，超过 **{GAP_DAYS}** 天。",
        f"- 缺字段：`date` 或 `source_url` 为空的比例超过 **{int(MISSING_FIELD_RATIO * 100)}%**。",
        f"- `kind=unknown` 比例超过 **{int(UNKNOWN_KIND_RATIO * 100)}%**。",
        "",
        f"全仓合计 **{len(rows)}** 条。",
        "",
        "## 按人总览",
        "",
        "| 人 | 条目 | said | did | corrected | rejected | other | unknown | 日期跨度 | 30 天以上断档 | date 空缺 | url 空缺 |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|",
    ]

    details: list[str] = []
    suggest_block: list[str] = ["## 该补哪类素材（优先三类）", ""]
    suggest_block.append(
        "优先补这三类：现场问答的追问往返、对新手的纠正、带时间戳的产物数据。追求更深，不追求更多同类表述。"
    )
    suggest_block.append("")

    for slug, name in people_order(config):
        items = by_person.get(slug) or []
        counts = kind_counts(items)
        dates = dated(items)
        span = f"{dates[0].isoformat()} — {dates[-1].isoformat()}" if dates else "（无日期）"
        gaps = find_gaps(dates, today)
        date_miss = field_missing_ratio(items, "date")
        url_miss = field_missing_ratio(items, "source_url")
        unk_ratio = (counts.get("unknown", 0) / len(items)) if items else 0.0

        lines.append(
            "| {name} `{slug}` | {n} | {said} | {did} | {cor} | {rej} | {oth} | {unk} | {span} | {gaps} | {dm} | {um} |".format(
                name=name,
                slug=slug,
                n=len(items),
                said=counts["said"],
                did=counts["did"],
                cor=counts["corrected"],
                rej=counts["rejected"],
                oth=counts["other"],
                unk=counts["unknown"],
                span=span,
                gaps=len(gaps),
                dm=f"{date_miss:.0%}",
                um=f"{url_miss:.0%}",
            )
        )

        if gaps:
            alarms.append(f"{name}（{slug}）：{len(gaps)} 段超过 {GAP_DAYS} 天的断档")
        if date_miss > MISSING_FIELD_RATIO:
            alarms.append(f"{name}（{slug}）：date 空缺 {date_miss:.0%}，超过 {int(MISSING_FIELD_RATIO * 100)}%")
        if url_miss > MISSING_FIELD_RATIO:
            alarms.append(f"{name}（{slug}）：source_url 空缺 {url_miss:.0%}，超过 {int(MISSING_FIELD_RATIO * 100)}%")
        if unk_ratio > UNKNOWN_KIND_RATIO:
            alarms.append(f"{name}（{slug}）：kind=unknown 占 {unk_ratio:.0%}，超过 {int(UNKNOWN_KIND_RATIO * 100)}%")

        details += [
            f"### {name}（`{slug}`）",
            "",
            f"- 条目：{len(items)}（其中封存 holdout {sum(1 for r in items if r.get('holdout'))} 条）",
            f"- 日期跨度：{span}",
            f"- kind：said {counts['said']}，did {counts['did']}，corrected {counts['corrected']}，rejected {counts['rejected']}，other {counts['other']}，unknown {counts['unknown']}",
            f"- 缺字段：date {date_miss:.0%}，source_url {url_miss:.0%}",
            "",
        ]
        if dates and gaps:
            details.append("| 断档起 | 断档止 | 间隔（天） |")
            details.append("|---|---|---:|")
            # 断档可能很多（如刘小排从 2014 年起），最多列 12 段，其余汇总
            shown = gaps[:12]
            for a, b, n in shown:
                details.append(f"| {a.isoformat()} | {b.isoformat()} | {n} |")
            if len(gaps) > 12:
                details.append(f"| … | 另有 {len(gaps) - 12} 段未列出 | |")
            details.append("")
        elif not dates:
            details.append("没有可解析的日期，无法计算断档。")
            details.append("")
        else:
            details.append(f"有日期的条目之间没有超过 {GAP_DAYS} 天的断档，最后一条距今也不超过 {GAP_DAYS} 天。")
            details.append("")

        tips = suggestions(slug, name, items, counts)
        suggest_block.append(f"### {name}（`{slug}`）")
        suggest_block.append("")
        if tips:
            for t in tips:
                suggest_block.append(f"- {t}")
        else:
            suggest_block.append("- 优先三类暂无明显缺口。")
        suggest_block.append("")

    # 清单里有、配置里没有的人
    known = {s for s, _ in people_order(config)}
    extras = sorted(set(by_person) - known)
    if extras:
        lines.append("")
        lines.append(f"警告：清单中有未在 people.yaml 出现的人：{', '.join(extras)}")
        alarms.append(f"未登记的人：{', '.join(extras)}")

    lines += ["", "## 按人明细", ""] + details + suggest_block

    if alarms:
        lines += ["## 本次报警", ""]
        for a in alarms:
            lines.append(f"- {a}")
        lines.append("")
        lines.append("以上条目使本脚本以非 0 退出码结束，便于定时任务发出警报。")
        lines.append("")
    else:
        lines += ["## 本次报警", "", "未触发阈值。", ""]

    return "\n".join(lines).rstrip() + "\n", alarms


def main() -> int:
    parser = argparse.ArgumentParser(description="统计原料覆盖率并在超阈值时报警")
    parser.add_argument("--manifest", default=str(MANIFEST_PATH))
    parser.add_argument("--output", default=str(OUTPUT_PATH))
    args = parser.parse_args()

    manifest = Path(args.manifest)
    if not manifest.is_file():
        raise SystemExit(f"找不到 {manifest}，请先跑 python3 tools/build_manifest.py")
    if not PEOPLE_YAML.is_file():
        raise SystemExit(f"找不到 {PEOPLE_YAML}")

    rows = load_manifest(manifest)
    config = load_yaml(PEOPLE_YAML)
    today = dt.datetime.now(BEIJING).date()
    text, alarms = render(config, rows, today)
    out = Path(args.output)
    out.write_text(text, encoding="utf-8")
    print(f"wrote {out if out.is_absolute() and ROOT in out.parents else out}")
    if alarms:
        print(f"报警 {len(alarms)} 条：")
        for a in alarms:
            print(" -", a)
        return 1
    print("未触发报警")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
