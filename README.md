# priority-quant

项目优先级量化评估skill

## 功能

- 双轨制评估（Fast-track极速4象限 / Deep-track深度6维度）
- 战略对齐检验
- 飞书多维表格集成
- WBS拆解触发

## 适配智能体

✅ 编程智能体：Claude Code、Codex、Windsurf、Cursor、Trae、GitHub Copilot

❌ 自主智能体：不适用（编程项目评估工具）

## 使用方式

1. 参考 `SKILL.md` 了解具体使用方法
2. 查看 `adapters/adapter-config.json` 了解适配配置
3. 运行 `scripts/evaluate.py` 进行项目评估

## 目录结构

```
.
├── SKILL.md                   # 主文档
├── adapters/                  # 适配器配置
├── references/                # 参考文档
├── scripts/                   # 执行脚本
└── MULTI_AGENT_ADAPTER_FRAMEWORK.md  # 通用适配框架
```

## 版本历史

- v1.0.0 (2024-04-17): 初始版本
