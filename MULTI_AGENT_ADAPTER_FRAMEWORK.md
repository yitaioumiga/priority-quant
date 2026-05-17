# 多智能体适配框架

## 概述

本框架定义了如何让skill适配不同类型的智能体平台，包括编程智能体和自主智能体。

## 智能体分类

### 编程智能体 (Programming Agents)
专注于代码编辑、执行和调试的智能体平台。

| 智能体 | 特点 | 适配重点 |
|--------|------|----------|
| Claude Code | 直接执行、自然语言交互 | 脚本执行、实时反馈 |
| Codex | 沙箱执行、安全隔离 | 资源限制、网络访问 |
| Windsurf | 工作区环境、状态持久化 | 协作支持、后台任务 |
| Cursor | 内联执行、实时预览 | 编辑器集成、即时反馈 |
| Trae | 集成执行、原生体验 | IDE功能集成、通知支持 |
| GitHub Copilot | 对话交互、智能建议 | 自然语言处理、上下文感知 |

### 自主智能体 (Autonomous Agents)
专注于任务规划、自动执行和决策支持的智能体平台。

| 智能体 | 特点 | 适配重点 |
|--------|------|----------|
| OpenClaw | 任务规划、自动执行 | 任务分解、依赖追踪、定时执行 |
| Hermes | 深度规划、并行执行 | 多层分解、上下文感知、历史学习 |

## 适配器配置结构

每个skill的适配器配置文件 (`adapters/adapter-config.json`) 包含：

```json
{
  "skill_name": "skill名称",
  "version": "版本号",
  "description": "描述",
  "compatibility": {
    "programming_agents": {
      "agent_name": {
        "compatible": true/false,
        "trigger_patterns": ["触发词"],
        "execution_mode": "执行模式",
        "script_runner": "脚本运行器",
        "agent_specific_config": {}
      }
    },
    "autonomous_agents": {
      "agent_name": {
        "compatible": true/false,
        "trigger_patterns": ["触发词"],
        "execution_mode": "autonomous",
        "task_planning": {
          "enabled": true,
          "decomposition_depth": 3,
          "dependency_tracking": true
        },
        "autonomous_features": {
          "scheduled_execution": true,
          "proactive_monitoring": true,
          "decision_making": true,
          "multi_step_workflows": true
        },
        "task_templates": {}
      }
    }
  },
  "execution_modes": {}
}
```

## 执行模式

### 编程智能体执行模式

1. **direct** - 直接在当前环境执行
   - 优点：实时反馈、无需额外配置
   - 缺点：依赖本地环境

2. **sandbox** - 在隔离沙箱中执行
   - 优点：安全隔离、资源可控
   - 缺点：需要沙箱支持

3. **workspace** - 在工作区环境中执行
   - 优点：状态持久化、支持协作
   - 缺点：需要工作区配置

4. **inline** - 内联执行并显示结果
   - 优点：即时预览、无缝集成
   - 缺点：可能影响编辑体验

5. **integrated** - 集成到IDE功能中
   - 优点：深度集成、原生体验
   - 缺点：需要IDE支持

6. **chat** - 通过对话交互执行
   - 优点：自然语言交互、灵活
   - 缺点：可能不够精确

### 自主智能体执行模式

7. **autonomous** - 自主执行模式
   - 优点：自动化程度高、支持复杂工作流、可定时执行
   - 缺点：需要任务规划能力、可能需要用户确认关键决策

## 任务模板结构

自主智能体使用任务模板来定义自动化工作流：

```json
{
  "task_name": {
    "description": "任务描述",
    "steps": ["步骤1", "步骤2", ...],
    "schedule": "执行计划",
    "priority": "优先级",
    "trigger": "触发条件"
  }
}
```

## 适配指南

### 为编程智能体适配skill

1. 确保脚本使用标准库，减少依赖
2. 提供清晰的命令行接口
3. 支持JSON输入输出
4. 处理平台差异（路径、编码等）
5. 提供实时反馈和进度显示

### 为自主智能体适配skill

1. 定义清晰的任务模板
2. 设计合理的任务分解层次
3. 支持依赖追踪和并行执行
4. 提供决策点和用户确认机制
5. 支持定时执行和主动监控

## 最佳实践

1. **渐进式适配**: 先支持编程智能体，再扩展到自主智能体
2. **配置驱动**: 使用JSON配置文件管理适配参数
3. **模板复用**: 为常见任务创建可复用模板
4. **测试覆盖**: 为每种智能体模式编写测试用例
5. **文档完善**: 提供清晰的使用示例和适配指南

## 示例

### 项目优先级量化模型
- 仅支持编程智能体
- 专注于项目评估和排序
- 提供脚本执行和结果分析

### 理财检查策略
- 支持编程智能体和自主智能体
- 提供自动化任务规划和执行
- 支持定时检查和主动监控

## 版本历史
- v1.0.0 (2024-04-17): 初始版本，定义多智能体适配框架
