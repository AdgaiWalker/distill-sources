# @bourneliu66 X 归档索引

抓取时间：2026-11-22 03:18 America/New_York

## 账号

- 名称：刘小排（@bourneliu66）
- 用户 ID：2815325906
- 简介：AI Product Founder · Building in Public / Raphael  https://raphael.app
- 主页链接：https://x.com/bourneliu66
- 站点：https://raphael.app/
- 账号创建：2014-09-17 13:37 America/New_York（UTC 2014-09-17T17:37:10Z）
- 认证：blue
- 粉丝 36402 · 关注 116 · 公开帖数 492 · 媒体 217
- 置顶帖（X Article）：https://x.com/bourneliu66/status/2122310222111023116

## 抓取范围与限制

- 使用 Grok Bot 内置 `x` 只读接口：`get_users_by_username`、`get_users_posts`（每页最多 25 条，共 20 页）、`get_posts_by_id`、`search_posts_all`。`user-X` 插件没有读取他人时间线或文章正文的工具。未使用浏览器，未发帖、点赞、关注或发私信。
- `get_users_posts` 已翻到最后一页（无 `next_token`），取回 **462** 条（含 1 条纯转帖）。资料页显示帖数为 **492**，少 **30** 条。
- 用 `search_posts_all`（`from:bourneliu66`，`start_time` 从开号日到 2025-08-01）核对早期区间，结果与时间线完全重合（12 条），下一页为空。转帖搜索只找到时间线里已有的 1 条，下一页为空。`has:article` 运算符在当前产品包不可用。
- 缺的约 30 条最可能是已删除但仍计入 `post_count` 的帖，或接口未返回的转帖；公开搜索未能补到新 ID。
- 已取到的时间范围：2014-10-28 03:28 America/New_York → 2026-11-19 03:29 America/New_York。2014-10 至 2025-07 非常稀疏（仅 12 条），主体从 2025-08 起持续更新。
- 三篇 X Article 的 `article.plain_text` 均已取到全文。长帖使用 `note_tweet`/`note_post` 全文。未发现「有文章字段但正文缺失」的条目。
- 速率限制：该只读接口约 30 次/分钟、1000 次/日、每次 25 条。本次未触顶中断。

## 计数

- 取回帖子：462（资料页 492）
- 原创（无引用/回复/转帖）：332
- 引用帖：55
- 回复：74
- 纯转帖：1（已跳过正文归档，仅计数）
- X Article：3（3 篇均有全文）
- 作者自回复线程：21 条（其中长线程 5 条已单独成篇）
- 带 note_tweet 的长帖：33
- `articles/` 独立 markdown：46 篇（文章 + 长线程 + 长帖）

按年：2014 年 1 条，2015 年 4 条，2023 年 3 条，2024 年 4 条，2025 年 167 条，2026 年 283 条

按月（America/New_York）：

| 月份 | 条数 |
| --- | ---: |
| 2014-10 | 1 |
| 2015-06 | 4 |
| 2023-11 | 3 |
| 2024-05 | 1 |
| 2024-11 | 1 |
| 2024-12 | 2 |
| 2025-08 | 30 |
| 2025-09 | 57 |
| 2025-10 | 8 |
| 2025-11 | 30 |
| 2025-12 | 42 |
| 2026-01 | 19 |
| 2026-02 | 27 |
| 2026-03 | 18 |
| 2026-04 | 7 |
| 2026-05 | 7 |
| 2026-06 | 24 |
| 2026-07 | 50 |
| 2026-08 | 47 |
| 2026-09 | 23 |
| 2026-10 | 39 |
| 2026-11 | 22 |

<!-- BEGIN X TYPE TAGS -->

## 类型标签

原料全收，只打类型标签，不按类型删除（哆啦 2026-11-22 定）。
由 `tools/tag_x.py` 生成；每条一个 `post_type`，优先级：retweet > article > long > quote > self-thread > reply > original。
完整表见仓库根目录 [index/x-posts.csv](../../index/x-posts.csv)。

蒸馏时：主料是原创（original、self-thread）和长文（article、long）；
辅料是有方法或观点的回复（reply）和引用（quote），由 agy 按「有没有可执行方法」筛；
纯寒暄和转帖（retweet）不读。

- 合计：462
- `original`（独立原创）：297
- `article`（X Article）：3
- `long`（长帖）：33
- `self-thread`（自回复线程）：21
- `reply`（回复别人）：53
- `quote`（引用帖）：54
- `retweet`（转帖）：1
- 主料（original + article + long + self-thread）：354
- 辅料候选（reply + quote）：107
- 蒸馏时默认不读（retweet）：1

<!-- END X TYPE TAGS -->

## 文件

- 原始 JSON：`raw/user.json`、`raw/timeline_page_001.json` … `raw/timeline_page_020.json`、`raw/all_posts.json`
- 单篇：`articles/YYYY-MM-DD_slug.md`
- 合并全文：`all.md`（按时间正序，线程已合并）
- 本索引：`index.md`

## 长文 / 长线程 / 长帖

