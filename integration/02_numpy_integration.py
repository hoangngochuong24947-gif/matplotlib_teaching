"""
第二层：模块联合教学 - Matplotlib + NumPy 科学计算可视化
学习目标：掌握 NumPy 数组与 matplotlib 的高效集成
知识点分类：【熟悉掌握】
"""

import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ============ 1. NumPy 数组生成与绘图 ============
print("=" * 50)
print("示例 1：NumPy 数组生成方法")
print("=" * 50)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 方法 1：np.linspace() - 等间距数组（最常用）
# 语法：np.linspace(起始值, 结束值, 数据点数量)
x1 = np.linspace(0, 10, 100)  # 从0到10生成100个等间距点
y1 = np.sin(x1)
axes[0, 0].plot(x1, y1, 'b-', linewidth=2)
axes[0, 0].set_title('np.linspace() - 等间距数组', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('X')
axes[0, 0].set_ylabel('sin(X)')
axes[0, 0].grid(True, alpha=0.3)

# 方法 2：np.arange() - 步长数组
# 语法：np.arange(起始值, 结束值, 步长)
x2 = np.arange(0, 10, 0.1)  # 从0到10，步长0.1
y2 = np.cos(x2)
axes[0, 1].plot(x2, y2, 'r-', linewidth=2)
axes[0, 1].set_title('np.arange() - 步长数组', fontsize=12, fontweight='bold')
axes[0, 1].set_xlabel('X')
axes[0, 1].set_ylabel('cos(X)')
axes[0, 1].grid(True, alpha=0.3)

# 方法 3：np.random - 随机数组
# np.random.randn() 生成标准正态分布随机数
x3 = np.random.randn(1000)
axes[1, 0].hist(x3, bins=30, color='green', alpha=0.7, edgecolor='black')
axes[1, 0].set_title('np.random.randn() - 正态分布随机数', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('值')
axes[1, 0].set_ylabel('频数')
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 方法 4：np.logspace() - 对数间距数组
# 语法：np.logspace(起始指数, 结束指数, 数据点数量)
x4 = np.logspace(0, 3, 50)  # 10^0 到 10^3，50个点
y4 = np.log10(x4)
axes[1, 1].plot(x4, y4, 'o-', linewidth=2, markersize=4, color='purple')
axes[1, 1].set_title('np.logspace() - 对数间距数组', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('X (对数刻度)')
axes[1, 1].set_ylabel('log10(X)')
axes[1, 1].set_xscale('log')  # X轴使用对数刻度
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============ 2. NumPy 数学运算与可视化 ============
print("\n" + "=" * 50)
print("示例 2：NumPy 数学运算")
print("=" * 50)

x = np.linspace(0, 2 * np.pi, 200)

fig, axes = plt.subplots(2, 3, figsize=(15, 8))

# 三角函数
axes[0, 0].plot(x, np.sin(x), 'b-', linewidth=2)
axes[0, 0].set_title('sin(x)', fontweight='bold')
axes[0, 0].grid(True, alpha=0.3)

axes[0, 1].plot(x, np.cos(x), 'r-', linewidth=2)
axes[0, 1].set_title('cos(x)', fontweight='bold')
axes[0, 1].grid(True, alpha=0.3)

axes[0, 2].plot(x, np.tan(x), 'g-', linewidth=2)
axes[0, 2].set_ylim(-5, 5)  # 限制Y轴范围（tan函数有渐近线）
axes[0, 2].set_title('tan(x)', fontweight='bold')
axes[0, 2].grid(True, alpha=0.3)

# 指数和对数函数
x_exp = np.linspace(0, 3, 100)
axes[1, 0].plot(x_exp, np.exp(x_exp), 'b-', linewidth=2)
axes[1, 0].set_title('exp(x)', fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

x_log = np.linspace(0.1, 10, 100)
axes[1, 1].plot(x_log, np.log(x_log), 'r-', linewidth=2)
axes[1, 1].set_title('log(x)', fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

# 幂函数
x_pow = np.linspace(0, 5, 100)
axes[1, 2].plot(x_pow, x_pow**2, label='x²', linewidth=2)
axes[1, 2].plot(x_pow, x_pow**3, label='x³', linewidth=2)
axes[1, 2].plot(x_pow, np.sqrt(x_pow), label='√x', linewidth=2)
axes[1, 2].set_title('幂函数', fontweight='bold')
axes[1, 2].legend()
axes[1, 2].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============ 3. NumPy 统计函数与可视化 ============
print("\n" + "=" * 50)
print("示例 3：NumPy 统计分析")
print("=" * 50)

# 生成模拟数据：两组学生成绩
np.random.seed(42)
class_a = np.random.normal(75, 10, 100)  # 均值75，标准差10
class_b = np.random.normal(70, 15, 100)  # 均值70，标准差15

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 子图 1：直方图对比
axes[0, 0].hist(class_a, bins=20, alpha=0.6, label='A班', color='blue', edgecolor='black')
axes[0, 0].hist(class_b, bins=20, alpha=0.6, label='B班', color='red', edgecolor='black')
axes[0, 0].set_title('成绩分布对比', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('成绩')
axes[0, 0].set_ylabel('人数')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3, axis='y')

# 子图 2：箱线图对比
axes[0, 1].boxplot([class_a, class_b], labels=['A班', 'B班'], patch_artist=True)
axes[0, 1].set_title('成绩分布箱线图', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('成绩')
axes[0, 1].grid(True, alpha=0.3, axis='y')

# 子图 3：统计指标对比
stats_labels = ['均值', '中位数', '标准差', '最大值', '最小值']
class_a_stats = [
    np.mean(class_a),      # 均值
    np.median(class_a),    # 中位数
    np.std(class_a),       # 标准差
    np.max(class_a),       # 最大值
    np.min(class_a)        # 最小值
]
class_b_stats = [
    np.mean(class_b),
    np.median(class_b),
    np.std(class_b),
    np.max(class_b),
    np.min(class_b)
]

x = np.arange(len(stats_labels))
width = 0.35
axes[1, 0].bar(x - width/2, class_a_stats, width, label='A班', alpha=0.8)
axes[1, 0].bar(x + width/2, class_b_stats, width, label='B班', alpha=0.8)
axes[1, 0].set_title('统计指标对比', fontsize=12, fontweight='bold')
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(stats_labels)
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3, axis='y')

# 子图 4：累积分布函数（CDF）
# np.sort() 排序，用于绘制CDF
sorted_a = np.sort(class_a)
sorted_b = np.sort(class_b)
cdf_a = np.arange(1, len(sorted_a) + 1) / len(sorted_a)
cdf_b = np.arange(1, len(sorted_b) + 1) / len(sorted_b)

axes[1, 1].plot(sorted_a, cdf_a, label='A班', linewidth=2)
axes[1, 1].plot(sorted_b, cdf_b, label='B班', linewidth=2)
axes[1, 1].set_title('累积分布函数（CDF）', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('成绩')
axes[1, 1].set_ylabel('累积概率')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nA班统计：")
print(f"均值: {np.mean(class_a):.2f}")
print(f"中位数: {np.median(class_a):.2f}")
print(f"标准差: {np.std(class_a):.2f}")
print(f"最大值: {np.max(class_a):.2f}")
print(f"最小值: {np.min(class_a):.2f}")

# ============ 4. NumPy 数组操作与可视化 ============
print("\n" + "=" * 50)
print("示例 4：NumPy 数组操作")
print("=" * 50)

# 生成原始数据
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.randn(100) * 0.2  # 带噪声的正弦波

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 子图 1：原始数据
axes[0, 0].plot(x, y, 'o', markersize=3, alpha=0.5, label='原始数据')
axes[0, 0].set_title('原始数据（带噪声）', fontsize=12, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# 子图 2：移动平均平滑（使用 np.convolve）
# np.convolve() 卷积运算，用于移动平均
window_size = 10
window = np.ones(window_size) / window_size  # 平均窗口
y_smooth = np.convolve(y, window, mode='same')  # mode='same' 保持长度不变

axes[0, 1].plot(x, y, 'o', markersize=3, alpha=0.3, label='原始数据')
axes[0, 1].plot(x, y_smooth, 'r-', linewidth=2, label=f'{window_size}点移动平均')
axes[0, 1].set_title('移动平均平滑', fontsize=12, fontweight='bold')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# 子图 3：数组切片与索引
# 布尔索引：选择满足条件的数据
high_values = y > 0.5
low_values = y < -0.5
middle_values = ~(high_values | low_values)  # ~ 表示取反

axes[1, 0].plot(x[high_values], y[high_values], 'ro', label='高值 (>0.5)', markersize=5)
axes[1, 0].plot(x[low_values], y[low_values], 'bo', label='低值 (<-0.5)', markersize=5)
axes[1, 0].plot(x[middle_values], y[middle_values], 'go', label='中间值', markersize=3, alpha=0.5)
axes[1, 0].set_title('布尔索引分类', fontsize=12, fontweight='bold')
axes[1, 0].legend()
axes[1, 0].grid(True, alpha=0.3)

# 子图 4：数组运算（向量化）
# NumPy 数组支持向量化运算，无需循环
y_squared = y ** 2  # 平方
y_abs = np.abs(y)   # 绝对值
y_cumsum = np.cumsum(y)  # 累积和

axes[1, 1].plot(x, y, label='原始', linewidth=2)
axes[1, 1].plot(x, y_abs, label='绝对值', linewidth=2)
axes[1, 1].set_title('数组运算', fontsize=12, fontweight='bold')
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# ============ 5. 财务场景：投资回报率计算 ============
print("\n" + "=" * 50)
print("示例 5：财务场景 - 投资回报率计算")
print("=" * 50)

# 投资参数
initial_investment = 100000  # 初始投资
annual_return = 0.08         # 年化收益率
years = 20                   # 投资年限

# 使用 NumPy 计算复利增长
time = np.arange(0, years + 1)
# 复利公式：FV = PV * (1 + r)^t
future_value = initial_investment * (1 + annual_return) ** time

# 计算每年的收益
annual_profit = np.diff(future_value)  # np.diff() 计算相邻元素差值
annual_profit = np.insert(annual_profit, 0, 0)  # 第一年收益为0

fig, axes = plt.subplots(2, 1, figsize=(12, 10))

# 子图 1：投资价值增长
axes[0].plot(time, future_value, 'o-', linewidth=2, markersize=6, color='#2E86AB')
axes[0].fill_between(time, future_value, alpha=0.3, color='#2E86AB')
axes[0].set_title(f'投资增长曲线（年化收益率 {annual_return*100}%）',
                  fontsize=14, fontweight='bold')
axes[0].set_xlabel('年份')
axes[0].set_ylabel('投资价值（元）')
axes[0].grid(True, alpha=0.3)

# 标注起点和终点
axes[0].text(0, initial_investment, f'初始: {initial_investment:,.0f}',
            ha='left', va='bottom', fontsize=10, fontweight='bold')
axes[0].text(years, future_value[-1], f'最终: {future_value[-1]:,.0f}',
            ha='right', va='bottom', fontsize=10, fontweight='bold')

# 子图 2：每年收益
axes[1].bar(time, annual_profit, color='#06A77D', alpha=0.8)
axes[1].set_title('每年收益', fontsize=14, fontweight='bold')
axes[1].set_xlabel('年份')
axes[1].set_ylabel('收益（元）')
axes[1].grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.show()

print(f"\n投资分析结果：")
print(f"初始投资: {initial_investment:,.0f} 元")
print(f"最终价值: {future_value[-1]:,.0f} 元")
print(f"总收益: {future_value[-1] - initial_investment:,.0f} 元")
print(f"总收益率: {(future_value[-1] / initial_investment - 1) * 100:.2f}%")

print("\n" + "=" * 50)
print("NumPy + Matplotlib 联合教学完成！")
print("=" * 50)
print("\n【必须掌握的 NumPy 函数】：")
print("1. np.linspace() - 等间距数组生成")
print("2. np.arange() - 步长数组生成")
print("3. np.random.randn() - 正态分布随机数")
print("4. np.mean() / np.median() / np.std() - 统计函数")
print("5. np.max() / np.min() - 最值")
print("6. np.sum() / np.cumsum() - 求和与累积和")
print("7. np.diff() - 差分（相邻元素差）")
print("8. np.convolve() - 卷积（移动平均）")
print("\n【NumPy 优势】：")
print("- 向量化运算（无需循环，速度快）")
print("- 丰富的数学函数")
print("- 与 matplotlib 无缝集成")
print("- 内存效率高")
