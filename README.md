<div align="center">

# 🎯 Priority Quant

**项目优先级量化评估模型 - 多智能体适配版**

[![Version](https://img.shields.io/badge/version-1.1.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)]()
[![Agents](https://img.shields.io/badge/agents-8-green.svg)]()

[快速开始](#-快速开始) · [功能特性](#-功能特性) · [使用示例](#-使用示例) · [适配智能体](#-适配智能体)

</div>

---

## 📖 简介

**Priority Quant** 是一个基于多维度量化模型的项目优先级评估工具，通过双轨制评估（极速4象限/深度6维度）帮助用户做出科学的资源分配决策。

### 适用场景

- 🚀 项目选型：多个项目同时进行，需要确定优先级
- 📊 资源分配：有限资源下，如何分配人力物力
- 🎯 战略对齐：确保项目与核心目标一致
- 📋 任务管理：日常任务的优先级排序

---

## ✨ 功能特性

| 功能 | 说明 | 触发方式 |
|------|------|----------|
| **双轨制评估** | Fast-track极速4象限 / Deep-track深度6维度 | 自动识别项目复杂度 |
| **6维度量化** | 紧急度、重要度、规模、可行性、ROI、依赖阻塞 | 加权计算 |
| **战略对齐检验** | 验证项目与核心目标的对齐度 | 每次评估自动 |
| **AI预审推荐** | 智能体预估评分，用户复核微调 | Deep-track模式 |
| **飞书集成** | 评估结果导出到飞书多维表格 | 可选配置 |
| **WBS拆解** | Top1项目自动触发任务拆解 | 评估完成后 |

---

## 🚀 快速开始

### 前置要求

- Python 3.8+
- 智能体环境（Claude Code / Codex / Windsurf / Cursor / Trae / GitHub Copilot / OpenClaw / Hermes）

### 基本使用

```bash
# 克隆仓库
git clone https://github.com/yitaioumiga/priority-quant.git
cd priority-quant

# 执行评估
python scripts/evaluate.py --projects '[{"name":"项目A","urgency":5,"importance":5,"scale":3,"feasibility":4,"roi":4,"dependencies":2}]'
```

---

## 📚 使用示例

### 示例 1: Fast-track 极速模式

**场景**：日常小任务，单人执行，<1周工作量

**输入**：
```
整理笔记、写周报、回复邮件
```

**输出**：
```
✅ Fast-track模式
- 整理笔记：重要不紧急 → 安排固定时间段
- 写周报：重要紧急 → 立即处理
- 回复邮件：紧急不重要 → 批量处理或委托
```

### 示例 2: Deep-track 深度模式

**场景**：复杂项目，多方协作，≥1周工作量

**输入**：
```json
{
  "name": "电商平台重构",
  "description": "涉及前后端、数据迁移、用户体验优化，预计2个月",
  "urgency": 3,
  "importance": 5,
  "scale": 4,
  "feasibility": 4,
  "roi": 5,
  "dependencies": 3
}
```

**输出**：
```
✅ Deep-track模式
📊 综合评分：4.15/5.0
📈 排名：第1名
🎯 战略对齐度：完全对齐

行动建议：
1. 立即启动，组建项目团队
2. 拆解为最小启动单元
3. 优先处理数据迁移模块
```

### 示例 3: 战略偏离警告

**场景**：项目与当前核心目标不一致

**输入**：
```
当前核心目标：产品上线
新项目：社交媒体营销方案
```

**输出**：
```
⚠️ 战略偏离警告
该项目与当前核心目标"产品上线"严重偏离
建议：暂缓或放弃该项目，集中精力聚焦产品上线
```

---

## 🤖 适配智能体

### 编程智能体

| 智能体 | 适配程度 | 触发方式 | 执行模式 |
|--------|----------|----------|----------|
| **Claude Code** | ✅ 完全适配 | `/project-priority` 或自然语言 | 直接执行 |
| **Codex** | ✅ 完全适配 | 自然语言触发 | 沙箱执行 |
| **Windsurf** | ✅ 完全适配 | 工作区内触发 | 工作区执行 |
| **Cursor** | ✅ 完全适配 | 内联触发 | 内联执行 |
| **Trae** | ✅ 完全适配 | 集成触发 | 集成执行 |
| **GitHub Copilot** | ✅ 完全适配 | 对话触发 | 对话执行 |

### 自主智能体

| 智能体 | 适配程度 | 自主能力 | 特殊功能 |
|--------|----------|----------|----------|
| **OpenClaw** | ✅ 完全适配 | 定时执行、主动监控 | 3层任务分解、依赖追踪 |
| **Hermes** | ✅ 完全适配 | 定时执行、主动监控、并行执行 | 4层任务分解、上下文感知 |

### 适配说明

#### 编程智能体

本skill完全适配以下编程智能体：

- **Claude Code**: 直接执行，支持自然语言交互
- **Codex**: 沙箱执行，资源隔离
- **Windsurf**: 工作区执行，状态持久化
- **Cursor**: 内联执行，实时预览
- **Trae**: 集成执行，原生体验
- **GitHub Copilot**: 对话执行，智能建议

#### 自主智能体

本skill完全适配以下自主智能体：

- **OpenClaw**: 支持任务规划和自动执行
  - 3层任务分解
  - 依赖追踪
  - 定时执行

- **Hermes**: 支持更深层次的任务规划
  - 4层任务分解
  - 上下文感知
  - 历史学习
  - 并行执行

### 使用方式

#### 编程智能体

```bash
# Claude Code
/project-priority 或自然语言描述

# Codex
自然语言描述

# Windsurf
工作区内触发

# Cursor
内联触发

# Trae
集成触发

# GitHub Copilot
对话触发
```

#### 自主智能体

```python
# OpenClaw
自动规划任务执行流程
支持3层任务分解和依赖追踪

# Hermes
支持更深层次的任务规划和并行执行
4层任务分解，支持上下文感知和历史学习
```

---

## 📁 项目结构

```
priority-quant/
├── SKILL.md                          # 主文档
├── README.md                         # 本文件
├── MULTI_AGENT_ADAPTER_FRAMEWORK.md  # 通用适配框架
├── adapters/
│   └── adapter-config.json           # 智能体适配配置
├── references/
│   └── scoring-guide.md              # 评分指南
└── scripts/
    └── evaluate.py                   # 评估脚本
```

---

## 📖 文档

- [SKILL.md](SKILL.md) - 完整使用文档
- [评分指南](references/scoring-guide.md) - 6维度评分标准
- [适配框架](MULTI_AGENT_ADAPTER_FRAMEWORK.md) - 多智能体适配原理

---

## 🤝 贡献

欢迎贡献！请遵循以下步骤：

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

---

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

---

## 🙏 致谢

- [awesome-readme](https://github.com/matiassingers/awesome-readme) - README最佳实践
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template) - README模板

---

<div align="center">

**[⬆ 回到顶部](#-priority-quant)**

</div>
