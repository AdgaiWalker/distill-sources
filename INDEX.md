# 人物与用途索引

分类口径：**哪些人的材料，拿来做什么用。**

- 哥飞、西门 → **出海**
- 刘小排 → **产品**

不是按 SEO、外链、需求挖掘等主题分类。

- **原文件不移动、不改名、不改内容**。本文件与 `people/`、`index/classification.csv` 都是新增索引。
- 由 [`scripts/classify.py`](scripts/classify.py) 生成，可重跑。
- 会员 GitHub 仓按 `UPSTREAM.md` / 仓库名归到对应的人，只记到仓，不逐文件列出。`github-seed` 归哥飞。
- 生成时间：2026-11-22 16:48（北京时间）。

## 一览

| 人 | 用途 | 条目 | 清单 |
|---|---|---:|---|
| 哥飞 | 出海 | 1195 | [gefei.md](people/gefei.md) |
| 西门 | 出海 | 1 | [ximen.md](people/ximen.md) |
| 刘小排 | 产品 | 49 | [liuxiaopai.md](people/liuxiaopai.md) |

合计条目：1245。

## 用途对照

| 用途 | 对应的人 | 条目 |
|---|---|---:|
| 出海 | 哥飞、西门 | 1196 |
| 产品 | 刘小排 | 49 |
| 未分类 | — | 0 |

细目来源见 [SOURCES.md](SOURCES.md)。

## 覆盖范围

- `gefei/wechat-articles/` → 哥飞 / 出海（逐篇）
- `gefei/group-chat/` → 哥飞 / 出海（转录逐篇，截图按目录）
- `gefei/github-seed/` → 哥飞 / 出海（文本逐篇，封面图按目录）
- `gefei/github-member-repos/` → 按仓归人（这批均为哥飞相关整理，出海）
- `gefei/ximen-notes/` → 西门 / 出海（逐篇）
- `liuxiaopai/x-archive/` → 刘小排 / 产品（长文/长帖逐篇，索引与 raw JSON 按条/目录）

## 重跑

```bash
python3 scripts/classify.py
```
