#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""distill-sources 语料清单的共用函数。不改任何原料文件。"""

from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "scripts") not in sys.path:
    sys.path.insert(0, str(ROOT / "scripts"))

BEIJING = dt.timezone(dt.timedelta(hours=8))
MANIFEST_PATH = ROOT / "manifest.jsonl"
SCHEMA_PATH = ROOT / "schema" / "manifest.schema.json"
PEOPLE_YAML = ROOT / "people.yaml"
X_POSTS_CSV = ROOT / "index" / "x-posts.csv"
SEALED_MD = ROOT / "bbkirstry" / "cognitive-model" / "封存测试集" / "SEALED.md"
HOLDOUT_DIR_REL = "bbkirstry/cognitive-model/封存测试集"

PLATFORMS = ("wechat", "x", "feishu", "group-chat", "github", "notes", "other")
KINDS = ("said", "did", "corrected", "rejected", "other", "unknown")
LICENSE_STATUSES = ("公开", "会员内容经哆啦批准公开", "未知")

# kind 只能从已有标签推断，不准根据正文猜测。
X_POST_TYPE_KIND = {
    "original": "said",
    "article": "said",
    "long": "said",
    "self-thread": "said",
    "reply": "said",  # 回复仍是本人说的话；是否「纠正」无法从标签判断
    "quote": "said",
    "retweet": "other",  # 纯转帖，不是本人表述
}

ISO_DATE = re.compile(r"(20\d{2})[-年_]?(\d{2})[-月_]?(\d{2})")
MDY_PREFIX = re.compile(r"^(\d{2})-(\d{2})(?:\s|$)")
SKIP_DIR_NAMES = {".git", ".github", ".obsidian", ".agents", "node_modules", "__pycache__"}

MANIFEST_FIELDS = [
    "id",
    "person",
    "platform",
    "kind",
    "date",
    "source_url",
    "path",
    "sha256",
    "license_status",
    "context_tags",
    "fetched_at",
    "holdout",
]


def now_beijing() -> str:
    return dt.datetime.now(BEIJING).strftime("%Y-%m-%d %H:%M")


def load_yaml(path: Path) -> dict:
    from classify import load_yaml as _load

    return _load(path)


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


def date_from_mdy_prefix(name: str, year: int = 2026) -> str:
    """文件名以 MM-DD 开头时，按给定年份补全。年份必须有依据才调用。"""
    m = MDY_PREFIX.match(name)
    if not m:
        return ""
    try:
        return dt.date(year, int(m.group(1)), int(m.group(2))).isoformat()
    except ValueError:
        return ""


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_json(obj) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return sha256_text(payload)


def tree_hash(dir_path: Path) -> str:
    """目录内容的稳定哈希：相对路径 + 文件 sha256，用于把整个仓当成一条。"""
    lines: list[str] = []
    for p in sorted(dir_path.rglob("*")):
        if not p.is_file():
            continue
        if any(part in SKIP_DIR_NAMES for part in p.parts):
            continue
        rel = p.relative_to(dir_path).as_posix()
        lines.append(f"{rel}\t{sha256_file(p)}")
    return sha256_text("\n".join(lines) + ("\n" if lines else ""))


def license_from_visibility(visibility: str | None) -> str:
    if visibility == "public":
        return "公开"
    if visibility == "member":
        return "会员内容经哆啦批准公开"
    return "未知"


def fetched_to_beijing(raw: str | None) -> str:
    """把各种抓取时间记法归一成北京时间 YYYY-MM-DD HH:MM。无法解析则留空。"""
    if not raw:
        return ""
    s = raw.strip()
    s = re.sub(r"\s*北京时间\s*$", "", s).strip()
    m = re.match(r"^(\d{4}-\d{2}-\d{2})[ T](\d{2}:\d{2})(?::(\d{2}))?\s*(EST|ET|UTC|CST|BJ|北京)?", s)
    if not m:
        return ""
    day, hm, sec, tz = m.group(1), m.group(2), m.group(3) or "00", (m.group(4) or "").upper()
    try:
        naive = dt.datetime.strptime(f"{day} {hm}:{sec}", "%Y-%m-%d %H:%M:%S")
    except ValueError:
        return ""
    if tz in {"EST", "ET"}:
        aware = naive.replace(tzinfo=dt.timezone(dt.timedelta(hours=-5)))
        return aware.astimezone(BEIJING).strftime("%Y-%m-%d %H:%M")
    if tz == "UTC":
        aware = naive.replace(tzinfo=dt.timezone.utc)
        return aware.astimezone(BEIJING).strftime("%Y-%m-%d %H:%M")
    # 无时区、CST、BJ、北京时间：按北京时间记录
    return naive.strftime("%Y-%m-%d %H:%M")


