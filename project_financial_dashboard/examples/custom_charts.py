"""
自定义图表示例
展示如何基于 FinancialDashboard 创建自定义图表
"""

from financial_dashboard import FinancialDashboard
import matplotlib.pyplot as plt
import numpy as np

# 创建仪表盘
dashboard = FinancialDashboard()
dashboard.generate_sample_data(months=12)

# ============ 示例 1：自定义双轴图表 ============
print("=" * 50)
print("示例 1：自定义双轴图表（收入 + 利润率）")
print("=" * 50)

fig, ax1 = plt.subplots(figsize=(12, 6))

# 左轴：营业收入
x = range(len(dashboard.data))
revenue = dashboard.data['营业收入'].values

ax1.bar(x, revenue, alpha=0.6, color=dashboard.colors['revenue'], label='营业收入')
ax1.set_xlabel('月份')
ax1.set_ylabel('营业收入（万元）', color=dashboard.colors['revenue'])
ax1.tick_params(axis='y', labelcolor=dashboard.colors['revenue'])

# 右轴：净利率
ax2 = ax1.twinx()
net_margin = (dashboard.data['净利润'] / dashboard.data['营业收入'] * 100).values
ax2.plot(x, net_margin, 'o-', linewidth=2, markersize=8,
         color=dashboard.colors['profit'], label='净利率')
ax2.set_ylabel('净利率 (%)', color=dashboard.colors['profit'])
ax2.tick_params(axis='y', labelcolor=dashboard.colors['profit'])

plt.title('营业收入与净利率双轴图', fontsize=14, fontweight='bold')
fig.tight_layout()
plt.savefig('custom_dual_axis.png', dpi=300, bbox_inches='tight')
print("双轴图表已保存：custom_dual_axis.png")
plt.show()

# ============ 示例 2：环形饼图 ============
print("\n" + "=" * 50)
print("示例 2：环形饼图（成本结构）")
print("=" * 50)

fig, ax = plt.subplots(figsize=(10, 8))

# 计算总成本和利润
total_cost = dashboard.data['营业成本'].sum()
total_profit = dashboard.data['净利润'].sum()
total_revenue = dashboard.data['营业收入'].sum()

# 假设成本细分
categories = ['原材料', '人工', '制造费用', '管理费用', '净利润']
values = [
    total_cost * 0.5,  # 原材料
    total_cost * 0.25, # 人工
    total_cost * 0.15, # 制造费用
    total_cost * 0.1,  # 管理费用
    total_profit       # 净利润
]

colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', dashboard.colors['profit']]

# 绘制环形饼图
wedges, texts, autotexts = ax.pie(values, labels=categories, autopct='%1.1f%%',
                                    startangle=90, colors=colors,
                                    wedgeprops=dict(width=0.5))  # width < 1 创建环形

# 设置文字样式
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')
    autotext.set_fontsize(11)

plt.title('收入结构环形图', fontsize=14, fontweight='bold')
plt.savefig('custom_donut_chart.png', dpi=300, bbox_inches='tight')
print("环形饼图已保存：custom_donut_chart.png")
plt.show()

# ============ 示例 3：雷达图 ============
print("\n" + "=" * 50)
print("示例 3：雷达图（财务健康度）")
print("=" * 50)

fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# 财务指标（归一化到 0-100）
categories = ['盈利能力', '偿债能力', '运营能力', '成长能力', '现金流']
values = [75, 85, 70, 80, 90]  # 示例评分

# 闭合雷达图
values += values[:1]
angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]

# 绘制雷达图
ax.plot(angles, values, 'o-', linewidth=2, color=dashboard.colors['revenue'])
ax.fill(angles, values, alpha=0.25, color=dashboard.colors['revenue'])

# 设置标签
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20', '40', '60', '80', '100'], fontsize=10)
ax.grid(True)

plt.title('财务健康度雷达图', fontsize=14, fontweight='bold', pad=20)
plt.savefig('custom_radar_chart.png', dpi=300, bbox_inches='tight')
print("雷达图已保存：custom_radar_chart.png")
plt.show()

# ============ 示例 4：瀑布图（详细版）============
print("\n" + "=" * 50)
print("示例 4：瀑布图（利润构成）")
print("=" * 50)

fig, ax = plt.subplots(figsize=(12, 7))

# 利润构成数据
categories = ['营业收入', '营业成本', '税金', '管理费用', '财务费用', '净利润']
values = [
    dashboard.data['营业收入'].sum(),
    -dashboard.data['营业成本'].sum(),
    -dashboard.data['营业收入'].sum() * 0.05,  # 假设税金
    -dashboard.data['营业收入'].sum() * 0.03,  # 假设管理费用
    -dashboard.data['营业收入'].sum() * 0.02,  # 假设财务费用
    dashboard.data['净利润'].sum()
]

# 计算累积值
cumulative = [0]
for v in values[:-1]:
    cumulative.append(cumulative[-1] + v)

# 绘制瀑布图
for i, (cat, val) in enumerate(zip(categories, values)):
    if i == 0 or i == len(categories) - 1:
        # 起点和终点：从 0 开始
        color = dashboard.colors['revenue'] if i == 0 else dashboard.colors['profit']
        ax.bar(i, val, color=color, alpha=0.8, width=0.6)
    else:
        # 中间项：从累积值开始
        color = dashboard.colors['profit'] if val > 0 else dashboard.colors['cost']
        ax.bar(i, val, bottom=cumulative[i], color=color, alpha=0.8, width=0.6)
        # 绘制连接线
        ax.plot([i - 0.3, i + 0.3], [cumulative[i], cumulative[i]],
                'k--', linewidth=1, alpha=0.5)
        if i < len(categories) - 1:
            ax.plot([i + 0.3, i + 0.7], [cumulative[i+1], cumulative[i+1]],
                    'k--', linewidth=1, alpha=0.5)

    # 显示数值
    y_pos = val / 2 if i == 0 or i == len(categories) - 1 else cumulative[i] + val / 2
    ax.text(i, y_pos, f'{abs(val):.0f}', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, rotation=15, ha='right')
ax.set_ylabel('金额（万元）')
ax.set_title('利润构成瀑布图', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('custom_waterfall_detailed.png', dpi=300, bbox_inches='tight')
print("瀑布图已保存：custom_waterfall_detailed.png")
plt.show()

print("\n" + "=" * 50)
print("所有自定义图表示例完成！")
print("=" * 50)
print("\n生成的图表：")
print("1. custom_dual_axis.png - 双轴图表")
print("2. custom_donut_chart.png - 环形饼图")
print("3. custom_radar_chart.png - 雷达图")
print("4. custom_waterfall_detailed.png - 瀑布图")
