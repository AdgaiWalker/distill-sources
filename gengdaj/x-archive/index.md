# @gengdaJ X 归档索引

抓取时间：2026-11-22 18:12 北京时间

## 账号

- 名称：逸尘（@gengdaJ）
- 用户 ID：1897545708770840576
- 简介：🦄06年 | 渝客松发起人 | 永远在学习的法学生 / 💗付费咨询（yichen10801）：企业AI服务&AI自媒体增长 / 🚢付费社群：TradeWinds / 📮gengdajin1101@gmail.com / 🔪没素材了，去流浪地球攒一点 / 👀yichen-skill、Agent记忆系统、Ailu开发者
- 主页链接：https://x.com/gengdaJ
- 站点：https://yichen.ai
- GitHub：https://github.com/mcncarl
- 账号创建：2025-03-06 15:12 北京时间（UTC 2025-03-06T07:12:24.000Z）
- 认证：blue
- 粉丝 64147 · 关注 363 · 公开帖数 4412 · 媒体 614
- 置顶帖：https://x.com/gengdaJ/status/2100508398240288797（接口返回不存在，可能已删除或不可见）

## 抓取范围与限制

- 使用 Grok Bot 内置 `x` 只读接口：`get_users_by_username`、`get_users_posts`（每页最多 25 条）、`get_posts_by_ids`、`search_posts_all`（含 `from:gengdaJ` 按月翻页，以及 `from:gengdaJ -is:reply -is:retweet` 原创检索）。未使用浏览器，未发帖、点赞、关注或发私信。
- 资料页显示帖数为 **4412**，本次去重后取回 **590** 条，少 **3822** 条。差额主要来自：时间线与按月搜索均未翻完（回复密度高，每页 25 条）、部分早期月份检索为 0 或极少、搜索翻页偶发空页（需改用 end_time 续翻）、转帖与已删除帖。本次优先保证原创帖、X Article 与长帖尽量取全。
- 已取到的时间范围：2025-04-06 18:01 北京时间 → 2026-11-22 17:36 北京时间。
- 长帖使用 `note_tweet`/`note_post` 全文；X Article 使用 `article.plain_text` 全文。置顶帖接口返回不存在。
- 速率限制：该只读接口约 30 次/分钟、1000 次/日、每次 25 条。`get_users_posts` 的 `max_results=100` 仍只返回 25 条。同一日另有任务在用同一额度。搜索翻页的 `next_token` 有时会返回空页，需用更早的 `end_time` 才能继续。

## 计数

- 取回帖子：590（资料页 4412）
- 原创（无引用/回复/转帖）：74
- 引用帖：87
- 回复：412
- 纯转帖：17（已跳过正文归档，仅计数）
- X Article：3（3 篇有全文）
- 带 note_tweet 的长帖：76
- 作者自回复线程（已合并）：10 条（其中长线程 3 条）
- `articles/` 独立 markdown：81 篇（文章 + 长线程 + 长帖）

按年（北京时间）：2025 年 3 条，2026 年 587 条

按月（北京时间）：

| 月份 | 条数 |
| --- | ---: |
| 2025-04 | 2 |
| 2025-12 | 1 |
| 2026-01 | 25 |
| 2026-02 | 25 |
| 2026-03 | 25 |
| 2026-04 | 25 |
| 2026-05 | 25 |
| 2026-06 | 49 |
| 2026-07 | 50 |
| 2026-08 | 51 |
| 2026-09 | 79 |
| 2026-10 | 74 |
| 2026-11 | 159 |

<!-- BEGIN X TYPE TAGS -->

## 类型标签

原料全收，只打类型标签，不按类型删除（哆啦 2026-11-22 定）。
由 `tools/tag_x.py` 生成；每条一个 `post_type`，优先级：retweet > article > long > quote > self-thread > reply > original。
完整表见仓库根目录 [index/x-posts.csv](../../index/x-posts.csv)。

蒸馏时：主料是原创（original、self-thread）和长文（article、long）；
辅料是有方法或观点的回复（reply）和引用（quote），由 agy 按「有没有可执行方法」筛；
纯寒暄和转帖（retweet）不读。

- 合计：590
- `original`（独立原创）：41
- `article`（X Article）：3
- `long`（长帖）：76
- `self-thread`（自回复线程）：19
- `reply`（回复别人）：372
- `quote`（引用帖）：62
- `retweet`（转帖）：17
- 主料（original + article + long + self-thread）：139
- 辅料候选（reply + quote）：434
- 蒸馏时默认不读（retweet）：17

<!-- END X TYPE TAGS -->

## 文件

- 原始 JSON：`raw/user.json`、各 `raw/timeline_page_*.json`、`raw/search_*.json`、`raw/all_posts.json`
- 单篇：`articles/YYYY-MM-DD_slug.md`
- 合并全文：`all.md`（按时间正序，线程已合并）
- 本索引：`index.md`

## 长文 / 长线程 / 长帖

