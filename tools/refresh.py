#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""一条命令刷新全部索引。在仓库根目录运行：

    python3 tools/refresh.py            # 刷新索引、清单、覆盖率和 README 状态行
    python3 tools/refresh.py --fetched  # 抓到新原料后用：先记录抓取时间，再刷新
    python3 tools/refresh.py --check    # 只校验，不写任何文件（GitHub Action 用）

步骤：record_fetch（仅 --fetched）→ holdout_filter → tag_x → build_manifest（含 schema 校验）
→ coverage → README 状态行。每步写一行 JSONL 到 logs/refresh.jsonl，事件定义见 SCHEMA.md「统计事件」。
schema 不通过或某步崩溃时退出码非 0；覆盖率报警只记录，不算失败。
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import uuid
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
LOG = ROOT / "logs" / "refresh.jsonl"
README = ROOT / "README.md"
LAST_FETCH = ROOT / "index" / "last-fetch.txt"
BJ = dt.timezone(dt.timedelta(hours=8))
STATUS_RE = re.compile(r"<!-- STATUS -->.*?<!-- /STATUS -->", re.S)


def now() -> str:
    return dt.datetime.now(BJ).strftime("%Y-%m-%d %H:%M:%S")


class Log:
    def __init__(self, write: bool):
        self.write = write
        self.run_id = uuid.uuid4().hex[:8]

    def event(self, event: str, **detail) -> None:
        rec = {"ts": now(), "run": self.run_id, "event": event, **detail}
        print(json.dumps(rec, ensure_ascii=False))
        if self.write:
            LOG.parent.mkdir(exist_ok=True)
            with LOG.open("a", encoding="utf-8") as f:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def run_step(log: Log, name: str, args: list[str], ok_codes=(0,)) -> tuple[bool, str]:
    log.event("step_start", step=name)
    try:
        r = subprocess.run([sys.executable, *args], cwd=ROOT, capture_output=True, text=True, timeout=900)
    except subprocess.TimeoutExpired:
        log.event("step_fail", step=name, error="timeout 900s")
        return False, ""
    out = (r.stdout or "") + (r.stderr or "")
    if r.returncode in ok_codes:
        log.event("step_ok", step=name, code=r.returncode, tail=out.strip().splitlines()[-1:] or [])
        return True, out
    log.event("step_fail", step=name, code=r.returncode, tail=out.strip().splitlines()[-8:])
    return False, out


def last_fetch() -> str:
    if LAST_FETCH.is_file():
        m = re.search(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}", LAST_FETCH.read_text(encoding="utf-8"))
        if m:
            return m.group(0)
    return "未知"


def update_status(ok: bool, entries: int, alarms: int, failed: str) -> None:
    text = README.read_text(encoding="utf-8")
    state = "通过" if ok else f"失败（{failed}，见 logs/refresh.jsonl）"
    line = (
        f"<!-- STATUS -->状态：最近抓取 {last_fetch()} · 最近刷新 {now()[:16]} 北京时间 · "
        f"校验{state} · {entries} 条原料 · 覆盖率报警 {alarms} 条<!-- /STATUS -->"
    )
    if STATUS_RE.search(text):
        text = STATUS_RE.sub(line, text, count=1)
    else:
        text = text.rstrip("\n") + "\n\n" + line + "\n"
    README.write_text(text, encoding="utf-8")


def check_only(log: Log) -> int:
    sys.path.insert(0, str(TOOLS))
    from corpusutil import load_manifest, validate_manifest

    rows = load_manifest()
    errors = validate_manifest(rows) if rows else ["manifest.jsonl 为空或不存在"]
    if errors:
        log.event("schema_fail", count=len(errors), first=errors[:10])
        return 1
    log.event("schema_ok", entries=len(rows))
    ok, out = run_step(log, "coverage", ["tools/coverage.py", "--output", "/dev/null"], ok_codes=(0, 1))
    alarms = re.search(r"报警 (\d+) 条", out)
    log.event("coverage_alarm", count=int(alarms.group(1)) if alarms else 0)
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="刷新索引、清单、覆盖率和 README 状态行")
    ap.add_argument("--fetched", action="store_true", help="抓到新原料后用，先记录抓取时间")
    ap.add_argument("--check", action="store_true", help="只校验，不写文件")
    args = ap.parse_args()

    log = Log(write=not args.check)
    log.event("refresh_start", mode="check" if args.check else ("fetched" if args.fetched else "refresh"))
    if args.check:
        code = check_only(log)
        log.event("refresh_end", ok=code == 0)
        return code

    steps = []
    if args.fetched:
        steps.append(("record_fetch", ["tools/record_fetch.py"], (0,)))
    steps += [
        ("holdout_filter", ["tools/holdout_filter.py"], (0,)),
        ("tag_x", ["tools/tag_x.py"], (0,)),
        ("build_manifest", ["tools/build_manifest.py"], (0,)),
        ("coverage", ["tools/coverage.py"], (0, 1)),
    ]
    failed, entries, alarms = "", 0, 0
    for name, cmd, codes in steps:
        ok, out = run_step(log, name, cmd, codes)
        if name == "holdout_filter" and ok:
            try:
                removed = json.loads(out.strip().splitlines()[-1])
                if any(removed.values()):
                    log.event("holdout_removed", **removed)
            except (ValueError, IndexError):
                pass
        if name == "build_manifest" and ok:
            m = re.search(r"manifest 条目 (\d+)", out)
            entries = int(m.group(1)) if m else 0
            log.event("manifest_count", entries=entries)
        if name == "coverage" and ok:
            m = re.search(r"报警 (\d+) 条", out)
            alarms = int(m.group(1)) if m else 0
            if alarms:
                log.event("coverage_alarm", count=alarms)
        if not ok:
            failed = name
            if name == "build_manifest":
                log.event("schema_fail", tail=out.strip().splitlines()[-5:])
            break
    if not entries:
        try:
            entries = sum(1 for _ in (ROOT / "manifest.jsonl").open(encoding="utf-8"))
        except OSError:
            entries = 0
    update_status(not failed, entries, alarms, failed)
    log.event("refresh_end", ok=not failed, failed=failed or None)
    if failed:
        print(f"\n失败在 {failed}。日志：logs/refresh.jsonl。原料没有被删除，修好后重跑即可。", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
