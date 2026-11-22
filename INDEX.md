# 蒸馏原料索引

三层结构：**用途 → 人 → 来源类型**。

- **用途**：这种知识能帮着蒸馏出哪类 skill。每人一个主用途，可以有多个用途。已用：出海、产品。可扩展（例如 IP、AI 工具、具身智能）。
- **人**：每人一张人物卡，见 `people/<slug>.md`。
- **来源类型**：`wechat`（公众号）/ `group-chat`（会员群）/ `x` / `github` / `notes`（笔记）。

原文件不移动、不改名、不改内容。本文件与 `index/classification.csv`、人物卡里的材料清单由 [`scripts/classify.py`](scripts/classify.py) 根据 [`people.yaml`](people.yaml) 生成，可重跑。

生成时间：2026-11-22 17:25（北京时间）。合计条目：1245。

## 用途：出海

这类知识用来蒸馏「出海」相关 skill。2 人，1196 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 哥飞 | 出海 | 出海 | 1195 | 1176 | 19 | [gefei.md](people/gefei.md) |
| 西门 | 出海 | 出海 | 1 | 0 | 1 | [ximen.md](people/ximen.md) |

## 用途：产品

这类知识用来蒸馏「产品」相关 skill。1 人，49 条。

| 人 | 主用途 | 全部用途 | 条目 | public | member | 人物卡 |
|---|---|---|---:|---:|---:|---|
| 刘小排 | 产品 | 产品 | 49 | 49 | 0 | [liuxiaopai.md](people/liuxiaopai.md) |

## 可见性

合计 public 1225，member 20。

- `public`：公开公众号文章、公开 X 帖、公开的开源仓库。
- `member`：会员群材料、会员 GitHub 仓；拿不准的也标 member（例如非公开笔记）。
- **从会员材料蒸馏出的 skill 不得公开发布。** 本仓含会员内容，禁止改成公开仓库。

细目来源见 [SOURCES.md](SOURCES.md)。新增一个人的步骤见 [README.md](README.md)。

## 重跑

```bash
python3 scripts/classify.py
```
