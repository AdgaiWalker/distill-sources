# 原料清单数据格式

本仓只收原始数据，不放蒸馏结论。目录结构和已有文件保持不动；本说明、JSON Schema、清单和工具都是新增文件。

目的：让任何人、任何 Agent 都能按人、时间、类型检索一手原文，再在仓库之外蒸馏思维模型。加工好的能力卡和 skill 不进本仓，验证成绩只以链接回填到 [results.md](results.md)。

## 文件

| 文件 | 作用 |
|---|---|
| [schema/manifest.schema.json](schema/manifest.schema.json) | 每条清单的 JSON Schema |
| [manifest.jsonl](manifest.jsonl) | 每个原始条目一行 |
| [tools/build_manifest.py](tools/build_manifest.py) | 扫描全仓，增量生成清单 |
| [tools/coverage.py](tools/coverage.py) | 覆盖率统计与断档报警，写出 [COVERAGE.md](COVERAGE.md) |
| [tools/query.py](tools/query.py) | 检索原文片段和出处，默认排除验证区 |
| [HOLDOUT.md](HOLDOUT.md) | 公共验证区规则 |
| [results.md](results.md) | 验证成绩回填表 |

## 一条清单是什么

一条 = 一份一手原料，不是索引里的目录汇总。

- 一篇公众号文章、一篇飞书文章、一条 X 帖、一份会员群转录、一份笔记，各算一条。
- GitHub 会员整理仓按仓计一条（他人汇编，不是逐文件拆开）。
- `gefei/github-seed/` 里的文章和脚本按文件计。
- 飞书以可检索的 `md/*.md` 和工具表 csv 计；对应的 docx / xlsx 原件不另计，避免和转换稿重复。
- 飞书根目录的 README、目录，以及认知模型里的标注、认知卡，不进清单：前两者是说明，后两者是蒸馏结论。
- X 帖以 `index/x-posts.csv` 与 `raw/all_posts.json` 为准；`all.md`、`articles/` 是同一批帖的可读稿，不重复计。
- 小晚封存测试集里的文件单独登记，并给对应的原始条目标 `holdout=true`。依据是 [SEALED.md](bbkirstry/cognitive-model/封存测试集/SEALED.md) 的窗口和文件名，不读取封存正文。

## 字段

每行一个 JSON 对象，字段如下。空值用空字符串或空数组，不要省略字段，也不要编造。

| 字段 | 取值 | 说明 |
|---|---|---|
| `id` | 字符串 | 稳定唯一编号，形如 `{person}:{platform}:{key}`。例如 `bbkirstry:x:2057491244188897653`、`gefei:wechat:20231027_今日停更一天`。 |
| `person` | slug | 与 [people.yaml](people.yaml) 一致，如 `gefei`、`ximen`、`liuxiaopai`、`poteto`、`bbkirstry`、`gengdaj`。 |
| `platform` | `wechat` / `x` / `feishu` / `group-chat` / `github` / `notes` / `other` | 来源平台。 |
| `kind` | 见下表 | 只能从已有标签推断；推断不出写 `unknown`，不准根据正文猜测。 |
| `date` | `YYYY-MM-DD` 或 `""` | 条目自身日期（北京时间的日历日）。来自文件名、文内「发布时间」，或 X 归档已换算好的日期。飞书文件名只有月-日时，因封存说明写明这些篇目属于 2026 年，补为 `2026-MM-DD`。 |
| `source_url` | URL 或 `""` | 原始出处。来自文内「原文链接」、X 帖链接、飞书注释、GitHub `UPSTREAM.md`。没有依据就留空。 |
| `path` | 相对路径 | 仓内文件路径。一条 X 帖的 path 指向该人的 `x-archive/raw/all_posts.json`，用 `id` 区分帖。 |
| `sha256` | 64 位小写十六进制 | 本条内容的哈希。普通文件用文件字节；X 帖用该帖 JSON 的规范序列化；GitHub 会员仓用「相对路径 + 文件哈希」拼成的目录树哈希。 |
| `license_status` | `公开` / `会员内容经哆啦批准公开` / `未知` | 由 `people.yaml` 的 visibility 映射：`public` → 公开，`member` → 会员内容经哆啦批准公开。 |
| `context_tags` | 字符串数组 | 平台、帖子类型、阶段等。没有依据则 `[]`，不准编市场阶段或算法版本。 |
| `fetched_at` | `YYYY-MM-DD HH:MM` 或 `""` | 抓取时间，一律记北京时间。来自各人 `all_posts.json` 里的抓取字段。没有记录就留空，不用文件修改时间冒充。 |
| `holdout` | 布尔 | `true` 表示属于公共验证区，禁止拿来蒸馏。 |

