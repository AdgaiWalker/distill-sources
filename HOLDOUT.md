# 公共验证区

每人预留一个 holdout，用来给各家蒸馏出的思维模型考试，不给任何人拿去学习。

## 规则

1. 每人封存近期一批原始数据，用 SHA-256 锁定。哈希写在该批自己的说明里（小晚见下方样例的 `SEALED.md`）。
2. 封存后禁止用于标注、写认知卡、调整规则或任何形式的蒸馏。
3. [`tools/query.py`](tools/query.py) 默认不返回 `holdout=true` 的条目，也不读取封存目录里的正文。只有考试时才加 `--include-holdout`。
4. 不要复制或移动已有封存文件。清单只引用路径和说明文件，在 `manifest.jsonl` 里给这些条目标 `holdout=true`。
5. 考试成绩回填到 [results.md](results.md)，只记链接和分数，不把结论写进原料。

## 现有样例：小晚不在（bbkirstry）

- 目录：[bbkirstry/cognitive-model/封存测试集/](bbkirstry/cognitive-model/封存测试集/)
- 说明（含窗口、条数、文件哈希）：[bbkirstry/cognitive-model/封存测试集/SEALED.md](bbkirstry/cognitive-model/封存测试集/SEALED.md)
- 窗口：2026-09-23 至 2026-11-23（北京时间，含起止日），详见 SEALED.md。
- 内容（以 SEALED.md 为准，此处不复述正文）：X 帖 369 条（打包文件 `x/posts_enriched.json`）、飞书文章 9 篇（`feishu/`）。
- 清单处理：上述封存文件各登记一条且 `holdout=true`；同时把对应的原始条目（日期落在该窗口内的 X 帖，以及与那 9 个文件名对应的 `bbkirstry/feishu-kb/` 文章）标为 `holdout=true`。依据是 SEALED.md 的窗口和文件名，不读取封存正文。
- 本说明不取代 SEALED.md，拆封前仍以那里的哈希复核。

其他人的 holdout 尚未封存。有了以后在本文件追加一节，并在清单里标 `holdout=true`。
