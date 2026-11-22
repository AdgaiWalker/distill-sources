# 来源与规模

收录日期：2026-11-22。下列大小为复制后本仓内 `du -sh` 结果（不含上游 `.git`）。

## 总览

| 仓内路径 | 本机原路径 | 上游 URL | 文件数 | 大小 |
|---|---|---|---:|---|
| `gefei/wechat-articles/` | `/workspace/gefei/articles/` | 无单独上游仓库；正文来自哥飞公众号 | 867 | 8.1M |
| `gefei/group-chat/` | `/workspace/gefei/group-chat/` | 无；会员群本地整理 | 14 | 1.7M |
| `gefei/github-seed/` | `/workspace/gefei/github_seed/` | https://github.com/mundane799699/gefei_mp_export.git （收录时 commit `105cd6bed2c65c277502b5aed7c32156ca8887eb`） | 608 | 20M |
| `gefei/ximen-notes/` | `/workspace/gefei/ximen-notes/` | 无；哆啦整理的西门笔记 | 1 | 8.0K |
| `liuxiaopai/x-archive/` | `/workspace/x-archive/bourneliu66/` | 无代码仓库；内容来自刘小排 X 账号 [@bourneliu66](https://x.com/bourneliu66) | 70 | 1.9M |
| `poteto/x-archive/` | `/workspace/x-archive/poteto/` | 无代码仓库；内容来自 [@poteto](https://x.com/poteto) 公开 X 帖（Grok Bot 相关为主） | 88 | 4.5M |
| `gefei/github-member-repos/` | `/workspace/gefei/github-refs/` | 见下表各仓 | 4488（另加各目录 `UPSTREAM.md`） | 470M |

复制完成后，本仓合计约 502M（含 README / SOURCES / `.gitignore` / 各 `UPSTREAM.md` 之前约为 502M）。

## 分类说明

### 哥飞公众号 `gefei/wechat-articles/`

867 篇 markdown 正文。无上游 git 仓库。

### 会员群 `gefei/group-chat/`

- 记录：`20261004.md`、`20261022.md`、`刘小排分工.md`
- 截图：`screenshots/` 下 11 张 png

### GitHub 会员资料种子 `gefei/github-seed/`

工作区结构：`readme.md`、`extract_wechat_url.py`、`公众号/`（39 个文件）、`哥飞/`（567 个文件）。已排除上游 `.git`。

### 西门笔记 `gefei/ximen-notes/`

1 个文件：`2026-10-27-出海经验整理.md`（3356 字节）。

### 刘小排 X 归档 `liuxiaopai/x-archive/`

- `index.md`、`all.md`
- `articles/`：46 个文件（X Article 与长帖/长线程）
- `raw/`：22 个文件（原始 JSON 等）

### 土豆姐 X 归档 `poteto/x-archive/`

- `index.md`、`all.md`（Grok Bot 相关）、`other.md`（本次取到但明显无关）
- `articles/`：42 个文件（X Article、长帖与长线程）
- `raw/`：43 个文件（账号资料、合并帖、各次搜索/时间线原始 JSON）

### 会员 GitHub 工作区 `gefei/github-member-repos/`

每个子目录都有 `UPSTREAM.md`。下表 SHA 为 2026-11-22 从本机原仓读取的当时 HEAD。

| 子目录 | 上游 origin | 当时 commit SHA | 文件数 | 大小 |
|---|---|---|---:|---|
| `32103210_gefei-seo-guide` | https://github.com/32103210/gefei-seo-guide.git | `37d64004bf980ebaaccb8dde0527856b03404eb9` | 104 | 1.4M |
| `32103210_gefei-seo-handbook` | https://github.com/32103210/gefei-seo-handbook.git | `fe354f87ed34d6865e8c38d8bb748aa5569b914d` | 43 | 604K |
| `Hubert111_gefei-archive` | https://github.com/Hubert111/gefei-archive.git | `1f9386c24ace04b728b69fe2121dd8a578d2f769` | 23 | 2.8M |
| `Jayin_gefei-seo-cookbook` | https://github.com/Jayin/gefei-seo-cookbook.git | `0d73d58141a30095b4ef72f3c4a4b71e05721cb3` | 1213 | 8.7M |
| `Maynor996_gefei-community-double11-renew-2026` | https://github.com/Maynor996/gefei-community-double11-renew-2026 | `0191a051544c77156af7d471d23ec48d230a34e1` | 5 | 52K |
| `OpenGeFei` | https://github.com/qiayue/OpenGeFei | `4b9243a6737824957b937864c9446c0ce2c3be45` | 497 | 4.1M |
| `dokibbu_gefei-450-articles` | https://github.com/dokibbu/gefei-450-articles.git | `2148dfb84c0c41193e9389747b5762daa1164cca` | 649 | 249M |
| `gangbo_gefei-make-money` | https://github.com/gangbo/gefei-make-money | `4a9859f52cfb1162997e4d96dc68f002cac2e553` | 692 | 40M |
| `hanshan0228_gefei-perspective` | https://github.com/hanshan0228/gefei-perspective.git | `bbd6f764a873a12d460c0be1d836b8d2eb7ae356` | 9 | 152K |
| `hlwhut225_gefei-knowledge-base` | https://github.com/hlwhut225/gefei-knowledge-base.git | `406c7e36206a9907c51e2d71494a14a88b5b9517` | 749 | 154M |
| `huodesheng_sitemap-monitor-ext` | https://github.com/huodesheng/sitemap-monitor-ext.git | `187ce04f00c1b1c2e5754de2fd5b9dc04185595b` | 29 | 700K |
| `ifyour_gefei-seo-skill` | https://github.com/ifyour/gefei-seo-skill.git | `3fea58a54ab3cff7ec425e8114be4d2c385ce648` | 33 | 236K |
| `tens1x_gefei-perspective-skill` | https://github.com/tens1x/gefei-perspective-skill.git | `b2a719ca9eadb3cdbac543ac4f38fe359279540b` | 21 | 276K |
| `wentao-hu_gefei-learn` | https://github.com/wentao-hu/gefei-learn.git | `8eb3566f655a22298cf8f39f85eda53ce30fcbde` | 1 | 84K |
| `yuanqingsong2024_gefei-quest` | https://github.com/yuanqingsong2024/gefei-quest.git | `bf4e128f829da4aa942ecd9db5f87b6025d63e79` | 420 | 9.2M |

上表文件数为写入 `UPSTREAM.md` 之前的工作区文件数；每个子目录另有 1 个 `UPSTREAM.md`。
