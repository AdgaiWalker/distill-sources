---
name: 小晚不在
slug: bbkirstry
primary_purpose: 自媒体
purposes:
  - 自媒体
expertise: 品牌内容营销、个人 IP 策划、多平台起号与 AI 辅助创作（依据其公开 X 归档与账号简介）
planned_skills: 自媒体 / 个人 IP 运营方法
existing_skills:
  - 本机已有从她公开 X Article 蒸馏的文档（未公开，非本仓、非独立 skill）
sources:
  - x
  - feishu
  - notes
coverage_until: "2026-11-22"
update_method: 待补（本次时间线与按月搜索均未翻完，可用同样的 x 只读接口续抓；收录新帖后跑 `python3 tools/tag_x.py`）
visibility: public
---

# 小晚不在

主用途是**自媒体**：用她的公开分享蒸馏自媒体、个人 IP 运营相关 skill。X 账号 [@bbkirstry](https://x.com/bbkirstry)，显示名「小晚不在」。哆啦也称她「小晚不在」。不要与本机的 IP 顾问 bot「小晚」混为同一人。

## 擅长

可核实的部分：账号简介写明「品牌内容营销 × AI增长 × IP策划」，WayToBot 社区联合发起人，赛博小晚 Skill 作者（[github.com/cyberxiaowan](https://github.com/cyberxiaowan)）。本仓收有她的公开 X 归档（16 篇 X Article 均有全文，另有长帖与原始 JSON），以及 2026-11-23 经哆啦批准公开的飞书知识库导出和认知模型原料（见 `bbkirstry/feishu-kb/` 与 `bbkirstry/cognitive-model/`）。公开长文涉及个人 IP 如何走到商业成交、小红书起号与对标拆解、内容即销售、以及用 ChatGPT 聊天写稿去 AI 味等。简介称 2026 年 6 月底起做自媒体。

尚未单独做成一套「小晚不在 skill」。本机另有一份 2026-11-09 的蒸馏文档，不在本仓。

X 原料全收，只打类型标签（`tools/tag_x.py`，见 `index/x-posts.csv`）。蒸馏时主料是原创和长文，辅料是有方法或观点的回复和引用（agy 按「有没有可执行方法」筛），纯寒暄和转帖不读。
## 已有相关 skill

- 本机蒸馏文档（非独立 skill、非本仓）：未公开

## 计划蒸馏成的 skill

自媒体 / 个人 IP 运营方法。细节待补。

## 材料

用 `python3 tools/query.py --person bbkirstry --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的原始文件放进该人在 `people.yaml` 里登记的目录（不要改已有原文，不要改名）。
2. 若是新的来源类型或可见性，先改仓库根目录的 `people.yaml`。
3. 在仓库根目录运行 `python3 tools/refresh.py --fetched`（打 X 类型标签、重建清单和覆盖率）。
4. 可见性拿不准时可先标 `member`（表示来源，不表示禁止公开）。