| 日期（北京时间） | 类型 | 标题 / 首行 | 链接 | 赞 | 有全文 | 文件 |
| --- | --- | --- | --- | ---: | --- | --- |
| 2026-11-22 | X Article | 告别 Codex 降智与 Claude 封号！Antigravity 桌面端从0到1保姆级教程，把每个细节讲透！ | https://x.com/gengdaJ/status/2124376935883272681 | 185 | 是 | [2026-11-22_告别-Codex-降智与-Claude-封号Antigravity-桌面端从0到.md](articles/2026-11-22_告别-Codex-降智与-Claude-封号Antigravity-桌面端从0到.md) |
| 2026-11-18 | 长帖 | 在Antigravity里面调用Gemini 4 Carbon，使用下面这个普通到极致的提示词分析了17分钟，却得到了我完全不敢想象的建议（甚至碾压Fable5… | https://x.com/gengdaJ/status/2122994499622203846 | 292 | 是 | [2026-11-18_在Antigravity里面调用Gemini-4-Carbon使用下面这个普通到.md](articles/2026-11-18_在Antigravity里面调用Gemini-4-Carbon使用下面这个普通到.md) |
| 2026-11-18 | 长线程 | 我靠，兄弟们快冲，最后的机会，免费领12个月Google Ultra 5×，爽用Gemini4，我已经成功开通两个号了！时间不等人！ | https://x.com/gengdaJ/status/2122869389238382875 | 528 | 是 | [2026-11-18_我靠兄弟们快冲最后的机会免费领12个月Google-Ultra-5爽用Gemin.md](articles/2026-11-18_我靠兄弟们快冲最后的机会免费领12个月Google-Ultra-5爽用Gemin.md) |
| 2026-11-17 | 长帖 | AIGC这一块学的慢确实不用学。。。Higgsfield推出Short Drama Studio，通过MCP连接Claude Code和Codex，制作短剧门槛… | https://x.com/gengdaJ/status/2122537008270807240 | 32 | 是 | [2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S.md](articles/2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S.md) |
| 2026-11-17 | 长帖 | AIGC这一块学的慢确实不用学。。。Higgsfield推出Short Drama Studio，通过MCP连接Claude Code和Codex，制作短剧门槛… | https://x.com/gengdaJ/status/2122536880789148062 | 0 | 是 | [2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S_2.md](articles/2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S_2.md) |
| 2026-11-17 | 长帖 | AIGC这一块学的慢确实不用学。。。Higgsfield推出Short Drama Studio，通过MCP连接Claude Code和Codex，门槛低的离谱… | https://x.com/gengdaJ/status/2122536629495853382 | 0 | 是 | [2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S_3.md](articles/2026-11-17_AIGC这一块学的慢确实不用学Higgsfield推出Short-Drama-S_3.md) |
| 2026-11-14 | 长帖 | 大厂的AI商战真是朴实无华，就是猛猛砸钱找专家，猛猛做数据标注。。。字节的Xpert，10月份有一个人领了18万。。。 | https://x.com/gengdaJ/status/2121442608845328697 | 1253 | 是 | [2026-11-14_大厂的AI商战真是朴实无华就是猛猛砸钱找专家猛猛做数据标注字节的Xpert10月.md](articles/2026-11-14_大厂的AI商战真是朴实无华就是猛猛砸钱找专家猛猛做数据标注字节的Xpert10月.md) |
| 2026-11-12 | 长帖 | 我去真的后悔没早点用上啊，@chatcutapp帮我打开了全新的剪辑思路——直接用手机版Grok bot实现了云剪辑，爽飞啊！出门在外，再也不用背电脑，一部手机… | https://x.com/gengdaJ/status/2120690544825250061 | 199 | 是 | [2026-11-12_我去真的后悔没早点用上啊chatcutapp帮我打开了全新的剪辑思路直接用手机版.md](articles/2026-11-12_我去真的后悔没早点用上啊chatcutapp帮我打开了全新的剪辑思路直接用手机版.md) |
| 2026-11-11 | 长帖 | 硬件大佬思路就是牛逼，微信自动化写入都能突破，给我吓坏了… | https://x.com/gengdaJ/status/2120491932917141711 | 112 | 是 | [2026-11-11_硬件大佬思路就是牛逼微信自动化写入都能突破给我吓坏了.md](articles/2026-11-11_硬件大佬思路就是牛逼微信自动化写入都能突破给我吓坏了.md) |
| 2026-10-31 | 长帖 | Ryuu @ryuu_restart 就是我的神！直接把他的Max账号（已过KYC）给我用了，还手把手教我怎么避免Claude封号，不查不知道，一查发现原来是W… | https://x.com/gengdaJ/status/2116397558545453168 | 601 | 是 | [2026-10-31_Ryuu-ryuu_restart-就是我的神直接把他的Max账号已过KYC给我.md](articles/2026-10-31_Ryuu-ryuu_restart-就是我的神直接把他的Max账号已过KYC给我.md) |
| 2026-10-30 | 长帖 | 有 Tibo 这波额度翻倍，我真的彻底放弃 Claude 官方订阅了。。。 | https://x.com/gengdaJ/status/2115973270692585551 | 94 | 是 | [2026-10-30_有-Tibo-这波额度翻倍我真的彻底放弃-Claude-官方订阅了.md](articles/2026-10-30_有-Tibo-这波额度翻倍我真的彻底放弃-Claude-官方订阅了.md) |
| 2026-10-28 | 长帖 | 大家千万不要用Claude Code CLI接CC Switch去修改网络相关的设置。。。我踏马天塌了。。。 | https://x.com/gengdaJ/status/2115245071159419069 | 60 | 是 | [2026-10-28_大家千万不要用Claude-Code-CLI接CC-Switch去修改网络相关的.md](articles/2026-10-28_大家千万不要用Claude-Code-CLI接CC-Switch去修改网络相关的.md) |
| 2026-10-27 | 长帖 | 所有老板和流量操盘手都来和我一起偷师！ | https://x.com/gengdaJ/status/2115025631167795550 | 88 | 是 | [2026-10-27_所有老板和流量操盘手都来和我一起偷师.md](articles/2026-10-27_所有老板和流量操盘手都来和我一起偷师.md) |
| 2026-10-27 | 长帖 | 所有中国人即将进入Personal Agent时代！灵光2.0上线，今天试用了一下，第一次体验到老外用Muse的感觉，确实很方便！ | https://x.com/gengdaJ/status/2115004998711152654 | 224 | 是 | [2026-10-27_所有中国人即将进入Personal-Agent时代灵光20上线今天试用了一下第一.md](articles/2026-10-27_所有中国人即将进入Personal-Agent时代灵光20上线今天试用了一下第一.md) |
| 2026-10-26 | 长帖 | 真诚求问：Grok Bot、Muse、Dot 相比于 Claude Code 和 Codex 强在哪里？ | https://x.com/gengdaJ/status/2114666429194883429 | 60 | 是 | [2026-10-26_真诚求问Grok-BotMuseDot-相比于-Claude-Code-和-Co.md](articles/2026-10-26_真诚求问Grok-BotMuseDot-相比于-Claude-Code-和-Co.md) |
| 2026-10-26 | 长帖 | Codex仅存的战胜Claude Code的能力：去找到、下载并使用（包括逆向）正版软件的破解版。 | https://x.com/gengdaJ/status/2114529695882526916 | 38 | 是 | [2026-10-26_Codex仅存的战胜Claude-Code的能力去找到下载并使用包括逆向正版软件.md](articles/2026-10-26_Codex仅存的战胜Claude-Code的能力去找到下载并使用包括逆向正版软件.md) |
| 2026-10-25 | 长帖 | Opus5.5确实在审美这一块太无敌了！我用Opus5.5做了一个3D游戏，纪念《卖火柴的小女孩》，全程花费0$。 | https://x.com/gengdaJ/status/2114350632215924921 | 161 | 是 | [2026-10-25_Opus55确实在审美这一块太无敌了我用Opus55做了一个3D游戏纪念卖火柴的.md](articles/2026-10-25_Opus55确实在审美这一块太无敌了我用Opus55做了一个3D游戏纪念卖火柴的.md) |
| 2026-10-23 | 长帖 | Monid太牛批了啊，各种跨境电商相关的数据接口全都有。接入到Claude Code，什么网页都不用打开，就完成调研和商业思路分析了！ | https://x.com/gengdaJ/status/2113536025058586972 | 670 | 是 | [2026-10-23_Monid太牛批了啊各种跨境电商相关的数据接口全都有接入到Claude-Code.md](articles/2026-10-23_Monid太牛批了啊各种跨境电商相关的数据接口全都有接入到Claude-Code.md) |
| 2026-10-21 | 长帖 | ？？？兄弟们，我也是好起来了，都收到律师函了。。。 | https://x.com/gengdaJ/status/2112852661309669815 | 746 | 是 | [2026-10-21_兄弟们我也是好起来了都收到律师函了.md](articles/2026-10-21_兄弟们我也是好起来了都收到律师函了.md) |
| 2026-10-21 | 长帖 | 无头剪映和剪映Skill大升级！这次我把安装包分享给大家了，一定要保存！一定要保存！大家别再老是和我说版本不适配的问题了。。。😅 | https://x.com/gengdaJ/status/2112778834378670195 | 1055 | 是 | [2026-10-21_无头剪映和剪映Skill大升级这次我把安装包分享给大家了一定要保存一定要保存大家.md](articles/2026-10-21_无头剪映和剪映Skill大升级这次我把安装包分享给大家了一定要保存一定要保存大家.md) |
| 2026-10-17 | 长帖 | 当下最优的选择，不是用《Personal Agent》，而是用Claude Code打造一套专属自己的《Personal Agent》驯化思路——我眼即Agen… | https://x.com/gengdaJ/status/2111344530490552560 | 450 | 是 | [2026-10-17_当下最优的选择不是用Personal-Agent而是用Claude-Code打造.md](articles/2026-10-17_当下最优的选择不是用Personal-Agent而是用Claude-Code打造.md) |
| 2026-10-15 | 长帖 | 这俩天和很多混沌商学院的大佬交流，很惊讶地发现这些已经走在最前沿的企业家，其实都还没意识到Claude Code的工作效率已经远远领先Codex（至少是Code… | https://x.com/gengdaJ/status/2110724232246333792 | 717 | 是 | [2026-10-15_这俩天和很多混沌商学院的大佬交流很惊讶地发现这些已经走在最前沿的企业家其实都还没.md](articles/2026-10-15_这俩天和很多混沌商学院的大佬交流很惊讶地发现这些已经走在最前沿的企业家其实都还没.md) |
| 2026-10-14 | 长帖 | 很多用AI视频模型做虚拟人物Vlog、电商广告、产品带货的朋友，如果不知道这个无限Token的信息差，可能会给自己一耳光。。。 | https://x.com/gengdaJ/status/2110181059837231614 | 25 | 是 | [2026-10-14_很多用AI视频模型做虚拟人物Vlog电商广告产品带货的朋友如果不知道这个无限To.md](articles/2026-10-14_很多用AI视频模型做虚拟人物Vlog电商广告产品带货的朋友如果不知道这个无限To.md) |
| 2026-10-13 | 长帖 | X Premium、Grok、Cursor套餐终于统一成X Subscription了！ | https://x.com/gengdaJ/status/2109822043378364475 | 49 | 是 | [2026-10-13_X-PremiumGrokCursor套餐终于统一成X-Subscription.md](articles/2026-10-13_X-PremiumGrokCursor套餐终于统一成X-Subscription.md) |
| 2026-10-13 | 长帖 | 我宣布：Codex正式被打入冷宫，Claude Code+Opus5.5是唯一的版本答案！！！ | https://x.com/gengdaJ/status/2109811358841852290 | 584 | 是 | [2026-10-13_我宣布Codex正式被打入冷宫Claude-CodeOpus55是唯一的版本答案.md](articles/2026-10-13_我宣布Codex正式被打入冷宫Claude-CodeOpus55是唯一的版本答案.md) |
| 2026-10-12 | 长帖 | Claude Code其实可以直接调用Codex的Computer Use，就可以不占用屏幕，能同时干更多事情，物尽其用！ | https://x.com/gengdaJ/status/2109456518433350113 | 312 | 是 | [2026-10-12_Claude-Code其实可以直接调用Codex的Computer-Use就可以.md](articles/2026-10-12_Claude-Code其实可以直接调用Codex的Computer-Use就可以.md) |
| 2026-10-11 | 长帖 | 我靠，我为啥不早点用Codex控制我的手机领取各个App里面的免费福利🤦‍♂️！！！简直错过了一个亿！！！ | https://x.com/gengdaJ/status/2109084566615114234 | 607 | 是 | [2026-10-11_我靠我为啥不早点用Codex控制我的手机领取各个App里面的免费福利简直错过了一.md](articles/2026-10-11_我靠我为啥不早点用Codex控制我的手机领取各个App里面的免费福利简直错过了一.md) |
| 2026-10-10 | 长帖 | 这应该是Cloudflare改版以来我看到最详细的一个教程了，太干了，太干了，我跟着实操学习了快一个小时。 | https://x.com/gengdaJ/status/2108809864822866380 | 549 | 是 | [2026-10-10_这应该是Cloudflare改版以来我看到最详细的一个教程了太干了太干了我跟着实.md](articles/2026-10-10_这应该是Cloudflare改版以来我看到最详细的一个教程了太干了太干了我跟着实.md) |
| 2026-10-09 | 长帖 | 前两天回老家，看到有小朋友玩《保卫萝卜》，玩的不亦乐乎。 | https://x.com/gengdaJ/status/2108549740971311226 | 35 | 是 | [2026-10-09_前两天回老家看到有小朋友玩保卫萝卜玩的不亦乐乎.md](articles/2026-10-09_前两天回老家看到有小朋友玩保卫萝卜玩的不亦乐乎.md) |
| 2026-10-09 | 长帖 | Monid确实是Agent界的OpenRouter，聚合了2,443个tools & APIs，几乎涵盖了你能想象到的所有功能。 | https://x.com/gengdaJ/status/2108390780809482384 | 478 | 是 | [2026-10-09_Monid确实是Agent界的OpenRouter聚合了2443个tools.md](articles/2026-10-09_Monid确实是Agent界的OpenRouter聚合了2443个tools.md) |
| 2026-10-09 | 长帖 | 爽了！这下真的是所有人都能用上Claude了，国庆闭关给大家写了这篇超级保姆级教程——注册、订阅和过KYC全都讲清楚了。 | https://x.com/gengdaJ/status/2108365241960788340 | 487 | 是 | [2026-10-09_爽了这下真的是所有人都能用上Claude了国庆闭关给大家写了这篇超级保姆级教程注.md](articles/2026-10-09_爽了这下真的是所有人都能用上Claude了国庆闭关给大家写了这篇超级保姆级教程注.md) |
| 2026-10-09 | X Article | 任何人都能复刻的Claude注册、订阅和过KYC防封号教程 | https://x.com/gengdaJ/status/2108363527971041650 | 2505 | 是 | [2026-10-09_任何人都能复刻的Claude注册订阅和过KYC防封号教程.md](articles/2026-10-09_任何人都能复刻的Claude注册订阅和过KYC防封号教程.md) |
| 2026-10-09 | 长帖 | 兄弟们，原来“卧槽”真的是X的流量密码。。。我把余温的1027篇文章喂给Teamily AI（我觉得是Muse、Dots这些Personal Agent的进阶形… | https://x.com/gengdaJ/status/2108349221334319380 | 114 | 是 | [2026-10-09_兄弟们原来卧槽真的是X的流量密码我把余温的1027篇文章喂给Teamily-AI.md](articles/2026-10-09_兄弟们原来卧槽真的是X的流量密码我把余温的1027篇文章喂给Teamily-AI.md) |
| 2026-10-06 | 长帖 | 我去！这是一个潜力很大AI视频商业闭环项目啊。当别人还在用数字人带货的时候，你已经用Higgsfield AI influencer... | https://x.com/gengdaJ/status/2107282051456258248 | 412 | 是 | [2026-10-06_我去这是一个潜力很大AI视频商业闭环项目啊当别人还在用数字人带货的时候你已经用H.md](articles/2026-10-06_我去这是一个潜力很大AI视频商业闭环项目啊当别人还在用数字人带货的时候你已经用H.md) |
| 2026-10-01 | 长帖 | Codex的这波更新，其实我在意的不是dot，而是它想成为AI时代超级入口的野心！而且第一波受益的是所有AI视频工作者——电商带货、YouTube AI视频从业… | https://x.com/gengdaJ/status/2105494159557533897 | 199 | 是 | [2026-10-01_Codex的这波更新其实我在意的不是dot而是它想成为AI时代超级入口的野心而且.md](articles/2026-10-01_Codex的这波更新其实我在意的不是dot而是它想成为AI时代超级入口的野心而且.md) |
| 2026-10-01 | 长帖 | 才发现Codex还更新了“空间”这个巨牛逼的功能，一口气直接杀死Obsidian和飞书！！！ | https://x.com/gengdaJ/status/2105472933196177754 | 417 | 是 | [2026-10-01_才发现Codex还更新了空间这个巨牛逼的功能一口气直接杀死Obsidian和飞书.md](articles/2026-10-01_才发现Codex还更新了空间这个巨牛逼的功能一口气直接杀死Obsidian和飞书.md) |
| 2026-10-01 | 长帖 | 牛逼了，TinyFish除了Search和Fetch，还可以储存你的浏览器网站登录状态，所有Agent都能复用。 | https://x.com/gengdaJ/status/2105465426134315335 | 50 | 是 | [2026-10-01_牛逼了TinyFish除了Search和Fetch还可以储存你的浏览器网站登录状.md](articles/2026-10-01_牛逼了TinyFish除了Search和Fetch还可以储存你的浏览器网站登录状.md) |
| 2026-09-28 | 长帖 | Vesta是我最好的朋友之一，也是我现实里面见过最夸张、最会社交、最会抱大腿的 06 年同龄人，也是我同级的校友。 | https://x.com/gengdaJ/status/2104460368676626479 | 84 | 是 | [2026-09-28_Vesta是我最好的朋友之一也是我现实里面见过最夸张最会社交最会抱大腿的-06.md](articles/2026-09-28_Vesta是我最好的朋友之一也是我现实里面见过最夸张最会社交最会抱大腿的-06.md) |
| 2026-09-28 | 长帖 | 特喵的，以后可以笑着走出理发店了，让GPT-image 2.5给我发型和美容建议，太夸张了！！！ | https://x.com/gengdaJ/status/2104414578239267314 | 1186 | 是 | [2026-09-28_特喵的以后可以笑着走出理发店了让GPT-image-25给我发型和美容建议太夸张.md](articles/2026-09-28_特喵的以后可以笑着走出理发店了让GPT-image-25给我发型和美容建议太夸张.md) |
| 2026-09-28 | 长帖 | 特喵的，以后可以笑着走出理发店了，让GPT-image 2.5给我发型和美容建议，太夸张了！！！ | https://x.com/gengdaJ/status/2104413979703677022 | 0 | 是 | [2026-09-28_特喵的以后可以笑着走出理发店了让GPT-image-25给我发型和美容建议太夸张_2.md](articles/2026-09-28_特喵的以后可以笑着走出理发店了让GPT-image-25给我发型和美容建议太夸张_2.md) |
| 2026-09-28 | 长帖 | 兄弟们，这几天我没有玩Muse，但是我已经把Claude玩疯了，中国护照过的，没封号！！！ | https://x.com/gengdaJ/status/2104405179827359892 | 91 | 是 | [2026-09-28_兄弟们这几天我没有玩Muse但是我已经把Claude玩疯了中国护照过的没封号.md](articles/2026-09-28_兄弟们这几天我没有玩Muse但是我已经把Claude玩疯了中国护照过的没封号.md) |
| 2026-09-28 | 长帖 | 兄弟们，这几天我没有玩Muse，但是我已经把Claude玩疯了，Mac上玩，iPhone上玩，开着UU远程玩，云端玩，本地也玩，想怎么玩怎么玩，就和打游戏一样上… | https://x.com/gengdaJ/status/2104402581376368782 | 1 | 是 | [2026-09-28_兄弟们这几天我没有玩Muse但是我已经把Claude玩疯了Mac上玩iPhone.md](articles/2026-09-28_兄弟们这几天我没有玩Muse但是我已经把Claude玩疯了Mac上玩iPhone.md) |
| 2026-09-26 | 长帖 | 过去的三个月，就和做梦一样，这绝对是我人生目前为止最浓墨重彩的一笔！ | https://x.com/gengdaJ/status/2103726169317413244 | 395 | 是 | [2026-09-26_过去的三个月就和做梦一样这绝对是我人生目前为止最浓墨重彩的一笔.md](articles/2026-09-26_过去的三个月就和做梦一样这绝对是我人生目前为止最浓墨重彩的一笔.md) |
| 2026-09-24 | 长帖 | wtf？原来中国护照就能过Claude的KYC认证，之前谁在吓唬我！！！ | https://x.com/gengdaJ/status/2103049745984037061 | 1207 | 是 | [2026-09-24_wtf原来中国护照就能过Claude的KYC认证之前谁在吓唬我.md](articles/2026-09-24_wtf原来中国护照就能过Claude的KYC认证之前谁在吓唬我.md) |
| 2026-09-24 | 长帖 | 太爽了！！！今天刚用上Claude，官方就开始发福利了！所有Claude Pro和Max用户都能免费领取云端Claude Code额度，你的电脑关闭了，CC还能… | https://x.com/gengdaJ/status/2102955817838547207 | 86 | 是 | [2026-09-24_太爽了今天刚用上Claude官方就开始发福利了所有Claude-Pro和Max用.md](articles/2026-09-24_太爽了今天刚用上Claude官方就开始发福利了所有Claude-Pro和Max用.md) |
| 2026-09-24 | 长帖 | 看到大家都在说Opus5.5多么多么牛逼，说不眼红，肯定是假的，我是喜欢用Codex，但架不住它的内容交互模式确实不讨人喜欢。。。 | https://x.com/gengdaJ/status/2102939502646108332 | 388 | 是 | [2026-09-24_看到大家都在说Opus55多么多么牛逼说不眼红肯定是假的我是喜欢用Codex但架.md](articles/2026-09-24_看到大家都在说Opus55多么多么牛逼说不眼红肯定是假的我是喜欢用Codex但架.md) |
| 2026-09-24 | 长帖 | 我越来越觉得，在AI时代，有部分医学生真的能成为世界巨星。 | https://x.com/gengdaJ/status/2102929512694796438 | 146 | 是 | [2026-09-24_我越来越觉得在AI时代有部分医学生真的能成为世界巨星.md](articles/2026-09-24_我越来越觉得在AI时代有部分医学生真的能成为世界巨星.md) |
| 2026-09-23 | 长帖 | WTF？？？GPT-6 Sol和GPT-6 Luna正式上线，简直是价格屠夫，Luna直接比DeepSeek还便宜，咱老百姓也能爽玩Codex了！ | https://x.com/gengdaJ/status/2102559119672852951 | 91 | 是 | [2026-09-23_WTFGPT-6-Sol和GPT-6-Luna正式上线简直是价格屠夫Luna直接.md](articles/2026-09-23_WTFGPT-6-Sol和GPT-6-Luna正式上线简直是价格屠夫Luna直接.md) |
| 2026-09-22 | 长帖 | 三年华为土农民用上iPhone 18 Pro Max有感： | https://x.com/gengdaJ/status/2102409589782397142 | 206 | 是 | [2026-09-22_三年华为土农民用上iPhone-18-Pro-Max有感.md](articles/2026-09-22_三年华为土农民用上iPhone-18-Pro-Max有感.md) |
| 2026-09-21 | 长帖 | 太不容易了，终于吃上细糠，把用了三年的华为换成了iPhone 18 Pro Max。 | https://x.com/gengdaJ/status/2101947356438765651 | 1627 | 是 | [2026-09-21_太不容易了终于吃上细糠把用了三年的华为换成了iPhone-18-Pro-Max.md](articles/2026-09-21_太不容易了终于吃上细糠把用了三年的华为换成了iPhone-18-Pro-Max.md) |
| 2026-09-21 | 长帖 | Codex的插件生态顶尖到没有对手。。。到现在为止还没有接入Codex的第三方工具要思考下自己到底适不适合AI时代了。。。 | https://x.com/gengdaJ/status/2101878755396591750 | 214 | 是 | [2026-09-21_Codex的插件生态顶尖到没有对手到现在为止还没有接入Codex的第三方工具要思.md](articles/2026-09-21_Codex的插件生态顶尖到没有对手到现在为止还没有接入Codex的第三方工具要思.md) |
| 2026-09-19 | 长帖 | 🔥剪映项目最新更新：11.5.0版本（剪映最新版）开源！ | https://x.com/gengdaJ/status/2101142776725557366 | 319 | 是 | [2026-09-19_剪映项目最新更新1150版本剪映最新版开源.md](articles/2026-09-19_剪映项目最新更新1150版本剪映最新版开源.md) |
| 2026-09-18 | 长帖 | 把我珍藏已久的好东西分享给家人们，剪映11.4.2开源！！！🥳🥳🥳https://t.co/CGXDq1tcIh | https://x.com/gengdaJ/status/2100748639228367257 | 3947 | 是 | [2026-09-18_把我珍藏已久的好东西分享给家人们剪映1142开源httpstcoCGXDq1tc.md](articles/2026-09-18_把我珍藏已久的好东西分享给家人们剪映1142开源httpstcoCGXDq1tc.md) |
| 2026-09-17 | 长帖 | 其实TradeWinds第一期仅两天就满人了（还是在我筛了人的情况下），还有些走后门的🤣 但是这两天还是有很多人在问我能不能加。 | https://x.com/gengdaJ/status/2100508398240288797 | 32 | 是 | [2026-09-17_其实TradeWinds第一期仅两天就满人了还是在我筛了人的情况下还有些走后门的.md](articles/2026-09-17_其实TradeWinds第一期仅两天就满人了还是在我筛了人的情况下还有些走后门的.md) |
| 2026-09-17 | 长帖 | 这些天吵着Astra太贵，Codex额度不够用的，我把五折渠道给你们挖到了！ | https://x.com/gengdaJ/status/2100391787864928494 | 162 | 是 | [2026-09-17_这些天吵着Astra太贵Codex额度不够用的我把五折渠道给你们挖到了.md](articles/2026-09-17_这些天吵着Astra太贵Codex额度不够用的我把五折渠道给你们挖到了.md) |
| 2026-09-16 | 长帖 | 兄弟们，天大的好消息啊，OpenAI又发福利了！！！ | https://x.com/gengdaJ/status/2100028044702547987 | 291 | 是 | [2026-09-16_兄弟们天大的好消息啊OpenAI又发福利了.md](articles/2026-09-16_兄弟们天大的好消息啊OpenAI又发福利了.md) |
| 2026-09-15 | 长帖 | 卧槽！Hypit太特喵变态了！ | https://x.com/gengdaJ/status/2099657261488787639 | 1063 | 是 | [2026-09-15_卧槽Hypit太特喵变态了.md](articles/2026-09-15_卧槽Hypit太特喵变态了.md) |
| 2026-09-14 | 长帖 | Codex的含金量还在上升！ | https://x.com/gengdaJ/status/2099368435222479253 | 27 | 是 | [2026-09-14_Codex的含金量还在上升.md](articles/2026-09-14_Codex的含金量还在上升.md) |
| 2026-09-14 | 长帖 | 我突然发现，AI时代，找人的逻辑要完全变了啊！猎头公司可能要被干没了。。。 | https://x.com/gengdaJ/status/2099305057451913719 | 282 | 是 | [2026-09-14_我突然发现AI时代找人的逻辑要完全变了啊猎头公司可能要被干没了.md](articles/2026-09-14_我突然发现AI时代找人的逻辑要完全变了啊猎头公司可能要被干没了.md) |
| 2026-09-12 | 长帖 | 分享我自用了一段时间的Codex的Agent.md，非常适合给Astra使用。 | https://x.com/gengdaJ/status/2098675769514041571 | 223 | 是 | [2026-09-12_分享我自用了一段时间的Codex的Agentmd非常适合给Astra使用.md](articles/2026-09-12_分享我自用了一段时间的Codex的Agentmd非常适合给Astra使用.md) |
| 2026-09-12 | 长帖 | ⚠️虐待ChatGPT的人会被封Codex号！！！直接用Computer Use操恐微信的认会被警告！！！ | https://x.com/gengdaJ/status/2098668811054387585 | 2 | 是 | [2026-09-12_虐待ChatGPT的人会被封Codex号直接用Computer-Use操恐微信的.md](articles/2026-09-12_虐待ChatGPT的人会被封Codex号直接用Computer-Use操恐微信的.md) |
| 2026-09-11 | 长帖 | 所有做出海产品的朋友一定要收藏这个宝藏工具——AIsa，等你做GTM（Go-to-market）的时候，能给你省一大笔钱！ | https://x.com/gengdaJ/status/2098252168625332263 | 308 | 是 | [2026-09-11_所有做出海产品的朋友一定要收藏这个宝藏工具AIsa等你做GTMGo-to-mar.md](articles/2026-09-11_所有做出海产品的朋友一定要收藏这个宝藏工具AIsa等你做GTMGo-to-mar.md) |
| 2026-09-10 | 长帖 | 很多假粉丝都不知道我已经把微信生态都做成了Skill。。。 | https://x.com/gengdaJ/status/2097960663616471410 | 974 | 是 | [2026-09-10_很多假粉丝都不知道我已经把微信生态都做成了Skill.md](articles/2026-09-10_很多假粉丝都不知道我已经把微信生态都做成了Skill.md) |
| 2026-09-10 | 长帖 | 终于要摆脱华为苦海，换上iphone18了🥹但是我可能等不及折叠屏iphone Duo。。。 | https://x.com/gengdaJ/status/2097848740484895102 | 6 | 是 | [2026-09-10_终于要摆脱华为苦海换上iphone18了但是我可能等不及折叠屏iphone-Du.md](articles/2026-09-10_终于要摆脱华为苦海换上iphone18了但是我可能等不及折叠屏iphone-Du.md) |
| 2026-09-10 | 长帖 | 终于要摆脱华为苦海，换上iphone18了🥹但是我可能等不及折叠屏iphone Duo。。。 | https://x.com/gengdaJ/status/2097848493922722085 | 0 | 是 | [2026-09-10_终于要摆脱华为苦海换上iphone18了但是我可能等不及折叠屏iphone-Du_2.md](articles/2026-09-10_终于要摆脱华为苦海换上iphone18了但是我可能等不及折叠屏iphone-Du_2.md) |
| 2026-09-09 | 长帖 | GPT Image2.5震撼来袭，生成速度快一倍，SOTA生图模型！质量和可掌控性都大幅上升。。。 | https://x.com/gengdaJ/status/2097696041802096779 | 36 | 是 | [2026-09-09_GPT-Image25震撼来袭生成速度快一倍SOTA生图模型质量和可掌控性都大幅.md](articles/2026-09-09_GPT-Image25震撼来袭生成速度快一倍SOTA生图模型质量和可掌控性都大幅.md) |
| 2026-08-31 | 长帖 | 你可以试试我这个把 Markdown 文档上传到 GitHub 的 skill：https://t.co/RU9A2R03XR，里面有一个子 skill 专门做… | https://x.com/gengdaJ/status/2094278640230133994 | 2 | 是 | [2026-08-31_你可以试试我这个把-Markdown-文档上传到-GitHub-的-skillh.md](articles/2026-08-31_你可以试试我这个把-Markdown-文档上传到-GitHub-的-skillh.md) |
| 2026-08-31 | 长帖 | Codex为什么能够碾压Claude Code、workbuddy等一众工具？我觉得核心原因之一就在于Codex的Computer Use功能实在太过于惊艳！ | https://x.com/gengdaJ/status/2094265319330373951 | 172 | 是 | [2026-08-31_Codex为什么能够碾压Claude-Codeworkbuddy等一众工具我觉得.md](articles/2026-08-31_Codex为什么能够碾压Claude-Codeworkbuddy等一众工具我觉得.md) |
| 2026-07-31 | X Article | Clash Verge从0~1零基础教程（界面认识） | https://x.com/gengdaJ/status/2083195661353394227 | 1305 | 是 | [2026-07-31_Clash-Verge从01零基础教程界面认识.md](articles/2026-07-31_Clash-Verge从01零基础教程界面认识.md) |
| 2026-05-31 | 长帖 | 今天去重庆waytoagi线下做了个关于Codex的分享 | https://x.com/gengdaJ/status/2061074796369358916 | 18 | 是 | [2026-05-31_今天去重庆waytoagi线下做了个关于Codex的分享.md](articles/2026-05-31_今天去重庆waytoagi线下做了个关于Codex的分享.md) |
| 2026-05-30 | 长帖 | 很多人觉得我抖音就几百粉丝教什么AI自媒体，但是我特喵想说，我就几百粉丝，但也有好几个商单找我啊。 | https://x.com/gengdaJ/status/2060722262056304845 | 319 | 是 | [2026-05-30_很多人觉得我抖音就几百粉丝教什么AI自媒体但是我特喵想说我就几百粉丝但也有好几个.md](articles/2026-05-30_很多人觉得我抖音就几百粉丝教什么AI自媒体但是我特喵想说我就几百粉丝但也有好几个.md) |
| 2026-05-30 | 长帖 | 5.这就是我的自媒体数字军团💪​ | https://x.com/gengdaJ/status/2060682538730078445 | 4 | 是 | [2026-05-30_5这就是我的自媒体数字军团.md](articles/2026-05-30_5这就是我的自媒体数字军团.md) |
| 2026-05-30 | 长帖 | 4.用Focusee录制AI自媒体视频，这个没啥技巧，就是录制好视频导出就行了，记得化妆把自己弄帅/漂亮点～ | https://x.com/gengdaJ/status/2060682536133800103 | 4 | 是 | [2026-05-30_4用Focusee录制AI自媒体视频这个没啥技巧就是录制好视频导出就行了记得化妆.md](articles/2026-05-30_4用Focusee录制AI自媒体视频这个没啥技巧就是录制好视频导出就行了记得化妆.md) |
| 2026-05-30 | 长帖 | 3.​结合上述报告分析，以及自己的写作思路，手写口播搞初稿。 | https://x.com/gengdaJ/status/2060682533508091906 | 3 | 是 | [2026-05-30_3结合上述报告分析以及自己的写作思路手写口播搞初稿.md](articles/2026-05-30_3结合上述报告分析以及自己的写作思路手写口播搞初稿.md) |
| 2026-05-30 | 长帖 | 1.我把找对标、粗剪等脏活累活全丢给了本地的 AI Agent，自己只专注核心创作。​ | https://x.com/gengdaJ/status/2060682529213125079 | 9 | 是 | [2026-05-30_1我把找对标粗剪等脏活累活全丢给了本地的-AI-Agent自己只专注核心创作.md](articles/2026-05-30_1我把找对标粗剪等脏活累活全丢给了本地的-AI-Agent自己只专注核心创作.md) |
| 2026-05-30 | 长帖 | 《如何开启你的真人出镜AI自媒体之路》 | https://x.com/gengdaJ/status/2060682526772150765 | 531 | 是 | [2026-05-30_如何开启你的真人出镜AI自媒体之路.md](articles/2026-05-30_如何开启你的真人出镜AI自媒体之路.md) |
| 2026-01-31 | 长帖 | 好家伙，我也中招了，Google AI学生认证的账号被收回了，我真的很痛苦——antigravity、gemini pro大量调用notebooklm、veo3… | https://x.com/gengdaJ/status/2017604421430218993 | 528 | 是 | [2026-01-31_好家伙我也中招了Google-AI学生认证的账号被收回了我真的很痛苦antigr.md](articles/2026-01-31_好家伙我也中招了Google-AI学生认证的账号被收回了我真的很痛苦antigr.md) |
| 2026-01-30 | 长帖 | 我白嫖用上199元/月的kimi2.5 Agent集群做了个“三角恋”AI kpop 视频😃——故事讲了kpop三个主角狗血的三角恋然后和好“一起玩”的视频。 | https://x.com/gengdaJ/status/2017251928087122351 | 4 | 是 | [2026-01-30_我白嫖用上199元月的kimi25-Agent集群做了个三角恋AI-kpop-视.md](articles/2026-01-30_我白嫖用上199元月的kimi25-Agent集群做了个三角恋AI-kpop-视.md) |
| 2026-01-30 | 长帖 | 今天我的小红书来了一位从我在其他社媒公开表达吸引过来的客户，让我高兴的不只是出单这件事，更因为是我Build in public获得正反馈而激动。 | https://x.com/gengdaJ/status/2017219649193366006 | 4 | 是 | [2026-01-30_今天我的小红书来了一位从我在其他社媒公开表达吸引过来的客户让我高兴的不只是出单这.md](articles/2026-01-30_今天我的小红书来了一位从我在其他社媒公开表达吸引过来的客户让我高兴的不只是出单这.md) |
| 2026-01-29 | 长帖 | 小白阶段，不要谈道德，先搞钱。 | https://x.com/gengdaJ/status/2016852715117392376 | 26 | 是 | [2026-01-29_小白阶段不要谈道德先搞钱.md](articles/2026-01-29_小白阶段不要谈道德先搞钱.md) |
| 2026-01-29 | 长线程 | @b_justin51767 是的 | https://x.com/gengdaJ/status/2016664641855012995 | 0 | 是 | [2026-01-29_b_justin51767-是的.md](articles/2026-01-29_b_justin51767-是的.md) |
