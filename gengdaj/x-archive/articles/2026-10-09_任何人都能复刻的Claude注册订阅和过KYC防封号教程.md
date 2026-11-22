# 任何人都能复刻的Claude注册、订阅和过KYC防封号教程

- 类型：X Article
- 链接：https://x.com/gengdaJ/status/2108363527971041650
- 时间：2026-10-09 09:06 北京时间（原文 UTC 2026-10-09T01:06:51.000Z）
- 数据：赞 2505 · 转帖 307 · 回复 104 · 引用 52 · 书签 4915 · 曝光 589604
- 是否有全文：是（article.plain_text）
- 帖子 ID：2108363527971041650

## 正文

Fable5.2和Opus5.5的实力不必多说，我把最新（更新于2026.11.10）的稳定使用Claude Code的方法重新更新了一下。
这篇文章，我会把我的全流程保姆级地进行讲解。涉及到很多微小细节，建议先收藏，空了再跟着一步步，谨小慎微地实操。
由于Anthropic封禁账号的多样性和随机性，这篇文章仅分享我的真实开通流程，不承诺任何防封号保证！
硬性门槛提前看：
护照（过支付和KYC）
一个本地Agent（Codex）
一台Mac（Windows设置和Mac不一样，不敢保证效果）
一台iPhone（可选，如需在手机使用Claude App）
Shadowrocket（保证电脑和手机网络分流规则一致性）
好了，话不多说，我们开始👇
一、在iPhone上注册一个全新的Gmail账号
在iPhone上下载一个Chrome浏览器，然后注册一个Gmail账号——右上角头像 → 添加账号 → 创建账号。我注册的时候没有遇到需要手机号验证的情况。
但是用电脑注册，可能就会需要手机号验证，这一步虽然大陆+86手机号也能通过验证，但是如果后续Claude需要验证手机号，我个人觉得，如果两边不都是同时用美国（或其他支持地区）手机号，会有一点影响，所以在下文我也给大家准备了在国行版iPhone开通美国eSIM手机号教程。
二、注册全新美区Apple ID，充值礼品卡购买Shadowrocket
Shadowrocket，也就是常说的小火箭，需要2.99$购买，这个主要用来配置后面的干净网络以及分流规则。
同时，需要美区Apple ID才能在App Store搜索到Shadowrocket。所以，第一步，咱们先来注册一个免费的Apple ID。
来到：https://account.apple.com/account，在这里，用中国手机号即可注册美区Apple ID。
 
然后再用这个新注册的免费美区Apple ID分别登录Mac和iPhone的App Store，购买Shadowrocket就行，但是这一步也有个麻烦，就是没有美国银行卡不能直接充，所以需要先去支付宝充个礼品卡。
支付宝【Nidiya礼品卡】，然后来到这个界面，选择第一个Apple Gift Card US，充值3$到上面美区Apple ID绑定的Google邮箱即可，然后在App Store下载Shadowrocket。
 
 
三、搭建干净的网络出口IP
因为Claude封号，大多封的就是乱蹦乱跳的垃圾IP，所以网络配置一定是整个Claude注册环节的重中之重！
两种选择：自建VPS或者IPEqual打包服务，都是美国静态独享IP，延迟都在150-190ms直连。
前者流量较多，有回国路线优化，但是经常缺货且是机房IP，而且任何网络问题，都需要自己维护。如果想要住宅IP，还得自己去套一层（经常是大的号池），两者加起来的价格和折腾层面来说，后者是优选。
后者出了问题有技术快速修复，不需要自己操心，而且是静态住宅IP（优选IP段），有回国路线优化，不需要复杂的链式配置，有1v1专属客服，只建议上Max及以上套餐（因为是独享）。
我自用的是VPS自建服务，感兴趣的可以去看这一篇，也可以把这一篇文章丢给Codex直接配置，记住改端口为443。
推荐购买两种VPS：
1、DMIT（经常缺货）：https://www.dmit.io/aff.php?aff=18784
2、搬瓦工：https://bandwagonhost.com/aff.php?aff=84928
 
IPEqual，是我之前看YouTube大佬分享的，前段时间也推给了朋友使用，也反馈说速度不错，延迟和前者差不多，如果不想麻烦地配置、就想快速使用Claude的朋友，可以直接买这个：https://www.equaldcdn.com
 
