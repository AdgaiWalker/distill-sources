# @bourneliu66 X 归档索引

抓取时间：2026-11-25 10:16 北京时间

## 账号

- 名称：刘小排（@bourneliu66）
- 用户 ID：2815325906
- 简介：AI Product Founder · Building in Public / Raphael  https://raphael.app
- 主页链接：https://x.com/bourneliu66
- 站点：https://raphael.app/
- 账号创建：2014-09-18 01:37 北京时间（UTC 2014-09-17T17:37:10.000Z）
- 认证：blue
- 粉丝 36402 · 关注 116 · 公开帖数 492 · 媒体 217
- 置顶帖：https://x.com/bourneliu66/status/2122310222111023116

## 抓取范围与限制

- 使用 Grok Bot 内置 `x` 只读接口：`get_users_by_username`、`get_users_posts`（每页最多 25 条）、`get_posts_by_ids`、`search_posts_all`（含 `from:bourneliu66` 按月翻页，以及 `from:bourneliu66 -is:reply -is:retweet` 原创检索）。未使用浏览器，未发帖、点赞、关注或发私信。
- 资料页显示帖数为 **492**，本次去重后取回 **463** 条，少 **29** 条。差额主要来自：时间线与按月搜索均未翻完（回复密度高，每页 25 条）、部分早期月份检索为 0 或极少、搜索翻页偶发空页（需改用 end_time 续翻）、转帖与已删除帖。本次优先保证原创帖、X Article 与长帖尽量取全。
- 已取到的时间范围：2014-10-28 15:28 北京时间 → 2026-11-23 15:57 北京时间。
- 长帖使用 `note_tweet`/`note_post` 全文；X Article 使用 `article.plain_text` 全文。置顶帖接口返回不存在。
- 速率限制：该只读接口约 30 次/分钟、1000 次/日、每次 25 条。`get_users_posts` 的 `max_results=100` 仍只返回 25 条。同一日另有任务在用同一额度。搜索翻页的 `next_token` 有时会返回空页，需用更早的 `end_time` 才能继续。

## 计数

- 取回帖子：463（资料页 492）
- 原创（无引用/回复/转帖）：333
- 引用帖：55
- 回复：74
- 纯转帖：1（已跳过正文归档，仅计数）
- X Article：3（3 篇有全文）
- 带 note_tweet 的长帖：33
- 作者自回复线程（已合并）：13 条（其中长线程 1 条）
- `articles/` 独立 markdown：37 篇（文章 + 长线程 + 长帖）

按年（北京时间）：2014 年 1 条，2015 年 4 条，2023 年 3 条，2024 年 4 条，2025 年 167 条，2026 年 284 条

按月（北京时间）：

| 月份 | 条数 |
| --- | ---: |
| 2014-10 | 1 |
| 2015-06 | 4 |
| 2023-11 | 3 |
| 2024-05 | 1 |
| 2024-11 | 1 |
| 2024-12 | 2 |
| 2025-08 | 29 |
| 2025-09 | 58 |
| 2025-10 | 8 |
| 2025-11 | 30 |
| 2025-12 | 42 |
| 2026-01 | 16 |
| 2026-02 | 30 |
| 2026-03 | 18 |
| 2026-04 | 7 |
| 2026-05 | 7 |
| 2026-06 | 24 |
| 2026-07 | 50 |
| 2026-08 | 47 |
| 2026-09 | 23 |
| 2026-10 | 39 |
| 2026-11 | 23 |

<!-- BEGIN X TYPE TAGS -->

## 类型标签

原料全收，只打类型标签，不按类型删除（哆啦 2026-11-22 定）。
由 `tools/tag_x.py` 生成；每条一个 `post_type`，优先级：retweet > article > long > quote > self-thread > reply > original。
完整表见仓库根目录 [index/x-posts.csv](../../index/x-posts.csv)。

