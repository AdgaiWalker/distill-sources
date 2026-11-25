# @poteto X 归档索引（Grok Bot 相关）

抓取时间：2026-11-25 10:16 北京时间

## 账号

- 名称：lauren（@poteto）；哆啦称她「土豆姐」
- 用户 ID：2832427459
- 简介：grok @bot at @SpaceXSI. react compiler core team, prev cursor, meta, netflix
- 主页链接：https://x.com/poteto
- 站点：https://x.ai/bot/plugin/9717366
- 所在地：OC
- 账号创建：2014-09-26 09:06 北京时间（原文 UTC 2014-09-26T01:06:36.000Z）
- 认证：blue
- 粉丝 329296 · 关注 911 · 公开帖数 8230 · 媒体 545
- 置顶帖：https://x.com/poteto/status/2121673563489140863

## 抓取范围与限制

- 使用 Grok Bot 内置 `x` 只读接口：`get_users_by_username`、`search_posts_all`、`get_users_posts`、`get_posts_by_ids`。未使用浏览器，未发帖、点赞、关注或发私信。未使用 `user-X` 插件发帖权限。
- 检索策略：先 `from:poteto (grok OR grokbot OR "Grok Bot" OR "grok bot" OR GrokBot)` 全量翻页；因接口常在仍有 `next_token` 时返回空页，改用更早的 `end_time` 分段续翻（分别在约 2026-10-23、2026-09-23、2026-08-24、2026-07-26 处接上）。再搜 `from:poteto @bot` 补不含 “grok” 字样的用法帖，并翻了近期时间线以查漏。
- 长帖/长文：搜索结果里已带部分 `note_tweet` / `article.plain_text`。对看起来被 280 字截断的高价值帖，再用 `get_posts_by_ids` 补全文，补到 11 条长帖正文。视频帖（如 2500 PR 分享）只有帖面文字，没有另取视频逐字稿。
- 速率限制：该只读接口约 30 次/分钟、1000 次/日、每次最多约 25 条。本次未触日限额中断。翻页时遇到一次 HTTP 503，退避后重试成功。
- 不是全量时间线：资料页显示公开帖数约 8230，本次只收 Grok Bot / @bot / Grok 关键词及近期时间线抽样。Grok Bot 公开讨论大致从 2026-08-11 产品发布帖起；更早命中多为 Grok 模型或 Cursor，已放入 `other.md`。
- `@bot` 不含 “grok” 的回复在 2026-10 月中旬以前可能还有未翻完的页（有 `next_token`），未继续穷尽。
- 转帖正文一般为 RT 摘要，完整原文取决于 includes；未再逐条展开每一条被转帖。

已取到的相关帖时间范围：2026-08-12 01:20 北京时间 → 2026-11-25 03:54 北京时间。

## 计数

- 本次取回且去重后的 @poteto 帖：722
- 判定与 Grok Bot 相关：600
- 明显无关、写入 `other.md`：122
- 其中：原创帖 46 · 引用 64 · 引用回复 7 · 回复 231 · 转帖 247
- 带 `note_tweet` 或 X Article 全文的相关长帖/长文：38（X Article 1）
- `articles/` 独立 markdown：42 篇（长文 + 长帖 + 长线程）

按年（北京时间）：2026 年 595 条

按月（北京时间）：

| 月份 | 条数 |
| --- | ---: |
| 2026-08 | 120 |
| 2026-09 | 96 |
| 2026-10 | 307 |
| 2026-11 | 72 |

<!-- BEGIN X TYPE TAGS -->

## 类型标签

原料全收，只打类型标签，不按类型删除（哆啦 2026-11-22 定）。
由 `tools/tag_x.py` 生成；每条一个 `post_type`，优先级：retweet > article > long > quote > self-thread > reply > original。
完整表见仓库根目录 [index/x-posts.csv](../../index/x-posts.csv)。

蒸馏时：主料是原创（original、self-thread）和长文（article、long）；
辅料是有方法或观点的回复（reply）和引用（quote），由 agy 按「有没有可执行方法」筛；
纯寒暄和转帖（retweet）不读。

- 合计：722
- `original`（独立原创）：38
- `article`（X Article）：1
- `long`（长帖）：39
- `self-thread`（自回复线程）：14
- `reply`（回复别人）：286
- `quote`（引用帖）：62
- `retweet`（转帖）：282
- 主料（original + article + long + self-thread）：92
- 辅料候选（reply + quote）：348
- 蒸馏时默认不读（retweet）：282

