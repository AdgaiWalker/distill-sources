# something that keeps bothering me is how some people see slop as something that is happening to them, like they're some 

- 类型：长帖
- 链接：https://x.com/poteto/status/2109699980248408574
- 时间：2026-10-13 01:37 北京时间（原文 UTC 2026-10-12T17:37:26.000Z）
- 数据：赞 4621 · 转帖 339 · 回复 231 · 引用 103 · 书签 2647 · 曝光 336774
- 是否有全文：是（note_tweet）
- 帖子 ID：2109699980248408574

## 正文

something that keeps bothering me is how some people see slop as something that is happening to them, like they're some kind of helpless bystander powerless to do anything about it

excuse me but you are a software engineer, you literally learned how to make sand think and make computers do your bidding?! and now you can't do anything about it? please

the 2 things you should know to cut through all the noise:

1. you need to give your agent a way to verify its own work (i just posted about this so won't rehash)
2. your codebase is memory

the 2nd is not new either, we have always had lint rules, compilers with good diagnostics and strong type systems, LSPs, etc to help us write better code. there is no difference when agents write the code instead, you just need more of them, and stronger ones.

forget rules and skills. you can add those later.

yes, your codebase is a form of memory to agents! agents love extending what already exists. so every nit and every annoyance you've ever seen, every mistake and bad pattern you observe from agents, needs to turn into a constraint, or the agents will just keep repeating those same mistakes like a virus in your code. then you keep observing and repeating this process until your codebase is locked down enough that even agents with little context can one shot a high quality PR.

an even better direction is to refactor/rewrite your code such that agent anti-patterns become categorically impossible. use type systems to your advantage, use libraries/frameworks that reduce the architectural search space, or heck, create your own framework like we did for grok bot and design high quality primitives and well thought out APIs
