---
name:
slug:
primary_purpose:
purposes: []
expertise: 待补
planned_skills: 待补
existing_skills: 待补
sources: []
coverage_until:
update_method: 待补
visibility: 待补
---

# 姓名

## 擅长

待补。只写可核实的事实，吃不准就留待补。

## 已有相关 skill

待补。

## 计划蒸馏成的 skill

待补。

## 材料

用 `python3 tools/query.py --person <slug> --brief --limit 0` 列出全部原料。

## 如何补充新材料

1. 把新的原始文件放进该人在 `people.yaml` 里登记的目录（不要改已有原文，不要改名）。
2. 若是新的来源类型或可见性，先改仓库根目录的 `people.yaml`。
3. 在仓库根目录运行 `python3 tools/refresh.py --fetched`（打 X 类型标签、重建清单和覆盖率）。
4. 可见性拿不准时可先标 `member`（表示来源，不表示禁止公开）。
