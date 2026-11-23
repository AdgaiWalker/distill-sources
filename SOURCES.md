# 来源与规模

本仓现已公开。收录范围包括公开文章、已公开的 GitHub 资料，以及经仓主决定一并公开的会员群转录/截图和西门笔记。

收录日期：2026-11-22。2026-11-23 增补小晚不在飞书知识库与认知模型（经哆啦批准公开）。下列大小为复制后本仓内 `du -sh` 结果（不含上游 `.git`）。同日按哆啦规则：X 原料全收，只打类型标签（见 `scripts/tag_x.py` 与 [index/x-posts.csv](index/x-posts.csv)）；蒸馏时主料是原创和长文，辅料是有方法/观点的回复和引用，纯寒暄和转帖不读。

## 总览

| 仓内路径 | 本机原路径 | 上游 URL | 文件数 | 大小 |
|---|---|---|---:|---|
| `gefei/wechat-articles/` | `/workspace/gefei/articles/` | 无单独上游仓库；正文来自哥飞公众号 | 883 | 8.3M |
| `gefei/group-chat/` | `/workspace/gefei/group-chat/` | 无；会员群本地整理 | 14 | 1.7M |
| `gefei/github-seed/` | `/workspace/gefei/github_seed/` | https://github.com/mundane799699/gefei_mp_export.git （收录时 commit `105cd6bed2c65c277502b5aed7c32156ca8887eb`） | 608 | 20M |
| `gefei/ximen-notes/` | `/workspace/gefei/ximen-notes/` | 无；哆啦整理的西门笔记 | 1 | 8.0K |
| `liuxiaopai/x-archive/` | `/workspace/x-archive/bourneliu66/` | 无代码仓库；内容来自刘小排 X 账号 [@bourneliu66](https://x.com/bourneliu66) | 70 | 1.9M |
| `poteto/x-archive/` | `/workspace/x-archive/poteto/` | 无代码仓库；内容来自 [@poteto](https://x.com/poteto) 公开 X 帖（Grok Bot 相关为主） | 88 | 4.5M |
| `bbkirstry/x-archive/` | `/workspace/x-archive/bbkirstry/` | 无代码仓库；内容来自 [@bbkirstry](https://x.com/bbkirstry) 公开 X 帖 | 95 | 4.9M |
| `bbkirstry/feishu-kb/` | `/workspace/私有原料/小晚知识库/` | 飞书知识库 https://scn05304jwti.feishu.cn/wiki/ILFPwo7mBij3loks3AwcWCSYnCr ；2026-11-23 经哆啦批准公开 | 288 | 13M |
| `bbkirstry/cognitive-model/` | `/workspace/私有原料/小晚认知模型/` | 无单独上游仓库；AGE-13 工作原料。2026-11-23 经哆啦批准公开 | 40 | 15M |
| `gengdaj/x-archive/` | `/workspace/x-archive/gengdaJ/` | 无代码仓库；内容来自 [@gengdaJ](https://x.com/gengdaJ) 公开 X 帖 | 117 | 4.2M |
| `gefei/github-member-repos/` | `/workspace/gefei/github-refs/` | 见下表各仓 | 4488（另加各目录 `UPSTREAM.md`） | 470M |

复制完成后，本仓工作区合计约 516M（不含 `.git`；含 README / SOURCES / 人物卡与索引）。

## 分类说明

### 哥飞公众号 `gefei/wechat-articles/`

883 篇 markdown 正文。无上游 git 仓库。2026-11-22 补入 16 篇（11-08 之后 12 篇，以及此前缺的 11-02、11-03、11-04、11-07）。官方微信正文页触发环境异常，搜狗跳转被反爬，这 16 篇正文从 ReaderMX 收录，文首「来源」已注明；11-14 的 ReaderMX 条目是失败页，未收录。

### 会员群 `gefei/group-chat/`

经仓主决定一并公开。截图中可能含有头像或昵称。

- 记录：`20261004.md`、`20261022.md`、`刘小排分工.md`
- 截图：`screenshots/` 下 11 张 png

### GitHub 会员资料种子 `gefei/github-seed/`

工作区结构：`readme.md`、`extract_wechat_url.py`、`公众号/`（39 个文件）、`哥飞/`（567 个文件）。已排除上游 `.git`。

### 西门笔记 `gefei/ximen-notes/`

经仓主决定一并公开。1 个文件：`2026-10-27-出海经验整理.md`（3356 字节）。

### 刘小排 X 归档 `liuxiaopai/x-archive/`

- `index.md`（含类型标签）、`all.md`
- `articles/`：46 个文件（X Article 与长帖/长线程）
- `raw/`：22 个文件（原始 JSON 等）
- 原料全收，类型见 `index.md` 与仓库根目录 `index/x-posts.csv`

### 土豆姐 X 归档 `poteto/x-archive/`

- `index.md`（含类型标签）、`all.md`（Grok Bot 相关）、`other.md`（本次取到但明显无关，保留）
- `articles/`：42 个文件（X Article、长帖与长线程）
- `raw/`：43 个文件（账号资料、合并帖、各次搜索/时间线原始 JSON）
- 原料全收，类型见 `index.md` 与仓库根目录 `index/x-posts.csv`

### 小晚不在 X 归档 `bbkirstry/x-archive/`

- `index.md`（含类型标签）、`all.md`
- `articles/`：60 个文件（X Article、长帖与长线程）
- `raw/`：33 个文件（账号资料、合并帖、时间线与各次搜索的原始 JSON）
- 资料页公开帖数 2789，本次去重后取回 551 条（16 篇 X Article 均有全文）。未翻完，详见该目录 `index.md`。
- 原料全收，类型见 `index.md` 与仓库根目录 `index/x-posts.csv`

### 小晚不在飞书知识库 `bbkirstry/feishu-kb/`

2026-11-23 经哆啦批准公开。本机原目录为 `/workspace/私有原料/小晚知识库/`（复制入库，未移动原文）。

- 126 个 Word（`.docx`）与 1 个 Excel（社群好用工具库）
- 根目录另有 `README.md`、`目录.md`，以及由哆啦粘贴的 `11-16 写给所有正在 AI 时代寻找自己的人.md`
- `md/`：127 篇 Markdown（126 篇由 Word 转换，加上上述 11-16 粘贴稿）和工具库 CSV（两个工作表）
- `md/media/`：29 张插图，分属 5 篇
- 导出方法见该目录 `README.md`。飞书导出的部分 Word 缺 `tblGrid`，转换时已补上，以免章节目录表丢失。

### 小晚认知模型 `bbkirstry/cognitive-model/`

2026-11-23 经哆啦批准公开。本机原目录为 `/workspace/私有原料/小晚认知模型/`（复制入库，未移动原文）。`标注/` 为训练集标注（`annotations.jsonl`、`标注说明.md`、`初步规律.md`）。`认知卡/` 为第 3 步产物（`认知卡.md`、`反例.md`、`预测说明.md`），只根据训练集写成。

- `X档案补全/`：551 条公开 X 帖的补全（`posts_enriched.json`）、`进度.md`、接口回包 `fetch_raw/`
- `封存测试集/`：2026-09-23 至 2026-11-23 的预留验证集（X 369 条 + 飞书 9 篇）。标注和写认知卡时不要打开。详见 `SEALED.md`
- `训练集索引.md`：其余 302 条的来源、日期、类型、路径，不含原文
- `标注/`：训练集标注（`annotations.jsonl`、`标注说明.md`、`初步规律.md`）
- `认知卡/`：第 3 步判断规则、反例与第 4 步预测说明。写卡和出预测时不要打开封存测试集
- `scripts/build_age13_step1.py`：第一步切分脚本

### 逸尘 X 归档 `gengdaj/x-archive/`

- `index.md`（含类型标签）、`all.md`
- `articles/`：81 个文件（X Article、长帖与长线程）
- `raw/`：34 个文件（账号资料、合并帖、时间线与各次搜索的原始 JSON）
- 资料页公开帖数 4412，本次去重后取回 590 条（3 篇 X Article 均有全文）。未翻完，详见该目录 `index.md`。
- 原料全收，类型见 `index.md` 与仓库根目录 `index/x-posts.csv`

### 会员 GitHub 工作区 `gefei/github-member-repos/`

上游均为已公开 GitHub 仓，本仓可见性标 public。目录名保留历史称呼。每个子目录都有 `UPSTREAM.md`。下表 SHA 为 2026-11-22 从本机原仓读取的当时 HEAD。

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
