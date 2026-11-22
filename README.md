# distill-sources

这是一份**私有蒸馏原料仓**，只放原始材料，供后续蒸馏使用。

仓库中含有会员内容（会员群记录、会员整理的 GitHub 资料等）。**禁止改成公开仓库，禁止再分发会员内容。**

加工好的能力卡和蒸馏产出不在本仓，仍放在本机 `/workspace/gefei/gefei-skill-pack`。

收录日期：2026-11-22。材料从共享电脑对应目录复制而来（`rsync -a --exclude '.git'`），原目录未移动。

## 目录说明

| 目录 | 内容 | 归属 |
|---|---|---|
| `gefei/wechat-articles/` | 哥飞公众号正文 markdown（867 篇） | 哥飞公众号 |
| `gefei/group-chat/` | 会员群记录与截图 | 哥飞会员群 |
| `gefei/github-seed/` | GitHub 会员资料种子仓工作区（已排除 `.git`） | 上游仓库 [mundane799699/gefei_mp_export](https://github.com/mundane799699/gefei_mp_export) |
| `gefei/github-member-repos/` | 各会员整理的哥飞相关仓库工作区（已排除每个仓的 `.git`）；每个子目录有 `UPSTREAM.md`，记录 origin URL 与当时 commit SHA | 各上游仓库（见 `SOURCES.md`） |
| `gefei/ximen-notes/` | 西门笔记 | 哆啦整理的西门笔记 |
| `liuxiaopai/x-archive/` | 刘小排 X 归档（帖子、长文、原始 JSON） | 刘小排 [@bourneliu66](https://x.com/bourneliu66) |

更细的本机原路径、上游 URL、文件数与大小见 [SOURCES.md](SOURCES.md)。

人物与用途索引见 [INDEX.md](INDEX.md)（由 `scripts/classify.py` 生成；原文件不移动）。哥飞、西门用于出海，刘小排用于产品。按人清单在 `people/`，机器可读表在 `index/classification.csv`。

## 不收录

- `gefei-skill-pack` 及其备份、`gefei-agent-oss`（加工后的能力卡 / 蒸馏结果）
- zip、tar、抓取日志、`failed*.jsonl`、`articles_bak_*`、`batch*`、`tools`、`x-promo`、`newword-sources`、`browser_text`、`feedback`
- 密钥、`.env`、token 文件、账号清单
