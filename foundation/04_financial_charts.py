"""
第一层：基础语法教学 - 财务图表实战
学习目标：综合运用 matplotlib 绘制专业财务报表图表
知识点分类：【熟悉掌握】
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-darkgrid')  # 使用专业样式

# ============ 1. 财务三表趋势图 ============
print("=" * 50)
print("示例 1：财务三表趋势分析")
print("=" * 50)

# 模拟 12 个月的财务数据
months = ['1月', '2月', '3月', '4月', '5月', '6月',
          '7月', '8月', '9月', '10月', '11月', '12月']

# 营业收入（万元）
revenue = np.array([450, 520, 480, 610, 580, 670,
                    720, 680, 750, 800, 820, 900])

# 净利润（万元）
profit = revenue * 0.25 + np.random.randn(12) * 10

# 经营现金流（万元）
cash_flow = profit * 1.1 + np.random.randn(12) * 15

# 创建画布和子图
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10))

# 子图 1：营业收入
ax1.plot(months, revenue, 'o-', linewidth=2, markersize=8,
         color='#2E86AB', label='营业收入')
ax1.fill_between(range(len(months)), revenue, alpha=0.3, color='#2E86AB')
ax1.set_title('营业收入趋势', fontsize=14, fontweight='bold')
ax1.set_ylabel('金额（万元）', fontsize=12)
ax1.legend(loc='upper left', fontsize=11)
ax1.grid(True, alpha=0.3)

# 在数据点上显示数值
for i, v in enumerate(revenue):
    ax1.text(i, v + 20, f'{v:.0f}', ha='center', fontsize=9)

# 子图 2：净利润
ax2.plot(months, profit, 's-', linewidth=2, markersize=8,
         color='#A23B72', label='净利润')
ax2.fill_between(range(len(months)), profit, alpha=0.3, color='#A23B72')
ax2.set_title('净利润趋势', fontsize=14, fontweight='bold')
ax2.set_ylabel('金额（万元）', fontsize=12)
ax2.legend(loc='upper left', fontsize=11)
ax2.grid(True, alpha=0.3)

# 子图 3：经营现金流
ax3.plot(months, cash_flow, '^-', linewidth=2, markersize=8,
         color='#F18F01', label='经营现金流')
ax3.fill_between(range(len(months)), cash_flow, alpha=0.3, color='#F18F01')
ax3.set_title('经营现金流趋势', fontsize=14, fontweight='bold')
ax3.set_xlabel('月份', fontsize=12)
ax3.set_ylabel('金额（万元）', fontsize=12)
ax3.legend(loc='upper left', fontsize=11)
ax3.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('financial_trends.png', dpi=300, bbox_inches='tight')
print("图表已保存：financial_trends.png")
plt.show()

# ============ 2. 利润率分析仪表盘 ============
print("\n" + "=" * 50)
print("示例 2：利润率分析仪表盘")
print("=" * 50)

# 计算各项利润率
gross_margin = (revenue - revenue * 0.6) / revenue * 100  # 毛利率
operating_margin = profit / revenue * 100  # 营业利润率
net_margin = profit / revenue * 100  # 净利率

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 子图 1：毛利率趋势
axes[0, 0].plot(months, gross_margin, 'o-', linewidth=2, color='#06A77D')
axes[0, 0].axhline(y=np.mean(gross_margin), color='red', linestyle='--',
                   linewidth=2, label=f'平均值: {np.mean(gross_margin):.1f}%')
axes[0, 0].set_title('毛利率趋势', fontsize=13, fontweight='bold')
axes[0, 0].set_ylabel('毛利率 (%)', fontsize=11)
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 子图 2：营业利润率趋势
axes[0, 1].plot(months, operating_margin, 's-', linewidth=2, color='#D62246')
axes[0, 1].axhline(y=np.mean(operating_margin), color='blue', linestyle='--',
                   linewidth=2, label=f'平均值: {np.mean(operating_margin):.1f}%')
axes[0, 1].set_title('营业利润率趋势', fontsize=13, fontweight='bold')
axes[0, 1].set_ylabel('营业利润率 (%)', fontsize=11)
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 子图 3：利润率对比（箱线图）
data_margins = [gross_margin, operating_margin, net_margin]
bp = axes[1, 0].boxplot(data_margins, labels=['毛利率', '营业利润率', '净利率'],
                        patch_artist=True)
colors = ['#06A77D', '#D62246', '#F18F01']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.7)
axes[1, 0].set_title('利润率分布对比', fontsize=13, fontweight='bold')
axes[1, 0].set_ylabel('利润率 (%)', fontsize=11)
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 子图 4：季度平均利润率
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
q_gross = [gross_margin[:3].mean(), gross_margin[3:6].mean(),
           gross_margin[6:9].mean(), gross_margin[9:].mean()]
q_operating = [operating_margin[:3].mean(), operating_margin[3:6].mean(),
               operating_margin[6:9].mean(), operating_margin[9:].mean()]
q_net = [net_margin[:3].mean(), net_margin[3:6].mean(),
         net_margin[6:9].mean(), net_margin[9:].mean()]

x = np.arange(len(quarters))
width = 0.25

axes[1, 1].bar(x - width, q_gross, width, label='毛利率', color='#06A77D', alpha=0.8)
axes[1, 1].bar(x, q_operating, width, label='营业利润率', color='#D62246', alpha=0.8)
axes[1, 1].bar(x + width, q_net, width, label='净利率', color='#F18F01', alpha=0.8)
axes[1, 1].set_title('季度平均利润率对比', fontsize=13, fontweight='bold')
axes[1, 1].set_xlabel('季度', fontsize=11)
axes[1, 1].set_ylabel('利润率 (%)', fontsize=11)
axes[1, 1].set_xticks(x)
axes[1, 1].set_xticklabels(quarters)
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('profit_margin_dashboard.png', dpi=300, bbox_inches='tight')
print("图表已保存：profit_margin_dashboard.png")
plt.show()

# ============ 3. 成本结构分析 ============
print("\n" + "=" * 50)
print("示例 3：成本结构分析（双饼图）")
print("=" * 50)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 上半年成本结构
h1_categories = ['原材料', '人工', '制造费用', '管理费用', '销售费用']
h1_costs = [180000, 120000, 60000, 45000, 35000]

# 下半年成本结构
h2_costs = [200000, 135000, 70000, 50000, 40000]

# 饼图 1：上半年
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']
explode = (0.05, 0, 0, 0, 0)

wedges1, texts1, autotexts1 = ax1.pie(h1_costs, labels=h1_categories, autopct='%1.1f%%',
                                        startangle=90, colors=colors, explode=explode,
                                        textprops={'fontsize': 11})
ax1.set_title('上半年成本结构', fontsize=14, fontweight='bold')

# 饼图 2：下半年
wedges2, texts2, autotexts2 = ax2.pie(h2_costs, labels=h1_categories, autopct='%1.1f%%',
                                        startangle=90, colors=colors, explode=explode,
                                        textprops={'fontsize': 11})
ax2.set_title('下半年成本结构', fontsize=14, fontweight='bold')

# 设置百分比文字为白色加粗
for autotext in autotexts1 + autotexts2:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

plt.tight_layout()
plt.savefig('cost_structure.png', dpi=300, bbox_inches='tight')
print("图表已保存：cost_structure.png")
plt.show()

# ============ 4. 现金流瀑布图 ============
print("\n" + "=" * 50)
print("示例 4：现金流瀑布图")
print("=" * 50)

# 现金流数据
categories = ['期初余额', '经营活动', '投资活动', '筹资活动', '期末余额']
values = [500000, 320000, -150000, 80000, 750000]

# 计算累积值（用于绘制瀑布图）
cumulative = [0]
for i, v in enumerate(values[:-1]):
    cumulative.append(cumulative[-1] + v)

fig, ax = plt.subplots(figsize=(12, 7))

# 绘制瀑布图
colors_waterfall = ['#2E86AB', '#06A77D', '#D62246', '#F18F01', '#2E86AB']
for i in range(len(categories)):
    if i == 0 or i == len(categories) - 1:
        # 期初和期末：从 0 开始
        ax.bar(i, values[i], color=colors_waterfall[i], alpha=0.8, width=0.6)
    else:
        # 中间项：从累积值开始
        color = '#06A77D' if values[i] > 0 else '#D62246'
        ax.bar(i, values[i], bottom=cumulative[i], color=color, alpha=0.8, width=0.6)
        # 绘制连接线
        ax.plot([i - 0.3, i + 0.3], [cumulative[i], cumulative[i]],
                'k--', linewidth=1, alpha=0.5)
        if i < len(categories) - 1:
            ax.plot([i + 0.3, i + 0.7], [cumulative[i+1], cumulative[i+1]],
                    'k--', linewidth=1, alpha=0.5)

# 在柱子上显示数值
for i, v in enumerate(values):
    if i == 0 or i == len(categories) - 1:
        y_pos = v / 2
    else:
        y_pos = cumulative[i] + v / 2
    ax.text(i, y_pos, f'{v:,}', ha='center', va='center',
            fontsize=11, fontweight='bold', color='white')

ax.set_xticks(range(len(categories)))
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylabel('金额（元）', fontsize=12)
ax.set_title('现金流瀑布图', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('cash_flow_waterfall.png', dpi=300, bbox_inches='tight')
print("图表已保存：cash_flow_waterfall.png")
plt.show()

print("\n" + "=" * 50)
print("财务图表实战完成！")
print("=" * 50)
print("\n【财务图表设计要点】：")
print("1. 配色方案：使用专业配色（避免过于鲜艳）")
print("2. 数据标注：关键数值必须显示在图表上")
print("3. 参考线：添加平均值、目标值等参考线")
print("4. 图例说明：清晰标注各项指标含义")
print("5. 保存高清：dpi=300 用于打印和报告")
print("\n【推荐配色方案】：")
print("- 蓝色系：#2E86AB（收入、资产）")
print("- 绿色系：#06A77D（利润、正向指标）")
print("- 红色系：#D62246（成本、负向指标）")
print("- 橙色系：#F18F01（现金流、中性指标）")
