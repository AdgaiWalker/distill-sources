---
name: 刘小排
slug: liuxiaopai
primary_purpose: 产品
purposes:
  - 产品
expertise: 产品与相关实操（依据其公开 X 归档，以及已写入的「他人补充」）
planned_skills: 待补
existing_skills:
  - 已作为补充写入哥飞能力包（未公开）（非独立 skill，且须标明刘小排、不得混作哥飞原话）
sources:
  - x
coverage_until: "2026-11-22"
update_method: 待补（收录新帖后跑 `python3 tools/tag_x.py`）
visibility: public
---

# 刘小排

主用途是**产品**：用他的知识蒸馏产品相关 skill。X 账号 [@bourneliu66](https://x.com/bourneliu66)。

## 擅长

可核实的部分：本仓收有他的公开 X 归档（长文、长帖与原始 JSON）。其中可执行的方法已作为「他人补充·刘小排（非哥飞）」写入本机 `gefei/references/practitioner/liuxiaopai.md`，并附在若干哥飞能力卡末节。引用必须标明刘小排，不得混作哥飞原话。

尚未单独做成一套「刘小排 skill」。

X 原料全收，只打类型标签（`tools/tag_x.py`，见 `index/x-posts.csv`）。蒸馏时主料是原创和长文，辅料是有方法或观点的回复和引用（agy 按「有没有可执行方法」筛），纯寒暄和转帖不读。
## 已有相关 skill

- 补充页（非独立 skill）：哥飞能力包内（未公开）

## 计划蒸馏成的 skill

待补。

## 材料

用 `python3 tools/query.py --person liuxiaopai --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的 X 归档放进 `liuxiaopai/x-archive/`（文章进 `articles/`，原始 JSON 进 `raw/`）。不要改已有原文，不要改名。
2. 若改来源类型或可见性，先改 `people.yaml`。
3. 更新 X 归档后，在仓库根目录运行 `python3 tools/refresh.py --fetched`。
4. 本批材料来自公开 X 帖，标 `public`。若以后收入会员群等来源材料，可标 `member`（表示来源，不表示禁止公开）。
