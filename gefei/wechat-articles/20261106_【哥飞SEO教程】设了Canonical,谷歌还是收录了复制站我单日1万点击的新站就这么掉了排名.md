# 【哥飞SEO教程】设了 Canonical，谷歌还是收录了复制站：我单日 1 万点击的新站就这么掉了排名

- 公众号: 哥飞
- 发布时间: 2026-11-06 00:00
- 原文链接: https://mp.weixin.qq.com/s?src=11&timestamp=1794211495&ver=7077&signature=3KqYhEVuzGbluhKHvgjH5GXRGBrFHBcgn8cE5Qb8oA-jys3i9*hcNQG7iA5ETkbMVKPEmsqPKjendEV2QB66M4BRU5BuIxvBmBBNo*eTp2IHpl5GzBfXkfFxhEYlHM61&new=1&nwr_flag=1
- 来源: curl 抓取（搜狗微信临时链接）

---

![新站刚有排名，别复制一份去挂广告](https://mmbiz.qpic.cn/sz_mmbiz_png/lv8zoLgTIicLYEcEnDZjLrpEDG2xfJjZ9tic3wVj8TD3PH5I94K38WRHqdCUGBUQSPzMnnzCuFd8EyOrgziaWhdOvm0wyg0aIzic6dPmuIianeZQ/640?wx_fmt=png&from=appmsg)

新站刚有排名，别复制一份去挂广告

大家好，我是哥飞。

哥飞社群双十一优惠活动，史上最低价格：[哥飞社群元旦开始涨价，今天开始双十一超低折扣，为期十一天，以后再也没有这样的优惠价格了](<https://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650094032&idx=1&sn=05a23f9fcd44f95201fbe3a9560d7da1&scene=21#wechat_redirect>)

今天跟大聊聊去年做的一个新网站因为急于变现而搞没了流量的故事。

新站流量刚起来，很多朋友第一个念头就是：赶紧变现。手里要是正好有一个已经通过 AdSense 审核的老站，就会想借老站的广告账号，先把广告挂上。

我自己就这么干过，结果一个刚上线、单日从谷歌拿到 1 万多次点击的新站，一个下午排名就没了。

![Google Search Console 效果表：网站 A 在 1 月 28 日拿到 10,304 次点击、37,379 次展示，之后每天只剩一百多到七百多次](https://mmbiz.qpic.cn/sz_mmbiz_png/lv8zoLgTIicJEqtCOAs3X0dgPXY2UgfnChdxrwQ2l446nTClB3TQ7kdf6IK6SbuZvvsgN1pk9XUfIToiboHs1alJicmpPv5P4WEHHJEmqaKzlA/640?wx_fmt=png&from=appmsg)Google Search Console 效果表：网站 A 在 1 月 28 日拿到 10,304 次点击、37,379 次展示，之后每天只剩一百多到七百多次

今天把这次教训完整讲一遍：我做了什么，为什么设了 Canonical 也没用，想变现该怎么做，已经做了类似操作的话，怎么检查。

## 一个新词，两个新站

2025 年除夕（1 月 28 日）早上 6 点，我醒来刷手机，发现了一个新词。

这个词是 0 点出现的，我查了一下，相关域名最早在 1 点半左右被注册，两点多又有人注册了一个。我在 6 点多注册了 2 个域名，一开始就打算同一个关键词上两个网站，做对照实验。

之后洗漱、吃早餐、配置域名、建 GitHub 仓库、收集关键词相关信息、让 Claude 写文案和 HTML、调样式、补文案、调标题、描述和 H1（TDH），到 10 点半左右，第一个网站 A 上线了。

到中午 12 点，访问量开始变多，每小时都在涨，当天就有 2600 个 UV。

A 站上线就给了外链，很快拿到了排名。同一天我还上了第二个网站 B，B 站先没给外链，当对照。

GSC 里，A 站 1 月 28 日这一天拿到了 10,304 次点击。GSC 的日期按美国太平洋时间算，这个 1 月 28 日，大致对应北京时间 28 日下午到 29 日下午，正好是 A 站流量最好的那一天。

第二天，每小时的访问量继续往上走，下午 2 点最高到了一小时 880 个访客。

![网站统计后台按小时的访客曲线：1 月 29 日下午 2 点最高 880 个访客，傍晚断崖式下跌](https://mmbiz.qpic.cn/sz_mmbiz_png/lv8zoLgTIicKCOECkATruegkr3xndgNsCyoEWAjdO1DhN17LLzmoJNDvNpzg5Q4CbNIVciaSgfMRUlN1R5LPO6sR8SIGdFRfKIbHeW32pCtTc/640?wx_fmt=png&from=appmsg)网站统计后台按小时的访客曲线：1 月 29 日下午 2 点最高 880 个访客，傍晚断崖式下跌

然后，曲线就掉下来了。

## 我做了什么

就在 1 月 29 日下午 2 点半左右，我提交了一个新版本。先交代一下，A 站的主体，是用 iframe 嵌入的另一个域名的页面。

  1. 1\. 我有一个已经通过 AdSense 审核的 C 网站，给它开了一个子域名 A.C.com，解析绑定到 A 网站的 Vercel 后台；
  2. 2\. 这样一来，A.C.com 打开的内容和 A.com 一模一样，等于我自己把自己的网站复制了一份；
  3. 3\. 我把 A.C.com 的 Canonical 设成了 A 域名，但谷歌依然收录了 A.C.com；
  4. 4\. 在网站里加了一个 /app/ 目录。假设被嵌入的 iframe 域名是 I.com，原来是 A.com 直接嵌入 I.com，现在改成 A.com 嵌入 A.C.com/app/，再由 /app/ 去嵌入 I.com，这样广告就能挂在 A.C.com 的页面上；
  5. 5\. 把 A.com 导航栏和按钮的链接都改成打开 A.C.com。



绕这么一大圈，目的只有一个：让打开 A.com 的用户，能看到 C 站账号下的广告，把流量变现。

提交完代码，我就带娃出去玩了，晚上才回来。一看，天塌了，流量没了。

仔细找原因，就是自己复制自己导致的：排名下降，曝光减少，点击也就少了。GSC 里，A 站从 1 月 30 日起，每天只剩一百多到七百多次点击。

## Canonical 为什么没拦住

很多朋友会觉得，我都设了 Canonical，告诉谷歌原站是 A 了，复制出来的那个不就不算数了吗？

我当时也是这么想的，结果谷歌还是把 A.C.com 收录了。

谷歌官方文档里，介绍怎么指定规范网址时，把 rel="canonical" 写成一个“强信号”（strong signal），意思是告诉谷歌“我希望哪个网址当规范网址”。它是一个信号，不是一条谷歌必须照办的命令。

![Google Search Central 文档：rel=](https://mmbiz.qpic.cn/sz_mmbiz_png/lv8zoLgTIicLhWklZicaOtJwDPiahGozpwRo3tbrn1Gib8PokWJyKB1ybw0h8KEEViblxic0eibYXXVrJaupp9lLswo8HyauY6libdF9Z7Bb1MnicVP8/640?wx_fmt=png&from=appmsg)Google Search Central 文档：rel="canonical" 被写成让指定网址成为规范网址的强信号

同一篇文档的最佳实践里还写着：站内链接要链到规范网址，而不是重复网址。我这次正好反着来，A 站自己的导航栏和按钮，全都链到了复制出来的 A.C.com。

Canonical 平时该怎么写，可以看我之前写的[《【哥飞SEO教程】再聊 Canonical 标签，用好有好处，用错有坏处，需要小心用》](<https://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650085707&idx=1&sn=e9b13292ce5d0a9a05c7ce0b3ba867a5&scene=21#wechat_redirect>)。那篇里也说过，更规范的做法是选定一个主域名，其他能打开同样内容的域名，都用 301 跳转到主域名。

## 排名丢了，很难再拿回来

发现问题之后，我试着给 A 站加了更多外链，但都没用。排名已经丢失了，被别的网站抢走了，你想再拿回来，就很难了。

好在除夕那天还上了 B 站。B 站一开始没给外链，没有排名和点击，第二天才加上外链。A 站排名丢了之后，B 站的排名上来了，拿到的是另一个更小的关键词，从 1 月 29 日起每天有两三千次点击。

![Google Search Console 效果表：网站 B 从 1 月 29 日起，每天两三千次点击](https://mmbiz.qpic.cn/mmbiz_png/lv8zoLgTIicIAHuicXhiaHBkYVUB4GzepFnkWiaO2zegRfB7BZ3JUibeMBGDIdPzLicAZVDnb9FsWezBMeAo2Nxy39fL7nRls1yG3uicjSSEOmxbOw/640?wx_fmt=png&from=appmsg)Google Search Console 效果表：网站 B 从 1 月 29 日起，每天两三千次点击

A 站让出来的更大机会，被另一位朋友的网站接住了，他的流量比我的 B 站更大，估计有两三倍。

一个单日 1 万多访问的网站，从上线到排名丢失，前后两天。流量来得快，去得也快。

## 新站想变现，该怎么做

我的教训就两条：

  1. 1\. 网站才刚上线，排名还不稳定，先别想着搞钱，先让网站成长起来再说；
  2. 2\. 即使要搞钱，也要直接拿这个域名去申请 AdSense，或者接入支付，别像我一样骚操作，自己复制自己。



用新站自己的域名去申请 AdSense，提交时有几个小细节，可以看[《【哥飞出海教程】Adsense 提交网站申请的小细节》](<https://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650086809&idx=1&sn=f5d2c0e79f29870a6ec615bcaed25707&scene=21#wechat_redirect>)。

## 已经这么做了，怎么检查

如果你也用别的域名、子域名把网站复制过一份，不管是为了挂广告还是别的原因，可以这样查：

  1. 1\. 在谷歌搜索 site:复制站的域名或子域名（比如 site:A.C.com），看复制出来的地址有没有被收录；
  2. 2\. 在复制站所在域名的 Google Search Console 里，用“网址检查”查复制出来的页面，对比“用户声明的规范网址”和“Google 选择的规范网址”，看谷歌最后认的是哪一个；
  3. 3\. 有被收录的，就别再让两个地址同时能打开同样的内容，把多余的地址 301 跳转回主域名。



做完这些，谷歌会慢慢把复制站的收录合并回主域名。但排名丢了不一定回得来，最好的办法还是一开始就别这么做。

新站该怎么起量、什么时候变现，也是我和社群朋友们平时经常一起讨论的事情。

如果你是第一次看我的文章，也简单介绍一下我自己。

我是哥飞，做网站和 SEO 很多年了，现在在运营“哥飞的朋友们”社群。平时我会和大家一起研究怎么挖掘需求、做网站、获取流量，再把流量变成收入。

如果你对哥飞的朋友们社群感兴趣，可以先看看社群介绍页：

https://new.web.cafe/about

如果看完之后觉得这个社群适合你，可以加哥飞微信咨询了解。

微信搜索框，输入 361079，点击查找 QQ 号，就能加哥飞微信了。

![哥飞微信](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lv8zoLgTIicLLxQxKibsK3faSd6FYyUe8VSBxhcRs2VmoEURXia6uH7ZAev3dKoYfp0eFGUzW2VzYGzznPF5GkYQ9QaCvQibibCHPMlWw2ibibboLQ/640?wx_fmt=other&from=appmsg)哥飞微信

哥飞社群双十一优惠活动，史上最低价格：[哥飞社群元旦开始涨价，今天开始双十一超低折扣，为期十一天，以后再也没有这样的优惠价格了](<https://mp.weixin.qq.com/s?__biz=MjM5OTIzMzYyMA==&mid=2650094032&idx=1&sn=05a23f9fcd44f95201fbe3a9560d7da1&scene=21#wechat_redirect>)

⬇️点击左下角阅读原文，加入哥飞社群⬇️
