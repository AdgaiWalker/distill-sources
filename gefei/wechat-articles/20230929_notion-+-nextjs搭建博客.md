# notion + nextjs搭建博客

- 公众号: 懒编程
- 发布时间: 2023-09-29 21:49:24
- 原文链接: https://mp.weixin.qq.com/s/kBJfQQl_YQg3i7GfN3QWWQ?nwr_flag=1
- 封面: https://mmbiz.qpic.cn/sz_mmbiz_jpg/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqOFpYLibibLNcCdtrFYmzzGjDLGWuwC5ts35VdtqQic1FAuuOnp5G16Qlw/0?wx_fmt=jpeg

---

SaaS可以通过博客来获得SEO流量，之前我自己在nextjs上，基于MarkDown + Cloudfare来构建博客，很快我就了解到更优雅的方案：notion + nextjs搭建博客，之前搭建了过，没有记录，这次刚好又要弄，打算记录一下。

notion + nextjs有很多解决方案：

  * https://github.com/tangly1024/NotionNext
  * https://github.com/transitive-bullshit/nextjs-notion-starter-kit



这里，我们基于nextjs-notion-starter-kit来搭建blog，为了方便，以kit来表示这个项目。

首先，我们找到项目中提供的notion default page：https://transitive-bs.notion.site/transitive-bs/Next-js-Notion-Starter-Kit-Template-7875426197cf461698809def95960ebf

因为项目会基于notion docs的结构进行适配，所以一般都会提供。

我们打开后，点击【Duplicate】，将这个notion page复制到自己的notion上

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqf1IlxV1rBrjADvBOYP9vLGEibMHiaoA7dasku9VvsfWnzUfdJduVgOrQ/640?wx_fmt=png)

复制后，将notion page share出来，并复制share url，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqicqemibuED9zC93u3tdiatXic2nhZDPPwJosCf2f8QOt8BQndK8dWxpugQ/640?wx_fmt=png)

获得的url如下：
    
    
    https://glowing-kip-bf2.notion.site/Next-js-Notion-Starter-Kit-Template-0f3b6xxxxxxxxxxxxxxxxxxxxxxxx91a?pvs=4  
    

将0f3b6xxxxxxxxxxxxxxxxxxxxxxxx91a复制出来，然后放到kit项目的site.config.ts中，赋值给rootNotionPageId，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqjgibaWVicmxRh8yJORbib1ZmeYuPvx5bEQfkx97Tk0cLn7RvgTvvvMGoA/640?wx_fmt=png)

然后，本地先运行一下项目，看看效果，然后就是修改配置，比如将twitter修改成自己的之类的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqGQbrt0OEZhdXyfq0Ek1ibB2Rt68ibWEQ5HTKukjLYPbkjGVkicyz5IxIA/640?wx_fmt=png)

当然，使用的过程中，你也会发现一些问题，比如图片无法访问或视频无法访问，这是因为notion升级改变了上传后，图片、视频等资源的保存规则而导致的。（我看到一个做notion to blog 这类SaaS产品的twitter 大V 在issue中狂问问题。notion的变化，影响到他SaaS正常功能了）

目前本文中提到的NotionNext、nextjs-notion-starter-kit的最新版都解决了图片问题，但今天发现，视频还是无法正常加载。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJqJtkicBdfQicV7hg7X162gNibEwprKChiaktIVIJPeowzsicEj43QWrzxS0Q/640?wx_fmt=jpeg)2b567093-8690-4455-abef-1240d6bf49b0.jpeg

其主要原因是，视频对应的url还是公网无法访问的url。

我无意深入研究notion变化带来限制的原因，也不想去细看项目代码，从代码层面找解决方案，浏览了相关项目的issue后，也没发现有人讨论。就尝试了一下曲线救国的方案，我将视频放到youtube，然后再嵌入到notion中，从而实现视频的播放，效果不错。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KkCMRahHfcrwv1KuQHzFgWEmAkwEMYJq0iamOrpotBqPpvEIyZOAviaWOXXdA7X8C6f5PqxByWTfqC1L7U9o3grg/640?wx_fmt=png)

最后就是上线，因为是nextjs开发的，所以直接vercel上线则可。

至此，一个免费的博客系统就搭建好了，你可以基于notion免费写文章，上传图片、视频等内容，帮你的SaaS获得SEO流量，而这一切是免费的，不需要花钱买图床、服务器等东西。喔~老伙计，域名还是要花钱的。
