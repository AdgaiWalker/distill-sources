# my favorite use case for Grok Bot is for the first and the last mile of getting work done.

- 类型：长线程
- 链接：https://x.com/poteto/status/2107510472601985336
- 时间：2026-10-07 00:37 北京时间（原文 UTC 2026-10-06T16:37:06.000Z）
- 数据：赞 1536 · 转帖 74 · 回复 118 · 引用 15 · 书签 1431 · 曝光 98572
- 是否有全文：是（note_tweet）
- 帖子 ID：2107510472601985336

## 正文

### 1. 2026-10-07 00:37 北京时间 · https://x.com/poteto/status/2107510472601985336

my favorite use case for Grok Bot is for the first and the last mile of getting work done.

the first mile is figuring out what work you should even be doing at all. that involves connecting Bot to the different apps and services you use, so that it can grab whatever context it needs - whether it's your calendar, your CRM, slack, email, or the many other connectors available. then, the first mile begins when you combine these connections, allowing you to provide context to your bot ("look at this slack channel for new features we've built and then look through our CRM to see which  customers we should nudge") instead of micromanage it.

you can automate further by setting up routines - they let your bot do something on a schedule ("check my email every morning") or as a reaction to something ("do this whenever this slack channel has a new message"). so a new lead can kick off a whole workflow that you setup for your bot, allowing you to delegate the work you would otherwise have to do to your bot!

the last mile involves actually following through and closing the loop. one example of this is building a new feature, or fixing a bug that your customers have reported. this is where Bot can hand off tasks to Cursor - our engineering focused agents that can write code in the cloud, on their own computers.

when you've gotten the hang of this, the next thing you can try is building a loop. here's a simple example that i use daily:

1. watch this slack channel for feedback about our app
2. create a ticket for this in Linear
3. create a Cursor cloud agent to triage and reproduce the issue on its own computer, using pstack
4. if the issue clearly reproduces, put up a fix and fuzz the pull request with a small swarm of agents
5. if the fuzz has no issues, ping me on Slack, and rebase and auto-merge the PR after 1 hour unless i request changes

you can also install my bot Dr Eggbot and ask it to teach you how to setup a loop like this for yourself!

https://t.co/U1shj39y3J

### 2. 2026-10-07 00:46 北京时间 · https://x.com/poteto/status/2107512785081168254

@farzeenilya grok bot is more for general knowledge work, while cursor is more specialized for doing engineering work

### 3. 2026-10-07 01:00 北京时间 · https://x.com/poteto/status/2107516481844269509

- we have verification skills and CLIs that our agents use to run and debug the app (you can create one yourself by using the skill i linked)
- usual testing stuff: good unit and integration tests, a few critical e2e ones
- grok bot desktop's CI is quite optimized and runs in about 5 minutes

https://t.co/xYQArsuVWR

### 4. 2026-10-07 01:16 北京时间 · https://x.com/poteto/status/2107520367082508620

@heyosud give it a try! pstack works best in Grok Bot and Cursor
