"""
第二层：模块联合教学 - Matplotlib + Pandas 数据可视化
学习目标：掌握 pandas DataFrame 与 matplotlib 的集成使用
知识点分类：【熟悉掌握】
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ============ 1. DataFrame 直接绘图 ============
print("=" * 50)
print("示例 1：DataFrame 直接绘图（最简单方式）")
print("=" * 50)

# 创建财务数据 DataFrame
data = {
    '月份': ['1月', '2月', '3月', '4月', '5月', '6月'],
    '营业收入': [450, 520, 480, 610, 580, 670],
    '营业成本': [270, 312, 288, 366, 348, 402],
    '净利润': [120, 145, 135, 175, 165, 195]
}
df = pd.DataFrame(data)

print("数据预览：")
print(df)

# DataFrame.plot() 方法直接绘图
# kind 参数指定图表类型：'line', 'bar', 'barh', 'pie', 'scatter', 'area'
# x 参数指定 x 轴列，y 参数指定 y 轴列（可以是列表）
df.plot(x='月份', y=['营业收入', '营业成本', '净利润'],
        kind='line',           # 折线图
        figsize=(12, 6),       # 画布大小
        marker='o',            # 数据点标记
        linewidth=2,           # 线条粗细
        title='月度财务数据趋势')  # 标题

plt.ylabel('金额（万元）')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============ 2. 多种图表类型对比 ============
print("\n" + "=" * 50)
print("示例 2：DataFrame 多种图表类型")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 折线图
df.plot(x='月份', y=['营业收入', '净利润'], kind='line',
        ax=axes[0, 0], marker='o', title='折线图')
axes[0, 0].set_ylabel('金额（万元）')
axes[0, 0].grid(True, alpha=0.3)

# 柱状图
df.plot(x='月份', y=['营业收入', '营业成本'], kind='bar',
        ax=axes[0, 1], title='柱状图', alpha=0.8)
axes[0, 1].set_ylabel('金额（万元）')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# 面积图
df.plot(x='月份', y=['营业收入', '营业成本', '净利润'], kind='area',
        ax=axes[1, 0], title='面积图', alpha=0.6)
axes[1, 0].set_ylabel('金额（万元）')
axes[1, 0].grid(True, alpha=0.3)

# 饼图（只显示最后一个月的数据）
last_month = df.iloc[-1]  # 获取最后一行
last_month[['营业收入', '营业成本', '净利润']].plot(
    kind='pie', ax=axes[1, 1], autopct='%1.1f%%',
    title=f'{last_month["月份"]}收入结构', ylabel='')

plt.tight_layout()
plt.show()

# ============ 3. 分组数据可视化 ============
print("\n" + "=" * 50)
print("示例 3：分组数据可视化")
print("=" * 50)

# 创建多部门销售数据
sales_data = {
    '月份': ['1月', '2月', '3月', '4月', '5月', '6月'] * 3,
    '部门': ['销售部'] * 6 + ['市场部'] * 6 + ['技术部'] * 6,
    '业绩': [120, 135, 128, 145, 152, 160,
            80, 88, 92, 95, 100, 105,
            50, 55, 58, 62, 65, 70]
}
df_sales = pd.DataFrame(sales_data)

print("数据预览：")
print(df_sales.head(10))

# 使用 pivot() 重塑数据：行=月份，列=部门，值=业绩
# pivot() 将长格式数据转换为宽格式（透视表）
df_pivot = df_sales.pivot(index='月份', columns='部门', values='业绩')

print("\n透视后的数据：")
print(df_pivot)

# 绘制分组柱状图
df_pivot.plot(kind='bar', figsize=(12, 6), width=0.8, alpha=0.8)
plt.title('各部门月度业绩对比', fontsize=14, fontweight='bold')
plt.xlabel('月份')
plt.ylabel('业绩（万元）')
plt.xticks(rotation=0)  # 旋转 x 轴标签（0度=水平）
plt.legend(title='部门', fontsize=11)
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ============ 4. 时间序列数据可视化 ============
print("\n" + "=" * 50)
print("示例 4：时间序列数据可视化")
print("=" * 50)

# 创建时间序列数据
# pd.date_range() 生成日期范围
dates = pd.date_range('2024-01-01', periods=180, freq='D')  # 180天，每天一个数据点

# 生成模拟股价数据
np.random.seed(42)
price = 100 + np.cumsum(np.random.randn(180) * 2)  # 累积随机游走

df_stock = pd.DataFrame({
    '日期': dates,
    '收盘价': price
})

# 设置日期为索引（时间序列分析的标准做法）
df_stock.set_index('日期', inplace=True)

print("数据预览：")
print(df_stock.head())

# 计算移动平均线（技术分析常用指标）
# rolling(window).mean() 计算滚动窗口平均值
df_stock['MA5'] = df_stock['收盘价'].rolling(window=5).mean()   # 5日均线
df_stock['MA20'] = df_stock['收盘价'].rolling(window=20).mean()  # 20日均线

# 绘制时间序列图
fig, ax = plt.subplots(figsize=(14, 6))

df_stock['收盘价'].plot(ax=ax, label='收盘价', linewidth=1.5, color='#2E86AB')
df_stock['MA5'].plot(ax=ax, label='5日均线', linewidth=2, color='#F18F01', linestyle='--')
df_stock['MA20'].plot(ax=ax, label='20日均线', linewidth=2, color='#D62246', linestyle='--')

plt.title('股价走势与移动平均线', fontsize=14, fontweight='bold')
plt.xlabel('日期')
plt.ylabel('价格（元）')
plt.legend(fontsize=11)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============ 5. 相关性矩阵热力图 ============
print("\n" + "=" * 50)
print("示例 5：相关性矩阵热力图")
print("=" * 50)

# 创建多指标财务数据
np.random.seed(42)
n = 100
financial_data = pd.DataFrame({
    '营业收入': np.random.normal(500, 100, n),
    '净利润': np.random.normal(100, 20, n),
    '总资产': np.random.normal(2000, 400, n),
    '净资产': np.random.normal(1000, 200, n),
    '现金流': np.random.normal(80, 15, n)
})

# 添加一些相关性
financial_data['净利润'] = financial_data['营业收入'] * 0.2 + np.random.normal(0, 10, n)
financial_data['现金流'] = financial_data['净利润'] * 0.8 + np.random.normal(0, 5, n)

print("数据预览：")
print(financial_data.head())

# 计算相关性矩阵
# corr() 计算 DataFrame 各列之间的相关系数
corr_matrix = financial_data.corr()

print("\n相关性矩阵：")
print(corr_matrix)

# 绘制热力图
fig, ax = plt.subplots(figsize=(10, 8))

# 使用 imshow 显示矩阵
im = ax.imshow(corr_matrix, cmap='coolwarm', vmin=-1, vmax=1)

# 设置刻度标签
ax.set_xticks(range(len(corr_matrix.columns)))
ax.set_yticks(range(len(corr_matrix.columns)))
ax.set_xticklabels(corr_matrix.columns, rotation=45, ha='right')
ax.set_yticklabels(corr_matrix.columns)

# 在每个格子中显示数值
for i in range(len(corr_matrix)):
    for j in range(len(corr_matrix)):
        text = ax.text(j, i, f'{corr_matrix.iloc[i, j]:.2f}',
                      ha='center', va='center', color='black', fontsize=11)

plt.colorbar(im, ax=ax, label='相关系数')
plt.title('财务指标相关性热力图', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

# ============ 6. 数据聚合与可视化 ============
print("\n" + "=" * 50)
print("示例 6：数据聚合与可视化")
print("=" * 50)

# 创建详细交易数据
transaction_data = {
    '日期': pd.date_range('2024-01-01', periods=90, freq='D'),
    '产品': np.random.choice(['产品A', '产品B', '产品C'], 90),
    '销售额': np.random.randint(1000, 5000, 90),
    '数量': np.random.randint(10, 100, 90)
}
df_trans = pd.DataFrame(transaction_data)

print("原始数据预览：")
print(df_trans.head())

# 按产品分组，计算总销售额
# groupby() 分组，sum() 求和
sales_by_product = df_trans.groupby('产品')['销售额'].sum().sort_values(ascending=False)

print("\n各产品总销售额：")
print(sales_by_product)

# 绘制水平柱状图
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# 子图 1：总销售额
sales_by_product.plot(kind='barh', ax=ax1, color='#2E86AB', alpha=0.8)
ax1.set_title('各产品总销售额', fontsize=13, fontweight='bold')
ax1.set_xlabel('销售额（元）')
ax1.grid(True, alpha=0.3, axis='x')

# 在柱子右侧显示数值
for i, v in enumerate(sales_by_product):
    ax1.text(v + 5000, i, f'{v:,}', va='center', fontsize=10)

# 子图 2：按月统计销售趋势
df_trans['月份'] = df_trans['日期'].dt.to_period('M')  # 提取月份
monthly_sales = df_trans.groupby(['月份', '产品'])['销售额'].sum().unstack()

monthly_sales.plot(kind='line', ax=ax2, marker='o', linewidth=2)
ax2.set_title('各产品月度销售趋势', fontsize=13, fontweight='bold')
ax2.set_xlabel('月份')
ax2.set_ylabel('销售额（元）')
ax2.legend(title='产品', fontsize=10)
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("Pandas + Matplotlib 联合教学完成！")
print("=" * 50)
print("\n【必须掌握的 Pandas 绘图方法】：")
print("1. df.plot() - DataFrame 直接绘图")
print("2. df.plot(kind='bar') - 指定图表类型")
print("3. df.pivot() - 数据透视（重塑数据）")
print("4. df.groupby() - 数据分组聚合")
print("5. df.corr() - 计算相关性矩阵")
print("6. df.rolling() - 滚动窗口计算")
print("\n【Pandas 绘图优势】：")
print("- 自动处理索引和列名")
print("- 自动生成图例")
print("- 支持链式调用")
print("- 代码更简洁")