购买/搭建相关服务之后，把得到的链接导入Shadowrocket，这一步点击右上角的+，再点击导入即可，实在不会，让Codex帮忙导入也行的。然后就能得到一个稳定的出口IP了。
四、清理旧的Claude登录与转发配置
我觉得我之前被Claude封号就是关于其乱七八糟的配置没有清理，所以这次做了次大扫除——把Claude Code、CC Switch、Claude桌面端都狠狠清理了。
我用的是claude-cleanup Skill，清理时保留了Claude Code的历史会话、Skills、插件和自建配置。第三方转发配置和小火箭分流另外处理。
这一步直接交给Codex就可以，咱们非科班改代码也改不明白。。。
1、先退出Claude，把下面这段复制给Codex
退出Claude桌面应用和正在运行的Claude Code会话，Codex保持打开（可能会用到Computer Use操作CC Switch）。然后发送：
我准备使用官方Claude账号，请检查这台Mac上的Claude Code和Claude Desktop旧配置。

先获取并审查这份claude-cleanup Skill，参考它的白名单和保护范围做只读审计，暂不执行清理脚本：
https://github.com/suyuan2022/suyuan-skill/blob/423473db6b618c7e040f1a5a6879bc83e69e8b3b/claude-cleanup/SKILL.md

请先列出简短的清理方案：
1. 检查旧登录凭据、账号缓存，以及Claude缓存和日志。
2. 检查主身份文件中的userID、machineID，说明重置这些本地标识的影响和范围。
3. 检查Claude Code的第三方API地址、认证覆盖项和模型映射。如果使用CC Switch，准备切回Claude Official并关闭Claude接管。
4. 保留历史会话、Skills、插件、Hooks、自建规则、桌面端持久数据，以及飞书等其他工具依赖的配置。不要清空整个.claude或CC Switch数据库，不要卸载应用。

不要输出密码或令牌。先告诉我要处理什么、保留什么、有什么影响，等我确认后再执行。
2、执行清理操作
把这段发给Codex：
按刚才列明的清单执行。先在本机完整备份相关配置，正常退出需要退出的Claude进程，再清理已确认的旧登录、账号缓存和缓存日志，重置已确认的本地标识，移除Claude Code的旧第三方转发配置。

文件只移入废纸篓；钥匙串只删除刚才明确列出的Claude记录。保留其余数据和配置，修改后逐项核验。如果切换供应商时误清了其他设置，请从备份精确恢复。

完成后告诉我：处理结果、备份位置，以及需要重新打开哪些应用。
如果脚本要求在终端输入CONFIRM，按Codex提示自己输入。核验完成后，按提示重新打开应用即可。
我当时做了两轮处理：先清旧登录和缓存、重置部分本地ID，后来又用这个Skill把Claude桌面应用和5项桌面端数据移入废纸篓。Claude Code历史、Skills、共享CC Switch配置和一份旧身份副本保留。
上面的提示词默认保留桌面端数据和应用。如果想连桌面端也一起清理，就在Codex列清单时明确说明，安全重新再来。
五、配置Shadowrocket分流
这一步的目标很简单：电脑和手机访问Claude，都走前面准备好的同一个固定节点，最大程度减少IP的改变
分流规则直接使用Ryuu维护的上游仓库：https://github.com/ryuu-restart/agent-route。
有一套完整的分流规则、DNS规则和WebTRC规则。适配客户端：Mihomo、FlClash、Clash Verge Rev、Surge、Shadowrocket 或 sing-box。
配置好了检查是否还有泄露：
https://ippure.com 
下面三张截图用于核对Shadowrocket键位设置。你可以直接把后面的提示词交给Codex操作。
设置一下小火箭的TUN模式：设置 → 代理 → 代理类型 → None（TUN Mode）。
 
“全局路由 → 配置”负责按规则分流，这项也要打开，后续教程中，Codex会来改规则。
 
再打开「设置 → 隧道 → 包括所有网络」，Mac和iPhone都开启。这个开关会让普通应用的联网流量交给小火箭接管，再按分流规则决定走哪个节点或直连。开启后，仍需核验Claude请求是否走指定节点。
 
1、选好节点，复制提示词给Codex
先在Mac的小火箭首页选中自己的固定节点，“全局路由”选择“配置”。
 
如果以前用过Clash等其他代理工具，部分程序可能还留着旧代理地址，出现浏览器能上网、Claude Code却连不上的情况。这一步不用自己找文件，把检查要求一起交给Codex即可。
随便取一个节点名称，把下面的【节点名称】替换成小火箭里显示的名字，再发给Codex：
请帮我配置Mac上的Shadowrocket，固定使用节点【节点名称】。

检查并将“设置 → 代理 → 代理类型”设为None（TUN Mode），“全局路由”使用“配置”。

开启“设置 → 隧道 → 包括所有网络”，确认开关已生效，再核验Claude请求是否命中指定节点。