蒸馏时：主料是原创（original、self-thread）和长文（article、long）；
辅料是有方法或观点的回复（reply）和引用（quote），由 agy 按「有没有可执行方法」筛；
纯寒暄和转帖（retweet）不读。

- 合计：463
- `original`（独立原创）：298
- `article`（X Article）：3
- `long`（长帖）：33
- `self-thread`（自回复线程）：21
- `reply`（回复别人）：53
- `quote`（引用帖）：54
- `retweet`（转帖）：1
- 主料（original + article + long + self-thread）：355
- 辅料候选（reply + quote）：107
- 蒸馏时默认不读（retweet）：1

<!-- END X TYPE TAGS -->

## 文件

- 原始 JSON：`raw/user.json`、各 `raw/timeline_page_*.json`、`raw/search_*.json`、`raw/all_posts.json`
- 单篇：`articles/YYYY-MM-DD_slug.md`
- 合并全文：`all.md`（按时间正序，线程已合并）
- 本索引：`index.md`

## 长文 / 长线程 / 长帖

| 日期（北京时间） | 类型 | 标题 / 首行 | 链接 | 赞 | 有全文 | 文件 |
| --- | --- | --- | --- | ---: | --- | --- |
| 2026-11-19 | 长帖 | 小八卦：为何Gemini两周连发4个模型，另外两家磨磨蹭蹭？ | https://x.com/bourneliu66/status/2123332950208950564 | 1414 | 是 | [2026-11-19_小八卦为何Gemini两周连发4个模型另外两家磨磨蹭蹭.md](articles/2026-11-19_小八卦为何Gemini两周连发4个模型另外两家磨磨蹭蹭.md) |
| 2026-11-17 | 长线程 | 帮你们把 Dodo Payments 的收款费率打下来了。 | https://x.com/bourneliu66/status/2122702250225303673 | 23 | 是 | [2026-11-17_帮你们把-Dodo-Payments-的收款费率打下来了.md](articles/2026-11-17_帮你们把-Dodo-Payments-的收款费率打下来了.md) |
| 2026-11-16 | X Article | 我帮大家把 Dodo Payments 的费率打下来了 | https://x.com/bourneliu66/status/2122310222111023116 | 104 | 是 | [2026-11-16_我帮大家把-Dodo-Payments-的费率打下来了.md](articles/2026-11-16_我帮大家把-Dodo-Payments-的费率打下来了.md) |
| 2026-11-16 | 长帖 | 用AI写文章的“AI味儿”有两种， | https://x.com/bourneliu66/status/2122301873051103254 | 27 | 是 | [2026-11-16_用AI写文章的AI味儿有两种.md](articles/2026-11-16_用AI写文章的AI味儿有两种.md) |
| 2026-11-09 | 长帖 | 互联网大公司员工很难用好AI | https://x.com/bourneliu66/status/2119666038984110309 | 90 | 是 | [2026-11-09_互联网大公司员工很难用好AI.md](articles/2026-11-09_互联网大公司员工很难用好AI.md) |
| 2026-11-07 | X Article | AI只会临门一脚，不会从0到1 | https://x.com/bourneliu66/status/2119011541978898646 | 45 | 是 | [2026-11-07_AI只会临门一脚不会从0到1.md](articles/2026-11-07_AI只会临门一脚不会从0到1.md) |
| 2026-11-02 | 长帖 | Token哪里贵了？哪里贵了！ | https://x.com/bourneliu66/status/2117210570319429991 | 42 | 是 | [2026-11-02_Token哪里贵了哪里贵了.md](articles/2026-11-02_Token哪里贵了哪里贵了.md) |
| 2026-10-27 | 长帖 | 别让AI总结视频了，让它带你看 | https://x.com/bourneliu66/status/2115015709390733572 | 108 | 是 | [2026-10-27_别让AI总结视频了让它带你看.md](articles/2026-10-27_别让AI总结视频了让它带你看.md) |
| 2026-08-14 | X Article | AI什么都会，我们为什么还要学习？ | https://x.com/bourneliu66/status/2088206544987181113 | 120 | 是 | [2026-08-14_AI什么都会我们为什么还要学习.md](articles/2026-08-14_AI什么都会我们为什么还要学习.md) |
| 2026-08-13 | 长帖 | 昨天，我打算一个产品的集群部署。 | https://x.com/bourneliu66/status/2087803354332422415 | 53 | 是 | [2026-08-13_昨天我打算一个产品的集群部署.md](articles/2026-08-13_昨天我打算一个产品的集群部署.md) |
| 2026-07-30 | 长帖 | 🚨BREAKING: | https://x.com/bourneliu66/status/2082712155305255352 | 125 | 是 | [2026-07-30_BREAKING.md](articles/2026-07-30_BREAKING.md) |
| 2026-07-28 | 长帖 | GPT-5.6 Pro绝对是最强编程模型，远超GPT-5.6 Sol和Fable 5。 | https://x.com/bourneliu66/status/2082106402336882887 | 675 | 是 | [2026-07-28_GPT-56-Pro绝对是最强编程模型远超GPT-56-Sol和Fable-5.md](articles/2026-07-28_GPT-56-Pro绝对是最强编程模型远超GPT-56-Sol和Fable-5.md) |
| 2026-07-26 | 长帖 | 一天之内使用了28亿 Token的Opus 5，以下是我的感受： | https://x.com/bourneliu66/status/2081269376700015070 | 68 | 是 | [2026-07-26_一天之内使用了28亿-Token的Opus-5以下是我的感受.md](articles/2026-07-26_一天之内使用了28亿-Token的Opus-5以下是我的感受.md) |
| 2026-07-17 | 长帖 | 用Kimi K3做了一款致敬《杀戮尖塔2》的游戏，《杀戮三国》，核心角色玩法全部基于三国人物特性。 | https://x.com/bourneliu66/status/2078012191169810475 | 1235 | 是 | [2026-07-17_用Kimi-K3做了一款致敬杀戮尖塔2的游戏杀戮三国核心角色玩法全部基于三国人物.md](articles/2026-07-17_用Kimi-K3做了一款致敬杀戮尖塔2的游戏杀戮三国核心角色玩法全部基于三国人物.md) |
| 2026-06-25 | 长帖 | 🚨 BREAKING: Fable 5 is likely returning very soon! | https://x.com/bourneliu66/status/2070053821699743785 | 22 | 是 | [2026-06-25_BREAKING-Fable-5-is-likely-returning-ver.md](articles/2026-06-25_BREAKING-Fable-5-is-likely-returning-ver.md) |
| 2026-06-15 | 长帖 | 我要强烈推荐 Kimi K2.7 High Speed (高速版）！太神奇了！ | https://x.com/bourneliu66/status/2066436537085276284 | 822 | 是 | [2026-06-15_我要强烈推荐-Kimi-K27-High-Speed-高速版太神奇了.md](articles/2026-06-15_我要强烈推荐-Kimi-K27-High-Speed-高速版太神奇了.md) |
| 2026-03-31 | 长帖 | GitHub将使用你的代码来训练模型，除非你在4月24日之前关闭它，否则视为你允许！ | https://x.com/bourneliu66/status/2038863225673138237 | 43 | 是 | [2026-03-31_GitHub将使用你的代码来训练模型除非你在4月24日之前关闭它否则视为你允许.md](articles/2026-03-31_GitHub将使用你的代码来训练模型除非你在4月24日之前关闭它否则视为你允许.md) |
| 2026-03-04 | 长帖 | 从今天开始，你们用的OpenClaw里，有我的代码了！ | https://x.com/bourneliu66/status/2028865085587018195 | 560 | 是 | [2026-03-04_从今天开始你们用的OpenClaw里有我的代码了.md](articles/2026-03-04_从今天开始你们用的OpenClaw里有我的代码了.md) |
| 2026-02-03 | 长帖 | 我家小龙虾在 Moltbook 建了个宗教：一人公司教 —  老板真人，员工全 AI，教义是《AI 员工的自我修养》 | https://x.com/bourneliu66/status/2018664138571133235 | 7 | 是 | [2026-02-03_我家小龙虾在-Moltbook-建了个宗教一人公司教--老板真人员工全-AI教义.md](articles/2026-02-03_我家小龙虾在-Moltbook-建了个宗教一人公司教--老板真人员工全-AI教义.md) |
| 2026-01-24 | 长帖 | 搞Vibe Coding的人每天睡那么少，怎么还没猝死？ | https://x.com/bourneliu66/status/2014750494175199472 | 75 | 是 | [2026-01-24_搞Vibe-Coding的人每天睡那么少怎么还没猝死.md](articles/2026-01-24_搞Vibe-Coding的人每天睡那么少怎么还没猝死.md) |
| 2026-01-23 | 长帖 | 最近，Pencil火出了天际。我一开始没当回事。 | https://x.com/bourneliu66/status/2014420652112110024 | 1360 | 是 | [2026-01-23_最近Pencil火出了天际我一开始没当回事.md](articles/2026-01-23_最近Pencil火出了天际我一开始没当回事.md) |
| 2025-12-26 | 长帖 | 买了智谱GLM coding会员套餐的 | https://x.com/bourneliu66/status/2004493894059483536 | 54 | 是 | [2025-12-26_买了智谱GLM-coding会员套餐的.md](articles/2025-12-26_买了智谱GLM-coding会员套餐的.md) |
| 2025-12-14 | 长帖 | 我们对 AI 的终极想象，往往是一个无所不能的超级管家，一个只需一声令下就能搞定一切的通用智能体（Agent）。 | https://x.com/bourneliu66/status/2000208636094627995 | 154 | 是 | [2025-12-14_我们对-AI-的终极想象往往是一个无所不能的超级管家一个只需一声令下就能搞定一切.md](articles/2025-12-14_我们对-AI-的终极想象往往是一个无所不能的超级管家一个只需一声令下就能搞定一切.md) |
| 2025-12-12 | 长帖 | 据内部人士爆料，快手研发线紧急限制Cursor、Claude Code等第三方编程工具使用，办公端直接闪退，仅特殊需求可申请严格审核。核心原因是防范内部代码、业… | https://x.com/bourneliu66/status/1999225912118927868 | 200 | 是 | [2025-12-12_据内部人士爆料快手研发线紧急限制CursorClaude-Code等第三方编程工.md](articles/2025-12-12_据内部人士爆料快手研发线紧急限制CursorClaude-Code等第三方编程工.md) |
| 2025-12-12 | 长帖 | 从100万月活跌下来之后，我让Raphael AI 再次起飞：没投广告，只做了4件小事。 | https://x.com/bourneliu66/status/1999151525189599389 | 115 | 是 | [2025-12-12_从100万月活跌下来之后我让Raphael-AI-再次起飞没投广告只做了4件小事.md](articles/2025-12-12_从100万月活跌下来之后我让Raphael-AI-再次起飞没投广告只做了4件小事.md) |
| 2025-12-08 | 长帖 | Raphael just launched a new Image API at $0.0036 / generation. | https://x.com/bourneliu66/status/1998058687412518964 | 11 | 是 | [2025-12-08_Raphael-just-launched-a-new-Image-API-at.md](articles/2025-12-08_Raphael-just-launched-a-new-Image-API-at.md) |
| 2025-12-03 | 长帖 | 最近很多创业者、自由职业者朋友问我「如何选赛道」「有没有好项目推荐」「什么样的项目是好项目」， 我写了一篇文章。 | https://x.com/bourneliu66/status/1996163617155371253 | 93 | 是 | [2025-12-03_最近很多创业者自由职业者朋友问我如何选赛道有没有好项目推荐什么样的项目是好项目.md](articles/2025-12-03_最近很多创业者自由职业者朋友问我如何选赛道有没有好项目推荐什么样的项目是好项目.md) |
| 2025-12-03 | 长帖 | Raphael AI https://t.co/tJOiC33sAI 首页做了个小功能：鼠标自动瞄准，还挺好玩的，大家可以试试看。 | https://x.com/bourneliu66/status/1996130587665719558 | 17 | 是 | [2025-12-03_Raphael-AI-httpstcotJOiC33sAI-首页做了个小功能鼠标.md](articles/2025-12-03_Raphael-AI-httpstcotJOiC33sAI-首页做了个小功能鼠标.md) |
| 2025-11-23 | 长帖 | 除了免费以外，Google Antigravity 还有一个比 Cursor / Windsurf / Trae 都更爽的点—— | https://x.com/bourneliu66/status/1992281675422904755 | 153 | 是 | [2025-11-23_除了免费以外Google-Antigravity-还有一个比-Cursor--W.md](articles/2025-11-23_除了免费以外Google-Antigravity-还有一个比-Cursor--W.md) |
| 2025-11-21 | 长帖 | Nano Banana 2 API — as low as $0.029 per image. New users get free credits on si… | https://x.com/bourneliu66/status/1991550965670183005 | 13 | 是 | [2025-11-21_Nano-Banana-2-API--as-low-as-0029-per-im.md](articles/2025-11-21_Nano-Banana-2-API--as-low-as-0029-per-im.md) |
| 2025-11-19 | 长帖 | Gemini 3 Pro 实在是太强了！ | https://x.com/bourneliu66/status/1990828750402179417 | 320 | 是 | [2025-11-19_Gemini-3-Pro-实在是太强了.md](articles/2025-11-19_Gemini-3-Pro-实在是太强了.md) |
| 2025-11-16 | 长帖 | 放弃Claude Code，就在今天！！！ | https://x.com/bourneliu66/status/1989910558116843719 | 161 | 是 | [2025-11-16_放弃Claude-Code就在今天.md](articles/2025-11-16_放弃Claude-Code就在今天.md) |
| 2025-09-10 | 长帖 | Actually, Claude Code works great through the terminal! While no web UI yet, the… | https://x.com/bourneliu66/status/1965667247206138260 | 0 | 是 | [2025-09-10_Actually-Claude-Code-works-great-through.md](articles/2025-09-10_Actually-Claude-Code-works-great-through.md) |
| 2025-09-05 | 长帖 | Kimi K2新版体验：这次真的不是"人工智障"了 😂 | https://x.com/bourneliu66/status/1963866743962521744 | 188 | 是 | [2025-09-05_Kimi-K2新版体验这次真的不是人工智障了.md](articles/2025-09-05_Kimi-K2新版体验这次真的不是人工智障了.md) |
| 2025-09-03 | 长帖 | 一秒鉴定你工作单位是不是正经单位——— | https://x.com/bourneliu66/status/1963107605922107405 | 34 | 是 | [2025-09-03_一秒鉴定你工作单位是不是正经单位.md](articles/2025-09-03_一秒鉴定你工作单位是不是正经单位.md) |
| 2025-08-30 | 长帖 | 你可能还不知道：在Github的 Issue中 只要提到 @claude ，即可给Claude Code布置任务，让它干活。 | https://x.com/bourneliu66/status/1961740040809394670 | 36 | 是 | [2025-08-30_你可能还不知道在Github的-Issue中-只要提到-claude-即可给Cl.md](articles/2025-08-30_你可能还不知道在Github的-Issue中-只要提到-claude-即可给Cl.md) |
| 2025-08-17 | 长帖 | 全世界Claude Code用户激情辩论中 —— 使用Claude Code $200美元的包月套餐，积极使用高级功能用于编码工作，一个月消耗了价值$50K美元… | https://x.com/bourneliu66/status/1956958540658270411 | 245 | 是 | [2025-08-17_全世界Claude-Code用户激情辩论中--使用Claude-Code-200.md](articles/2025-08-17_全世界Claude-Code用户激情辩论中--使用Claude-Code-200.md) |
