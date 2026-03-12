"""
第一层：基础语法教学 - 高级图表类型
学习目标：掌握直方图、箱线图、热力图等高级图表
知识点分类：【熟悉掌握】
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ============ 1. 直方图（Histogram）============
print("=" * 50)
print("示例 1：直方图 - 数据分布分析")
print("=" * 50)

# 生成符合正态分布的随机数据（模拟考试成绩）
# np.random.normal(均值, 标准差, 数据量)
scores = np.random.normal(75, 10, 1000)

plt.figure(figsize=(10, 6))

# plt.hist() 绘制直方图
# bins：柱子数量（分组数）
# edgecolor：柱子边框颜色
# alpha：透明度
plt.hist(scores, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

plt.title('学生成绩分布直方图', fontsize=14)
plt.xlabel('成绩')
plt.ylabel('人数')
plt.grid(True, alpha=0.3, axis='y')

# 添加均值线
mean_score = np.mean(scores)
plt.axvline(mean_score, color='red', linestyle='--', linewidth=2, label=f'平均分: {mean_score:.1f}')
plt.legend()

plt.show()

# ============ 2. 箱线图（Box Plot）============
print("\n" + "=" * 50)
print("示例 2：箱线图 - 数据分布和异常值检测")
print("=" * 50)

# 生成四个部门的销售数据
np.random.seed(42)
dept_a = np.random.normal(50000, 8000, 100)
dept_b = np.random.normal(60000, 12000, 100)
dept_c = np.random.normal(45000, 6000, 100)
dept_d = np.random.normal(70000, 15000, 100)

data = [dept_a, dept_b, dept_c, dept_d]
labels = ['部门A', '部门B', '部门C', '部门D']

plt.figure(figsize=(10, 6))

# plt.boxplot() 绘制箱线图
# 箱线图显示：最小值、下四分位数(Q1)、中位数(Q2)、上四分位数(Q3)、最大值
# patch_artist=True 允许填充颜色
box = plt.boxplot(data, labels=labels, patch_artist=True)

# 为箱子填充颜色
colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

plt.title('各部门月度销售额分布', fontsize=14)
plt.ylabel('销售额（元）')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

print("\n箱线图解读：")
print("- 箱子：包含 50% 的数据（Q1 到 Q3）")
print("- 箱子中的线：中位数")
print("- 须（whiskers）：延伸到 1.5 倍四分位距（IQR）")
print("- 圆点：异常值（超出须的范围）")

# ============ 3. 水平柱状图 ============
print("\n" + "=" * 50)
print("示例 3：水平柱状图 - 排名对比")
print("=" * 50)

# 产品销量数据
products = ['产品A', '产品B', '产品C', '产品D', '产品E']
sales = [23000, 45000, 18000, 67000, 34000]

# 按销量排序（从小到大）
sorted_indices = np.argsort(sales)
products_sorted = [products[i] for i in sorted_indices]
sales_sorted = [sales[i] for i in sorted_indices]

plt.figure(figsize=(10, 6))

# plt.barh() 绘制水平柱状图（h = horizontal）
# 颜色根据销量大小渐变
colors = plt.cm.viridis(np.linspace(0.3, 0.9, len(sales_sorted)))
plt.barh(products_sorted, sales_sorted, color=colors, alpha=0.8)

plt.title('产品销量排名', fontsize=14)
plt.xlabel('销量（件）')
plt.ylabel('产品')

# 在柱子右侧显示数值
for i, v in enumerate(sales_sorted):
    plt.text(v + 1000, i, f'{v:,}', va='center', fontsize=10)

plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()

# ============ 4. 堆叠柱状图 ============
print("\n" + "=" * 50)
print("示例 4：堆叠柱状图 - 成本结构分析")
print("=" * 50)

# 季度数据
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
# 各项成本
material_cost = [30000, 35000, 32000, 40000]
labor_cost = [25000, 28000, 27000, 30000]
overhead_cost = [15000, 16000, 14000, 18000]

x = np.arange(len(quarters))  # 柱子的位置
width = 0.6  # 柱子宽度

plt.figure(figsize=(10, 6))

# 堆叠柱状图：每次在前一个的基础上堆叠
# bottom 参数指定起始高度
plt.bar(x, material_cost, width, label='原材料成本', color='steelblue')
plt.bar(x, labor_cost, width, bottom=material_cost, label='人工成本', color='orange')

# 计算前两项的总和作为第三项的起始高度
bottom_sum = np.array(material_cost) + np.array(labor_cost)
plt.bar(x, overhead_cost, width, bottom=bottom_sum, label='管理费用', color='green')

plt.title('季度成本结构分析', fontsize=14)
plt.xlabel('季度')
plt.ylabel('成本（元）')
plt.xticks(x, quarters)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ============ 5. 分组柱状图 ============
print("\n" + "=" * 50)
print("示例 5：分组柱状图 - 多指标对比")
print("=" * 50)

# 三个城市的收入和支出数据
cities = ['北京', '上海', '深圳']
revenue = [120000, 150000, 135000]
expense = [80000, 95000, 88000]

x = np.arange(len(cities))
width = 0.35  # 柱子宽度

plt.figure(figsize=(10, 6))

# 绘制两组柱子，通过调整 x 坐标实现并排
# x - width/2：第一组柱子向左偏移
# x + width/2：第二组柱子向右偏移
plt.bar(x - width/2, revenue, width, label='收入', color='green', alpha=0.8)
plt.bar(x + width/2, expense, width, label='支出', color='red', alpha=0.8)

plt.title('各城市收支对比', fontsize=14)
plt.xlabel('城市')
plt.ylabel('金额（元）')
plt.xticks(x, cities)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.show()

# ============ 6. 面积图（Area Chart）============
print("\n" + "=" * 50)
print("示例 6：面积图 - 趋势累积展示")
print("=" * 50)

# 时间序列数据
months = np.arange(1, 13)
product_a = np.array([20, 25, 30, 28, 35, 40, 38, 45, 50, 48, 55, 60])
product_b = np.array([15, 18, 20, 22, 25, 28, 30, 32, 35, 38, 40, 45])
product_c = np.array([10, 12, 15, 18, 20, 22, 25, 28, 30, 32, 35, 38])

plt.figure(figsize=(12, 6))

# plt.fill_between() 绘制面积图
# 填充 x 轴到曲线之间的区域
plt.fill_between(months, 0, product_a, alpha=0.7, label='产品A')
plt.fill_between(months, product_a, product_a + product_b, alpha=0.7, label='产品B')
plt.fill_between(months, product_a + product_b, product_a + product_b + product_c,
                 alpha=0.7, label='产品C')

plt.title('产品销量趋势（堆叠面积图）', fontsize=14)
plt.xlabel('月份')
plt.ylabel('销量（千件）')
plt.xticks(months)
plt.legend(loc='upper left')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# ============ 7. 热力图（Heatmap）============
print("\n" + "=" * 50)
print("示例 7：热力图 - 相关性矩阵")
print("=" * 50)

# 生成相关性矩阵数据（模拟财务指标相关性）
np.random.seed(42)
indicators = ['营收', '利润', '现金流', '资产', '负债']
n = len(indicators)

# 生成对称的相关性矩阵
corr_matrix = np.random.rand(n, n)
corr_matrix = (corr_matrix + corr_matrix.T) / 2  # 对称化
np.fill_diagonal(corr_matrix, 1)  # 对角线为 1

plt.figure(figsize=(8, 6))

# plt.imshow() 显示矩阵为图像
# cmap：颜色映射（'coolwarm' 冷暖色调）
# vmin, vmax：颜色范围
im = plt.imshow(corr_matrix, cmap='coolwarm', vmin=0, vmax=1)

# 设置刻度标签
plt.xticks(range(n), indicators)
plt.yticks(range(n), indicators)

# 在每个格子中显示数值
for i in range(n):
    for j in range(n):
        text = plt.text(j, i, f'{corr_matrix[i, j]:.2f}',
                       ha='center', va='center', color='black', fontsize=10)

# plt.colorbar() 添加颜色条
plt.colorbar(im, label='相关系数')
plt.title('财务指标相关性热力图', fontsize=14)
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("高级图表教学完成！")
print("=" * 50)
print("\n【必须背诵的高级图表函数】：")
print("1. plt.hist() - 直方图（数据分布）")
print("2. plt.boxplot() - 箱线图（分布和异常值）")
print("3. plt.barh() - 水平柱状图")
print("4. plt.bar() + bottom 参数 - 堆叠柱状图")
print("5. plt.fill_between() - 面积图")
print("6. plt.imshow() - 热力图")
print("\n【图表选择建议】：")
print("- 数据分布 → 直方图、箱线图")
print("- 排名对比 → 水平柱状图")
print("- 成分结构 → 堆叠柱状图、饼图")
print("- 趋势变化 → 折线图、面积图")
print("- 相关性分析 → 热力图、散点图")