为以下4个域名添加DOMAIN-SUFFIX（域名后缀）规则，覆盖域名本身及其子域名，使用指定节点：
anthropic.com
claude.ai
claude.com
claudeusercontent.com

修改前备份配置，保留其他分流规则。Claude相关规则不使用直连备用或自动切换节点。检查当前实际加载的规则，并验证正常连接时的真实出口。

同时检查旧代理配置是否与当前Shadowrocket冲突，包括系统代理、环境变量、shell启动文件、npm、Git、Homebrew和Claude设置。

逐项判断用途，只处理失效或冲突项，保留正常使用的配置。需要修改时，先列出具体改动和影响；修改前备份，修改后核验实际使用的Claude客户端是否正常联网。不要输出密码或令牌，也不要直接套用以前Clash的代理端口或代理组名。

准备iPhone可用的相同Claude分流配置。下一步我会打开iPhone镜像，让你继续配置手机。最后说明哪些已经验证，哪些还需要操作。
2、用iPhone镜像＋Codex配置手机
在Mac打开「iPhone镜像」，按提示完成首次连接。iPhone和Mac两端要登录同一个系统Apple账户（不是App Store购买账号），开启Wi-Fi和蓝牙，手机放在Mac旁边并锁屏，开启连接。
 
Mac上看到手机画面后，在刚才的Codex对话里发送：
我已打开iPhone镜像，请使用Computer Use操作镜像窗口，完成手机上的Shadowrocket配置：

1. 先备份手机现有配置，保留其他分流规则，添加前面准备的4条Claude域名后缀规则。确认这些域名及其子域名走同一个固定节点，选择“配置”路由并连接。
2. 将“设置 → 代理 → 代理类型”设为None（TUN Mode），开启“设置 → 隧道 → 包括所有网络”，并开启“始终开启”，按当前版本识别对应入口并核验。
3. 分别核验Mac和iPhone的Claude请求是否命中指定节点，以及该节点的实际出口IP。不要只凭普通IP查询网页判断分流是否正确。

遇到密码、Face ID或系统授权，告诉我接手。不要打开微信或改动无关设置。如果无法操作镜像，或修改VPN后镜像断开，说明停在哪一步，给我最短的接手步骤；恢复后继续核验。不要把未完成的事项写成已完成。
六、修改Mac和iPhone时区
因为大陆时间和台北时间一致，且台北是可以用Claude的，所以把时区改成台北就很不错。
Mac这样修改：
系统设置 → 搜索“时区” → 改成“台北市-台湾”
关掉“自动设定时区”
 
搜索“定位服务” → 关掉“定位服务”
 
iPhone这样修改：
设置 → 搜索“日期与时间”，时区选“台北标准时间”，时区城市选“台北”
关掉“自动设定时间”
 
设置 → 搜索“系统服务”，关掉“设定时区”
 
七、注册全新的免费Claude账号
准备阶段，万事俱备，只欠东风，正式进入注册Claude阶段！
用新Gmail邮箱登录Chrome浏览器，打开claude.ai，点击“Continue with Google”。
接下来就是按照指示来做。然后到了手机号那一步，可填可不填。
 
八、绑定美国手机号
Claude要求验证手机号时，再按本节操作；没有要求的，可以直接跳到订阅章节。
关于手机号验证这一个，有些朋友遇到了，有些朋友没遇到，为了以防万一，我还是把焚决教给大家。
我选择的是RedPocket美国手机号+BeeSIM转换卡。（因为国行版iPhone不支持直接安装 RedPocket 的 eSIM，所以用了 BeeSIM 实体转换卡）
RedPocket是一年30美金，BeeSIM是19.9美金永久。（按照教程指导购买，用我的链接可以获取优惠价格）
这个是实体卡（要插入卡槽的，所以得预留一个卡槽位置），发货最快也要一两天才能到，所以建议提前购买。
1、购买RedPocket套餐
直接打开eBay的RedPocket商品页
因为RedPocket官网需要美国银行卡，eBay可以直接中国PayPal支付，且价格更便宜。
商品页链接：https://www.ebay.com/itm/136840233242
中国PayPal很好注册，这个就不在这里展开。
 
购买套餐
登录不登录都可以，不登录就游客购买，选择这个一个月2.5美元，一年30美元的套餐，下拉框这块选择eSIM Phone Kit（Most popular），然后点击“Buy it now”（截图中被下拉框挡住了）。
填写相关信息，用中国PayPal支付。
 
用ChatGPT或者Google地图找到一个美国免税州地址。
 
电话号的话填写中国手机号即可。
2、激活并开启漫游
支付成功后，需要静静等待十几分钟，然后在上述填写的邮箱中找到一封RedPocket的邮件。
打开redpocket.com/activate这个网址，输入Confirmation Code。
 
