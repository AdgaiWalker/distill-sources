# distill-sources

这是一份**私有蒸馏原料仓**。只放原始材料，用来把「人」的知识蒸馏成 skill。

加工好的能力卡和蒸馏产出不在本仓。哥飞的能力包仍在本机 `/workspace/gefei/gefei-skill-pack`。

仓库中含有会员内容（会员群记录、会员整理的 GitHub 资料等）。**禁止改成公开仓库，禁止再分发会员内容。从会员材料蒸馏出的 skill 不得公开发布。**

收录日期：2026-11-22。材料从共享电脑对应目录复制而来（`rsync -a --exclude '.git'`），原目录未移动。

## 三层结构

1. **用途**：这种知识能帮着蒸馏出哪类 skill。每人一个主用途，可以有多个用途。目前是「出海」（哥飞、西门）、「产品」（刘小排）和「AI 工具」（土豆姐 / @poteto）。以后可扩展，例如 IP、具身智能。
2. **人**：每人一张人物卡 `people/<slug>.md`（擅长、已有 skill、计划蒸馏成的 skill、材料清单、如何补充新材料）。
3. **来源类型**：统一用 `wechat`（公众号）/ `group-chat`（会员群）/ `x` / `github` / `notes`（笔记）。

索引见 [INDEX.md](INDEX.md)，按用途 → 人排列。机器可读表在 [index/classification.csv](index/classification.csv)。人物与来源配置在 [people.yaml](people.yaml)。重跑：`python3 scripts/classify.py`。原文件不移动、不改名、不改内容。

## 目录约定

- 新人用顶层目录 `<slug>/`，人物卡是 `people/<slug>.md`。
- 已有路径保持不动：西门笔记仍在 `gefei/ximen-notes/`，不要为了「按人分目录」去搬旧文件。
- 会员 GitHub 仓只记到仓（见各目录 `UPSTREAM.md`），不逐文件打标签。`github-seed` 归哥飞。
- 更细的本机原路径、上游 URL、文件数与大小见 [SOURCES.md](SOURCES.md)。

当前材料：

| 目录 | 内容 | 人 | 来源类型 | 可见性 |
|---|---|---|---|---|
| `gefei/wechat-articles/` | 哥飞公众号正文 markdown（867 篇） | 哥飞 | wechat | public |
| `gefei/group-chat/` | 会员群记录与截图 | 哥飞 | group-chat | member |
| `gefei/github-seed/` | GitHub 会员资料种子仓工作区（已排除 `.git`）；上游 [mundane799699/gefei_mp_export](https://github.com/mundane799699/gefei_mp_export) | 哥飞 | github | public |
| `gefei/github-member-repos/` | 各会员整理的哥飞相关仓库工作区（已排除每个仓的 `.git`） | 哥飞 | github | member |
| `gefei/ximen-notes/` | 西门笔记（历史路径，不移动） | 西门 | notes | member |
| `liuxiaopai/x-archive/` | 刘小排 X 归档（帖子、长文、原始 JSON） | 刘小排 | x | public |
| `poteto/x-archive/` | 土豆姐（@poteto）X 归档：Grok Bot 相关帖、长文、原始 JSON；无关帖见 other.md | 土豆姐（lauren） | x | public |

## 可见性规则

- `public`：公开公众号文章、公开 X 帖、公开的开源仓库。
- `member`：会员群材料、会员 GitHub 仓。拿不准时标 `member`（例如非公开笔记）。
- **从会员材料蒸馏出的 skill 不得公开发布。**

## 新增一个人

1. 确定主用途（以及是否还有其他用途）。若是新用途，先在 `people.yaml` 的 `known_purposes` 里加上。
2. 建顶层目录 `<slug>/`，把原始材料放进去（已有历史路径不要搬）。
3. 复制 [`templates/person-card.md`](templates/person-card.md) 为 `people/<slug>.md`，填写 frontmatter 和擅长、已有 skill 等。只写可核实的事实，吃不准写「待补」。
4. 在 [`people.yaml`](people.yaml) 增加一条：`slug`、`name`、用途，以及各材料路径、`source_type`、`visibility`、`scanner`。
5. 在仓库根目录运行 `python3 scripts/classify.py`，检查 `INDEX.md`、人物卡里的材料清单和 `index/classification.csv`。
6. 可见性拿不准标 `member`。从会员材料蒸出的 skill 不得公开发布。

## 重跑索引

```bash
python3 scripts/classify.py
```

脚本读 `people.yaml`，覆盖生成 `INDEX.md`、`index/classification.csv`，并只更新人物卡中 `<!-- BEGIN MATERIAL LIST -->` 与 `<!-- END MATERIAL LIST -->` 之间的清单，手写部分不动。时间使用北京时间。

## 不收录

- `gefei-skill-pack` 及其备份、`gefei-agent-oss`（加工后的能力卡 / 蒸馏结果）
- zip、tar、抓取日志、`failed*.jsonl`、`articles_bak_*`、`batch*`、`tools`、`x-promo`、`newword-sources`、`browser_text`、`feedback`
- 密钥、`.env`、token 文件、账号清单
