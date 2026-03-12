"""
第一层：基础语法教学 - 图表美化与定制
学习目标：掌握颜色、样式、字体、坐标轴等定制技巧
知识点分类：【熟悉掌握】
"""

import matplotlib.pyplot as plt
import numpy as np

# ============ 1. 颜色系统 ============
print("=" * 50)
print("示例 1：颜色系统")
print("=" * 50)

x = np.linspace(0, 10, 100)

plt.figure(figsize=(12, 6))

# 方式 1：单字母颜色代码
# 'r'=red, 'g'=green, 'b'=blue, 'c'=cyan, 'm'=magenta, 'y'=yellow, 'k'=black, 'w'=white
plt.plot(x, np.sin(x), 'r-', label='Red (r)')

# 方式 2：颜色名称（英文）
plt.plot(x, np.sin(x) + 1, color='orange', label='Orange (name)')

# 方式 3：十六进制颜色代码（网页颜色）
plt.plot(x, np.sin(x) + 2, color='#1f77b4', label='Hex Color')

# 方式 4：RGB 元组（0-1 范围）
plt.plot(x, np.sin(x) + 3, color=(0.2, 0.8, 0.2), label='RGB Tuple')

plt.title('Color System in Matplotlib', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ============ 2. 线条样式 ============
print("\n" + "=" * 50)
print("示例 2：线条样式")
print("=" * 50)

x = np.linspace(0, 10, 50)

plt.figure(figsize=(12, 6))

# linestyle 参数控制线条样式
# '-' 实线, '--' 虚线, '-.' 点划线, ':' 点线
plt.plot(x, x, linestyle='-', linewidth=2, label='Solid (-)')
plt.plot(x, x + 5, linestyle='--', linewidth=2, label='Dashed (--)')
plt.plot(x, x + 10, linestyle='-.', linewidth=2, label='Dash-dot (-.)')
plt.plot(x, x + 15, linestyle=':', linewidth=3, label='Dotted (:)')

# 组合写法：颜色 + 标记 + 线型
# 'ro-' = red + circle marker + solid line
plt.plot(x, x + 20, 'go-', linewidth=2, markersize=8, label='Green circles')

plt.title('Line Styles', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# ============ 3. 标记样式 ============
print("\n" + "=" * 50)
print("示例 3：标记样式（数据点标记）")
print("=" * 50)

x = np.arange(0, 10, 1)

plt.figure(figsize=(12, 8))

# marker 参数控制数据点标记形状
# 'o' 圆圈, 's' 方块, '^' 上三角, 'v' 下三角, 'D' 菱形, '*' 星号, '+' 加号, 'x' 叉号
markers = ['o', 's', '^', 'v', 'D', '*', '+', 'x']
labels = ['Circle (o)', 'Square (s)', 'Triangle up (^)', 'Triangle down (v)',
          'Diamond (D)', 'Star (*)', 'Plus (+)', 'Cross (x)']

for i, (marker, label) in enumerate(zip(markers, labels)):
    plt.plot(x, x + i * 2, marker=marker, markersize=10,
             linewidth=2, label=label)

plt.title('Marker Styles', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend(loc='upper left')  # loc 控制图例位置
plt.grid(True, alpha=0.3)
plt.show()

# ============ 4. 坐标轴定制 ============
print("\n" + "=" * 50)
print("示例 4：坐标轴定制")
print("=" * 50)

x = np.linspace(0, 10, 100)
y = np.exp(x / 5)  # 指数增长

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)

# 设置坐标轴范围
# plt.xlim(最小值, 最大值) 设置 x 轴范围
plt.xlim(0, 10)
# plt.ylim(最小值, 最大值) 设置 y 轴范围
plt.ylim(0, 10)

# 设置坐标轴刻度
# plt.xticks(刻度位置列表, 刻度标签列表)
plt.xticks([0, 2, 4, 6, 8, 10], ['Zero', 'Two', 'Four', 'Six', 'Eight', 'Ten'])

# 设置 y 轴刻度（只设置位置，不改标签）
plt.yticks(np.arange(0, 11, 2))

plt.title('Axis Customization', fontsize=14)
plt.xlabel('X Axis', fontsize=12)
plt.ylabel('Y Axis', fontsize=12)
plt.grid(True, alpha=0.3)
plt.show()

# ============ 5. 中文字体设置 ============
print("\n" + "=" * 50)
print("示例 5：中文字体设置（重要！）")
print("=" * 50)

# 方式 1：使用 rcParams 全局设置（推荐）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 财务数据示例
months = ['1月', '2月', '3月', '4月', '5月', '6月']
revenue = [45000, 52000, 48000, 61000, 58000, 67000]
profit = [12000, 15000, 13000, 18000, 17000, 21000]

plt.figure(figsize=(10, 6))

# 绘制双折线图
plt.plot(months, revenue, 'o-', linewidth=2, markersize=8, label='营业收入')
plt.plot(months, profit, 's-', linewidth=2, markersize=8, label='净利润')

plt.title('2024年上半年财务数据', fontsize=16, fontweight='bold')
plt.xlabel('月份', fontsize=12)
plt.ylabel('金额（元）', fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)

# 在数据点上显示数值
for i, (r, p) in enumerate(zip(revenue, profit)):
    plt.text(i, r + 2000, f'{r:,}', ha='center', fontsize=9)
    plt.text(i, p - 3000, f'{p:,}', ha='center', fontsize=9, color='red')

plt.tight_layout()
plt.show()

# ============ 6. 图表样式主题 ============
print("\n" + "=" * 50)
print("示例 6：图表样式主题")
print("=" * 50)

# matplotlib 内置多种样式主题
# 查看所有可用样式
print("可用样式主题：", plt.style.available)

# 使用样式主题
# 常用主题：'ggplot', 'seaborn', 'bmh', 'fivethirtyeight', 'dark_background'
plt.style.use('ggplot')

x = np.linspace(0, 10, 100)
plt.figure(figsize=(10, 6))

plt.plot(x, np.sin(x), label='sin(x)', linewidth=2)
plt.plot(x, np.cos(x), label='cos(x)', linewidth=2)

plt.title('Using ggplot Style', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()

# 恢复默认样式
plt.style.use('default')

# ============ 7. 图表保存 ============
print("\n" + "=" * 50)
print("示例 7：图表保存")
print("=" * 50)

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2)
plt.title('Save Figure Example', fontsize=14)
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True, alpha=0.3)

# plt.savefig() 保存图表
# 参数说明：
# - 文件名（支持 .png, .jpg, .pdf, .svg 等格式）
# - dpi：分辨率（dots per inch），默认 100，建议 300 用于打印
# - bbox_inches='tight'：自动裁剪空白边缘
# - transparent=True：透明背景
plt.savefig('my_chart.png', dpi=300, bbox_inches='tight')
print("图表已保存为 my_chart.png")

plt.show()

print("\n" + "=" * 50)
print("图表定制教学完成！")
print("=" * 50)
print("\n【必须背诵的定制参数】：")
print("1. color / c - 颜色")
print("2. linestyle / ls - 线条样式 (-, --, -., :)")
print("3. linewidth / lw - 线条粗细")
print("4. marker - 标记样式 (o, s, ^, v, D, *, +, x)")
print("5. markersize / ms - 标记大小")
print("6. alpha - 透明度 (0-1)")
print("7. label - 图例标签")
print("8. plt.xlim() / plt.ylim() - 坐标轴范围")
print("9. plt.xticks() / plt.yticks() - 坐标轴刻度")
print("10. plt.savefig() - 保存图表")
print("\n【中文显示必备设置】：")
print("plt.rcParams['font.sans-serif'] = ['SimHei']")
print("plt.rcParams['axes.unicode_minus'] = False")