然后下方的Device MEID/IMEI，在iPhone的设置 → 通用 → 关于本机 → IMEI即可找到。
 
继续在“Roaming”界面（这个要在App内部找一下。因为我不知道为啥最近电脑登不上RedPocket官网，只能用手机，手机上和电脑上Roaming入口略有差距，大家仔细找找肯定能找到），开启Roaming，然后下拉框选“CHINA”，如果出现“It’s Enabled.”，即代表激活开启漫游成功。
 
注意：有可能下方的Roaming Balances出现余额为0的情况（我遇到过），这个时候有两种解决办法：
法一：右下角咨询客服，让它把套餐额度加回来（有人成功过）。
法二：找eBay客服说明套餐额度问题，直接退款回PayPal，过一天再来重新购买套餐。
3、导入eSIM到BeeSIM
如果上述操作一切正常，就需要开始把号码写入BeeSIM了。
首先，购买BeeSIM的卡，通过这个链接才能享受九折优惠：
https://shop.beeesim.com/register?ref=7QLE2MXR
 
然后收到的信封上面有一个二维码，用微信扫描二维码就能跳转到BeeSIM小程序，或者直接微信搜索BeeSIM也能找到小程序。
然后开启蓝牙、连接BeeSIM。
 
导入eSIM的时候，需要去从邮箱里面找到RedPocket发过来的带美国手机号和二维码的这封邮件。
用BeeSIM的扫描二维码即可录入相关信息，绑定即可。其余操作看图指示。
 
到这一步，美国手机号应该就能收发短信和接打电话了。
这个RedPocket美国手机号除了绑定Claude，也有普遍的海外手机号绑定用途，囤着不亏的。这应该是我估算了七八家之后选定的最终方案，性价比拉满。
九、订阅Pro和Max
点击“Upgrade Plan”（哦对了，Claude没有中文界面，所以英文得好好学啊）。
 
先升级Pro，要不然直接升级Max，很容易封号（特别是20×）。
Full name随便填一个英文名。
Country or region选择United States。
Address需要在ChatGPT或者谷歌地图随便找一个免税州地址（就用前面那一个就行）。
Use a different name on invoices不填。
支付，我用的是StarryBlu，一张新加坡卡，成功通过了Claude订阅。
关于如何开卡，大家可以看我这个教程： 
 
有一点点门槛：护照；港卡（如果用国内银行卡需要支付不低的手续费）9.9$买张卡，才能使用，买了之后在问卷填写ID，我帮你加速审核：
https://bcn5ot9wwnew.feishu.cn/wiki/RpkuwzpHMiCoHak2gMjcuJeInFd?from=from_copylink
等Pro用满第一个五小时之后，我就直接升级了Max5×，从注册账号到开通Max总共一天不到。但是升级20×应该也没啥问题，只要每周的周限额不要打满（留个10%-20%，封号概率就会降低不少）。
【踩坑补充】：一定要20-100-200这样子慢慢升级，要不然直接充值200很容易被封。
Apple Store内购没问题，可以支付宝礼品卡购买，然后充值Claude——这里注意新的Apple Store账号需要申请购买，一般要等两天才能开通购买权限。Apple Store的好处就是谈KYC概率会变小，但是有苹果税，100变成125，200变成250，大家可以自行决定。
十、中国护照过KYC认证
我升级Max5×的时候遇到了一个问题——KYC认证。
当时可给我急坏了，刚充的Pro就用不了了？？？
所以，我直接谷歌搜索了一波，找到别人的通过方法——直接使用中国护照。

原理就是进行KYC认证的公司是Persona，这家公司的政策里面是允许中国护照的。
因为本来就有很多在美国工作的人和留学生，Anthropic也不可能一刀切中国人。
封号更重要的原因，可能还是在前面的出口IP和各种环境的设置。
我当时参考的说明如下（参考资料截图）：
 
过了KYC认证之后，我领了前段时间Claude官方赠送的250$云Claude Code额度，没出现什么问题。
我手机上也随时在用Claude App，也没有出现什么问题。
但是我没用过Claude Code CLI，所以不确定这个是否对账号有影响。。。（大家谨慎测试）
到这里，本篇教程就结束啦，大家快去尽情畅玩Claude Opus5.5吧，不管是写代码、对话、设计都是顶级，据说Fable5.5也不远了，早拥有，早享受！！！
我是逸尘，咱们下期见！

参考资料：
余温Claude防封号教程：
https://x.com/gkxspace/status/2101993381303820704?s=20

中国护照过KYC教程：
https://github.com/alchaincyf/zhangxuefeng-skill/issues/63
