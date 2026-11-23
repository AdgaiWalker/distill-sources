# 清单字段与统计事件

`manifest.jsonl` 每行一条一手原料，由 `python3 tools/refresh.py` 生成并用 [schema/manifest.schema.json](schema/manifest.schema.json) 校验。本仓只收原始数据，结论不进本仓。

## 一条清单是什么

- 一篇公众号文章、一篇飞书文章、一条 X 帖、一份会员群转录、一份笔记，各算一条。
- GitHub 会员整理仓按仓计一条；`gefei/github-seed/` 按文件计。
- 飞书以 `md/*.md` 和工具表 csv 计，对应的 docx / xlsx 原件不另计。
- X 帖以 `index/x-posts.csv` 与 `raw/all_posts.json` 为准；`all.md`、`articles/` 是同一批帖的可读稿，不重复计。
- 验证区原文不在本仓，因此不进清单，见 [HOLDOUT.md](HOLDOUT.md)。

## 字段

空值用空字符串或空数组，不省略字段，不编造。

| 字段 | 取值 | 说明 |
|---|---|---|
| `id` | 字符串 | 稳定唯一编号 `{person}:{platform}:{key}`，如 `gefei:wechat:20231027_今日停更一天`。 |
| `person` | slug | 与 [people.yaml](people.yaml) 一致。 |
| `platform` | `wechat` / `x` / `feishu` / `group-chat` / `github` / `notes` / `other` | 来源平台。 |
| `kind` | 见下表 | 只从已有标签推断，推断不出写 `unknown`。 |
| `origin` | 见「说话人」 | 谁在说。 |
| `title` | 字符串 | 文件取文件名（去掉日期前缀）；X 帖取正文或长文标题的首行前 60 字。 |
| `date` | `YYYY-MM-DD` 或 `""` | 条目自身日期（北京时间）。 |
| `source_url` | URL 或 `""` | 原始出处，没有依据就留空。 |
| `path` | 相对路径 | 一条 X 帖指向该人的 `x-archive/raw/all_posts.json`，用 `id` 区分。 |
| `sha256` | 64 位十六进制 | 文件用字节；X 帖用该帖 JSON 的规范序列化；会员仓用目录树哈希。 |
| `license_status` | `公开` / `会员内容经哆啦批准公开` / `未知` | 由 `people.yaml` 的 visibility 映射。 |
| `context_tags` | 字符串数组 | 平台、帖子类型等，没有依据则 `[]`。 |
| `fetched_at` | `YYYY-MM-DD HH:MM` | 北京时间。X 帖取归档 JSON 的抓取时间；其他文件取首次进入本仓的 commit 时间（即收录时间，不是原站发布时间）；尚未提交的新文件取刷新时间。 |
| `holdout` | 布尔 | 保留字段。验证区原文已移出本仓，公开清单里恒为 `false`。 |

### kind 取值

| 值 | 含义 | 本仓如何推断 |
|---|---|---|
| `said` | 说的话 | 公众号文章、飞书文章、会员群转录、笔记、X 的 original / article / long / self-thread / reply / quote。回复仍算本人说的话；是否「纠正」无法从现有标签判断，故不标 `corrected`。 |
| `did` | 做的产物 | 飞书工具表、github-seed 里的脚本等。带时间戳的站点或排名数据目前几乎没有。 |
| `corrected` | 对他人的纠正 | 现有标签不够判断，不自动标。有人工依据时可在增量更新时保留手工值。 |
| `rejected` | 放弃或否定的内容 | 同上，不自动标。 |
| `other` | 其他能判断的类型 | 例如纯转帖、他人整理的 GitHub 会员仓。 |
| `unknown` | 无法判断 | 现有标签不足以分类时使用，不准编。 |

## 说话人（origin）

只看路径和标题判断，有依据才判，说不准就标 `uncertain`。规则写在 `tools/build_manifest.py` 的 `_origin_of`。

| 值 | 检索里显示 | 依据 |
|---|---|---|
| `self` | 本人原文 | 本人公众号、飞书、X 原创/回复/引用，且标题没有他人信号 |
| `quoted` | 转述他人 | 标题明确写出另一位讲者，如「龙猫讲…」「小羊在深圳分享…」「嘉宾…」「访谈」「转载」「投稿」「已获得授权」「冠军复盘」 |
| `mixed` | 多人对话 | 会员群转录 |
| `compiled` | 他人汇编 | 会员整理仓、`github-seed` 导出副本、他人整理的笔记 |
| `other` | 他人内容 | X 纯转帖 |
| `uncertain` | 说话人待定 | 公众号标题有他人信号但说不准（「群友」「他靠」「复盘」「经验分享」「第一名」「议程」等）；飞书只认明确讲者，不用这些弱信号 |

已知局限：只看标题，正文里大段转述他人的文章仍可能标成 `self`（例如标题只写人物经历的群友故事）。蒸馏前请读原文确认。

## 统计事件

`tools/refresh.py` 每步写一行 JSON 到 `logs/refresh.jsonl`，公共字段 `ts`（北京时间）、`run`（本次运行编号）、`event`。

| event | 何时写 | 其他字段 |
|---|---|---|
| `refresh_start` | 开始 | `mode`：refresh / fetched / check |
| `step_start` | 每步开始 | `step` |
| `step_ok` | 每步成功 | `step`、`code`、`tail`（最后一行输出） |
| `step_fail` | 某步失败或超时 | `step`、`code` 或 `error`、`tail`（最后几行输出） |
| `holdout_removed` | 验证区原文被挡掉（同步带回了封存帖） | 各类移除数量 |
| `manifest_count` | 清单重建后 | `entries` |
| `schema_ok` / `schema_fail` | 校验结果 | `entries` 或错误摘要 |
| `coverage_alarm` | 覆盖率有报警（不算失败） | `count` |
| `refresh_end` | 结束 | `ok`、`failed` |

`--check` 模式（GitHub Action 用）只打印，不写日志文件。

## 检索

```bash
python3 tools/query.py 新词 --person gefei             # 标题命中在前，本人原文在前
python3 tools/query.py 新词 判断 --person gefei --brief # 多个词同时命中；每条一行
python3 tools/query.py 个人IP --person bbkirstry --json # {total, shown, folded_copies, results[]}
python3 tools/query.py --person gefei --since 2026-01-01 --platform wechat --origin self
```

退出码：0 有命中；1 没有命中（stderr 给出 ls / rg 兜底命令和合法人名）；2 人名写错或清单不存在。

## 覆盖率

`tools/coverage.py` 按人统计 kind、日期跨度、超过 30 天的断档、`date` / `source_url` 空缺比例和 X 帖类型，写出 [COVERAGE.md](COVERAGE.md)。有报警时退出码为 1，`refresh` 只记录不算失败。
