"""
基本使用示例
"""

from financial_dashboard import FinancialDashboard
import matplotlib.pyplot as plt

# ============ 示例 1：快速开始 ============
print("=" * 50)
print("示例 1：快速开始")
print("=" * 50)

# 创建仪表盘
dashboard = FinancialDashboard()

# 生成示例数据
dashboard.generate_sample_data(months=12)

# 生成完整报告
dashboard.generate_full_report(save_path='example_report.png')

# ============ 示例 2：单独绘制图表 ============
print("\n" + "=" * 50)
print("示例 2：单独绘制图表")
print("=" * 50)

# 创建画布
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制营业收入趋势图
dashboard.plot_revenue_trend(ax=ax)

plt.savefig('revenue_trend.png', dpi=300, bbox_inches='tight')
print("营业收入趋势图已保存：revenue_trend.png")
plt.show()

# ============ 示例 3：导出数据摘要 ============
print("\n" + "=" * 50)
print("示例 3：导出数据摘要")
print("=" * 50)

summary = dashboard.export_summary()

# 访问具体指标
print(f"\n重点指标：")
print(f"总营业收入：{summary['总营业收入']:,.2f} 万元")
print(f"总净利润：{summary['总净利润']:,.2f} 万元")
print(f"平均净利率：{summary['平均净利率']:.2f}%")

# ============ 示例 4：从 CSV 加载数据 ============
print("\n" + "=" * 50)
print("示例 4：从 CSV 加载数据")
print("=" * 50)

# 先保存示例数据为 CSV
dashboard.data.to_csv('sample_data.csv', index=False, encoding='utf-8-sig')
print("示例数据已保存为 sample_data.csv")

# 从 CSV 加载
dashboard2 = FinancialDashboard('sample_data.csv')
print("数据加载成功！")

# ============ 示例 5：自定义配色 ============
print("\n" + "=" * 50)
print("示例 5：自定义配色")
print("=" * 50)

# 创建新仪表盘
dashboard3 = FinancialDashboard()
dashboard3.generate_sample_data(months=6)

# 修改配色方案
dashboard3.colors = {
    'revenue': '#1E88E5',  # 蓝色
    'profit': '#43A047',   # 绿色
    'cost': '#E53935',     # 红色
    'cash': '#FB8C00'      # 橙色
}

# 绘制图表
fig, ax = plt.subplots(figsize=(12, 6))
dashboard3.plot_profit_analysis(ax=ax)
plt.savefig('custom_colors.png', dpi=300, bbox_inches='tight')
print("自定义配色图表已保存：custom_colors.png")
plt.show()

print("\n" + "=" * 50)
print("所有示例完成！")
print("=" * 50)