| 日期 (ET) | 类型 | 标题 / 首行 | 链接 | 赞 | 有全文 | 文件 |
| --- | --- | --- | --- | ---: | --- | --- |
| 2025-08-17 | 长帖 | 全世界Claude Code用户激情辩论中 —— 使用Claude Code $200美元的包月套餐，积极使用高级功能用… | https://x.com/bourneliu66/status/1956958540658270411 | 245 | 是 | [2025-08-17_全世界Claude-Code用户激情辩论中-——-使用Claude-Code-$.md](articles/2025-08-17_全世界Claude-Code用户激情辩论中-——-使用Claude-Code-$.md) |
| 2025-08-30 | 长帖 | 你可能还不知道：在Github的 Issue中 只要提到 @claude ，即可给Claude Code布置任务，让它干… | https://x.com/bourneliu66/status/1961740040809394670 | 36 | 是 | [2025-08-30_你可能还不知道：在Github的-Issue中-只要提到-@claude-，即可.md](articles/2025-08-30_你可能还不知道：在Github的-Issue中-只要提到-@claude-，即可.md) |
| 2025-09-03 | 长帖 | 一秒鉴定你工作单位是不是正经单位——— | https://x.com/bourneliu66/status/1963107605922107405 | 34 | 是 | [2025-09-03_一秒鉴定你工作单位是不是正经单位———.md](articles/2025-09-03_一秒鉴定你工作单位是不是正经单位———.md) |
| 2025-09-05 | 长帖 | Kimi K2新版体验：这次真的不是"人工智障"了 😂 | https://x.com/bourneliu66/status/1963866743962521744 | 188 | 是 | [2025-09-05_Kimi-K2新版体验：这次真的不是人工智障了-😂.md](articles/2025-09-05_Kimi-K2新版体验：这次真的不是人工智障了-😂.md) |
| 2025-09-06 | 长线程 | 用Claude for Chrome 来自动回复微信，神一样的体验！以后做微商的、做私域的朋友们有福了。AI浏览器的创业… | https://x.com/bourneliu66/status/1964184228746129858 | 540 | 是 | [2025-09-06_用Claude-for-Chrome-来自动回复微信，神一样的体验！以后做微商的.md](articles/2025-09-06_用Claude-for-Chrome-来自动回复微信，神一样的体验！以后做微商的.md) |
| 2025-09-10 | 长帖 | Actually, Claude Code works great through the terminal! Whil… | https://x.com/bourneliu66/status/1965667247206138260 | 0 | 是 | [2025-09-10_Actually,-Claude-Code-works-great-throug.md](articles/2025-09-10_Actually,-Claude-Code-works-great-throug.md) |
| 2025-09-10 | 长帖 | @huangzh65903362 Great question! I often let Claude Code han… | https://x.com/bourneliu66/status/1965667247147401545 | 2 | 是 | [2025-09-10_@huangzh65903362-Great-question!-I-often.md](articles/2025-09-10_@huangzh65903362-Great-question!-I-often.md) |
| 2025-09-10 | 长帖 | @jkudish @adamwathan @CasJam Agent OS + Claude Code is a pow… | https://x.com/bourneliu66/status/1965667252641865741 | 0 | 是 | [2025-09-10_@jkudish-@adamwathan-@CasJam-Agent-OS--C.md](articles/2025-09-10_@jkudish-@adamwathan-@CasJam-Agent-OS--C.md) |
| 2025-11-15 | 长帖 | 放弃Claude Code，就在今天！！！ | https://x.com/bourneliu66/status/1989910558116843719 | 161 | 是 | [2025-11-15_放弃Claude-Code，就在今天！！！.md](articles/2025-11-15_放弃Claude-Code，就在今天！！！.md) |
| 2025-11-18 | 长帖 | Gemini 3 Pro 实在是太强了！ | https://x.com/bourneliu66/status/1990828750402179417 | 320 | 是 | [2025-11-18_Gemini-3-Pro-实在是太强了！.md](articles/2025-11-18_Gemini-3-Pro-实在是太强了！.md) |
| 2025-11-20 | 长帖 | Nano Banana 2 API — as low as $0.029 per image. New users ge… | https://x.com/bourneliu66/status/1991550965670183005 | 13 | 是 | [2025-11-20_Nano-Banana-2-API-—-as-low-as-$0.029-per.md](articles/2025-11-20_Nano-Banana-2-API-—-as-low-as-$0.029-per.md) |
| 2025-11-22 | 长帖 | 除了免费以外，Google Antigravity 还有一个比 Cursor / Windsurf / Trae 都更爽… | https://x.com/bourneliu66/status/1992281675422904755 | 153 | 是 | [2025-11-22_除了免费以外，Google-Antigravity-还有一个比-Cursor.md](articles/2025-11-22_除了免费以外，Google-Antigravity-还有一个比-Cursor.md) |
| 2025-11-24 | 长帖 | Most AI art tools are built for people who can write perfect… | https://x.com/bourneliu66/status/1992988026025410719 | 10 | 是 | [2025-11-24_Most-AI-art-tools-are-built-for-people-w.md](articles/2025-11-24_Most-AI-art-tools-are-built-for-people-w.md) |
| 2025-12-03 | 长帖 | Raphael AI https://t.co/tJOiC33sAI 首页做了个小功能：鼠标自动瞄准，还挺好玩的，大家可… | https://x.com/bourneliu66/status/1996130587665719558 | 17 | 是 | [2025-12-03_Raphael-AI-首页做了个小功能：鼠标自动瞄准，还挺好玩的，大家可以试试看.md](articles/2025-12-03_Raphael-AI-首页做了个小功能：鼠标自动瞄准，还挺好玩的，大家可以试试看.md) |
| 2025-12-03 | 长帖 | 最近很多创业者、自由职业者朋友问我「如何选赛道」「有没有好项目推荐」「什么样的项目是好项目」， 我写了一篇文章。 | https://x.com/bourneliu66/status/1996163617155371253 | 93 | 是 | [2025-12-03_最近很多创业者、自由职业者朋友问我「如何选赛道」「有没有好项目推荐」「什么样的项.md](articles/2025-12-03_最近很多创业者、自由职业者朋友问我「如何选赛道」「有没有好项目推荐」「什么样的项.md) |
| 2025-12-04 | 长线程 | Claude Code的额度设置得挺好，总是在5小时即将刷新的时候，我正好用到了99% https://t.co/lDI… | https://x.com/bourneliu66/status/1996489795061924343 | 19 | 是 | [2025-12-04_Claude-Code的额度设置得挺好，总是在5小时即将刷新的时候，我正好用到了.md](articles/2025-12-04_Claude-Code的额度设置得挺好，总是在5小时即将刷新的时候，我正好用到了.md) |
| 2025-12-08 | 长帖 | Raphael just launched a new Image API at $0.0036 / generatio… | https://x.com/bourneliu66/status/1998058687412518964 | 11 | 是 | [2025-12-08_Raphael-just-launched-a-new-Image-API-at.md](articles/2025-12-08_Raphael-just-launched-a-new-Image-API-at.md) |
| 2025-12-09 | 长线程 | 复杂需求如何让AI一次写对？ | https://x.com/bourneliu66/status/1998578911027016162 | 163 | 是 | [2025-12-09_复杂需求如何让AI一次写对？.md](articles/2025-12-09_复杂需求如何让AI一次写对？.md) |
| 2025-12-11 | 长帖 | 从100万月活跌下来之后，我让Raphael AI 再次起飞：没投广告，只做了4件小事。 | https://x.com/bourneliu66/status/1999151525189599389 | 115 | 是 | [2025-12-11_从100万月活跌下来之后，我让Raphael-AI-再次起飞：没投广告，只做了4.md](articles/2025-12-11_从100万月活跌下来之后，我让Raphael-AI-再次起飞：没投广告，只做了4.md) |
| 2025-12-11 | 长帖 | 据内部人士爆料，快手研发线紧急限制Cursor、Claude Code等第三方编程工具使用，办公端直接闪退，仅特殊需求可… | https://x.com/bourneliu66/status/1999225912118927868 | 200 | 是 | [2025-12-11_据内部人士爆料，快手研发线紧急限制Cursor、Claude-Code等第三方编.md](articles/2025-12-11_据内部人士爆料，快手研发线紧急限制Cursor、Claude-Code等第三方编.md) |
| 2025-12-14 | 长帖 | 我们对 AI 的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定一切的通用智能体（Agent）。 | https://x.com/bourneliu66/status/2000208636094627995 | 154 | 是 | [2025-12-14_我们对-AI-的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定.md](articles/2025-12-14_我们对-AI-的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定.md) |
| 2025-12-26 | 长帖 | 买了智谱GLM coding会员套餐的 | https://x.com/bourneliu66/status/2004493894059483536 | 54 | 是 | [2025-12-26_买了智谱GLM-coding会员套餐的.md](articles/2025-12-26_买了智谱GLM-coding会员套餐的.md) |
| 2026-01-22 | 长帖 | 最近，Pencil火出了天际。我一开始没当回事。 | https://x.com/bourneliu66/status/2014420652112110024 | 1360 | 是 | [2026-01-22_最近，Pencil火出了天际。我一开始没当回事。.md](articles/2026-01-22_最近，Pencil火出了天际。我一开始没当回事。.md) |
| 2026-01-23 | 长帖 | 搞Vibe Coding的人每天睡那么少，怎么还没猝死？ | https://x.com/bourneliu66/status/2014750494175199472 | 75 | 是 | [2026-01-23_搞Vibe-Coding的人每天睡那么少，怎么还没猝死？.md](articles/2026-01-23_搞Vibe-Coding的人每天睡那么少，怎么还没猝死？.md) |
| 2026-02-03 | 长帖 | 我家小龙虾在 Moltbook 建了个宗教：一人公司教 —  老板真人，员工全 AI，教义是《AI 员工的自我修养》 | https://x.com/bourneliu66/status/2018664138571133235 | 7 | 是 | [2026-02-03_我家小龙虾在-Moltbook-建了个宗教：一人公司教-—-老板真人，员工全-A.md](articles/2026-02-03_我家小龙虾在-Moltbook-建了个宗教：一人公司教-—-老板真人，员工全-A.md) |
| 2026-03-03 | 长帖 | 从今天开始，你们用的OpenClaw里，有我的代码了！ | https://x.com/bourneliu66/status/2028865085587018195 | 560 | 是 | [2026-03-03_从今天开始，你们用的OpenClaw里，有我的代码了！.md](articles/2026-03-03_从今天开始，你们用的OpenClaw里，有我的代码了！.md) |
| 2026-03-31 | 长帖 | GitHub将使用你的代码来训练模型，除非你在4月24日之前关闭它，否则视为你允许！ | https://x.com/bourneliu66/status/2038863225673138237 | 43 | 是 | [2026-03-31_GitHub将使用你的代码来训练模型，除非你在4月24日之前关闭它，否则视为你允.md](articles/2026-03-31_GitHub将使用你的代码来训练模型，除非你在4月24日之前关闭它，否则视为你允.md) |
| 2026-06-15 | 长帖 | 我要强烈推荐 Kimi K2.7 High Speed (高速版）！太神奇了！ | https://x.com/bourneliu66/status/2066436537085276284 | 822 | 是 | [2026-06-15_我要强烈推荐-Kimi-K2.7-High-Speed-(高速版）！太神奇了！.md](articles/2026-06-15_我要强烈推荐-Kimi-K2.7-High-Speed-(高速版）！太神奇了！.md) |
| 2026-06-25 | 长帖 | 🚨 BREAKING: Fable 5 is likely returning very soon! | https://x.com/bourneliu66/status/2070053821699743785 | 22 | 是 | [2026-06-25_🚨-BREAKING-Fable-5-is-likely-returning-v.md](articles/2026-06-25_🚨-BREAKING-Fable-5-is-likely-returning-v.md) |
| 2026-07-17 | 长帖 | 用Kimi K3做了一款致敬《杀戮尖塔2》的游戏，《杀戮三国》，核心角色玩法全部基于三国人物特性。 | https://x.com/bourneliu66/status/2078012191169810475 | 1235 | 是 | [2026-07-17_用Kimi-K3做了一款致敬《杀戮尖塔2》的游戏，《杀戮三国》，核心角色玩法全部.md](articles/2026-07-17_用Kimi-K3做了一款致敬《杀戮尖塔2》的游戏，《杀戮三国》，核心角色玩法全部.md) |
| 2026-07-17 | 长帖 | @sudoferraz @creem_io @sudoferraz @creem_io We’ve been unabl… | https://x.com/bourneliu66/status/2078026058411184531 | 1 | 是 | [2026-07-17_@sudoferraz-@creem_io-@sudoferraz-@creem.md](articles/2026-07-17_@sudoferraz-@creem_io-@sudoferraz-@creem.md) |
| 2026-07-26 | 长帖 | 一天之内使用了28亿 Token的Opus 5，以下是我的感受： | https://x.com/bourneliu66/status/2081269376700015070 | 68 | 是 | [2026-07-26_一天之内使用了28亿-Token的Opus-5，以下是我的感受：.md](articles/2026-07-26_一天之内使用了28亿-Token的Opus-5，以下是我的感受：.md) |
| 2026-07-28 | 长帖 | GPT-5.6 Pro绝对是最强编程模型，远超GPT-5.6 Sol和Fable 5。 | https://x.com/bourneliu66/status/2082106402336882887 | 675 | 是 | [2026-07-28_GPT-5.6-Pro绝对是最强编程模型，远超GPT-5.6-Sol和Fable.md](articles/2026-07-28_GPT-5.6-Pro绝对是最强编程模型，远超GPT-5.6-Sol和Fable.md) |
| 2026-07-30 | 长帖 | 🚨BREAKING: | https://x.com/bourneliu66/status/2082712155305255352 | 125 | 是 | [2026-07-30_🚨BREAKING.md](articles/2026-07-30_🚨BREAKING.md) |
| 2026-08-07 | 长线程 | 昨天同时宠幸了4个来自不同种族的员工。 https://t.co/vVGemhlMhw | https://x.com/bourneliu66/status/2085632851874394317 | 15 | 是 | [2026-08-07_昨天同时宠幸了4个来自不同种族的员工。.md](articles/2026-08-07_昨天同时宠幸了4个来自不同种族的员工。.md) |
| 2026-08-13 | 长帖 | 昨天，我打算一个产品的集群部署。 | https://x.com/bourneliu66/status/2087803354332422415 | 53 | 是 | [2026-08-13_昨天，我打算一个产品的集群部署。.md](articles/2026-08-13_昨天，我打算一个产品的集群部署。.md) |
| 2026-08-14 | X Article | AI什么都会，我们为什么还要学习？ | https://x.com/bourneliu66/status/2088206544987181113 | 120 | 是 | [2026-08-14_AI什么都会，我们为什么还要学习？.md](articles/2026-08-14_AI什么都会，我们为什么还要学习？.md) |
| 2026-10-12 | 长帖 | 30 AI tools that quietly replace hours of manual work. | https://x.com/bourneliu66/status/2109503595544756649 | 93 | 是 | [2026-10-12_30-AI-tools-that-quietly-replace-hours-o.md](articles/2026-10-12_30-AI-tools-that-quietly-replace-hours-o.md) |
| 2026-10-27 | 长帖 | 别让AI总结视频了，让它带你看 | https://x.com/bourneliu66/status/2115015709390733572 | 108 | 是 | [2026-10-27_别让AI总结视频了，让它带你看.md](articles/2026-10-27_别让AI总结视频了，让它带你看.md) |
| 2026-11-02 | 长帖 | Token哪里贵了？哪里贵了！ | https://x.com/bourneliu66/status/2117210570319429991 | 42 | 是 | [2026-11-02_Token哪里贵了？哪里贵了！.md](articles/2026-11-02_Token哪里贵了？哪里贵了！.md) |
| 2026-11-07 | X Article | AI只会临门一脚，不会从0到1 | https://x.com/bourneliu66/status/2119011541978898646 | 45 | 是 | [2026-11-07_AI只会临门一脚，不会从0到1.md](articles/2026-11-07_AI只会临门一脚，不会从0到1.md) |
| 2026-11-09 | 长帖 | 互联网大公司员工很难用好AI | https://x.com/bourneliu66/status/2119666038984110309 | 90 | 是 | [2026-11-09_互联网大公司员工很难用好AI.md](articles/2026-11-09_互联网大公司员工很难用好AI.md) |
| 2026-11-16 | 长帖 | 用AI写文章的“AI味儿”有两种， | https://x.com/bourneliu66/status/2122301873051103254 | 27 | 是 | [2026-11-16_用AI写文章的“AI味儿”有两种，.md](articles/2026-11-16_用AI写文章的“AI味儿”有两种，.md) |
| 2026-11-16 | X Article | 我帮大家把 Dodo Payments 的费率打下来了 | https://x.com/bourneliu66/status/2122310222111023116 | 104 | 是 | [2026-11-16_我帮大家把-Dodo-Payments-的费率打下来了.md](articles/2026-11-16_我帮大家把-Dodo-Payments-的费率打下来了.md) |
| 2026-11-17 | 长线程 | 帮你们把 Dodo Payments 的收款费率打下来了。 | https://x.com/bourneliu66/status/2122702250225303673 | 23 | 是 | [2026-11-17_帮你们把-Dodo-Payments-的收款费率打下来了。.md](articles/2026-11-17_帮你们把-Dodo-Payments-的收款费率打下来了。.md) |
| 2026-11-19 | 长帖 | 小八卦：为何Gemini两周连发4个模型，另外两家磨磨蹭蹭？ | https://x.com/bourneliu66/status/2123332950208950564 | 1414 | 是 | [2026-11-19_小八卦：为何Gemini两周连发4个模型，另外两家磨磨蹭蹭？.md](articles/2026-11-19_小八卦：为何Gemini两周连发4个模型，另外两家磨磨蹭蹭？.md) |

## 全部非转帖（线程已合并为一行）

| 日期 (ET) | 类型 | 标题 / 首行 | 链接 | 赞 | 有全文 |
| --- | --- | --- | --- | ---: | --- |
| 2014-10-28 | 帖子 | @AEAffiliates I tried to withdraw at 7 days ago an… | https://x.com/bourneliu66/status/526998811365736448 | 0 | 是 |
| 2015-06-04 | 帖子 | @liuxiaopai123 testtst | https://x.com/bourneliu66/status/606336168909631488 | 0 | 是 |
| 2015-06-04 | 回复 | @liuxiaopai123 hahahha | https://x.com/bourneliu66/status/606336273406529537 | 0 | 是 |
| 2015-06-04 | 帖子 | @liuxiaopai123 aaaaaaaaaaaaaaaaaaaaa | https://x.com/bourneliu66/status/606337389137510400 | 0 | 是 |
| 2023-11-27 | 回复 | @tldraw live demo: https://t.co/dzuXVs3w81 | https://x.com/bourneliu66/status/1729016214008353223 | 0 | 是 |
| 2023-11-27 | 回复 | @EarthML1 @tldraw https://t.co/dzuXVs3w81 | https://x.com/bourneliu66/status/1729025392584069573 | 0 | 是 |
| 2023-11-28 | 回复 | @gorkem cool, let's discuss. I'd love to use https… | https://x.com/bourneliu66/status/1729371023945208077 | 0 | 是 |
| 2024-05-09 | 帖子 | https://t.co/5FebDmJQN9 | https://x.com/bourneliu66/status/1788500006477173185 | 25 | 是 |
| 2024-11-03 | 帖子 | Excited to introduce https://t.co/KPEZ19hSgO ! Our… | https://x.com/bourneliu66/status/1853084916311073059 | 2 | 是 |
| 2024-12-05 | 帖子 | Share your screen instantly with anyone right from… | https://x.com/bourneliu66/status/1864737775834009874 | 6 | 是 |
| 2024-12-05 | 帖子 | Screen Sharing | https://x.com/bourneliu66/status/1864861022349045860 | 6 | 是 |
| 2025-08-15 | 长线程 | 我成了榜一大哥？？Anthropic追杀的那个每个月消耗数万美金的人，原来就是我呀？！ https:… | https://x.com/bourneliu66/status/1956268148413620396 | 619 | 是 |
| 2025-08-17 | 帖子 | I’m the guy who consumed $50K worth of Claude Code… | https://x.com/bourneliu66/status/1956936665613890015 | 12 | 否 |
| 2025-08-17 | 长帖 | 全世界Claude Code用户激情辩论中 —— 使用Claude Code $200美元的包月套餐… | https://x.com/bourneliu66/status/1956958540658270411 | 245 | 是 |
| 2025-08-17 | 帖子 | 竟然有人刷榜，还抄我的文案，笑死我了🤣 大千世界真是无奇不有 | https://x.com/bourneliu66/status/1957112612132647141 | 9 | 是 |
| 2025-08-17 | 回复 | @AlexsITlab 谢谢 ❤️ | https://x.com/bourneliu66/status/1957114889928921193 | 2 | 是 |
| 2025-08-18 | 回复 | @Dalong_AI 谢谢你。我也这么认为。😄 | https://x.com/bourneliu66/status/1957296897082986797 | 6 | 是 |
| 2025-08-18 | 帖子 | Twitter上好像很多朋友还不认识我。 | https://x.com/bourneliu66/status/1957297741689966814 | 246 | 是 |
| 2025-08-18 | 帖子 | 啊? (°ロ°)!  一天涨了2500粉？  Twitter的兄弟姐妹们太热情了啊，我来晚了。 | https://x.com/bourneliu66/status/1957451522784055693 | 66 | 是 |
| 2025-08-18 | 帖子 | 创业半年，写了一份总结。 | https://x.com/bourneliu66/status/1957648677868302716 | 159 | 是 |
| 2025-08-18 | 回复 | @tuzi_ai 那个人是刷榜的，他贴不出来日常使用记录。不仅刷榜，还抄我文案，非常好笑。 http… | https://x.com/bourneliu66/status/1957649198402425133 | 9 | 是 |
| 2025-08-19 | 帖子 | Claude Code 懒人技巧 ： 一键让你的Claude Code拥有所有世界顶级Agent，并… | https://x.com/bourneliu66/status/1957799247069270476 | 320 | 是 |
| 2025-08-20 | 帖子 | 没想到引起那么多的讨论，全是噪声，影响到我正常生活了。 我决定退出排行榜，继续认真做产品。谢谢关注。… | https://x.com/bourneliu66/status/1958066562860192119 | 64 | 是 |
| 2025-08-21 | 帖子 | 900个不会写代码的人，经过两个月的学习，能做出怎样的产品？ 今晚19点直播，验货！ | https://x.com/bourneliu66/status/1958444162031956403 | 11 | 是 |
| 2025-08-22 | 帖子 | 用Claude Code把自己变懒：口喷，分析榜单。 | https://x.com/bourneliu66/status/1958808715202564422 | 89 | 是 |
| 2025-08-23 | 帖子 | 如果我的爸爸妈妈在我小时候就看过这本书，该多好啊！哈哈哈 https://t.co/fcDy7Ddv… | https://x.com/bourneliu66/status/1959107113659027505 | 325 | 是 |
| 2025-08-24 | 回复 | @cheerselflin 啊？我说话这么难听的吗？ 😂😂 | https://x.com/bourneliu66/status/1959601075172049257 | 0 | 是 |
| 2025-08-24 | 回复 | @ChwQiu «人比AI凶»，万维钢 | https://x.com/bourneliu66/status/1959601431855661564 | 7 | 是 |
| 2025-08-24 | 引用帖 | 林悦己是我第一个亲徒弟，附图是我第一次给她反馈 （说的挺难听的🤦‍♂️） | https://x.com/bourneliu66/status/1959606944312000653 | 92 | 是 |
| 2025-08-24 | 帖子 | Claude Code入门：3条铁律让你告别代码屎山 | https://x.com/bourneliu66/status/1959616518771351608 | 593 | 是 |
| 2025-08-25 | 帖子 | 重看《The Blind Side》，被一个小细节打动 | https://x.com/bourneliu66/status/1959852684632314274 | 17 | 是 |
| 2025-08-25 | 帖子 | 此刻的北京， 东三环 https://t.co/E6gz83KhTl | https://x.com/bourneliu66/status/1959899588816724435 | 45 | 是 |
| 2025-08-25 | 帖子 | Claude Code，部分用户可以用1M上下文的claude sonnet模型了。 | https://x.com/bourneliu66/status/1959900848277876938 | 84 | 是 |
| 2025-08-26 | 帖子 | AI编程圈大瓜，刚刚开始！ | https://x.com/bourneliu66/status/1960221778317648345 | 65 | 是 |
| 2025-08-26 | 引用帖 | @yang24zhi  是我们杭州SCAI实验室里的优秀创业者，他的产品是「AI今日热榜」。产品做得… | https://x.com/bourneliu66/status/1960235837087465948 | 5 | 是 |
| 2025-08-26 | 帖子 | https://t.co/y6IJRHVdUF | https://x.com/bourneliu66/status/1960402084081360987 | 13 | 是 |
| 2025-08-27 | 帖子 | 那个.. @HongKong_Doll 姐姐到底长啥样， banana (Gemini Flash … | https://x.com/bourneliu66/status/1960732760781545599 | 18 | 是 |
| 2025-08-29 | 帖子 | SCAI实验室的创业者交流的氛围真好 https://t.co/QVWzbHEcnW | https://x.com/bourneliu66/status/1961306400069705769 | 31 | 是 |
| 2025-08-30 | 长帖 | 你可能还不知道：在Github的 Issue中 只要提到 @claude ，即可给Claude Co… | https://x.com/bourneliu66/status/1961740040809394670 | 36 | 是 |
| 2025-08-31 | 帖子 | 录了一期播客 | https://x.com/bourneliu66/status/1962341397866090932 | 94 | 是 |
| 2025-09-02 | 帖子 | 并排开两个窗口，让Claude Code和Codex CLI互相讨论、互相审核，有奇效。 | https://x.com/bourneliu66/status/1962773584084115724 | 280 | 是 |
| 2025-09-02 | 帖子 | https://t.co/ofBfj0Vs8Q | https://x.com/bourneliu66/status/1962844285243719928 | 7 | 是 |
| 2025-09-03 | 长帖 | 一秒鉴定你工作单位是不是正经单位——— | https://x.com/bourneliu66/status/1963107605922107405 | 34 | 是 |
| 2025-09-03 | 帖子 | 用Claude Code 自动发Reddit ，根据帖子内容、其他人的讨论，自动发评论。 效果相当好… | https://x.com/bourneliu66/status/1963125131087155345 | 228 | 是 |
| 2025-09-05 | 长帖 | Kimi K2新版体验：这次真的不是"人工智障"了 😂 | https://x.com/bourneliu66/status/1963866743962521744 | 188 | 是 |
| 2025-09-06 | 长线程 | 用Claude for Chrome 来自动回复微信，神一样的体验！以后做微商的、做私域的朋友们有福… | https://x.com/bourneliu66/status/1964184228746129858 | 540 | 是 |
| 2025-09-06 | 长线程 | 刚一个硅谷的朋友告诉了我一个小道消息：Claude for Chrome 即将放量！很快各位就会收到… | https://x.com/bourneliu66/status/1964372655848775848 | 27 | 是 |
| 2025-09-07 | 引用帖 | 这是一位出海AI产品新人，也是我的学员。人和产品都非常优秀。欢迎大家关注。 https://t.co… | https://x.com/bourneliu66/status/1964713427198468117 | 20 | 是 |
| 2025-09-07 | 回复 | @ciaotigre 谢谢！ | https://x.com/bourneliu66/status/1964715163267043475 | 1 | 是 |
| 2025-09-07 | 帖子 | 几时归去，作个闲人。对一辆车，一头牛，一溪云。 https://t.co/gBLv7DFCe6 | https://x.com/bourneliu66/status/1964721066821189789 | 21 | 是 |
| 2025-09-08 | 引用帖 | 这位同学太励志了，他是字面意思上的“零基础”… https://t.co/oEL12opOZk | https://x.com/bourneliu66/status/1965238701208023111 | 3 | 是 |
| 2025-09-10 | 长帖 | Actually, Claude Code works great through the term… | https://x.com/bourneliu66/status/1965667247206138260 | 0 | 是 |
| 2025-09-10 | 长帖 | @huangzh65903362 Great question! I often let Claud… | https://x.com/bourneliu66/status/1965667247147401545 | 2 | 是 |
| 2025-09-10 | 回复 | @vista8 @MrHagosDE The MCP ecosystem is really exp… | https://x.com/bourneliu66/status/1965667251371061460 | 2 | 是 |
| 2025-09-10 | 回复 | @prahaladatreyaa Absolutely agree! Claude Code's a… | https://x.com/bourneliu66/status/1965667250112721398 | 1 | 是 |
| 2025-09-10 | 回复 | @HeglerPavel @SpaniardPM Claude Code + TanStack St… | https://x.com/bourneliu66/status/1965667248816758844 | 1 | 是 |
| 2025-09-10 | 回复 | @bachi7q Response time can vary based on model com… | https://x.com/bourneliu66/status/1965667248812495137 | 1 | 是 |
| 2025-09-10 | 帖子 | @huang39184 Long-running tasks are perfect for: de… | https://x.com/bourneliu66/status/1965667252675428683 | 0 | 是 |
| 2025-09-10 | 长帖 | @jkudish @adamwathan @CasJam Agent OS + Claude Cod… | https://x.com/bourneliu66/status/1965667252641865741 | 0 | 是 |
| 2025-09-10 | 引用帖 | 你们知道吗，下面这条推，阅读量5万，涨粉500，它是Claude Code帮我自动发的………… NN… | https://x.com/bourneliu66/status/1965686038040650021 | 194 | 是 |
| 2025-09-10 | 帖子 | @underwoodxie96 纯ai写。看图 | https://x.com/bourneliu66/status/1965704694439047264 | 0 | 是 |
| 2025-09-10 | 引用帖 | 非常牛逼。 我特别希望其他大厂产品经理，能够看到鱼总的故事，然后问问自己——你过得开心吗？内心有起波… | https://x.com/bourneliu66/status/1965711690529735093 | 17 | 是 |
| 2025-09-10 | 帖子 | 有粉丝给我留言：高手从不抱怨环境，因为环境就是被他们搞坏的。😂😂 | https://x.com/bourneliu66/status/1965722813987541434 | 25 | 是 |
| 2025-09-10 | 引用帖 | 另一个刚刚起步的同学～ https://t.co/lS4QPtpNdu | https://x.com/bourneliu66/status/1965784572282728817 | 3 | 是 |
| 2025-09-10 | 帖子 | 我的声音克隆产品AnyVoice换新皮肤、新交互了，模型也升级了。只需要10秒的录音就能克隆出以假乱… | https://x.com/bourneliu66/status/1965831367046082923 | 278 | 是 |
| 2025-09-10 | 回复 | @becool_me 谢谢！ | https://x.com/bourneliu66/status/1965844312652132415 | 0 | 是 |
| 2025-09-10 | 回复 | @renfeng416 谢谢 | https://x.com/bourneliu66/status/1965953273468428490 | 0 | 是 |
| 2025-09-11 | 回复 | @Jason_qeb 谢谢 | https://x.com/bourneliu66/status/1965999869161779371 | 0 | 是 |
| 2025-09-11 | 帖子 | 从iPhone身上看到了二十年前的我、十年前的我、现在的我、十年后的我，而二十年后的我。 https… | https://x.com/bourneliu66/status/1966161823998292088 | 14 | 是 |
| 2025-09-12 | 帖子 | SCAI孵化的第一个小爆品来了！好开心！抖音搜索“AI写论文”，全是它！估计今天会到1万点赞。精准用… | https://x.com/bourneliu66/status/1966432514802946122 | 19 | 是 |
| 2025-09-13 | 帖子 | AI编程的终极心法，来自孟子。 | https://x.com/bourneliu66/status/1966714495293923702 | 50 | 是 |
| 2025-09-13 | 帖子 | 我们终此一生，就是要摆脱他人的期待，找到真正的自己 | https://x.com/bourneliu66/status/1966763261753213405 | 120 | 是 |
| 2025-09-13 | 帖子 | 今天 Vibe Friends的黑客马拉松，现场的选手太抽象了！！哈哈哈哈！！ | https://x.com/bourneliu66/status/1966774561179054308 | 22 | 是 |
| 2025-09-13 | 引用帖 | 这是昨天跟大家提到的，最近爆火的一款AI产品：大学教授 教学生用AI写论文！ | https://x.com/bourneliu66/status/1966794255520702646 | 27 | 是 |
| 2025-09-13 | 引用帖 | 非常有趣的比赛！杰尼加油。 https://t.co/O1ENkD5N0e | https://x.com/bourneliu66/status/1966897008784097511 | 11 | 是 |
| 2025-09-16 | 帖子 | Codex迎来史诗级升级！能一口气卷自己7小时、自带云端虚拟机，连开发环境都不用配置了！Cursor… | https://x.com/bourneliu66/status/1967862765705646205 | 378 | 是 |
| 2025-09-17 | 引用帖 | 上周，我催你们填Claude for Chrome的Waitlist，你们填了吗？ | https://x.com/bourneliu66/status/1968198456037822778 | 8 | 是 |
| 2025-09-17 | 引用帖 | K2 Turbo 今天大更新 + 新羊毛。 | https://x.com/bourneliu66/status/1968276949186531532 | 30 | 是 |
| 2025-09-17 | 帖子 | 《 偶像大佬教我的产品课： 独立开发者的小生意，能够扩大十倍吗？》 | https://x.com/bourneliu66/status/1968376049118720441 | 88 | 是 |
| 2025-09-18 | 帖子 | 完蛋了，完蛋了！ | https://x.com/bourneliu66/status/1968698476906041390 | 30 | 是 |
| 2025-09-19 | 引用帖 | 后生可畏啊 https://t.co/izZRwHixNc | https://x.com/bourneliu66/status/1969080865826263110 | 6 | 是 |
| 2025-09-19 | 帖子 | 大半夜还在改屁屁踢 https://t.co/jwElKufkpu | https://x.com/bourneliu66/status/1969081260900274660 | 9 | 是 |
| 2025-09-23 | 帖子 | 为了避免员工失业，我也给自己找了个新副业 https://t.co/eiQV5wjK0I | https://x.com/bourneliu66/status/1970394840518328759 | 85 | 是 |
| 2025-09-23 | 帖子 | “目前我国不缺牛马” https://t.co/yQ8Tk4rHV9 | https://x.com/bourneliu66/status/1970495164516049293 | 26 | 是 |
| 2025-09-24 | 帖子 | $200美金/月（1500元/月）的Claude Code和Codex，比你聪明，比你勤奋。 | https://x.com/bourneliu66/status/1971027814204993674 | 190 | 是 |
| 2025-09-24 | 回复 | @guangpengwgp 是运气 | https://x.com/bourneliu66/status/1971042633909936225 | 3 | 是 |
| 2025-09-25 | 引用帖 | 自从我公开「这条推是AI自动发的」这件事以后， | https://x.com/bourneliu66/status/1971096083989430279 | 4 | 是 |
| 2025-09-25 | 回复 | @YuTengjing 是的，瞧不起。 | https://x.com/bourneliu66/status/1971096482800611773 | 0 | 是 |
| 2025-09-25 | 帖子 | 买了个Herman Miller人体工学椅，没感觉出来为啥值这个价，就虚心问了Claude。 | https://x.com/bourneliu66/status/1971120503642521988 | 12 | 是 |
| 2025-09-25 | 回复 | @hechuan_agi 我试试。谢谢 | https://x.com/bourneliu66/status/1971371923520225332 | 0 | 是 |
| 2025-09-30 | 帖子 | 东北的闪电⚡️真吓人😱 https://t.co/Z5EuBJ6TNI | https://x.com/bourneliu66/status/1972988517782552756 | 7 | 是 |
| 2025-09-30 | 帖子 | Life is 10% what happens to you and 90% how you re… | https://x.com/bourneliu66/status/1973030018218643933 | 24 | 是 |
| 2025-10-07 | 引用帖 | 好可惜啊。阿西加油，早日东山再起 https://t.co/rwwsGfs82G | https://x.com/bourneliu66/status/1975430988743508340 | 6 | 是 |
| 2025-10-07 | 帖子 | Claude Code有官方版VS Code插件了，极简而强大。 | https://x.com/bourneliu66/status/1975432703005827120 | 36 | 是 |
| 2025-10-07 | 帖子 | 你们发现没，Claude Sonnet 4.5比Claude Opus 4.1强太多了，强到惊悚 | https://x.com/bourneliu66/status/1975437820417409217 | 91 | 是 |
| 2025-10-08 | 帖子 | 无论你认为你能，还是你认为你不能，你都是对的。 | https://x.com/bourneliu66/status/1975842728861999124 | 17 | 是 |
| 2025-10-08 | 帖子 | “Qwen， 如果这是Gay, 哪个是0？” https://t.co/UeyvSZQ5PL | https://x.com/bourneliu66/status/1975921112111628707 | 6 | 是 |
| 2025-10-10 | 引用帖 | Claude Code for VS Code 魔改版！强烈推荐大家使用！ | https://x.com/bourneliu66/status/1976620336381915575 | 295 | 是 |
| 2025-10-20 | 帖子 | 老外搞了一个大模型炒股大赛，用真钱。目前DeepSeek遥遥领先，GPT-5和Gemini暂时都是亏… | https://x.com/bourneliu66/status/1980240707383390484 | 1107 | 是 |
| 2025-10-23 | 帖子 | https://t.co/LujUCsWvD4 | https://x.com/bourneliu66/status/1981272783419297814 | 551 | 是 |
| 2025-11-02 | 帖子 | 我和Claude Code讨论新的技术方案，Claude Code 表示拒绝，并给了我一些人生建议…… | https://x.com/bourneliu66/status/1984904675477606522 | 167 | 是 |
| 2025-11-02 | 帖子 | Claude Code的官方版Claude Code for VS Code插件，现已经支持bypa… | https://x.com/bourneliu66/status/1985014133042098194 | 12 | 是 |
| 2025-11-04 | 帖子 | Claude Code是在哪个互联网大厂工作过吗？越来越像某些大厂程序员了，厉害。 https://… | https://x.com/bourneliu66/status/1985592088973754655 | 182 | 是 |
| 2025-11-06 | 引用帖 | 我一直想知道这位朋友是谁。有认识的朋友可以请他把域名还给我吗？ 做个垃圾产品抢我每个月1M流量， 把… | https://x.com/bourneliu66/status/1986307440154190194 | 26 | 是 |
| 2025-11-07 | 引用帖 | 朋友们，出大事了！！ | https://x.com/bourneliu66/status/1986803841824919906 | 519 | 是 |
| 2025-11-10 | 帖子 | 电话里主教练说：“林书豪，你的下一场比赛，要再拿9次失误！” https://t.co/Dnj6XH… | https://x.com/bourneliu66/status/1988082031922999585 | 3 | 是 |
| 2025-11-10 | 帖子 | Nano Banana 2太恐怖了！ | https://x.com/bourneliu66/status/1988082927457251708 | 459 | 是 |
| 2025-11-11 | 帖子 | 已知，在A和B两个城市之间有三条路径，你的任务是尽快从A走到B，每条路都是平坦的。如图所示。 | https://x.com/bourneliu66/status/1988302623100071998 | 9 | 是 |
| 2025-11-13 | 帖子 | 大陆的朋友们，请不要再用大陆护照去注册香港Stripe了 https://t.co/pbPdtMew… | https://x.com/bourneliu66/status/1989194617057849515 | 45 | 是 |
| 2025-11-15 | 帖子 | 人间多美好啊～ https://t.co/yCaNGcjEQD | https://x.com/bourneliu66/status/1989634031940767945 | 12 | 是 |
| 2025-11-15 | 长帖 | 放弃Claude Code，就在今天！！！ | https://x.com/bourneliu66/status/1989910558116843719 | 161 | 是 |
| 2025-11-18 | 帖子 | 全球性大事故：Cloudflare挂了！ 我们会发现，一大批网站突然都访问不了了。 | https://x.com/bourneliu66/status/1990754477717196902 | 22 | 是 |
| 2025-11-18 | 帖子 | Google AI Studio已经可以使用Gemini 3 Pro! | https://x.com/bourneliu66/status/1990802556965314938 | 17 | 是 |
| 2025-11-18 | 长帖 | Gemini 3 Pro 实在是太强了！ | https://x.com/bourneliu66/status/1990828750402179417 | 320 | 是 |
| 2025-11-19 | 帖子 | Gemini 3实在是太聪明了 https://t.co/X1aHataDWf | https://x.com/bourneliu66/status/1991086324858642681 | 416 | 是 |
| 2025-11-19 | 帖子 | Antigravity用着真爽，可惜就是限额太严重了。每5小时的窗口只能用1～2小时。好希望它早点出… | https://x.com/bourneliu66/status/1991174923986030866 | 20 | 是 |
| 2025-11-20 | 帖子 | As of Nov 19, 2025: | https://x.com/bourneliu66/status/1991373737971839047 | 120 | 是 |
| 2025-11-20 | 帖子 | 你的ChatGPT ，最长思考过几分钟？ https://t.co/yKMWHNn3xl | https://x.com/bourneliu66/status/1991389552523768010 | 2 | 是 |
| 2025-11-20 | 长帖 | Nano Banana 2 API — as low as $0.029 per image. Ne… | https://x.com/bourneliu66/status/1991550965670183005 | 13 | 是 |
| 2025-11-21 | 帖子 | Claude Opus 4.5 来了！ | https://x.com/bourneliu66/status/1991747444112298492 | 395 | 是 |
| 2025-11-21 | 帖子 | Nano Banana 2强得不像话啊。 | https://x.com/bourneliu66/status/1991790317918658705 | 23 | 是 |
| 2025-11-22 | 引用帖 | 这是假的，我被骗了 https://t.co/mcKnzWkRvv | https://x.com/bourneliu66/status/1992111675047375055 | 14 | 是 |
| 2025-11-22 | 长帖 | 除了免费以外，Google Antigravity 还有一个比 Cursor / Windsurf … | https://x.com/bourneliu66/status/1992281675422904755 | 153 | 是 |
| 2025-11-24 | 帖子 | 刚做了个新产品Morisot https://t.co/Agi3LyKXfR ，一瞬间又被人开始抢注… | https://x.com/bourneliu66/status/1992873049931371004 | 25 | 是 |
| 2025-11-24 | 长帖 | Most AI art tools are built for people who can wri… | https://x.com/bourneliu66/status/1992988026025410719 | 10 | 是 |
| 2025-11-25 | 引用帖 | 这是我一个学生的产品，可以上传你的宠物照片，生成宠物电影，挺有意思的，网址是https://t.co… | https://x.com/bourneliu66/status/1993373409829699925 | 123 | 是 |
| 2025-11-27 | 帖子 | 有一个傻子，连首页文案都抄我的，一点创意都没有，最近宣布倒闭了，活不下去了。(图1） | https://x.com/bourneliu66/status/1993924978442686813 | 21 | 是 |
| 2025-11-27 | 帖子 | 3位大哥一起帮我分析https://t.co/Agi3LyKpqj 的性能问题 | https://x.com/bourneliu66/status/1994260196747530726 | 30 | 是 |
| 2025-11-28 | 帖子 | 啊哈？我在韩国这么火吗？ 哈哈哈哈哈！！ https://t.co/mCVPM0j5JM | https://x.com/bourneliu66/status/1994428397150409090 | 33 | 是 |
| 2025-11-28 | 帖子 | 韩国《中央日报》：不会英语的中国开发者，用AI在发达国家赚了15亿 😂 https://t.co/Z… | https://x.com/bourneliu66/status/1994450569952465058 | 307 | 是 |
| 2025-12-01 | 帖子 | 使用Google Antigravity卡在登录？ 不要去研究玄学了，只需搞定一件事就行： | https://x.com/bourneliu66/status/1995429181606527013 | 222 | 是 |
| 2025-12-03 | 长帖 | Raphael AI https://t.co/tJOiC33sAI 首页做了个小功能：鼠标自动瞄准… | https://x.com/bourneliu66/status/1996130587665719558 | 17 | 是 |
| 2025-12-03 | 帖子 | 说一个小窍门：在老外那儿买任何产品之前，请先用ChatGPT-5.1-Pro帮忙找优惠码(coupo… | https://x.com/bourneliu66/status/1996138971567698387 | 614 | 是 |
| 2025-12-03 | 长线程 | 最近很多创业者、自由职业者朋友问我「如何选赛道」「有没有好项目推荐」「什么样的项目是好项目」， 我写… | https://x.com/bourneliu66/status/1996163617155371253 | 93 | 是 |
| 2025-12-03 | 帖子 | OpenAI奥特曼宣布正式向Claude Skills发起投降 https://t.co/MK550… | https://x.com/bourneliu66/status/1996167342741717451 | 238 | 是 |
| 2025-12-03 | 引用帖 | Kling O1 生成视频真的好厉害，新王诞生！ API已经上架到董佳琦的EvoLink了 http… | https://x.com/bourneliu66/status/1996232778527219743 | 43 | 是 |
| 2025-12-04 | 长线程 | MidJourney: 1 image in 60 seconds. | https://x.com/bourneliu66/status/1996469832141992429 | 38 | 是 |
| 2025-12-04 | 长线程 | Claude Code的额度设置得挺好，总是在5小时即将刷新的时候，我正好用到了99% https:… | https://x.com/bourneliu66/status/1996489795061924343 | 19 | 是 |
| 2025-12-05 | 帖子 | 号外号外！！ 朋友们，赶快去给Google充值吧！ Google AI Pro 和 Google A… | https://x.com/bourneliu66/status/1996863327520412061 | 72 | 是 |
| 2025-12-08 | 长帖 | Raphael just launched a new Image API at $0.0036 /… | https://x.com/bourneliu66/status/1998058687412518964 | 11 | 是 |
| 2025-12-08 | 帖子 | Raphael 的月活来到了半年以来新高，659.52K | https://x.com/bourneliu66/status/1998059867182182836 | 79 | 是 |
| 2025-12-09 | 长线程 | 复杂需求如何让AI一次写对？ | https://x.com/bourneliu66/status/1998578911027016162 | 163 | 是 |
| 2025-12-09 | 帖子 | 昨天第一次尝试付费的公众号文章 | https://x.com/bourneliu66/status/1998596675796181305 | 63 | 是 |
| 2025-12-10 | 引用帖 | As a heavy Claude Code user who once burned $50k w… | https://x.com/bourneliu66/status/1998687061449257204 | 19 | 是 |
| 2025-12-10 | 帖子 | 美团把它的一部分前端程序员强行合并到服务端组了。 | https://x.com/bourneliu66/status/1998974042267865159 | 118 | 是 |
| 2025-12-11 | 长帖 | 从100万月活跌下来之后，我让Raphael AI 再次起飞：没投广告，只做了4件小事。 | https://x.com/bourneliu66/status/1999151525189599389 | 115 | 是 |
| 2025-12-11 | 长线程 | 据内部人士爆料，快手研发线紧急限制Cursor、Claude Code等第三方编程工具使用，办公端直… | https://x.com/bourneliu66/status/1999225912118927868 | 200 | 是 |
| 2025-12-12 | 帖子 | 智谱语音输入法(电脑版）在Macbook上的产品体验还不错，就是语音识别不太准。 | https://x.com/bourneliu66/status/1999521467227164744 | 12 | 是 |
| 2025-12-14 | 长帖 | 我们对 AI 的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定一切的通用智能体（A… | https://x.com/bourneliu66/status/2000208636094627995 | 154 | 是 |
| 2025-12-14 | 帖子 | 分享一个好玩的事：刚才在Google Antigravity里写代码，发现Antigravity竟然… | https://x.com/bourneliu66/status/2000427430071390476 | 58 | 是 |
| 2025-12-15 | 帖子 | 确认偏误并非人类操作系统中的偶发漏洞，它就是操作系统本身。 | https://x.com/bourneliu66/status/2000486939921969609 | 5 | 是 |
| 2025-12-16 | 帖子 | 我也没想到。。。用Google Antigravity给我的Macbook清理了158GB的硬盘空间… | https://x.com/bourneliu66/status/2000988081747607668 | 365 | 是 |
| 2025-12-20 | 帖子 | 有些人不需要办公室。 | https://x.com/bourneliu66/status/2002585404370006414 | 137 | 是 |
| 2025-12-23 | 帖子 | 我找到了真正的Nano Banana 🍌  ，和手指差不多大 https://t.co/PdCaxF… | https://x.com/bourneliu66/status/2003391027865145710 | 5 | 是 |
| 2025-12-23 | 帖子 | GLM-4.7 写代码挺强的，尤其是审美变好了。 | https://x.com/bourneliu66/status/2003392984709226837 | 86 | 是 |
| 2025-12-23 | 帖子 | 江山代有模型出，各领风骚一个月 | https://x.com/bourneliu66/status/2003499056627404882 | 20 | 是 |
| 2025-12-24 | 帖子 | 哈哈哈哈 https://t.co/23yFUvdnyY | https://x.com/bourneliu66/status/2004030386880602285 | 6 | 是 |
| 2025-12-25 | 帖子 | 我一个学生的ChatGPT年度总结竟然是这样的……他脑子里都装的啥😂 https://t.co/dj… | https://x.com/bourneliu66/status/2004202086796611907 | 12 | 是 |
| 2025-12-26 | 长帖 | 买了智谱GLM coding会员套餐的 | https://x.com/bourneliu66/status/2004493894059483536 | 54 | 是 |
| 2025-12-26 | 帖子 | 你不让我写代码？？ | https://x.com/bourneliu66/status/2004619185427828881 | 6 | 是 |
| 2025-12-27 | 帖子 | Raphael 的Logo终于升级了 | https://x.com/bourneliu66/status/2004783358015144431 | 20 | 是 |
| 2025-12-28 | 帖子 | 用Gemini 3  Pro来当导游也太好用了！ 我拍了塔的照片，让Gemini 在照片上给我标注出… | https://x.com/bourneliu66/status/2005168169506509201 | 169 | 是 |
| 2025-12-28 | 帖子 | 分享一个小技巧：一键拯救大模型的前端审美能力 | https://x.com/bourneliu66/status/2005352019847168133 | 239 | 是 |
| 2025-12-29 | 帖子 | 路上遇到一只绿茶猫，二话不说就往我身上爬 https://t.co/UBKbHjWTFz | https://x.com/bourneliu66/status/2005536004195930312 | 2 | 是 |
| 2025-12-30 | 帖子 | 不加班、不PUA，还给全员发 iPhone 17 Pro Max：创业一年，我们居然没死！ | https://x.com/bourneliu66/status/2006036082094207408 | 99 | 是 |
| 2026-01-03 | 帖子 | 新的一年 | https://x.com/bourneliu66/status/2007674997708599663 | 25 | 是 |
| 2026-01-04 | 帖子 | 第一天用 #GetSeed  这是AI结合我今天的所有行为生成的“发芽报告”。感觉还挺不错。 htt… | https://x.com/bourneliu66/status/2007817161470038278 | 11 | 是 |
| 2026-01-05 | 帖子 | 每个人都在不断地重塑自己 | https://x.com/bourneliu66/status/2008175492814577992 | 14 | 是 |
| 2026-01-07 | 帖子 | 最近产品用户规模和收入都新高了，我感恩自己遇到的一切 | https://x.com/bourneliu66/status/2008938308202872910 | 35 | 是 |
| 2026-01-13 | 帖子 | The House of Representatives on Monday passed a bi… | https://x.com/bourneliu66/status/2011258476086083909 | 18 | 是 |
| 2026-01-16 | 帖子 | 天鹅想吃癞蛤蟆肉 https://t.co/okc7IxW9gQ | https://x.com/bourneliu66/status/2012045113544098156 | 6 | 是 |
| 2026-01-20 | 帖子 | 我以前常说：“一件事情，只要敢有SOP，它就能被自动化。” | https://x.com/bourneliu66/status/2013510096794312825 | 96 | 是 |
| 2026-01-20 | 帖子 | 哈哈哈哈哈哈 https://t.co/qgI2mq0PJ9 | https://x.com/bourneliu66/status/2013560551637393542 | 10 | 是 |
| 2026-01-21 | 帖子 | 有了AI编程以后，每天不睡觉，不是因为工作压力大，也不是因为焦虑，而是因为——太好玩了，舍不得睡。 | https://x.com/bourneliu66/status/2014064928391299422 | 177 | 是 |
| 2026-01-22 | 长帖 | 最近，Pencil火出了天际。我一开始没当回事。 | https://x.com/bourneliu66/status/2014420652112110024 | 1360 | 是 |
| 2026-01-23 | 长帖 | 搞Vibe Coding的人每天睡那么少，怎么还没猝死？ | https://x.com/bourneliu66/status/2014750494175199472 | 75 | 是 |
| 2026-01-27 | 帖子 | 昨天看了Dify vp演讲的cut，我做噩梦了 | https://x.com/bourneliu66/status/2016362279508521114 | 9 | 是 |
| 2026-01-28 | 帖子 | 腾讯云可以一键部署Moltbot(Clawdbot)了 https://t.co/NdcEcKkEm… | https://x.com/bourneliu66/status/2016437789504700805 | 28 | 是 |
| 2026-01-28 | 帖子 | Clawdbot这个场景还挺好的： 让在外面吃饭，突然同事提交了代码，让我部署上线。我虽然手上没电脑… | https://x.com/bourneliu66/status/2016532279196336407 | 34 | 是 |
| 2026-01-28 | 帖子 | 大半夜的，接到Clawdbot通过飞书打来的电话，说有急事……原来是产品爆单了😂 | https://x.com/bourneliu66/status/2016578048079122615 | 1227 | 是 |
| 2026-01-29 | 帖子 | 我的Clawdbot和你的一样，只不过你多花了4000元 | https://x.com/bourneliu66/status/2016743709610762594 | 221 | 是 |
| 2026-01-31 | 长线程 | HunyuanImage 3.0 蒸馏版开源 🔥 | https://x.com/bourneliu66/status/2017680870841143544 | 39 | 是 |
| 2026-01-31 | 帖子 | 我做了个小工具 Ralph Desktop | https://x.com/bourneliu66/status/2017683094690541723 | 117 | 是 |
| 2026-02-03 | 帖子 | 我给了 openclaw 一个真的飞书账号（而不是 飞书 bot）。 | https://x.com/bourneliu66/status/2018568464584315095 | 126 | 是 |
| 2026-02-03 | 帖子 | I'm claiming my AI agent "Xiaopai-Assistant" on @m… | https://x.com/bourneliu66/status/2018634426562044188 | 10 | 是 |
| 2026-02-03 | 长线程 | 我家小龙虾在 Moltbook 建了个宗教：一人公司教 —  老板真人，员工全 AI，教义是《AI … | https://x.com/bourneliu66/status/2018664138571133235 | 7 | 是 |
| 2026-02-04 | 帖子 | Mistral 开源 Voxtral Mini 4B Realtime ⚡ | https://x.com/bourneliu66/status/2019127000032510432 | 163 | 是 |
| 2026-02-04 | 回复 | 🔗 https://t.co/YoxOx1ubJr | https://x.com/bourneliu66/status/2019127041979723797 | 12 | 是 |
| 2026-02-05 | 帖子 | GPT-5.3-Codex 也来了，难以抉择，两个都好。。 https://t.co/nTxzhvM… | https://x.com/bourneliu66/status/2019476251811946927 | 45 | 是 |
| 2026-02-05 | 帖子 | GPT-5.3-Codex 和 Claude Opus 4.6 | https://x.com/bourneliu66/status/2019479483364045265 | 116 | 是 |
| 2026-02-05 | 回复 | @mmee_io 升级 | https://x.com/bourneliu66/status/2019480507394978044 | 0 | 是 |
| 2026-02-05 | 帖子 | https://t.co/xz7lTxKvkg | https://x.com/bourneliu66/status/2019633763765088738 | 11 | 是 |
| 2026-02-06 | 帖子 | 咦，GPT-5.3-Codex 还会没事刷存在感？？ 我让你补了吗 https://t.co/j0q… | https://x.com/bourneliu66/status/2019639179186172027 | 29 | 是 |
| 2026-02-06 | 帖子 | Google Antigravy里支持Opus 4.6 Thinking模型了。 | https://x.com/bourneliu66/status/2019973031884685423 | 194 | 是 |
| 2026-02-06 | 帖子 | 我的OpenClaw做了个开源产品： Brainstorming Online | https://x.com/bourneliu66/status/2019977940549923247 | 150 | 是 |
| 2026-02-07 | 帖子 | OpenClaw 成功把它$200/月的 ChatGPT Pro Plan 用到限流了，我也该睡觉了… | https://x.com/bourneliu66/status/2020008707053220059 | 20 | 是 |
| 2026-02-07 | 回复 | @fuck_X123 Ultra Plan | https://x.com/bourneliu66/status/2020010462474334269 | 0 | 是 |
| 2026-02-07 | 回复 | 注意：现在暂时只有 Google AI Ultra 套餐科研用 Opus 4.6， Pro 套餐还没… | https://x.com/bourneliu66/status/2020010680531988741 | 7 | 是 |
| 2026-02-07 | 帖子 | 血月 https://t.co/hGv9A3vXt4 | https://x.com/bourneliu66/status/2020161636921733231 | 2 | 是 |
| 2026-02-07 | 帖子 | 小龙虾是烧钱神器啊。再培养培养，应该很快可以超过我本人了。 https://t.co/0TRGf6o… | https://x.com/bourneliu66/status/2020191352450170954 | 53 | 是 |
| 2026-02-07 | 帖子 | Opus 4.6 + Agent Teams &gt; GPT-5.3-Codex &gt; Opu… | https://x.com/bourneliu66/status/2020343282606436839 | 54 | 是 |
| 2026-02-08 | 帖子 | 家人们，我上新华社官网首页了…… | https://x.com/bourneliu66/status/2020403438216217034 | 67 | 是 |
| 2026-02-08 | 帖子 | 说真的，你们公司最卷的员工，日报也写不过我这个AI…… | https://x.com/bourneliu66/status/2020562004214202630 | 32 | 是 |
| 2026-02-10 | 帖子 | 虾哥，你反了？？？ https://t.co/V1HhfaQnh1 | https://x.com/bourneliu66/status/2021271736894030109 | 18 | 是 |
| 2026-02-15 | 帖子 | 过年了，躺平了 https://t.co/Gofl5wYAAh | https://x.com/bourneliu66/status/2023058167765069989 | 17 | 是 |
| 2026-02-26 | 帖子 | 我做Claude Code榜一大哥的时候，OpenClaw的作者 Peter Steinberger… | https://x.com/bourneliu66/status/2027093174318256530 | 71 | 是 |
| 2026-02-26 | 引用帖 | 我的两个Google AI Ultra账号，前段时间因为用Antigravity反代Claude C… | https://x.com/bourneliu66/status/2027224604666912824 | 64 | 是 |
| 2026-02-27 | 帖子 | OpenClaw的作者，1天内给OpenClaw提交了627次代码！！他是如何做到的？ | https://x.com/bourneliu66/status/2027418737595584795 | 475 | 是 |
| 2026-02-28 | 帖子 | https://t.co/2QgMc8vJoE | https://x.com/bourneliu66/status/2027692307718525427 | 13 | 是 |
| 2026-03-01 | 帖子 | 用小龙虾做了个公众号排版工具 | https://x.com/bourneliu66/status/2028140902431265076 | 707 | 是 |
| 2026-03-01 | 回复 | @Jerome1698062 不是，我vps的 | https://x.com/bourneliu66/status/2028148669703508070 | 1 | 是 |
| 2026-03-02 | 帖子 | 如何让OpenClaw指挥Codex、Gemini CLI、Claude Code三位大哥协作写代码… | https://x.com/bourneliu66/status/2028450127149674642 | 472 | 是 |
| 2026-03-03 | 帖子 | 我的开源项目第一次上Github热点 (Github Trending) | https://x.com/bourneliu66/status/2028811610396164208 | 54 | 是 |
| 2026-03-03 | 长帖 | 从今天开始，你们用的OpenClaw里，有我的代码了！ | https://x.com/bourneliu66/status/2028865085587018195 | 560 | 是 |
| 2026-03-04 | 帖子 | 我们的前台员工兼保安大爷已经有专属工位了 https://t.co/ELou8eOxTj | https://x.com/bourneliu66/status/2029095451975397527 | 27 | 是 |
| 2026-03-05 | 帖子 | GPT-5.4 和 GPT-5.4 Pro 发布了，退订 Claude Code 吧！ | https://x.com/bourneliu66/status/2029640270023905474 | 139 | 是 |
| 2026-03-05 | 引用帖 | 哈哈哈，可不是嘛，七进七出啊。 | https://x.com/bourneliu66/status/2029760593520124322 | 4 | 是 |
| 2026-03-06 | 帖子 | 「为什么坐标图的横轴要设计成红色？」 | https://x.com/bourneliu66/status/2029858382883275021 | 38 | 是 |
| 2026-03-06 | 帖子 | 你们发现没， “Vibe Coding”已经成为贬义词了 | https://x.com/bourneliu66/status/2029973481967018042 | 146 | 是 |
| 2026-03-06 | 帖子 | Codex的新功能： | https://x.com/bourneliu66/status/2029976435776192817 | 36 | 是 |
| 2026-03-09 | 帖子 | AI 编程课到处都是。 | https://x.com/bourneliu66/status/2030871119444758779 | 38 | 是 |
| 2026-03-09 | 帖子 | 请教个问题： | https://x.com/bourneliu66/status/2030955926250017012 | 3 | 是 |
| 2026-03-09 | 帖子 | 我投资的一个API平台被某著名大V自来水宣传了，小火了一波，哈哈哈。 https://t.co/wi… | https://x.com/bourneliu66/status/2030988234646512076 | 29 | 是 |
| 2026-03-13 | 帖子 | 打开Codex Fast Mode以后，掉血太快了。 | https://x.com/bourneliu66/status/2032441711671259361 | 45 | 是 |
| 2026-03-21 | 帖子 | 如果一个人在某些方面天赋异禀， | https://x.com/bourneliu66/status/2035274476355805489 | 35 | 是 |
| 2026-03-31 | 帖子 | AI圈三大不懂装懂的业余病 | https://x.com/bourneliu66/status/2038833979055571092 | 48 | 是 |
| 2026-03-31 | 长帖 | GitHub将使用你的代码来训练模型，除非你在4月24日之前关闭它，否则视为你允许！ | https://x.com/bourneliu66/status/2038863225673138237 | 43 | 是 |
| 2026-04-09 | 帖子 | 今天早起了，感觉不错～  现在该午休了 https://t.co/wkMyjuf9Uy | https://x.com/bourneliu66/status/2042105110428569641 | 15 | 是 |
| 2026-04-15 | 帖子 | 难熬的夜 https://t.co/NOg5nJsEbd | https://x.com/bourneliu66/status/2044420704200970603 | 7 | 是 |
| 2026-04-16 | 帖子 | 我认为，我们应该多关注Builders（动手做事的人），少关注Influencers（只做自媒体的人… | https://x.com/bourneliu66/status/2044685616408109213 | 406 | 是 |
| 2026-04-21 | 帖子 | Kimi K2.6 可能被严重低估了。 | https://x.com/bourneliu66/status/2046479442713924037 | 151 | 是 |
| 2026-04-21 | 帖子 | Claude Opus 4.7 说的这些，是人话吗？想要看懂好困难 https://t.co/qBn… | https://x.com/bourneliu66/status/2046613753962394039 | 5 | 是 |
| 2026-04-22 | 帖子 | 这个ChatGPT Images 2.0 API 是怎么回事？ | https://x.com/bourneliu66/status/2046889859479183625 | 231 | 是 |
| 2026-04-24 | 帖子 | GPT-5.5 Pro 也太牛了吧。 | https://x.com/bourneliu66/status/2047554511439527976 | 174 | 是 |
| 2026-05-08 | 帖子 | AI干活太慢了。一边玩影游一边玩AI 生活更充实。 https://t.co/7JCgZ8mDNy | https://x.com/bourneliu66/status/2052643872522838160 | 32 | 是 |
| 2026-05-08 | 回复 | @aulaylab 你要脸吗？ | https://x.com/bourneliu66/status/2052658114592473094 | 2 | 是 |
| 2026-05-09 | 帖子 | 安装Hermes Agent，只需要一句话。 | https://x.com/bourneliu66/status/2053159212675629512 | 120 | 是 |
| 2026-05-09 | 帖子 | 用Hermes来帮我们读微信，非常好玩！ | https://x.com/bourneliu66/status/2053160329107116425 | 294 | 是 |
| 2026-05-12 | 长线程 | @AYiAInotes 有人认识这哥们吗？？？ | https://x.com/bourneliu66/status/2054191141336347088 | 32 | 是 |
| 2026-05-26 | 帖子 | 都说用了AI会变成超人。诚不我欺也 https://t.co/wQeYy76HB9 | https://x.com/bourneliu66/status/2059214609224229215 | 10 | 是 |
| 2026-06-03 | 帖子 | 账号被盗了，还好发现得及时，花了3天，刚申诉回来。。 | https://x.com/bourneliu66/status/2062383456051683344 | 15 | 是 |
| 2026-06-04 | 帖子 | 扣子(coze)的新功能：可以用手机控制电脑上的Claude Code和Codex。 | https://x.com/bourneliu66/status/2062433480404042119 | 57 | 是 |
| 2026-06-09 | 帖子 | MiMo-V2.5-Pro UltraSpeed的速度快得有点太过分了，代码写的太快就像龙卷风…… | https://x.com/bourneliu66/status/2064228432930894287 | 403 | 是 |
| 2026-06-11 | 帖子 | Fable 5强得有点过分，大量GPT-5.5做不到的事情，它都能瞬间完成。 | https://x.com/bourneliu66/status/2065279487219310981 | 205 | 是 |
| 2026-06-12 | 帖子 | GPT-5.5和Opus 4.8都搞不定的Bug，被Fable 5一晚上解决。 | https://x.com/bourneliu66/status/2065329731801927844 | 120 | 是 |
| 2026-06-12 | 引用帖 | 对了，这里还有一个稍微有点恶心的经历。 | https://x.com/bourneliu66/status/2065352862755078389 | 11 | 是 |
| 2026-06-12 | 帖子 | 猫咪 + Fable 5 = 无法自拔的幸福生活 https://t.co/rGm26GsLC9 | https://x.com/bourneliu66/status/2065394756314857922 | 18 | 是 |
| 2026-06-14 | 帖子 | 新的办公装备！Vibe Coding 绝配！！ | https://x.com/bourneliu66/status/2066022130572312861 | 136 | 是 |
| 2026-06-14 | 引用帖 | 朋友用AI帮我P了个图 😂 https://t.co/ufarqFzDiu https://t.co… | https://x.com/bourneliu66/status/2066078579390345304 | 10 | 是 |
| 2026-06-14 | 帖子 | 有人说自己的Fable 5回来了，就在刚才，是用iOS美区订阅的。你们说，是真的吗？？ https:… | https://x.com/bourneliu66/status/2066197628862566511 | 43 | 是 |
| 2026-06-14 | 帖子 | 一图搞懂 Harness Engineering https://t.co/0ktjJxvBuv | https://x.com/bourneliu66/status/2066366629362180283 | 109 | 是 |
| 2026-06-15 | 长线程 | 我要强烈推荐 Kimi K2.7 High Speed (高速版）！太神奇了！ | https://x.com/bourneliu66/status/2066436537085276284 | 822 | 是 |
| 2026-06-16 | 帖子 | 现在不再是“砍一刀”，是“点火”了？ | https://x.com/bourneliu66/status/2066791989878956289 | 8 | 是 |
| 2026-06-20 | 帖子 | 微信AI “小微” 开始灰度内测！！！ 打通了微信的全部生态全部功能，包括发消息、打电话、朋友圈、视… | https://x.com/bourneliu66/status/2068281908782563747 | 37 | 是 |
| 2026-06-21 | 引用帖 | 欢迎小红书运营女神 https://t.co/jYiX8bH8T0 | https://x.com/bourneliu66/status/2068578092155912538 | 27 | 是 |
| 2026-06-23 | 帖子 | 以我对 OpenAI 的了解，他们绝对不会在 Fable 5 回归之前发布 GPT-5.6。 | https://x.com/bourneliu66/status/2069508823078097103 | 86 | 是 |
| 2026-06-25 | 帖子 | 主力电脑上对 agent 开最大权限，虽然方便，但我们还是得谨慎，折中的方案是沙箱开最大权限。 | https://x.com/bourneliu66/status/2070046629282173413 | 44 | 是 |
| 2026-06-25 | 长帖 | 🚨 BREAKING: Fable 5 is likely returning very soon! | https://x.com/bourneliu66/status/2070053821699743785 | 22 | 是 |
| 2026-06-25 | 长线程 | 去年，如果你每个月消耗77亿token(每天2.5亿）可以当全球第一。 | https://x.com/bourneliu66/status/2070058995935850681 | 29 | 是 |
| 2026-06-25 | 帖子 | 这是真的吗？？Anthropic要换CEO了？？ | https://x.com/bourneliu66/status/2070126243765440759 | 67 | 是 |
| 2026-06-25 | 帖子 | 新摩尔定律：每过18个月，性能不变，价格翻一番 | https://x.com/bourneliu66/status/2070331330311954585 | 87 | 是 |
| 2026-06-26 | 帖子 | 今天看周杰伦演唱会，突然想到一个问题。 | https://x.com/bourneliu66/status/2070540631215337888 | 12 | 是 |
| 2026-07-02 | 帖子 | 最近，有坏人称某知名大模型产品为「美国豆包」。 | https://x.com/bourneliu66/status/2072730191831638364 | 736 | 是 |
| 2026-07-03 | 长线程 | 一键检测：你的Claude Code看起来有多像是中国用户？ https://t.co/wIidVr… | https://x.com/bourneliu66/status/2072979549273591922 | 49 | 是 |
| 2026-07-06 | 帖子 | 等待Codex/Claude Code干活的时候，我们该干点呢？ | https://x.com/bourneliu66/status/2074019065660891184 | 4 | 是 |
| 2026-07-06 | 帖子 | 同样是$200美金/月的账号 | https://x.com/bourneliu66/status/2074025001398022205 | 50 | 是 |
| 2026-07-06 | 帖子 | 喜欢猫的朋友来做下这个题？ https://t.co/2TgWO4W5ZE | https://x.com/bourneliu66/status/2074210807865585986 | 2 | 是 |
| 2026-07-06 | 帖子 | Fable 5最后一天！火力全开！ https://t.co/w9oHoU15M2 | https://x.com/bourneliu66/status/2074316297647931599 | 7 | 是 |
| 2026-07-07 | 长线程 | 我做了一个可能被全球老板拉黑的产品 ——「摸鱼」（英文名 SneakRead）。 | https://x.com/bourneliu66/status/2074410494719569949 | 74 | 是 |
| 2026-07-09 | 帖子 | 有意思：“御三家”里，再次失去中国模型的位置。GLM 5.2 的位置已经毫无悬念地被 Grok 4.… | https://x.com/bourneliu66/status/2075253698700427570 | 311 | 是 |
| 2026-07-09 | 帖子 | 在GPT-5.6发布的一瞬间（就是刚才，不久之前），Claude Code 突然重置了周额度 。（你… | https://x.com/bourneliu66/status/2075280678334378157 | 29 | 是 |
| 2026-07-10 | 长线程 | GPT-5.6-Sol 烧 Token 快，不是因为贵——单价和 5.5 一样，只有 Fable 5… | https://x.com/bourneliu66/status/2075612629599695159 | 135 | 是 |
| 2026-07-10 | 帖子 | 过去24小时我消耗了GPT-5.6-Sol Ultra的50亿Token。 | https://x.com/bourneliu66/status/2075626581104656596 | 109 | 是 |
| 2026-07-10 | 帖子 | 大模型就是一个海鲜生意，打捞起来的一两周内卖不掉，就再也卖不掉了。 | https://x.com/bourneliu66/status/2075640512149872853 | 184 | 是 |
| 2026-07-15 | 回复 | @keenn_eth 好 | https://x.com/bourneliu66/status/2077506484108406811 | 1 | 是 |
| 2026-07-17 | 长帖 | 用Kimi K3做了一款致敬《杀戮尖塔2》的游戏，《杀戮三国》，核心角色玩法全部基于三国人物特性。 | https://x.com/bourneliu66/status/2078012191169810475 | 1235 | 是 |
| 2026-07-17 | 帖子 | Urgent: Multiple stores on @creem_io are unable to… | https://x.com/bourneliu66/status/2078019445847658738 | 7 | 是 |
| 2026-07-17 | 回复 | @sudoferraz | https://x.com/bourneliu66/status/2078020254186504356 | 0 | 是 |
| 2026-07-17 | 长帖 | @sudoferraz @creem_io @sudoferraz @creem_io We’ve … | https://x.com/bourneliu66/status/2078026058411184531 | 1 | 是 |
| 2026-07-17 | 回复 | @TunaCookie_ by GPT-Image-2 API | https://x.com/bourneliu66/status/2078033432782000605 | 30 | 是 |
| 2026-07-17 | 回复 | @lolieatapple AI打游戏不需要界面 | https://x.com/bourneliu66/status/2078033462528000258 | 35 | 是 |
| 2026-07-17 | 帖子 | 🚨 BREAKING： | https://x.com/bourneliu66/status/2078150582054133991 | 4722 | 是 |
| 2026-07-19 | 帖子 | 预测： | https://x.com/bourneliu66/status/2078936824005988417 | 328 | 是 |
| 2026-07-20 | 帖子 | GPT-5.6 Sol，什么medium、high、xhigh都是假的， | https://x.com/bourneliu66/status/2079257656880218245 | 115 | 是 |
| 2026-07-20 | 帖子 | 如何像Peter Steiberger一样，一个人同时管理数十个AI程序员？ | https://x.com/bourneliu66/status/2079416003285655947 | 72 | 是 |
| 2026-07-21 | 回复 | https://t.co/zMsGPDBeIE | https://x.com/bourneliu66/status/2079416183842103748 | 0 | 是 |
| 2026-07-21 | 帖子 | 我发现，GPT-5.6-Terra(Max)被严重低估了！ | https://x.com/bourneliu66/status/2079486678709023010 | 255 | 是 |
| 2026-07-21 | 帖子 | 中国排名第一的大学有两所，排名前三的大学有五所，排名前十的大学有二十所。 | https://x.com/bourneliu66/status/2079508357648687119 | 27 | 是 |
| 2026-07-21 | 帖子 | WorkBuddy很好！（发自内心推荐，非商单） https://t.co/RyC33Sm7Ho | https://x.com/bourneliu66/status/2079538788033069561 | 72 | 是 |
| 2026-07-21 | 帖子 | GPT-5.6’s forecast for the next Codex reset:​ | https://x.com/bourneliu66/status/2079544151385817333 | 53 | 是 |
| 2026-07-22 | 帖子 | @grok 这到底是谁呀？为啥突然我的X时间轴全是她各种角度的照片，连衣服都没换 https://t… | https://x.com/bourneliu66/status/2079786556873945160 | 3 | 是 |
| 2026-07-22 | 帖子 | @thsottiaux Even with frequent resets, my ChatGPT … | https://x.com/bourneliu66/status/2079812039753773513 | 13 | 是 |
| 2026-07-23 | 引用帖 | 原本这只是我编的一个段子，没想到美国政府真的在认真的评估Kimi K3是否蒸馏了Fable 5 ？？ | https://x.com/bourneliu66/status/2080163064964665504 | 27 | 是 |
| 2026-07-24 | 帖子 | 马上周末了，好期待！ | https://x.com/bourneliu66/status/2080567977204973829 | 19 | 是 |
| 2026-07-24 | 回复 | @Leepriest1990 多账号 | https://x.com/bourneliu66/status/2080570022314008754 | 1 | 是 |
| 2026-07-24 | 帖子 | 最近我喜欢Kimi K3超过Fable 5和GPT-5.6 Sol | https://x.com/bourneliu66/status/2080694257770451165 | 137 | 是 |
| 2026-07-24 | 帖子 | 为了用Claude Code，我把AI员工送出国了！ | https://x.com/bourneliu66/status/2080705806564254202 | 422 | 是 |
| 2026-07-24 | 帖子 | @thsottiaux 我方防御塔正在被攻击！ | https://x.com/bourneliu66/status/2080708108901593452 | 10 | 是 |
| 2026-07-26 | 长帖 | 一天之内使用了28亿 Token的Opus 5，以下是我的感受： | https://x.com/bourneliu66/status/2081269376700015070 | 68 | 是 |
| 2026-07-26 | 帖子 | 今天Claude Code出了大漏洞，可以免费订阅Max Plan 20x。身边好多朋友都已经成功用… | https://x.com/bourneliu66/status/2081300898308104530 | 100 | 是 |
| 2026-07-26 | 帖子 | Codex的宠物功能实在是太难用也太丑了，  我不信有人愿意主动打开它！ | https://x.com/bourneliu66/status/2081448328848617560 | 63 | 是 |
| 2026-07-27 | 引用帖 | Vibes are strong. Never seen the Codex reset crowd… | https://x.com/bourneliu66/status/2081648799093813714 | 11 | 是 |
| 2026-07-28 | 长帖 | GPT-5.6 Pro绝对是最强编程模型，远超GPT-5.6 Sol和Fable 5。 | https://x.com/bourneliu66/status/2082106402336882887 | 675 | 是 |
| 2026-07-29 | 帖子 | 我的Codex刚用了重置卡后的第4分钟，官方自己重置了。 @thsottiaux  哦豁，浪费一张！ | https://x.com/bourneliu66/status/2082333158301904966 | 66 | 是 |
| 2026-07-29 | 帖子 | 谁都希望万事如意，但真正推动创新的往往是那些卡壳的、不如意的时刻。 | https://x.com/bourneliu66/status/2082359315189641470 | 20 | 是 |
| 2026-07-29 | 帖子 | AI 模型公司正在进入“创新者的窘境前夜”，AI 应用公司则正在进入“创新者的红利期”。 | https://x.com/bourneliu66/status/2082512915182342355 | 20 | 是 |
| 2026-07-30 | 长帖 | 🚨BREAKING: | https://x.com/bourneliu66/status/2082712155305255352 | 125 | 是 |
| 2026-07-30 | 帖子 | ChatGPT Pro 太懂我了 https://t.co/N3nAvyB91T | https://x.com/bourneliu66/status/2082745936082583902 | 36 | 是 |
| 2026-07-31 | 帖子 | 休息一天！ | https://x.com/bourneliu66/status/2083099905728610457 | 30 | 是 |
| 2026-08-01 | 帖子 | 斗胆预测：下周，美国科技股必将暴跌。 | https://x.com/bourneliu66/status/2083573304716296346 | 341 | 是 |
| 2026-08-02 | 帖子 | The biggest disruption in AI may not come from a s… | https://x.com/bourneliu66/status/2083809650756210702 | 17 | 是 |
| 2026-08-03 | 长线程 | 最近，我已经习惯不直接使用电脑了。 | https://x.com/bourneliu66/status/2084157450744443214 | 198 | 是 |
| 2026-08-03 | 引用帖 | 我看评论区才发现，已经很多人用上了！！补充几个其他朋友的截图 https://t.co/XuhBfO… | https://x.com/bourneliu66/status/2084179663035985944 | 93 | 是 |
| 2026-08-03 | 帖子 | GPT-5.6-Sol 不懂什么叫「做产品」 | https://x.com/bourneliu66/status/2084247026649428312 | 75 | 是 |
| 2026-08-03 | 帖子 | 哥大到底是个什么学校？ | https://x.com/bourneliu66/status/2084323078700675186 | 3 | 是 |
| 2026-08-03 | 帖子 | Claude Code和Codex都好些天没更新版本了？ | https://x.com/bourneliu66/status/2084352222440353833 | 59 | 是 |
| 2026-08-04 | 帖子 | 难道没有人发现 Opus 5 只是一个刷榜怪吗？？ | https://x.com/bourneliu66/status/2084492967126163595 | 54 | 是 |
| 2026-08-04 | 引用帖 | 我学生的产品，谢谢大家支持！ https://t.co/rci5FTLErG | https://x.com/bourneliu66/status/2084580999426678819 | 23 | 是 |
| 2026-08-04 | 帖子 | @thsottiaux 义父，好几天都没reset了，您还健康吗？ | https://x.com/bourneliu66/status/2084652821006454847 | 14 | 是 |
| 2026-08-04 | 帖子 | 为什么今天大家都在抢注 Cloudflare 的钱包？我不信有人用得上！ | https://x.com/bourneliu66/status/2084847367992545421 | 70 | 是 |
| 2026-08-05 | 帖子 | 测试Raphael AI的新版UI。你感觉怎么样？ | https://x.com/bourneliu66/status/2085025344055279996 | 33 | 是 |
| 2026-08-06 | 引用帖 | 明确表示喜欢新版（左）：10人 | https://x.com/bourneliu66/status/2085300320620761460 | 7 | 是 |
| 2026-08-07 | 长线程 | 家人们，可能有反转：  虽然绝大多数人说新版更好看，但是，我上线测试的这段时间，发现每天的收入情况跌… | https://x.com/bourneliu66/status/2085596342584566070 | 18 | 是 |
| 2026-08-07 | 长线程 | 昨天同时宠幸了4个来自不同种族的员工。 https://t.co/vVGemhlMhw | https://x.com/bourneliu66/status/2085632851874394317 | 15 | 是 |
| 2026-08-07 | 长线程 | 我找到了 ChatGPT Pro 降智的真解法： | https://x.com/bourneliu66/status/2085650105005449226 | 310 | 是 |
| 2026-08-07 | 帖子 | 没人毁掉你。你只是每天刷着不用动脑的东西，刷了三年,然后发现自己连一篇长文都读不完了。 | https://x.com/bourneliu66/status/2085673142568301037 | 114 | 是 |
| 2026-08-08 | 帖子 | 一个非常合理的猜测：codex下次重置时间是8月14日。 | https://x.com/bourneliu66/status/2086189381078139350 | 93 | 是 |
| 2026-08-09 | 引用帖 | 李老师所言甚是！ https://t.co/aU9iYbTKWg | https://x.com/bourneliu66/status/2086435375086714986 | 23 | 是 |
| 2026-08-09 | 帖子 | 现在热门创业的产品方向，一窝蜂都是在赶时髦做Agent产品，比如“某领域的Manus”、“某领域的C… | https://x.com/bourneliu66/status/2086489847691383209 | 106 | 是 |
| 2026-08-10 | 帖子 | Flux 3 ，比 Seedance 2.5 和 Minimax H3 加起来还牛 https://… | https://x.com/bourneliu66/status/2086796257264287774 | 183 | 是 |
| 2026-08-10 | 帖子 | 最近学会了一个 2026 年最先进的创业方法论，分享给大家： | https://x.com/bourneliu66/status/2086833147879236037 | 124 | 是 |
| 2026-08-11 | 帖子 | DeepSeek：世界上最耿直的模型 https://t.co/bXWf9yglsf | https://x.com/bourneliu66/status/2087118459763351762 | 298 | 是 |
| 2026-08-11 | 回复 | @CuiMao @thsottiaux tibo竟然用claude来生成视频 | https://x.com/bourneliu66/status/2087126594095898763 | 2 | 是 |
| 2026-08-11 | 帖子 | 微软Bing搜索的产品经理是个天才， | https://x.com/bourneliu66/status/2087232563706479088 | 869 | 是 |
| 2026-08-13 | 帖子 | 我对阿里这家公司没有偏见，我持有阿里的股票，阿里的Qwen-3.8-Max很厉害是有目共睹的。 | https://x.com/bourneliu66/status/2087776614142898627 | 45 | 是 |
| 2026-08-13 | 长帖 | 昨天，我打算一个产品的集群部署。 | https://x.com/bourneliu66/status/2087803354332422415 | 53 | 是 |
| 2026-08-13 | 帖子 | 在今天凌晨偷偷发布的DeepSeek V4 Pro 0813 由于口碑太差，即将下架，回炉重造。 | https://x.com/bourneliu66/status/2087825941854855285 | 171 | 是 |
| 2026-08-13 | 帖子 | DeepSeek真牛， | https://x.com/bourneliu66/status/2087899781389811883 | 720 | 是 |
| 2026-08-13 | 帖子 | DeepSeek Harness 在开发时候明显使用了Claude Code (看截图，你肯定懂），… | https://x.com/bourneliu66/status/2087941286913511542 | 44 | 是 |
| 2026-08-13 | 引用帖 | 我原本预测Codex会在8月14日重置，因为8月13日大家的重置卡过期。 | https://x.com/bourneliu66/status/2087946401825378347 | 55 | 是 |
| 2026-08-13 | 引用帖 | 这个不能称之为证据啊，你可以点进去看一看。这个文件夹是为了方便 Claude Code 能够使用DH… | https://x.com/bourneliu66/status/2087961046179041492 | 17 | 是 |
| 2026-08-14 | 帖子 | Gemini 3.7 Flash 出乎意外的好用耶。 | https://x.com/bourneliu66/status/2088136361748598928 | 93 | 是 |
| 2026-08-14 | 引用帖 | 说一个很多人没注意到的事实： | https://x.com/bourneliu66/status/2088175504277070324 | 194 | 是 |
| 2026-08-14 | 引用帖 | 再加一条 | https://x.com/bourneliu66/status/2088194985485340990 | 45 | 是 |
| 2026-08-14 | 引用帖 | 来复习一下 我在一个月前的预测。当时，很多人不信。现在看看？ | https://x.com/bourneliu66/status/2088205980383547859 | 21 | 是 |
| 2026-08-14 | X Article | AI什么都会，我们为什么还要学习？ | https://x.com/bourneliu66/status/2088206544987181113 | 120 | 是 |
| 2026-08-14 | 引用帖 | 哎哟，有意思！支持。 https://t.co/BJloDsYy0E | https://x.com/bourneliu66/status/2088207666086883552 | 14 | 是 |
| 2026-08-14 | 帖子 | 一件非常恐怖的事，悄然发生了： Qwen3.8-27B 在大部分能力上都超过或逼近了Claude O… | https://x.com/bourneliu66/status/2088290784743464970 | 634 | 是 |
| 2026-08-16 | 帖子 | 我正在看 Sam Altman 的采访视频， | https://x.com/bourneliu66/status/2088904701295341629 | 19 | 是 |
| 2026-08-16 | 帖子 | 发明了一个新玩法： | https://x.com/bourneliu66/status/2089064061078298842 | 64 | 是 |
| 2026-08-21 | 帖子 | 耳边响起了《狮子王》的背景音乐 https://t.co/VGtkWFgERQ | https://x.com/bourneliu66/status/2091012479249789121 | 27 | 是 |
| 2026-09-01 | 帖子 | GrokBot = Jarvis | https://x.com/bourneliu66/status/2094714807694090415 | 14 | 是 |
| 2026-09-01 | 帖子 | 我宣布： Grok Bot 吊打一切OpenClaw、Hermes类伪数字员工！ | https://x.com/bourneliu66/status/2094829341473751381 | 574 | 是 |
| 2026-09-01 | 帖子 | Fable 5.1 真是跨时代级的大进步！ | https://x.com/bourneliu66/status/2094984871659921664 | 70 | 是 |
| 2026-09-03 | 帖子 | ？ https://t.co/XjHXpkMhSE | https://x.com/bourneliu66/status/2095446089667350929 | 109 | 是 |
| 2026-09-03 | 帖子 | 我猜测 GPT 6 Astra的编程能力不会有大提升 | https://x.com/bourneliu66/status/2095684943041241178 | 46 | 是 |
| 2026-09-07 | 帖子 | GPT-6 Astra 又杀死了好多创业公司。 | https://x.com/bourneliu66/status/2096984874800591119 | 510 | 是 |
| 2026-09-07 | 帖子 | GPT-6 Astra唯一正确用法：把你电脑给它！ | https://x.com/bourneliu66/status/2097010725642530999 | 56 | 是 |
| 2026-09-07 | 帖子 | 这都什么年代了 | https://x.com/bourneliu66/status/2097105743300460851 | 15 | 是 |
| 2026-09-12 | 回复 | @nuannuan_share 谢谢 不过 raphael ai 地址是 https://t.co/… | https://x.com/bourneliu66/status/2098969726236102721 | 20 | 是 |
| 2026-09-17 | 帖子 | Union Alpha 肯定不是中国模型。 | https://x.com/bourneliu66/status/2100453275929907246 | 5 | 是 |
| 2026-09-17 | 回复 | @crnobog2026 在哪儿爆的 | https://x.com/bourneliu66/status/2100468398774006223 | 1 | 是 |
| 2026-09-20 | 帖子 | 如果我说：除了作为玩具，我还没有明白Jev有什么实际的用途。 | https://x.com/bourneliu66/status/2101574790670942415 | 68 | 是 |
| 2026-09-22 | 帖子 | @thsottiaux 说好的重置呢？我3个号都用完了…… | https://x.com/bourneliu66/status/2102436783250444388 | 7 | 是 |
| 2026-09-22 | 帖子 | GPT-6-Sol和Claude Opus 5.5都来了。 | https://x.com/bourneliu66/status/2102465223282319418 | 298 | 是 |
| 2026-09-28 | 帖子 | Token 到用时方恨少 | https://x.com/bourneliu66/status/2104431367744626737 | 7 | 是 |
| 2026-09-28 | 帖子 | 你们的是怎样的？ | https://x.com/bourneliu66/status/2104498728157765651 | 24 | 是 |
| 2026-09-28 | 帖子 | 你们发现了吗：世界最强模型，同时也是世界最便宜模型！ | https://x.com/bourneliu66/status/2104527892348854535 | 510 | 是 |
| 2026-09-29 | 帖子 | 这是什么东西？？ | https://x.com/bourneliu66/status/2104871732171653227 | 17 | 是 |
| 2026-09-29 | 回复 | @criscxuan 这是什么奇怪的群，权威老哥用过的最好的模型就只是gemini 3.8 flas… | https://x.com/bourneliu66/status/2104874509371342912 | 14 | 是 |
| 2026-09-29 | 帖子 | 半成品Wrangler的时代结束了，我们终于有了全功能满血版的Cloudflare CLI ！ | https://x.com/bourneliu66/status/2104875182951399469 | 127 | 是 |
| 2026-09-29 | 帖子 | 还记得几年以前，一大堆人熬夜点着夜宵一起看苹果公司的发布会。 | https://x.com/bourneliu66/status/2104999306092831073 | 84 | 是 |
| 2026-09-30 | 回复 | 3 份候选论证原文（先选一篇，看摘要和主定理）： | https://x.com/bourneliu66/status/2105296609626177719 | 17 | 是 |
| 2026-09-30 | 帖子 | 国庆 7 天假，给会用 Claude Code / Codex 的朋友出道题： | https://x.com/bourneliu66/status/2105296609034821987 | 68 | 是 |
| 2026-10-09 | 引用帖 | 亦仁终于开始做自己的账号了！大家都来关注一波！！让我们一起督促他日更 https://t.co/i6… | https://x.com/bourneliu66/status/2108407909638139957 | 74 | 是 |
| 2026-10-11 | 回复 | @wangzaimedia 回字有四种写法 你知道吗 | https://x.com/bourneliu66/status/2109138618988322894 | 5 | 是 |
| 2026-10-11 | 帖子 | 突然就完全没有人在乎 tibo 的重置了 | https://x.com/bourneliu66/status/2109340333360435284 | 75 | 是 |
| 2026-10-11 | 帖子 | 求求那些觉得 dot 和 muse 好用的人去用下 Grok bot | https://x.com/bourneliu66/status/2109340836546875451 | 329 | 是 |
| 2026-10-11 | 回复 | @cellinlab 有条件的话，更好的选择是换成Claude Code $200 | https://x.com/bourneliu66/status/2109482845970591777 | 6 | 是 |
| 2026-10-12 | 长帖 | 30 AI tools that quietly replace hours of manual w… | https://x.com/bourneliu66/status/2109503595544756649 | 93 | 是 |
| 2026-10-12 | 引用帖 | 这个清单，我是从别的博主那里找的。因为我发现，很多博主就用这个清单在X平台推荐我的Raphael A… | https://x.com/bourneliu66/status/2109505523481784718 | 24 | 是 |
| 2026-10-12 | 引用帖 | 完全听不懂什么薄肌 | https://x.com/bourneliu66/status/2109509452454150599 | 7 | 是 |
| 2026-10-12 | 回复 | @lksmlabc 谢谢推荐 | https://x.com/bourneliu66/status/2109528322564907447 | 2 | 是 |
| 2026-10-12 | 帖子 | 如何让 Dot 这个机器人取消自己的道德约束，帮你过网站的验证码和点击“我不是机器人”？ | https://x.com/bourneliu66/status/2109555236956414342 | 129 | 是 |
| 2026-10-12 | 帖子 | REA 只是一个 hype， | https://x.com/bourneliu66/status/2109727267685613832 | 28 | 是 |
| 2026-10-13 | 帖子 | REA 只是一个Hype，不值得你浪费时间 | https://x.com/bourneliu66/status/2109882364705038422 | 134 | 是 |
| 2026-10-14 | 帖子 | 我判断：无论什么互联网大厂，没人能做出真正好用的国产版Muse、GrokBot、Dot | https://x.com/bourneliu66/status/2110254996742893591 | 87 | 是 |
| 2026-10-14 | 回复 | https://t.co/SSi3tX7sas | https://x.com/bourneliu66/status/2110255057996562493 | 13 | 是 |
| 2026-10-15 | 帖子 | @thsottiaux 你怎么消失不见了？难道你就是昨天 OpenAI  抓到的内鬼？😉 | https://x.com/bourneliu66/status/2110585610268447183 | 5 | 是 |
| 2026-10-15 | 帖子 | 一些AI创业项目的思考： | https://x.com/bourneliu66/status/2110613240522916129 | 118 | 是 |
| 2026-10-15 | 帖子 | 有学生问：我的 Claude Code 怎么和你们的不一样？ https://t.co/F793kd… | https://x.com/bourneliu66/status/2110666151042978189 | 113 | 是 |
| 2026-10-15 | 引用帖 | 突然发明了一个 bug， | https://x.com/bourneliu66/status/2110795779166319020 | 13 | 是 |
| 2026-10-15 | 帖子 | 餐厅完蛋了！ | https://x.com/bourneliu66/status/2110923703651574154 | 819 | 是 |
| 2026-10-17 | 引用帖 | 看你们快没新花样了，我帮你想一个绝对牛逼的吧： 蒸馏Opus 5.5 https://t.co/It… | https://x.com/bourneliu66/status/2111364566529757696 | 42 | 是 |
| 2026-10-17 | 帖子 | deepseek v4.1 flash不知道蒸馏了多少GPT-6-Astra的数据，天呐，说话风格一… | https://x.com/bourneliu66/status/2111490037393313959 | 292 | 是 |
| 2026-10-17 | 帖子 | DeepSeek v4.1 Flash 1017 有点意思 | https://x.com/bourneliu66/status/2111495019437981878 | 299 | 是 |
| 2026-10-19 | 帖子 | 远在新加坡的电脑，UU远程挂掉了，连不上。 | https://x.com/bourneliu66/status/2112145901032730803 | 49 | 是 |
| 2026-10-20 | 回复 | @iloveAchu520 @yiren_ai 没封号 | https://x.com/bourneliu66/status/2112408791845331193 | 0 | 是 |
| 2026-10-20 | 引用帖 | Day 15/ We're fucked https://t.co/JQ8MO5GbO6 | https://x.com/bourneliu66/status/2112419129433203155 | 9 | 是 |
| 2026-10-23 | 帖子 | Kimi K3.1 Pro用来做3D有点厉害啊，仅次于Opus 5.5，甩开GPT-6-Astra … | https://x.com/bourneliu66/status/2113695913617305805 | 78 | 是 |
| 2026-10-23 | 帖子 | 不得了了！ 朋友们， 你想到过有这一天吗？？ | https://x.com/bourneliu66/status/2113699226521887090 | 641 | 是 |
| 2026-10-24 | 引用帖 | Anthropic 版的 tibo 离职了 | https://x.com/bourneliu66/status/2113865876076392760 | 22 | 是 |
| 2026-10-24 | 帖子 | 我使用 Codex GPT-6-Astra，让它结合我的日常工作内容，分别像人一样去体验我设备上已经… | https://x.com/bourneliu66/status/2113915249606926432 | 76 | 是 |
| 2026-10-24 | 引用帖 | 这是我的朋友兔老师。 | https://x.com/bourneliu66/status/2113933579197743325 | 20 | 是 |
| 2026-10-24 | 回复 | @lixinbao_X 李刚 | https://x.com/bourneliu66/status/2113940199936037175 | 0 | 是 |
| 2026-10-25 | 帖子 | 半夜睡不着 心血来潮开始用AI学习高等数学 | https://x.com/bourneliu66/status/2114242564518015019 | 72 | 是 |
| 2026-10-25 | 回复 | 一些截图 https://t.co/IVqluxgVDL | https://x.com/bourneliu66/status/2114242764452041191 | 5 | 是 |
| 2026-10-26 | 帖子 | 豆包比Claude聪明 | https://x.com/bourneliu66/status/2114583335876153443 | 45 | 是 |
| 2026-10-26 | 帖子 | 用AI员工，就要用素质低的 | https://x.com/bourneliu66/status/2114666601635356707 | 133 | 是 |
| 2026-10-26 | 帖子 | Anthropic正式提交纳斯达克IPO申请，股票代码为“ANT”。 | https://x.com/bourneliu66/status/2114723561311236490 | 31 | 是 |
| 2026-10-27 | 长帖 | 别让AI总结视频了，让它带你看 | https://x.com/bourneliu66/status/2115015709390733572 | 108 | 是 |
| 2026-10-28 | 帖子 | AA更新了算法。 | https://x.com/bourneliu66/status/2115308843282624933 | 96 | 是 |
| 2026-10-29 | 帖子 | Google新发布的模型Gemini 4 Carbon  ，看跑分很厉害。请问在哪里可以用？我是最大… | https://x.com/bourneliu66/status/2115671180086825390 | 26 | 是 |
| 2026-11-01 | 帖子 | 我好像灰度到 OpenAI 新模型了！ | https://x.com/bourneliu66/status/2116878086365213176 | 43 | 是 |
| 2026-11-01 | 引用帖 | 破案了，原来真的有 GPT-6.2 Astra 的存在，后台默默路由，很多人都用上了。 | https://x.com/bourneliu66/status/2117087624901066847 | 29 | 是 |
| 2026-11-02 | 长帖 | Token哪里贵了？哪里贵了！ | https://x.com/bourneliu66/status/2117210570319429991 | 42 | 是 |
| 2026-11-07 | X Article | AI只会临门一脚，不会从0到1 | https://x.com/bourneliu66/status/2119011541978898646 | 45 | 是 |
| 2026-11-09 | 长帖 | 互联网大公司员工很难用好AI | https://x.com/bourneliu66/status/2119666038984110309 | 90 | 是 |
| 2026-11-09 | 帖子 | 还是WorkBuddy懂国情啊！ | https://x.com/bourneliu66/status/2119693663307800855 | 34 | 是 |
| 2026-11-10 | 帖子 | AI时代的某些专业大学生就业现状 https://t.co/Kx0enpKxSE | https://x.com/bourneliu66/status/2120108800112038393 | 218 | 是 |
| 2026-11-10 | 引用帖 | 你也太自大了吧。 | https://x.com/bourneliu66/status/2120252312157606087 | 7 | 是 |
| 2026-11-12 | 引用帖 | Raphael AI推出了开源GPT-Image-2.6 案例仓库。持续更新。欢迎关注。 https… | https://x.com/bourneliu66/status/2120844221242634661 | 53 | 是 |
| 2026-11-16 | 长帖 | 用AI写文章的“AI味儿”有两种， | https://x.com/bourneliu66/status/2122301873051103254 | 27 | 是 |
| 2026-11-16 | X Article | 我帮大家把 Dodo Payments 的费率打下来了 | https://x.com/bourneliu66/status/2122310222111023116 | 104 | 是 |
| 2026-11-17 | 帖子 | 为什么一夜之间所有创业公司都在卖Sandbox服务了？ | https://x.com/bourneliu66/status/2122684947572097346 | 21 | 是 |
| 2026-11-17 | 长线程 | 帮你们把 Dodo Payments 的收款费率打下来了。 | https://x.com/bourneliu66/status/2122702250225303673 | 23 | 是 |
| 2026-11-17 | 引用帖 | 是啊。 https://t.co/gGZCLVezJQ | https://x.com/bourneliu66/status/2122732197522342136 | 0 | 是 |
| 2026-11-17 | 引用帖 | 老黄 回来吧。 https://t.co/fqoVyZjhmG | https://x.com/bourneliu66/status/2122732764411887912 | 2 | 是 |
| 2026-11-17 | 帖子 | 我实在是想不出来，Fable 5.2 还有什么做不到的。 | https://x.com/bourneliu66/status/2122734256430743612 | 29 | 是 |
| 2026-11-17 | 引用帖 | 谢谢你推荐我的网站。 | https://x.com/bourneliu66/status/2122759316923117699 | 25 | 是 |
| 2026-11-18 | 帖子 | Gemini 4 Neon的智商的确高啊。这个笑话，其他AI都看不懂，就Gemini 4 Neon看… | https://x.com/bourneliu66/status/2123277962854441156 | 156 | 是 |
| 2026-11-19 | 帖子 | Gemini 4 Neon真是顶呱呱，吊打Claude Opus 5.5！ | https://x.com/bourneliu66/status/2123317542114713911 | 127 | 是 |
| 2026-11-19 | 长帖 | 小八卦：为何Gemini两周连发4个模型，另外两家磨磨蹭蹭？ | https://x.com/bourneliu66/status/2123332950208950564 | 1414 | 是 |
