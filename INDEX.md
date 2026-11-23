# 目录与来源

每个目录装的是什么、从哪来。按人统计见 [COVERAGE.md](COVERAGE.md)，逐条原料见 `manifest.jsonl`。原文不移动、不改名、不改内容；唯一例外是封存窗口内的原文会被挡在本仓外，见 [HOLDOUT.md](HOLDOUT.md)。

## 出海

### 哥飞 `gefei`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `gefei/wechat-articles/` | 公众号正文 markdown，文件名是「日期_标题」 | 哥飞公众号（无单独上游仓库） | public |
| `gefei/group-chat/` | 会员群记录与截图 | 会员群本地整理 | member |
| `gefei/github-seed/` | 会员导出的公众号资料副本和导出脚本（检索时标为他人汇编，与原文同名会折叠） | [mundane799699/gefei_mp_export](https://github.com/mundane799699/gefei_mp_export)，收录时 commit `105cd6b` | public |
| `gefei/github-member-repos/` | 各会员整理的哥飞相关仓库（他人汇编），每个子目录有 `UPSTREAM.md` | 见下表 | public |

会员整理仓（2026-11-22 收录时的 HEAD）：

| 子目录 | 上游 | commit |
|---|---|---|
| `32103210_gefei-seo-guide` | https://github.com/32103210/gefei-seo-guide.git | `37d64004bf980ebaaccb8dde0527856b03404eb9` |
| `32103210_gefei-seo-handbook` | https://github.com/32103210/gefei-seo-handbook.git | `fe354f87ed34d6865e8c38d8bb748aa5569b914d` |
| `Hubert111_gefei-archive` | https://github.com/Hubert111/gefei-archive.git | `1f9386c24ace04b728b69fe2121dd8a578d2f769` |
| `Jayin_gefei-seo-cookbook` | https://github.com/Jayin/gefei-seo-cookbook.git | `0d73d58141a30095b4ef72f3c4a4b71e05721cb3` |
| `Maynor996_gefei-community-double11-renew-2026` | https://github.com/Maynor996/gefei-community-double11-renew-2026 | `0191a051544c77156af7d471d23ec48d230a34e1` |
| `OpenGeFei` | https://github.com/qiayue/OpenGeFei | `4b9243a6737824957b937864c9446c0ce2c3be45` |
| `dokibbu_gefei-450-articles` | https://github.com/dokibbu/gefei-450-articles.git | `2148dfb84c0c41193e9389747b5762daa1164cca` |
| `gangbo_gefei-make-money` | https://github.com/gangbo/gefei-make-money | `4a9859f52cfb1162997e4d96dc68f002cac2e553` |
| `hanshan0228_gefei-perspective` | https://github.com/hanshan0228/gefei-perspective.git | `bbd6f764a873a12d460c0be1d836b8d2eb7ae356` |
| `hlwhut225_gefei-knowledge-base` | https://github.com/hlwhut225/gefei-knowledge-base.git | `406c7e36206a9907c51e2d71494a14a88b5b9517` |
| `huodesheng_sitemap-monitor-ext` | https://github.com/huodesheng/sitemap-monitor-ext.git | `187ce04f00c1b1c2e5754de2fd5b9dc04185595b` |
| `ifyour_gefei-seo-skill` | https://github.com/ifyour/gefei-seo-skill.git | `3fea58a54ab3cff7ec425e8114be4d2c385ce648` |
| `tens1x_gefei-perspective-skill` | https://github.com/tens1x/gefei-perspective-skill.git | `b2a719ca9eadb3cdbac543ac4f38fe359279540b` |
| `wentao-hu_gefei-learn` | https://github.com/wentao-hu/gefei-learn.git | `8eb3566f655a22298cf8f39f85eda53ce30fcbde` |
| `yuanqingsong2024_gefei-quest` | https://github.com/yuanqingsong2024/gefei-quest.git | `bf4e128f829da4aa942ecd9db5f87b6025d63e79` |

### 西门 `ximen`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `gefei/ximen-notes/` | 西门出海经验笔记（历史路径，不搬） | 哆啦整理（检索时标为他人汇编） | member |

## 产品

### 刘小排 `liuxiaopai`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `liuxiaopai/x-archive/` | X 归档：`index.md`、`all.md`、`articles/`（长文与长帖）、`raw/`（原始 JSON） | [@bourneliu66](https://x.com/bourneliu66) | public |

## AI 工具

### 土豆姐 `poteto`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `poteto/x-archive/` | X 归档（Grok Bot 相关帖在 `all.md`，取到但无关的在 `other.md`） | [@poteto](https://x.com/poteto) | public |

## 自媒体

### 小晚不在 `bbkirstry`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `bbkirstry/x-archive/` | X 归档（未翻完全部公开帖）。2026-09-23 至 2026-11-23 的帖子是验证区，不在本仓 | [@bbkirstry](https://x.com/bbkirstry) | public |
| `bbkirstry/feishu-kb/` | 飞书知识库导出：根目录是 Word/Excel 原件，`md/` 是 Markdown 转换稿和工具表 CSV，`md/media/` 是插图。验证区的 9 篇不在本仓 | 小晚不在飞书知识库，2026-11-23 经哆啦批准公开 | public |

部分飞书 Word 缺 `tblGrid`，转换时补上了，以免章节目录表丢失。导出方法见 `bbkirstry/feishu-kb/README.md`。

### 逸尘 `gengdaj`

| 目录 | 内容 | 来源 | 可见性 |
|---|---|---|---|
| `gengdaj/x-archive/` | X 归档（未翻完全部公开帖） | [@gengdaJ](https://x.com/gengdaJ) | public |

## X 归档的共同结构

`index.md`（账号、抓取范围、类型统计）、`all.md`（按时间正序的合并全文）、`articles/YYYY-MM-DD_slug.md`（长文、长帖、长线程）、`raw/`（接口原始 JSON）。每条帖的类型标签在 `index/x-posts.csv`。
