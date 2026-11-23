---
name: 哥飞
slug: gefei
primary_purpose: 出海
purposes:
  - 出海
expertise: 出海建站与网站获流（依据其公众号正文，以及已蒸馏的能力卡）
planned_skills: 待补
existing_skills:
  - 哥飞能力包（能力卡，未公开，非本仓）
  - 公开仓库 https://github.com/AdgaiWalker/gefei-agent （非官方蒸馏，标注信息来源）
sources:
  - wechat
  - group-chat
  - github
coverage_until: "2026-11-22"
update_method: 待补
visibility: mixed
---

# 哥飞

主用途是**出海**：用他的知识蒸馏出海相关 skill。

## 擅长

可核实的部分：公众号长期写出海建站、找需求、做网站、获取流量。这些公开文章已被蒸馏成本机能力卡，并有一份公开的非官方蒸馏仓库。会员整理的 GitHub 仓上游已公开，标 `public`。会员群记录经仓主决定随本仓一并公开，来源仍标 `member`。

## 已有相关 skill

- 能力包：13 张能力卡，未公开，不在本仓
- GitHub 公开仓库：[AdgaiWalker/gefei-agent](https://github.com/AdgaiWalker/gefei-agent)（哥飞出海方法论 Agent，非官方蒸馏，标注信息来源）

## 计划蒸馏成的 skill

待补。

## 材料

用 `python3 tools/query.py --person gefei --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的原始文件放进已有目录：`gefei/wechat-articles/`（公众号）、`gefei/group-chat/`（会员群）、`gefei/github-seed/` 或 `gefei/github-member-repos/`（GitHub）。不要改已有原文，不要改名，不要移动旧路径。
2. 若是新的来源类型或可见性，先改仓库根目录的 `people.yaml`。
3. 在仓库根目录运行 `python3 tools/refresh.py --fetched`。
4. 会员群来源仍标 `member`（表示来源，不表示禁止公开）。上游已公开的 GitHub 整理资料标 `public`。