def read_text_head(path: Path, limit: int = 4000) -> str:
    try:
        data = path.read_bytes()[: limit * 2]
    except OSError:
        return ""
    if b"\x00" in data[:1024]:
        return ""
    return data.decode("utf-8", errors="replace")[:limit]


def extract_source_url(text: str) -> str:
    m = re.search(r"原文链接[：:\s]*(\S+)", text)
    if m:
        return m.group(1).rstrip("。）、]")
    m = re.search(r"来源：\s*(https?://\S+)", text)
    if m:
        return m.group(1).rstrip("。；;、）) ")
    m = re.search(r"(https://(?:mp\.weixin\.qq\.com|x\.com|twitter\.com|scn05304jwti\.feishu\.cn|www\.feishu\.cn|github\.com)\S+)", text)
    if m:
        return m.group(1).rstrip("。；;、）) ")
    return ""


def extract_date_from_text_or_name(path: Path, text: str = "") -> str:
    if text:
        m = re.search(r"(?:发布时间|日期|时间)[：:\s]*((?:20\d{2})[-年](?:0[1-9]|1[0-2])[-月](?:0[1-9]|[12]\d|3[01]))", text)
        if m:
            d = norm_date(m.group(1))
            if d:
                return d
    m = re.search(r"(?:^|/)((?:20\d{2})[-_]?(?:0[1-9]|1[0-2])[-_]?(?:0[1-9]|[12]\d|3[01]))", path.name) or re.search(
        r"((?:20\d{2})[-_]?(?:0[1-9]|1[0-2])[-_]?(?:0[1-9]|[12]\d|3[01]))", path.as_posix()
    )
    if m:
        return norm_date(m.group(1))
    return ""


def rel_posix(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def empty_record() -> dict:
    return {
        "id": "",
        "person": "",
        "platform": "",
        "kind": "unknown",
        "date": "",
        "source_url": "",
        "path": "",
        "sha256": "",
        "license_status": "未知",
        "context_tags": [],
        "fetched_at": "",
        "holdout": False,
    }


def make_record(**kwargs) -> dict:
    rec = empty_record()
    rec.update(kwargs)
    rec["date"] = rec.get("date") or ""
    rec["source_url"] = rec.get("source_url") or ""
    rec["fetched_at"] = rec.get("fetched_at") or ""
    rec["context_tags"] = list(rec.get("context_tags") or [])
    rec["holdout"] = bool(rec.get("holdout"))
    if rec["kind"] not in KINDS:
        rec["kind"] = "unknown"
    if rec["license_status"] not in LICENSE_STATUSES:
        rec["license_status"] = "未知"
    return rec


def load_manifest(path: Path = MANIFEST_PATH) -> list[dict]:
    if not path.is_file():
        return []
    rows = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))
    return rows


def write_manifest(rows: list[dict], path: Path = MANIFEST_PATH) -> None:
    rows = sorted(rows, key=lambda r: (r.get("person") or "", r.get("date") or "", r.get("id") or ""))
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for rec in rows:
            out = {k: rec.get(k, empty_record()[k]) for k in MANIFEST_FIELDS}
            f.write(json.dumps(out, ensure_ascii=False, separators=(",", ":")) + "\n")


def parse_sealed_files() -> list[dict]:
    """只读 SEALED.md 的路径与哈希，不打开封存正文。"""
    if not SEALED_MD.is_file():
        return []
    text = SEALED_MD.read_text(encoding="utf-8")
    items = []
    for m in re.finditer(
        r"\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*`([a-f0-9]{64})`\s*\|",
        text,
    ):
        rel, size, chars, digest = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        items.append({"rel": rel, "bytes": size, "chars": chars, "sha256": digest})
    return items


def sealed_window() -> tuple[str, str]:
    if not SEALED_MD.is_file():
        return "", ""
    text = SEALED_MD.read_text(encoding="utf-8")
    m = re.search(r"起止：\s*(\d{4}-\d{2}-\d{2})\s*至\s*(\d{4}-\d{2}-\d{2})", text)
    if m:
        return m.group(1), m.group(2)
    return "2026-09-23", "2026-11-23"


def validate_manifest(rows: list[dict], schema_path: Path = SCHEMA_PATH) -> list[str]:
    import jsonschema

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)
    errors = []
    for i, rec in enumerate(rows, start=1):
        for err in validator.iter_errors(rec):
            errors.append(f"line {i} id={rec.get('id')!r}: {err.message}")
    ids = [r.get("id") for r in rows]
    seen = set()
    for i, i_ in enumerate(ids, start=1):
        if i_ in seen:
            errors.append(f"line {i}: 重复 id {i_!r}")
        seen.add(i_)
    return errors
