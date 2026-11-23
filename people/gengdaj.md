---
name: 逸尘
slug: gengdaj
primary_purpose: 自媒体
purposes:
  - 自媒体
expertise: AI 辅助内容生产（口播自动剪辑、复刻爆款视频）与可复刻的工具教程（依据其公开 X 归档与账号简介）
planned_skills: 自媒体 / 个人 IP 运营方法
existing_skills: 待补
sources:
  - x
coverage_until: "2026-11-22"
update_method: 待补（本次时间线与按月搜索均未翻完，可用同样的 x 只读接口续抓；收录新帖后跑 `python3 tools/tag_x.py`）
visibility: public
---

# 逸尘

主用途是**自媒体**：用她的公开分享蒸馏自媒体、个人 IP 运营相关 skill。X 账号 [@gengdaJ](https://x.com/gengdaJ)，显示名「逸尘」。站点 [yichen.ai](https://yichen.ai)，GitHub 见简介中的 [github.com/mcncarl](https://github.com/mcncarl)。

## 擅长

可核实的部分：账号简介写明 2006 年生、渝客松发起人、法学生；付费咨询做企业 AI 服务与 AI 自媒体增长（微信号 yichen10801）；付费社群 TradeWinds；并提到 yichen-skill、Agent 记忆系统、Ailu 开发者。本仓收有她的公开 X 归档（3 篇 X Article 均有全文，另有长帖与原始 JSON）。公开内容里可核实的方法包括：用剪映 + Codex 做口播自动剪辑、用 Hypit Skill 复刻爆款视频，以及 Clash、Claude 注册/KYC、Antigravity 等保姆级工具教程。

尚未单独做成一套「逸尘 skill」。简介中的 yichen-skill 是否已有可引用成品，待补。

X 原料全收，只打类型标签（`tools/tag_x.py`，见 `index/x-posts.csv`）。蒸馏时主料是原创和长文，辅料是有方法或观点的回复和引用（agy 按「有没有可执行方法」筛），纯寒暄和转帖不读。
## 已有相关 skill

待补。

## 计划蒸馏成的 skill

自媒体 / 个人 IP 运营方法。细节待补。

## 材料

用 `python3 tools/query.py --person gengdaj --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的原始文件放进该人在 `people.yaml` 里登记的目录（不要改已有原文，不要改名）。
2. 若是新的来源类型或可见性，先改仓库根目录的 `people.yaml`。
3. 在仓库根目录运行 `python3 tools/refresh.py --fetched`（打 X 类型标签、重建清单和覆盖率）。
4. 可见性拿不准时可先标 `member`（表示来源，不表示禁止公开）。
