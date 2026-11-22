# 哥飞公众号 · 全量文章归档

862 篇文章 / 14 大主题分类，纯静态站点，零依赖、无需构建。

- 首屏 `index.html` 约 157 KB（索引 gzip 内联）
- 正文按分类分片存放在 `content/`，点开文章时才按需加载（3 KB – 524 KB / 片）
- 支持离线添加到主屏幕（PWA）

## 目录结构

```
index.html              入口页
content/*.json.gz       正文分片（18 个），gzip 压缩
manifest.json           PWA 配置
icon-180.png            图标
icon-512.png            图标
.nojekyll               关闭 Jekyll 处理，避免静态资源被过滤
```

## 部署到 GitHub Pages

1. 打开本仓库 **Settings** → 左侧 **Pages**。
2. **Source** 选 `Deploy from a branch`，Branch 选 `main`、目录选 `/ (root)`，点 **Save**。
3. 等 1–2 分钟，访问 `https://<你的用户名>.github.io/gefei-archive/`。

所有资源都使用相对路径，部署在子路径下也能正常工作。

## 本地预览

```bash
python -m http.server 8000
# 打开 http://localhost:8000
```

不要用 `file://` 直接打开——浏览器对本地文件的 fetch 有限制，正文分片会加载失败。

## 更新内容

1. 重新生成入口与分片（源工程脚本 `_opt-build.js`、`_chunk-build.js`）。
2. 覆盖 `index.html` 与 `content/`。
3. 若分片内容有变，请同步修改页面里 `content/...?v=` 的版本号，避免访客读到旧缓存。

## 说明

数据整理自网络公开归档，仅供个人学习检索使用，版权归原作者所有。
