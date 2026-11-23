---
name: 土豆姐（lauren）
slug: poteto
primary_purpose: AI 工具
purposes:
  - AI 工具
expertise: Grok Bot 使用与团队实践（依据其公开 X 归档与账号简介）
planned_skills: Grok Bot 使用方法
existing_skills: 待补
sources:
  - x
coverage_until: "2026-11-22"
update_method: 待补（收录新帖后跑 `python3 tools/tag_x.py`）
visibility: public
---

# 土豆姐（lauren）

主用途是**AI 工具**：用她关于 Grok Bot 的公开分享，蒸馏「Grok Bot 使用方法」相关 skill。X 账号 [@poteto](https://x.com/poteto)，显示名 lauren。哆啦称她「土豆姐」。

## 擅长

可核实的部分：账号简介写明在 [@SpaceXSI](https://x.com/SpaceXSI) 做 Grok Bot，并写过 React Compiler 核心组，以及此前在 Cursor、Meta、Netflix。本仓收有她公开 X 上与 Grok Bot 相关的帖子、长文、长帖与原始 JSON。

X 原料全收，只打类型标签（`tools/tag_x.py`，见 `index/x-posts.csv`）；与 Grok Bot 无关的已取帖仍在 `other.md`，不删。蒸馏时主料是原创和长文，辅料是有方法或观点的回复和引用（agy 按「有没有可执行方法」筛），纯寒暄和转帖不读。
## 已有相关 skill

待补。

## 计划蒸馏成的 skill

Grok Bot 使用方法。

## 材料

用 `python3 tools/query.py --person poteto --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的原始文件放进该人在 `people.yaml` 里登记的目录（不要改已有原文，不要改名）。
2. 若是新的来源类型或可见性，先改仓库根目录的 `people.yaml`。
3. 在仓库根目录运行 `python3 tools/refresh.py --fetched`（打 X 类型标签、重建清单和覆盖率）。
4. 可见性拿不准时可先标 `member`（表示来源，不表示禁止公开）。
