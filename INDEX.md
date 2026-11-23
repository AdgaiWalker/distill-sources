# 蒸馏原料索引

三层结构：**用途 → 人 → 来源类型**。

- **用途**：这种知识能帮着蒸馏出哪类 skill。每人一个主用途，可以有多个用途。已用：出海、产品、AI 工具。可扩展（例如 IP、具身智能）。
- **人**：每人一张人物卡，见 `people/<slug>.md`。
- **来源类型**：`wechat`（公众号）/ `group-chat`（会员群）/ `x` / `github` / `notes`（笔记）/ `feishu`（飞书知识库）。

原文件不移动、不改名、不改内容。本文件与 `index/classification.csv`、人物卡里的材料清单由 [`scripts/classify.py`](scripts/classify.py) 根据 [`people.yaml`](people.yaml) 生成，可重跑。

生成时间：2026-11-23 17:29（北京时间）。合计条目：1536。

## 用途：出海

这类知识用来蒸馏「出海」相关 skill。2 人，1212 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 哥飞 | 出海 | 出海 | 1211 | 1207 | 4 | [gefei.md](people/gefei.md) |
| 西门 | 出海 | 出海 | 1 | 0 | 1 | [ximen.md](people/ximen.md) |

## 用途：产品

这类知识用来蒸馏「产品」相关 skill。1 人，49 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 刘小排 | 产品 | 产品 | 49 | 49 | 0 | [liuxiaopai.md](people/liuxiaopai.md) |

## 用途：AI 工具

这类知识用来蒸馏「AI 工具」相关 skill。1 人，45 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 土豆姐（lauren） | AI 工具 | AI 工具 | 45 | 45 | 0 | [poteto.md](people/poteto.md) |

## 用途：自媒体

这类知识用来蒸馏「自媒体」相关 skill。2 人，230 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 小晚不在 | 自媒体 | 自媒体 | 146 | 146 | 0 | [bbkirstry.md](people/bbkirstry.md) |
| 逸尘 | 自媒体 | 自媒体 | 84 | 84 | 0 | [gengdaj.md](people/gengdaj.md) |

## 可见性

合计 public 1531，member 5。

- `public`：公开公众号文章、公开 X 帖、公开的开源仓库，以及上游已公开的 GitHub 整理资料。
- `member`：来源为会员群转录/截图，或仓主整理的非公开出处笔记。本仓现已公开；这些条目经仓主决定一并收入，标签只说明来源，不表示禁止公开。

细目来源见 [SOURCES.md](SOURCES.md)。新增一个人的步骤见 [README.md](README.md)。

## 重跑

```bash
python3 scripts/classify.py
```
