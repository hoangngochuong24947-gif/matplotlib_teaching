"""
第三层：高级功能教学 - 3D 图表与高级布局
学习目标：掌握 matplotlib 的 3D 绘图和复杂布局
知识点分类：【了解即可】
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D  # 3D 绘图工具

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ============ 1. 3D 折线图 ============
print("=" * 50)
print("示例 1：3D 折线图")
print("=" * 50)

# 创建 3D 图表
# projection='3d' 指定为 3D 坐标系
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 生成 3D 螺旋线数据
t = np.linspace(0, 10, 1000)
x = np.sin(t)
y = np.cos(t)
z = t

# 绘制 3D 折线
# ax.plot() 在 3D 坐标系中绘制折线
ax.plot(x, y, z, linewidth=2, color='#2E86AB')

ax.set_title('3D 螺旋线', fontsize=14, fontweight='bold')
ax.set_xlabel('X 轴')
ax.set_ylabel('Y 轴')
ax.set_zlabel('Z 轴')  # 3D 图表特有的 Z 轴标签

plt.show()

# ============ 2. 3D 散点图 ============
print("\n" + "=" * 50)
print("示例 2：3D 散点图")
print("=" * 50)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 生成随机 3D 数据（模拟三个财务指标）
np.random.seed(42)
n = 100
revenue = np.random.normal(500, 100, n)      # 营业收入
profit = revenue * 0.2 + np.random.randn(n) * 20  # 净利润
cash_flow = profit * 0.9 + np.random.randn(n) * 15  # 现金流

# 绘制 3D 散点图
# c 参数可以根据第四个维度设置颜色
# s 参数控制点的大小
scatter = ax.scatter(revenue, profit, cash_flow,
                     c=cash_flow,  # 颜色映射到现金流
                     s=50,
                     cmap='viridis',  # 颜色映射方案
                     alpha=0.6)

ax.set_title('财务指标 3D 散点图', fontsize=14, fontweight='bold')
ax.set_xlabel('营业收入（万元）')
ax.set_ylabel('净利润（万元）')
ax.set_zlabel('现金流（万元）')

# 添加颜色条
plt.colorbar(scatter, ax=ax, label='现金流（万元）')

plt.show()

# ============ 3. 3D 曲面图 ============
print("\n" + "=" * 50)
print("示例 3：3D 曲面图")
print("=" * 50)

fig = plt.figure(figsize=(14, 10))

# 子图 1：基本曲面
ax1 = fig.add_subplot(221, projection='3d')

# 创建网格数据
# np.meshgrid() 生成二维网格坐标矩阵
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))  # 计算 Z 值

# plot_surface() 绘制 3D 曲面
# cmap 设置颜色映射
surf1 = ax1.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax1.set_title('基本曲面', fontsize=12, fontweight='bold')
ax1.set_xlabel('X')
ax1.set_ylabel('Y')
ax1.set_zlabel('Z')
fig.colorbar(surf1, ax=ax1, shrink=0.5)

# 子图 2：等高线投影
ax2 = fig.add_subplot(222, projection='3d')
surf2 = ax2.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.7)
# contour() 在底部绘制等高线
ax2.contour(X, Y, Z, zdir='z', offset=-1, cmap='coolwarm')
ax2.set_title('曲面 + 等高线投影', fontsize=12, fontweight='bold')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_zlabel('Z')
ax2.set_zlim(-1, 1)

# 子图 3：线框图
ax3 = fig.add_subplot(223, projection='3d')
# plot_wireframe() 绘制线框图
ax3.plot_wireframe(X, Y, Z, color='blue', linewidth=0.5)
ax3.set_title('线框图', fontsize=12, fontweight='bold')
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_zlabel('Z')

# 子图 4：财务场景 - 利润曲面
ax4 = fig.add_subplot(224, projection='3d')

# 模拟：利润 = f(价格, 销量)
price = np.linspace(50, 150, 50)
quantity = np.linspace(100, 500, 50)
Price, Quantity = np.meshgrid(price, quantity)
# 利润 = (价格 - 成本) * 销量
cost = 40
Profit = (Price - cost) * Quantity

surf4 = ax4.plot_surface(Price, Quantity, Profit, cmap='RdYlGn', alpha=0.8)
ax4.set_title('利润曲面（价格 × 销量）', fontsize=12, fontweight='bold')
ax4.set_xlabel('价格（元）')
ax4.set_ylabel('销量（件）')
ax4.set_zlabel('利润（元）')
fig.colorbar(surf4, ax=ax4, shrink=0.5)

plt.tight_layout()
plt.show()

# ============ 4. 3D 柱状图 ============
print("\n" + "=" * 50)
print("示例 4：3D 柱状图")
print("=" * 50)

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# 数据：三个产品在四个季度的销售额
products = ['产品A', '产品B', '产品C']
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
sales_data = np.array([
    [120, 135, 128, 145],  # 产品A
    [80, 88, 92, 95],      # 产品B
    [50, 55, 58, 62]       # 产品C
])

# 设置柱子位置
x_pos = np.arange(len(quarters))
y_pos = np.arange(len(products))

# 为每个产品绘制柱状图
colors = ['#2E86AB', '#06A77D', '#F18F01']
for i, (product, color) in enumerate(zip(products, colors)):
    # bar3d(x位置, y位置, z起点, x宽度, y宽度, z高度)
    ax.bar3d(x_pos, [i] * len(quarters), np.zeros(len(quarters)),
             0.6, 0.6, sales_data[i],
             color=color, alpha=0.8, label=product)

ax.set_title('产品季度销售额 3D 柱状图', fontsize=14, fontweight='bold')
ax.set_xlabel('季度')
ax.set_ylabel('产品')
ax.set_zlabel('销售额（万元）')
ax.set_xticks(x_pos)
ax.set_xticklabels(quarters)
ax.set_yticks(y_pos)
ax.set_yticklabels(products)
ax.legend()

plt.show()

# ============ 5. 高级布局：GridSpec ============
print("\n" + "=" * 50)
print("示例 5：高级布局 - GridSpec")
print("=" * 50)

# GridSpec 允许创建不规则的子图布局
from matplotlib.gridspec import GridSpec

fig = plt.figure(figsize=(14, 10))
# 创建 3x3 网格
gs = GridSpec(3, 3, figure=fig, hspace=0.3, wspace=0.3)

# 大图：占据前两行
ax_main = fig.add_subplot(gs[0:2, :])
months = ['1月', '2月', '3月', '4月', '5月', '6月']
revenue = [450, 520, 480, 610, 580, 670]
ax_main.plot(months, revenue, 'o-', linewidth=2, markersize=8, color='#2E86AB')
ax_main.fill_between(range(len(months)), revenue, alpha=0.3, color='#2E86AB')
ax_main.set_title('主图：营业收入趋势', fontsize=14, fontweight='bold')
ax_main.set_ylabel('金额（万元）')
ax_main.grid(True, alpha=0.3)

# 小图 1：左下
ax1 = fig.add_subplot(gs[2, 0])
ax1.bar(['A', 'B', 'C'], [120, 80, 50], color='#06A77D', alpha=0.8)
ax1.set_title('产品销量', fontsize=11)
ax1.grid(True, alpha=0.3, axis='y')

# 小图 2：中下
ax2 = fig.add_subplot(gs[2, 1])
ax2.pie([60, 25, 15], labels=['成本', '利润', '税费'], autopct='%1.1f%%')
ax2.set_title('成本结构', fontsize=11)

# 小图 3：右下
ax3 = fig.add_subplot(gs[2, 2])
data = np.random.randn(100)
ax3.hist(data, bins=20, color='#F18F01', alpha=0.7, edgecolor='black')
ax3.set_title('数据分布', fontsize=11)
ax3.grid(True, alpha=0.3, axis='y')

plt.suptitle('高级布局示例：不规则子图', fontsize=16, fontweight='bold', y=0.98)
plt.show()

# ============ 6. 嵌套子图 ============
print("\n" + "=" * 50)
print("示例 6：嵌套子图（图中图）")
print("=" * 50)

fig, ax = plt.subplots(figsize=(12, 8))

# 主图
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax.plot(x, y, 'b-', linewidth=2)
ax.set_title('主图：正弦波', fontsize=14, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True, alpha=0.3)

# 创建嵌套子图（图中图）
# fig.add_axes([左, 下, 宽, 高]) 参数是相对于整个图表的比例（0-1）
ax_inset = fig.add_axes([0.55, 0.55, 0.3, 0.3])  # 右上角
x_zoom = np.linspace(1.5, 2.5, 50)
y_zoom = np.sin(x_zoom)
ax_inset.plot(x_zoom, y_zoom, 'r-', linewidth=2)
ax_inset.set_title('局部放大', fontsize=10)
ax_inset.grid(True, alpha=0.3)

# 在主图上标记放大区域
ax.axvspan(1.5, 2.5, alpha=0.2, color='red')  # 垂直阴影区域
ax.text(2, -0.5, '放大区域', ha='center', fontsize=10, color='red')

plt.show()

print("\n" + "=" * 50)
print("3D 图表与高级布局教学完成！")
print("=" * 50)
print("\n【3D 绘图函数】：")
print("1. ax.plot() - 3D 折线图")
print("2. ax.scatter() - 3D 散点图")
print("3. ax.plot_surface() - 3D 曲面图")
print("4. ax.plot_wireframe() - 3D 线框图")
print("5. ax.bar3d() - 3D 柱状图")
print("6. ax.contour() - 等高线图")
print("\n【高级布局】：")
print("1. GridSpec - 不规则网格布局")
print("2. fig.add_axes() - 嵌套子图（图中图）")
print("3. plt.subplot() - 规则网格布局")
print("\n【3D 图表应用场景】：")
print("- 多变量关系可视化")
print("- 曲面拟合展示")
print("- 地形数据可视化")
print("- 财务模型参数敏感性分析")
