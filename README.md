<div align="center">

# 🎯 priority-quant

**项目优先级量化评估 Skill**

[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Agents](https://img.shields.io/badge/agents-6-orange.svg)]()

*基于多维度量化模型，智能评估项目优先级，支持多种编程智能体平台*

[快速开始](#快速开始) · [功能特性](#功能特性) · [使用示例](#使用示例) · [适配智能体](#适配智能体)

</div>

---

## 📖 简介

**priority-quant** 是一个智能项目优先级评估工具，通过双轨制评估模型（极速4象限/深度6维度）量化项目优先级，结合战略对齐检验和工作流闭环，帮助你做出更明智的资源分配决策。

### 适用场景

- 🎯 项目选型与优先级排序
- 📊 资源分配决策
- 📋 日常任务管理
- 🎯 战略对齐验证

---

## ✨ 功能特性

### 双轨制评估

| 模式 | 适用场景 | 评估维度 |
|------|----------|----------|
| **Fast-track** | 日常小项目、单人任务、<1周工作量 | 重要/紧急4象限 |
| **Deep-track** | 复杂项目、多方协作、≥1周工作量 | 6维度加权评分 |

### 核心能力

- 🤖 **AI预审推荐** - 智能体基于项目描述预估评分
- 🎯 **战略对齐检验** - 验证项目与核心目标的一致性
- 📊 **量化评估** - 6维度加权模型（紧急程度、重要程度、规模大小、实现可能性、ROI预期、依赖阻塞）
- 📝 **飞书集成** - 支持导出到飞书多维表格
- 📋 **WBS拆解** - 自动触发最小启动单元拆解

### 评分维度

| 维度 | 权重 | 说明 |
|------|------|------|
| 紧急程度 | 25% | 时间敏感性和延迟后果 |
| 重要程度 | 30% | 对业务战略的价值贡献 |
| 规模大小 | 15% | 资源投入和工作量（反向） |
| 实现可能性 | 15% | 技术可行性和风险可控性 |
| ROI预期 | 10% | 投资回报率和价值产出 |
| 依赖阻塞 | 5% | 外部依赖程度（反向） |

---

## 🚀 快速开始

### 前置要求

- Python 3.8+
- 待评估项目的基本信息

### 安装

```bash
git clone https://github.com/yitaioumiga/priority-quant.git
cd priority-quant
```

### 基本使用

#### 1. Fast-track 极速模式

对于简单项目，直接描述即可：

```
用户：整理笔记
AI：判断为"重要不紧急"，建议安排在固定时间段处理
```

#### 2. Deep-track 深度模式

对于复杂项目，使用6维度评估：

```bash
python scripts/evaluate.py --projects '[
  {
    "name": "笔记侠系统重构",
    "urgency": 3,
    "importance": 5,
    "scale": 2,
    "feasibility": 4,
    "roi": 5,
    "dependencies": 3
  }
]'
```

**输出示例**：

```json
{
  "status": "success",
  "projects": [
    {
      "name": "笔记侠系统重构",
      "total_score": 4.1,
      "rank": 1,
      "weighted_scores": {
        "urgency": 0.75,
        "importance": 1.5,
        "scale": 0.6,
        "feasibility": 0.6,
        "roi": 0.5,
        "dependencies": 0.15
      }
    }
  ],
  "weights": {
    "urgency": 0.25,
    "importance": 0.30,
    "scale": 0.15,
    "feasibility": 0.15,
    "roi": 0.10,
    "dependencies": 0.05
  }
}
```

---

## 📚 使用示例

### 示例 1: 日常小任务

**输入**：
```
整理笔记
```

**输出**：
- 模式：Fast-track
- 分类：重要不紧急
- 建议：安排在固定时间段处理

### 示例 2: 复杂项目评估

**输入**：
```
笔记侠系统重构，涉及前后端、数据迁移、用户体验优化，预计2个月
```

**输出**：
- 模式：Deep-track
- AI预评分：紧急程度3分、重要程度5分、规模2分、实现可能性4分、ROI 5分、依赖3分
- 总分：4.1
- 排名：第1位
- 建议：优先推进

### 示例 3: 战略偏离警告

**输入**：
```
当前核心目标：校招准备
新项目：淘宝商业计划书
```

**输出**：
- ⚠️ 警告：此项目与当前核心目标不符
- 建议：暂缓或降优先级

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

本skill专注于编程项目评估，不适用于自主智能体。如需自主任务规划，请使用 [portfolio-guardian](https://github.com/yitaioumiga/portfolio-guardian)。

---

## 📁 项目结构

```
priority-quant/
├── SKILL.md                      # 主文档
├── adapters/
│   └── adapter-config.json       # 多智能体适配配置
├── references/
│   └── scoring-guide.md          # 评分标准指南
├── scripts/
│   └── evaluate.py               # 评估脚本
└── MULTI_AGENT_ADAPTER_FRAMEWORK.md  # 通用适配框架
```

---

## 📖 文档

- [SKILL.md](SKILL.md) - 完整使用文档
- [scoring-guide.md](references/scoring-guide.md) - 详细评分标准
- [adapter-config.json](adapters/adapter-config.json) - 适配器配置说明
- [MULTI_AGENT_ADAPTER_FRAMEWORK.md](MULTI_AGENT_ADAPTER_FRAMEWORK.md) - 多智能体适配框架

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

- [awesome-readme](https://github.com/matiassingers/awesome-readme) - README 最佳实践
- [Best-README-Template](https://github.com/othneildrew/Best-README-Template) - README 模板

---

<div align="center">

**[⬆ 回到顶部](#-priority-quant)**

</div>
