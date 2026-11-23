# 更新日志

## 2026-11-23（v1.0 之后）

- 说话人判断：公众号新增正文开头署名信号（「作者：某人」「投稿」「大家好，我是某某」等，非哥飞），20 篇由 `self` 改为 `quoted`，其中包括「新词新站赚钱秘诀：用好谷歌趋势」（嘉宾和平）。规则见 SCHEMA.md「说话人」。

## v1.0（2026-11-23）

蒸馏结论和验证区移出公开仓：
- 小晚认知模型（标注、认知卡、预测说明、脚本、训练集索引、X 档案补全、封存测试集）移到私有仓 `AdgaiWalker/distill-lab`。
- 验证区窗口 2026-09-23 至 2026-11-23 内的 bbkirstry X 帖 369 条和飞书文章 9 篇从当前版本移除，HOLDOUT.md 只留窗口、条数、SHA-256 和成绩，并加防污染标记（canary GUID）。
- 用普通删除提交移除，没有改写历史，旧 commit（`9a140a9` 及更早）里仍能查到这些原文。

更好用：
- README 首屏只放检索命令、兜底命令和「人 → 擅长 → 目录」表，加自动状态行，去掉本机路径。
- `tools/query.py`：可以直接写关键词；显示命中总数；标题命中在前、本人原文在前；标出「他人汇编」并折叠同名副本；`--brief` 只给路径和标题；没有命中或人名写错时列出合法人名和兜底命令，退出码非 0。
- 清单新增 `origin`（谁在说）和 `title` 字段，补全 `fetched_at`；修正说话人，如「龙猫讲…」标为转述他人，说不准的标为待定。

更少实体：
- INDEX.md 与 SOURCES.md 合并为 INDEX.md；按人统计只留在 COVERAGE.md；HOLDOUT.md 与 results.md 合并。
- `scripts/` 并入 `tools/`，删除 `classify.py`、`stats.py` 和 `index/classification.csv`；人物卡去掉自动生成的材料清单（gefei.md 从 21.6 万字降到约 1100 字）。
- 一条命令 `python3 tools/refresh.py [--fetched]` 跑完全部步骤，日志写入 `logs/refresh.jsonl`。
- GitHub Action（schema 不通过就失败，覆盖率只报警）已写好，但推送需要 GitHub 令牌的 `workflow` 权限，尚未进仓。
