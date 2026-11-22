# it's easy to fall into the trap of micromanaging your agents instead of correcting the environment that shapes its behav

- 类型：长帖
- 链接：https://x.com/poteto/status/2106542593656111276
- 时间：2026-10-04 08:31 北京时间（原文 UTC 2026-10-04T00:31:06.000Z）
- 数据：赞 4440 · 转帖 213 · 回复 190 · 引用 51 · 书签 5197 · 曝光 310892
- 是否有全文：是（note_tweet）
- 帖子 ID：2106542593656111276

## 正文

it's easy to fall into the trap of micromanaging your agents instead of correcting the environment that shapes its behavior. 

pstack 0.15.9 now ships a new /correct skill: if you keep correcting agents for the same mistakes, it finds the pattern and fixes it with architecture, types, and checks.

i like to imagine that commits rapidly flowing into the codebase are like a bonsai tree rapidly growing in whatever direction it pleases. what you want to do is not to give in to the chaos, but tame it intentionally with the right constraints

0.15.9 also has improvements to:
• /architect: now includes instructions on designing agent friendly architecture
• a new /benchmark-checklist skill based on @brendangregg's benchmarking checklist

here's a prompt you can give to grok bot to start architecting a better codebase with pstack: 

/poteto-mode create a new Project agent to refactor and rearchitect my repo so that our architecture is more agent friendly. it should use both the /correct and /architect skill to look through past commits and find the most common pitfalls that agents fall into, whether its with code quality, performance, or bugs. if relevant you can also use the /recall skill to find past conversations for context. it should make a high level plan for me to review. it should also answer its own open questions by prototyping rather than defer to me. come back to me with a plan backed by real data. once i approve the plan, use either the stack or full autopilot playbook (ask me which i want) to execute
