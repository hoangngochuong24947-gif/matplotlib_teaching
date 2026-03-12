"""
第一层：基础语法教学 - 基本绘图
学习目标：掌握 matplotlib 的核心绘图语法和基本图表类型
知识点分类：【必须背诵】
"""

# 导入 matplotlib 的绘图模块
# pyplot 是 matplotlib 最常用的接口，提供类似 MATLAB 的绘图风格
import matplotlib.pyplot as plt
# numpy 用于生成数据，是数据分析的基础库
import numpy as np

# ============ 1. 最简单的折线图 ============
print("=" * 50)
print("示例 1：最简单的折线图")
print("=" * 50)

# 准备数据：x 轴数据（横坐标）
x = [1, 2, 3, 4, 5]
# 准备数据：y 轴数据（纵坐标）
y = [2, 4, 6, 8, 10]

# plt.plot() 是绘制折线图的核心函数
# 语法：plt.plot(x轴数据, y轴数据)
plt.plot(x, y)

# plt.title() 设置图表标题
# 参数 fontsize 控制字体大小
plt.title('My First Line Chart', fontsize=14)

# plt.xlabel() 设置 x 轴标签
plt.xlabel('X Axis')

# plt.ylabel() 设置 y 轴标签
plt.ylabel('Y Axis')

# plt.show() 显示图表（必须调用，否则图表不会显示）
plt.show()

# ============ 2. 带样式的折线图 ============
print("\n" + "=" * 50)
print("示例 2：带样式的折线图")
print("=" * 50)

# 使用 numpy 生成更多数据点
# np.linspace(起始值, 结束值, 数据点数量) 生成等间距数组
x = np.linspace(0, 10, 50)  # 从 0 到 10 生成 50 个点
y = np.sin(x)  # 计算正弦值

# 绘制折线图，添加样式参数
# 'b-' 表示蓝色实线（b=blue, -=实线）
# linewidth 控制线条粗细
# label 设置图例标签（用于 plt.legend()）
plt.plot(x, y, 'b-', linewidth=2, label='sin(x)')

# 添加第二条曲线
y2 = np.cos(x)
# 'r--' 表示红色虚线（r=red, --=虚线）
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')

plt.title('Sine and Cosine Curves', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')

# plt.legend() 显示图例（根据 label 参数生成）
plt.legend()

# plt.grid() 显示网格线，方便读数
# alpha 控制透明度（0-1，0 完全透明，1 完全不透明）
plt.grid(True, alpha=0.3)

plt.show()

# ============ 3. 散点图 ============
print("\n" + "=" * 50)
print("示例 3：散点图")
print("=" * 50)

# 生成随机数据
# np.random.randn() 生成符合标准正态分布的随机数
x = np.random.randn(50)
y = np.random.randn(50)

# plt.scatter() 绘制散点图
# s 控制点的大小
# c 控制点的颜色
# alpha 控制透明度
plt.scatter(x, y, s=100, c='green', alpha=0.6)

plt.title('Scatter Plot Example', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)
plt.show()

# ============ 4. 柱状图 ============
print("\n" + "=" * 50)
print("示例 4：柱状图（财务场景：月度收入）")
print("=" * 50)

# 财务数据：月份和收入
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
revenue = [45000, 52000, 48000, 61000, 58000, 67000]

# plt.bar() 绘制柱状图
# 参数：x 轴位置, 柱子高度, 颜色, 透明度
plt.bar(months, revenue, color='steelblue', alpha=0.7)

plt.title('Monthly Revenue (CNY)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Revenue (CNY)')

# 在柱子上方显示数值
# enumerate() 同时获取索引和值
for i, v in enumerate(revenue):
    # plt.text() 在指定位置添加文字
    # 参数：x坐标, y坐标, 文字内容, 对齐方式
    plt.text(i, v + 1000, str(v), ha='center', fontsize=10)

plt.grid(True, alpha=0.3, axis='y')  # 只显示 y 轴网格
plt.show()

# ============ 5. 饼图 ============
print("\n" + "=" * 50)
print("示例 5：饼图（财务场景：费用结构）")
print("=" * 50)

# 费用类别和金额
categories = ['Salary', 'Rent', 'Marketing', 'R&D', 'Others']
expenses = [120000, 45000, 30000, 50000, 15000]

# plt.pie() 绘制饼图
# autopct 显示百分比格式
# startangle 设置起始角度（逆时针）
# explode 设置某个扇区的突出距离
explode = (0.1, 0, 0, 0, 0)  # 突出第一个扇区（Salary）

plt.pie(expenses, labels=categories, autopct='%1.1f%%',
        startangle=90, explode=explode)

plt.title('Expense Structure', fontsize=14)
# plt.axis('equal') 确保饼图是圆形（不是椭圆）
plt.axis('equal')
plt.show()

# ============ 6. 子图布局 ============
print("\n" + "=" * 50)
print("示例 6：子图布局（一次显示多个图表）")
print("=" * 50)

# plt.figure() 创建画布
# figsize 设置画布大小（宽, 高），单位是英寸
plt.figure(figsize=(12, 8))

# plt.subplot(行数, 列数, 当前子图编号) 创建子图
# 2, 2, 1 表示 2x2 网格的第 1 个位置（左上）
plt.subplot(2, 2, 1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro-')
plt.title('Line Chart')

# 第 2 个子图（右上）
plt.subplot(2, 2, 2)
plt.bar(['A', 'B', 'C'], [10, 20, 15], color='orange')
plt.title('Bar Chart')

# 第 3 个子图（左下）
plt.subplot(2, 2, 3)
plt.scatter(np.random.rand(20), np.random.rand(20), s=100, c='purple', alpha=0.6)
plt.title('Scatter Plot')

# 第 4 个子图（右下）
plt.subplot(2, 2, 4)
plt.pie([30, 25, 20, 25], labels=['Q1', 'Q2', 'Q3', 'Q4'], autopct='%1.1f%%')
plt.title('Pie Chart')

# plt.tight_layout() 自动调整子图间距，避免重叠
plt.tight_layout()
plt.show()

print("\n" + "=" * 50)
print("基础绘图教学完成！")
print("=" * 50)
print("\n【必须背诵的核心函数】：")
print("1. plt.plot(x, y) - 折线图")
print("2. plt.scatter(x, y) - 散点图")
print("3. plt.bar(x, height) - 柱状图")
print("4. plt.pie(values, labels) - 饼图")
print("5. plt.title() / plt.xlabel() / plt.ylabel() - 标题和标签")
print("6. plt.legend() - 图例")
print("7. plt.show() - 显示图表")
print("8. plt.subplot() - 子图布局")
