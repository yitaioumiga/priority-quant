#!/usr/bin/env python3
"""
项目优先级量化评估脚本

基于多维度加权模型计算项目优先级分数并排序
"""

import argparse
import json
import sys


def calculate_priority_score(project, weights):
    """
    计算单个项目的优先级分数

    参数:
        project: 项目字典，包含各维度评分
        weights: 权重字典

    返回:
        weighted_scores: 各维度加权分数
        total_score: 总分
    """
    weighted_scores = {}

    # 正向维度（评分越高，得分越高）
    weighted_scores['urgency'] = project['urgency'] * weights['urgency']
    weighted_scores['importance'] = project['importance'] * weights['importance']
    weighted_scores['feasibility'] = project['feasibility'] * weights['feasibility']
    weighted_scores['roi'] = project['roi'] * weights['roi']

    # 反向维度（评分越高，得分越低）
    # 规模：scale=1(大规模) → 得分低；scale=5(小规模) → 得分高
    weighted_scores['scale'] = (6 - project['scale']) / 5 * weights['scale'] * 5
    # 依赖：dependencies=1(重度依赖) → 得分低；dependencies=5(无依赖) → 得分高
    weighted_scores['dependencies'] = (6 - project['dependencies']) / 5 * weights['dependencies'] * 5

    total_score = sum(weighted_scores.values())

    return weighted_scores, total_score


def validate_project(project):
    """
    验证项目数据完整性

    参数:
        project: 项目字典

    返回:
        bool: 是否有效
        str: 错误信息
    """
    required_fields = ['name', 'urgency', 'importance', 'scale', 'feasibility', 'roi', 'dependencies']

    # 检查必需字段
    for field in required_fields:
        if field not in project:
            return False, f"缺少必需字段: {field}"

    # 检查评分范围
    score_fields = ['urgency', 'importance', 'scale', 'feasibility', 'roi', 'dependencies']
    for field in score_fields:
        value = project[field]
        if not isinstance(value, int) or value < 1 or value > 5:
            return False, f"{field} 必须是1-5之间的整数"

    return True, ""


def evaluate_projects(projects, custom_weights=None):
    """
    评估多个项目的优先级

    参数:
        projects: 项目列表
        custom_weights: 自定义权重（可选）

    返回:
        dict: 评估结果
    """
    # 默认权重配置
    weights = custom_weights or {
        'urgency': 0.25,        # 紧急程度 25%
        'importance': 0.30,     # 重要程度 30%
        'scale': 0.15,          # 规模大小 15%
        'feasibility': 0.15,    # 实现可能性 15%
        'roi': 0.10,            # ROI预期 10%
        'dependencies': 0.05    # 依赖阻塞 5%
    }

    # 计算每个项目的分数
    evaluated_projects = []
    for project in projects:
        # 验证数据
        is_valid, error = validate_project(project)
        if not is_valid:
            return {
                'status': 'error',
                'message': f"项目 '{project.get('name', '未知')}' 数据无效: {error}"
            }

        # 计算分数
        weighted_scores, total_score = calculate_priority_score(project, weights)

        evaluated_projects.append({
            'name': project['name'],
            'urgency': project['urgency'],
            'importance': project['importance'],
            'scale': project['scale'],
            'feasibility': project['feasibility'],
            'roi': project['roi'],
            'dependencies': project['dependencies'],
            'weighted_scores': weighted_scores,
            'total_score': round(total_score, 2)
        })

    # 按总分降序排序
    evaluated_projects.sort(key=lambda x: x['total_score'], reverse=True)

    # 添加排名
    for idx, project in enumerate(evaluated_projects, start=1):
        project['rank'] = idx

    return {
        'status': 'success',
        'projects': evaluated_projects,
        'weights': weights,
        'total_count': len(evaluated_projects)
    }


def main():
    parser = argparse.ArgumentParser(description='项目优先级量化评估')
    parser.add_argument('--projects', required=True, help='项目列表JSON格式')
    parser.add_argument('--weights', help='自定义权重JSON格式（可选）')

    args = parser.parse_args()

    try:
        # 解析输入
        projects = json.loads(args.projects)
        weights = json.loads(args.weights) if args.weights else None

        # 评估
        result = evaluate_projects(projects, weights)

        # 输出结果
        print(json.dumps(result, ensure_ascii=False, indent=2))

        # 返回状态码
        sys.exit(0 if result['status'] == 'success' else 1)

    except json.JSONDecodeError as e:
        print(json.dumps({
            'status': 'error',
            'message': f'JSON解析错误: {str(e)}'
        }, ensure_ascii=False))
        sys.exit(1)
    except Exception as e:
        print(json.dumps({
            'status': 'error',
            'message': f'评估失败: {str(e)}'
        }, ensure_ascii=False))
        sys.exit(1)


if __name__ == '__main__':
    main()
