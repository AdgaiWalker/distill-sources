# i just automated our release and QA process!

- 类型：长帖
- 链接：https://x.com/poteto/status/2107527180263829827
- 时间：2026-10-07 01:43 北京时间（原文 UTC 2026-10-06T17:43:30.000Z）
- 数据：赞 2899 · 转帖 105 · 回复 185 · 引用 50 · 书签 2038 · 曝光 331586
- 是否有全文：是（note_tweet）
- 帖子 ID：2107527180263829827

## 正文

i just automated our release and QA process!
using Grok Bot i made two Team Bots: sandcastle, my release manager, and poteto, my engineer bot. i added them to Slack and made a new channel for managing releases.

first i tell sandcastle that i want to do a cut. it'll DM all the contributors with links to their PRs so they know what goes in the next release and can DM the bot back if they have any blockers or objections.

sandcastle then kicks off the build, watches it automatically, and starts up an automated fuzz swarm. usually this is 10+ agents running on Grok 4.7 xhigh to run the build, click around and use it like a real user (using our verification skills and feature map), some are directed while a few are "chaos monkey" clicking things randomly to see what breaks. 

whenever it finds an issue, i tell it to @ mention my engineer bot poteto, to spin up a Cursor Project to own triaging and fixing all the high pri issues. depending on the severity i may ask it to cherry pick the fix into our release branch and cut a patch release, or if it's a pre-existing issue i still fix it but include in the next release instead

that's one more tedious task that Grok Bot now handles for our team