<!-- END X TYPE TAGS -->

## 文件

- 原始 JSON：`raw/user.json`、`raw/all_posts.json`、以及各次搜索/时间线页的 `raw/*.json`
- 单篇：`articles/YYYY-MM-DD_slug.md`
- 相关帖合并全文：`all.md`（按时间正序，线程已合并）
- 明显无关：`other.md`
- 本索引：`index.md`

## 长文 / 长线程 / 长帖

| 日期（北京时间） | 类型 | 标题 / 首行 | 链接 | 赞 | 有全文 | 文件 |
| --- | --- | --- | --- | ---: | --- | --- |
| 2026-08-12 | 长线程 | Extremely excited to share that we just launched Grok Bot! Bots do work on their | https://x.com/poteto/status/2087227636590465030 | 651 | 是 | [2026-08-12_Extremely-excited-to-share-that-we-just-launched-Grok-Bot!-B.md](articles/2026-08-12_Extremely-excited-to-share-that-we-just-launched-Grok-Bot!-B.md) |
| 2026-08-14 | 长帖 | worktrees are dead. cloud agents are the future. | https://x.com/poteto/status/2087977008253071816 | 1484 | 是 | [2026-08-14_worktrees-are-dead.-cloud-agents-are-the-future.md](articles/2026-08-14_worktrees-are-dead.-cloud-agents-are-the-future.md) |
| 2026-08-20 | 长帖 | this is a huge release! i shipped 1000 PRs last month and am on track to doublin | https://x.com/poteto/status/2090141955695198633 | 1603 | 是 | [2026-08-20_this-is-a-huge-release!-i-shipped-1000-PRs-last-month-and-am.md](articles/2026-08-20_this-is-a-huge-release!-i-shipped-1000-PRs-last-month-and-am.md) |
| 2026-08-23 | 长帖 | my number 1 tip for controlling your grok @bot usage is to avoid scheduled routi | https://x.com/poteto/status/2091368467060662497 | 738 | 是 | [2026-08-23_my-number-1-tip-for-controlling-your-grok-@bot-usage-is-to-a.md](articles/2026-08-23_my-number-1-tip-for-controlling-your-grok-@bot-usage-is-to-a.md) |
| 2026-08-27 | 长帖 | really happy that Grok @Bot is by far the smoothest agent desktop and mobile app | https://x.com/poteto/status/2092714420296433935 | 1074 | 是 | [2026-08-27_really-happy-that-Grok-@Bot-is-by-far-the-smoothest-agent-de.md](articles/2026-08-27_really-happy-that-Grok-@Bot-is-by-far-the-smoothest-agent-de.md) |
| 2026-08-28 | 长线程 | i also made a new skill called "/Make Bot UI" in pstack grokbot://app/v1/plugin/ | https://x.com/poteto/status/2093023533123400135 | 177 | 是 | [2026-08-28_i-also-made-a-new-skill-called-Make-Bot-UI-in-pstack-grokbo.md](articles/2026-08-28_i-also-made-a-new-skill-called-Make-Bot-UI-in-pstack-grokbo.md) |
| 2026-08-28 | 长帖 | i tend to use my swarm for refactoring, for example i made a skill that goes thr | https://x.com/poteto/status/2093070988074508763 | 44 | 是 | [2026-08-28_i-tend-to-use-my-swarm-for-refactoring,-for-example-i-made-a.md](articles/2026-08-28_i-tend-to-use-my-swarm-for-refactoring,-for-example-i-made-a.md) |
| 2026-08-29 | 长线程 | if you're new to using pstack, don't forget to run /create-verification-skill! i | https://x.com/poteto/status/2093414407196012990 | 1227 | 是 | [2026-08-29_if-you're-new-to-using-pstack,-don't-forget-to-run-create-v.md](articles/2026-08-29_if-you're-new-to-using-pstack,-don't-forget-to-run-create-v.md) |
| 2026-08-29 | 长帖 | i made you a bot! i'm not sure if it's good yet but i think if you talk to it, g | https://x.com/poteto/status/2093544292660965749 | 224 | 是 | [2026-08-29_i-made-you-a-bot!-i'm-not-sure-if-it's-good-yet-but-i-think.md](articles/2026-08-29_i-made-you-a-bot!-i'm-not-sure-if-it's-good-yet-but-i-think.md) |
| 2026-08-30 | 长线程 | @bot Add the X plugin to Grok @Bot!  | https://x.com/poteto/status/2093828101742731578 | 185 | 是 | [2026-08-30_@bot-Add-the-X-plugin-to-Grok-@Bot!.md](articles/2026-08-30_@bot-Add-the-X-plugin-to-Grok-@Bot!.md) |
| 2026-09-07 | 长线程 | the Grok @Bot desktop app just got a whole lot faster! there's still more to imp | https://x.com/poteto/status/2096786161981366338 | 3096 | 是 | [2026-09-07_the-Grok-@Bot-desktop-app-just-got-a-whole-lot-faster!-there.md](articles/2026-09-07_the-Grok-@Bot-desktop-app-just-got-a-whole-lot-faster!-there.md) |
| 2026-09-12 | 长线程 | @Adamlags i use it to build Grok @Bot, thousands of PRs a month! | https://x.com/poteto/status/2098636331673121274 | 2 | 是 | [2026-09-12_@Adamlags-i-use-it-to-build-Grok-@Bot,-thousands-of-PRs-a-mo.md](articles/2026-09-12_@Adamlags-i-use-it-to-build-Grok-@Bot,-thousands-of-PRs-a-mo.md) |
| 2026-09-13 | 长帖 | Next week, @mattyp @roshan_s and myself will be speedrunning building a new comp | https://x.com/poteto/status/2098815981787414978 | 4396 | 是 | [2026-09-13_Next-week,-@mattyp-@roshan_s-and-myself-will-be-speedrunning.md](articles/2026-09-13_Next-week,-@mattyp-@roshan_s-and-myself-will-be-speedrunning.md) |
| 2026-09-23 | 长线程 | the Grok @Bot desktop app just got even faster! we shipped 53 perf fixes over th | https://x.com/poteto/status/2102504221648339170 | 3618 | 是 | [2026-09-23_the-Grok-@Bot-desktop-app-just-got-even-faster!-we-shipped-5.md](articles/2026-09-23_the-Grok-@Bot-desktop-app-just-got-even-faster!-we-shipped-5.md) |
| 2026-09-24 | 长帖 | we started a game studio last week with grok @bot on the grok bot galaxy livestr | https://x.com/poteto/status/2102835770784694385 | 744 | 是 | [2026-09-24_we-started-a-game-studio-last-week-with-grok-@bot-on-the-gro.md](articles/2026-09-24_we-started-a-game-studio-last-week-with-grok-@bot-on-the-gro.md) |
| 2026-09-29 | 长帖 | in case you missed it over the weekend, grok @bot can help with your finances! c | https://x.com/poteto/status/2104646114427457941 | 1540 | 是 | [2026-09-29_in-case-you-missed-it-over-the-weekend,-grok-@bot-can-help-w.md](articles/2026-09-29_in-case-you-missed-it-over-the-weekend,-grok-@bot-can-help-w.md) |
| 2026-09-29 | 长帖 | very excited to share one of my favorite new features! grok @bot is now multipla | https://x.com/poteto/status/2104664283808428165 | 1818 | 是 | [2026-09-29_very-excited-to-share-one-of-my-favorite-new-features!-grok.md](articles/2026-09-29_very-excited-to-share-one-of-my-favorite-new-features!-grok.md) |
| 2026-10-01 | 长帖 | grok @bot combined with cloud agents is a magical experience! here's my favorite | https://x.com/poteto/status/2105377066942349794 | 1469 | 是 | [2026-10-01_grok-@bot-combined-with-cloud-agents-is-a-magical-experience.md](articles/2026-10-01_grok-@bot-combined-with-cloud-agents-is-a-magical-experience.md) |
| 2026-10-04 | 长帖 | it's easy to fall into the trap of micromanaging your agents instead of correcti | https://x.com/poteto/status/2106542593656111276 | 4440 | 是 | [2026-10-04_it's-easy-to-fall-into-the-trap-of-micromanaging-your-agents.md](articles/2026-10-04_it's-easy-to-fall-into-the-trap-of-micromanaging-your-agents.md) |
| 2026-10-07 | 长线程 | my favorite use case for Grok Bot is for the first and the last mile of getting  | https://x.com/poteto/status/2107510472601985336 | 1536 | 是 | [2026-10-07_my-favorite-use-case-for-Grok-Bot-is-for-the-first-and-the-l.md](articles/2026-10-07_my-favorite-use-case-for-Grok-Bot-is-for-the-first-and-the-l.md) |
| 2026-10-07 | 长帖 | i just automated our release and QA process! | https://x.com/poteto/status/2107527180263829827 | 2899 | 是 | [2026-10-07_i-just-automated-our-release-and-QA-process!.md](articles/2026-10-07_i-just-automated-our-release-and-QA-process!.md) |
| 2026-10-07 | 长帖 | there is more to building a good product and AI assistant than just the model! o | https://x.com/poteto/status/2107607575151952062 | 1254 | 是 | [2026-10-07_there-is-more-to-building-a-good-product-and-AI-assistant-th.md](articles/2026-10-07_there-is-more-to-building-a-good-product-and-AI-assistant-th.md) |
| 2026-10-09 | 长帖 | for me i work on many different projects in parallel, so it adds up pretty easil | https://x.com/poteto/status/2108279582088671583 | 948 | 是 | [2026-10-09_for-me-i-work-on-many-different-projects-in-parallel,-so-it.md](articles/2026-10-09_for-me-i-work-on-many-different-projects-in-parallel,-so-it.md) |
| 2026-10-12 | 长帖 | haha we're on the same page, maybe just talking past each other. i talk a lot ab | https://x.com/poteto/status/2109352063302058351 | 5 | 是 | [2026-10-12_haha-we're-on-the-same-page,-maybe-just-talking-past-each-ot.md](articles/2026-10-12_haha-we're-on-the-same-page,-maybe-just-talking-past-each-ot.md) |
| 2026-10-13 | 长帖 | something that keeps bothering me is how some people see slop as something that  | https://x.com/poteto/status/2109699980248408574 | 4621 | 是 | [2026-10-13_something-that-keeps-bothering-me-is-how-some-people-see-slo.md](articles/2026-10-13_something-that-keeps-bothering-me-is-how-some-people-see-slo.md) |
| 2026-10-13 | 长帖 | i think the beauty of grok bot is that you can choose your own agent/bot topolog | https://x.com/poteto/status/2109781899610874002 | 9 | 是 | [2026-10-13_i-think-the-beauty-of-grok-bot-is-that-you-can-choose-your-o.md](articles/2026-10-13_i-think-the-beauty-of-grok-bot-is-that-you-can-choose-your-o.md) |
| 2026-10-14 | 长帖 | it won't be long before "have your bot talk to my bot" becomes common! | https://x.com/poteto/status/2110192382096679248 | 2752 | 是 | [2026-10-14_it-won't-be-long-before-have-your-bot-talk-to-my-bot-becomes.md](articles/2026-10-14_it-won't-be-long-before-have-your-bot-talk-to-my-bot-becomes.md) |
| 2026-10-15 | 长帖 | try pstack! it’s my personal set of skills for rigorous and autonomous engineeri | https://x.com/poteto/status/2110757066709356851 | 4937 | 是 | [2026-10-15_try-pstack!-it’s-my-personal-set-of-skills-for-rigorous-and.md](articles/2026-10-15_try-pstack!-it’s-my-personal-set-of-skills-for-rigorous-and.md) |
| 2026-10-17 | 长帖 | how do you trust your agents' work more? copy this post/link and give it to your | https://x.com/poteto/status/2111133080526495985 | 7011 | 是 | [2026-10-17_how-do-you-trust-your-agents'-work-more-copy-this-post-link.md](articles/2026-10-17_how-do-you-trust-your-agents'-work-more-copy-this-post-link.md) |
| 2026-10-20 | 长线程 | what did you get done with grok @bot last week? | https://x.com/poteto/status/2112246281016119780 | 2455 | 是 | [2026-10-20_what-did-you-get-done-with-grok-@bot-last-week.md](articles/2026-10-20_what-did-you-get-done-with-grok-@bot-last-week.md) |
| 2026-10-22 | 长线程 | @davis7 @bot start a new project to implement all these | https://x.com/poteto/status/2113062261791334667 | 690 | 是 | [2026-10-22_@davis7-@bot-start-a-new-project-to-implement-all-these.md](articles/2026-10-22_@davis7-@bot-start-a-new-project-to-implement-all-these.md) |
| 2026-10-23 | 长线程 | the grok bot team is shipping at a incredible pace! please keep sending us your  | https://x.com/poteto/status/2113426421075050909 | 1876 | 是 | [2026-10-23_the-grok-bot-team-is-shipping-at-a-incredible-pace!-please-k.md](articles/2026-10-23_the-grok-bot-team-is-shipping-at-a-incredible-pace!-please-k.md) |
| 2026-10-28 | 长帖 | the Grok Bot team ships quality at an incredible pace! we've invested in making  | https://x.com/poteto/status/2115133011352240581 | 2154 | 是 | [2026-10-28_the-Grok-Bot-team-ships-quality-at-an-incredible-pace!-we've.md](articles/2026-10-28_the-Grok-Bot-team-ships-quality-at-an-incredible-pace!-we've.md) |
| 2026-10-28 | 长帖 | i've gotten a lot of questions about how i manage my X account with grok bot, so | https://x.com/poteto/status/2115205951649423585 | 6924 | 是 | [2026-10-28_i've-gotten-a-lot-of-questions-about-how-i-manage-my-X-accou.md](articles/2026-10-28_i've-gotten-a-lot-of-questions-about-how-i-manage-my-X-accou.md) |
| 2026-11-01 | 长帖 | here’s a short grok bot guide on how i create high quality bots and manage my te | https://x.com/poteto/status/2116576229319233596 | 10773 | 是 | [2026-11-01_here’s-a-short-grok-bot-guide-on-how-i-create-high-quality-b.md](articles/2026-11-01_here’s-a-short-grok-bot-guide-on-how-i-create-high-quality-b.md) |
| 2026-11-05 | 长线程 | some fun slides from my upcoming talk @aiDotEngineer  | https://x.com/poteto/status/2118017093677494706 | 2830 | 是 | [2026-11-05_some-fun-slides-from-my-upcoming-talk-@aiDotEngineer.md](articles/2026-11-05_some-fun-slides-from-my-upcoming-talk-@aiDotEngineer.md) |
| 2026-11-08 | 长帖 | i asked grok bot to make a video about how the music in https://t.co/sa18sM28uD  | https://x.com/poteto/status/2119313621188849806 | 1403 | 是 | [2026-11-08_i-asked-grok-bot-to-make-a-video-about-how-the-music-in-http.md](articles/2026-11-08_i-asked-grok-bot-to-make-a-video-about-how-the-music-in-http.md) |
| 2026-11-13 | 长线程 | good morning! what are you working on with grok @bot today? | https://x.com/poteto/status/2120937105602040110 | 1463 | 是 | [2026-11-13_good-morning!-what-are-you-working-on-with-grok-@bot-today.md](articles/2026-11-13_good-morning!-what-are-you-working-on-with-grok-@bot-today.md) |
| 2026-11-13 | 长帖 | one of the best ways to get the most out of grok bot is with our many connectors | https://x.com/poteto/status/2120967515224609057 | 1309 | 是 | [2026-11-13_one-of-the-best-ways-to-get-the-most-out-of-grok-bot-is-with.md](articles/2026-11-13_one-of-the-best-ways-to-get-the-most-out-of-grok-bot-is-with.md) |
| 2026-11-16 | 长线程 | @minheo93698092 @bot @mattyp 라이브 번역해 주시고 이해하기 쉽게 설명해 주셔서 감사해요~ | https://x.com/poteto/status/2122031468918833661 | 189 | 是 | [2026-11-16_@minheo93698092-@bot-@mattyp-라이브-번역해-주시고-이해하기-쉽게-설명해-주셔서-감사해.md](articles/2026-11-16_@minheo93698092-@bot-@mattyp-라이브-번역해-주시고-이해하기-쉽게-설명해-주셔서-감사해.md) |
| 2026-11-18 | 长帖 | grok @bot is both a great teammate and also a personal assistant! the more conte | https://x.com/poteto/status/2122774297840398639 | 1757 | 是 | [2026-11-18_grok-@bot-is-both-a-great-teammate-and-also-a-personal-assis.md](articles/2026-11-18_grok-@bot-is-both-a-great-teammate-and-also-a-personal-assis.md) |
| 2026-11-19 | X Article | Automation can be surprisingly hard to get right, even for people who do it ever | https://x.com/poteto/status/2123159537016533493 | 17476 | 是 | [2026-11-19_Automation-can-be-surprisingly-hard-to-get-right,-even-for-p.md](articles/2026-11-19_Automation-can-be-surprisingly-hard-to-get-right,-even-for-p.md) |