### kind 取值

| 值 | 含义 | 本仓如何推断 |
|---|---|---|
| `said` | 说的话 | 公众号文章、飞书文章、会员群转录、笔记、X 的 original / article / long / self-thread / reply / quote。回复仍算本人说的话；是否「纠正」无法从现有标签判断，故不标 `corrected`。 |
| `did` | 做的产物 | 飞书工具表、github-seed 里的脚本等。带时间戳的站点或排名数据目前几乎没有。 |
| `corrected` | 对他人的纠正 | 现有标签不够判断，不自动标。有人工依据时可在增量更新时保留手工值。 |
| `rejected` | 放弃或否定的内容 | 同上，不自动标。 |
| `other` | 其他能判断的类型 | 例如纯转帖、他人整理的 GitHub 会员仓、封存集里的打包 JSON。 |
| `unknown` | 无法判断 | 现有标签不足以分类时使用，不准编。 |

## 生成与增量

在仓库根目录：

```bash
python3 tools/build_manifest.py
python3 tools/build_manifest.py --full      # 忽略已有清单，全量重建
python3 tools/build_manifest.py --dry-run
```

默认增量：同一 `id` 且 `sha256` 未变时，保留已有条目里可能被人工改过的 `kind`、`context_tags`、`license_status`。`holdout` 每次按规则重算。文件消失的条目会从新清单里去掉。

成功抓取新原料后，在原有流程末尾追加：

```bash
python3 scripts/record_fetch.py
python3 scripts/tag_x.py
python3 scripts/classify.py
python3 scripts/stats.py
python3 tools/build_manifest.py
python3 tools/coverage.py
```

`scripts/stats.py` 结束时会调用后两步；它们的失败不会改变 `stats.py` 自己的退出码。覆盖率报警以直接运行 `coverage.py` 的退出码为准。

校验：

```bash
python3 -c "from pathlib import Path; from tools.corpusutil import load_manifest, validate_manifest; e=validate_manifest(load_manifest()); print('ok' if not e else e)"
```

需要 Python 包 `jsonschema`（本机可 `pip install --user jsonschema`）。

## 检索用法

```bash
python3 tools/query.py --person bbkirstry --kind said --q 定位
python3 tools/query.py --person gefei --since 2026-01-01 --until 2026-03-31 --platform wechat
python3 tools/query.py --person bbkirstry --q 个人IP --json
python3 tools/query.py --include-holdout --person bbkirstry --since 2026-09-23 --limit 5
```

参数：

- `--person` 人物 slug
- `--since` / `--until` 日期，含起止日
- `--kind`、`--platform`
- `--q` 关键词，匹配正文、路径、链接和标签
- `--json` 输出 JSON，供 Agent 调用
- `--include-holdout` 才返回验证区；默认排除
- `--limit` 最多条数，默认 20；`0` 表示不限制

默认输出：原文片段 + 出处（路径、链接、日期）。`--json` 字段为 `id`、`person`、`platform`、`kind`、`date`、`source_url`、`path`、`holdout`、`snippet`。

检索默认不打开 `bbkirstry/cognitive-model/封存测试集/` 下的正文。

## 以后做成 MCP 服务的思路

这次不实现服务。以后如果要给外部 Agent 调用，可以在本仓工具外包一层 MCP：

- 工具建议：`search_sources`（对应 `query.py` 的参数）、`get_item`（按 `id` 返回出处和正文）、`coverage`（读 COVERAGE.md 或重跑脚本）。
- 只读，不提供写入或改哈希的接口。
- 默认 `include_holdout=false`；需要拆封考试时由调用方显式打开，并在日志里记下。
- 返回原文加出处，不返回蒸馏结论。鉴权按仓库的公开范围即可；若日后有未公开条目，再按 `license_status` 过滤。

## 覆盖率

```bash
python3 tools/coverage.py
```

按人统计 kind 数量、日期跨度、超过 30 天的断档、`date` / `source_url` 空缺比例，写出 [COVERAGE.md](COVERAGE.md)。文末按人列出该补的素材，优先三类：现场问答的追问往返、对新手的纠正、带时间戳的产物数据。

超过阈值时退出码非 0，便于定时任务报警。阈值写在 `tools/coverage.py` 和生成的报告里。
