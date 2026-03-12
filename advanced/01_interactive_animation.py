"""
第三层：高级功能教学 - 交互式图表与动画
学习目标：掌握 matplotlib 的交互式功能和动画制作
知识点分类：【了解即可】
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, Button

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# ============ 1. 交互式滑块控制 ============
print("=" * 50)
print("示例 1：交互式滑块控制图表参数")
print("=" * 50)

# 创建初始数据
x = np.linspace(0, 10, 1000)
freq_init = 1.0  # 初始频率
amp_init = 1.0   # 初始振幅

# 创建图表
fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(bottom=0.25)  # 为滑块留出空间

# 绘制初始曲线
line, = ax.plot(x, amp_init * np.sin(2 * np.pi * freq_init * x), linewidth=2)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('交互式正弦波（拖动滑块改变参数）', fontsize=14, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True, alpha=0.3)

# 创建频率滑块
# plt.axes([左, 下, 宽, 高]) 创建滑块位置
ax_freq = plt.axes([0.15, 0.1, 0.7, 0.03])
# Slider(位置, 标签, 最小值, 最大值, 初始值)
slider_freq = Slider(ax_freq, '频率', 0.1, 5.0, valinit=freq_init)

# 创建振幅滑块
ax_amp = plt.axes([0.15, 0.05, 0.7, 0.03])
slider_amp = Slider(ax_amp, '振幅', 0.1, 2.0, valinit=amp_init)

# 定义更新函数（当滑块改变时调用）
def update(val):
    freq = slider_freq.val  # 获取当前频率值
    amp = slider_amp.val    # 获取当前振幅值
    # 更新曲线数据
    line.set_ydata(amp * np.sin(2 * np.pi * freq * x))
    fig.canvas.draw_idle()  # 重绘图表

# 绑定滑块事件
slider_freq.on_changed(update)
slider_amp.on_changed(update)

print("提示：拖动滑块可以实时改变正弦波的频率和振幅")
print("关闭窗口继续下一个示例")
plt.show()

# ============ 2. 交互式按钮控制 ============
print("\n" + "=" * 50)
print("示例 2：交互式按钮控制")
print("=" * 50)

# 创建数据
x = np.linspace(0, 10, 100)
functions = {
    'sin': np.sin,
    'cos': np.cos,
    'tan': lambda x: np.clip(np.tan(x), -5, 5)  # 限制tan值范围
}
current_func = 'sin'

# 创建图表
fig, ax = plt.subplots(figsize=(12, 8))
plt.subplots_adjust(bottom=0.2)

line, = ax.plot(x, functions[current_func](x), linewidth=2, label=current_func)
ax.set_xlim(0, 10)
ax.set_ylim(-2, 2)
ax.set_title('交互式函数切换（点击按钮切换函数）', fontsize=14, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.legend()
ax.grid(True, alpha=0.3)

# 创建按钮
button_width = 0.15
button_height = 0.05
button_y = 0.05

ax_btn_sin = plt.axes([0.2, button_y, button_width, button_height])
ax_btn_cos = plt.axes([0.4, button_y, button_width, button_height])
ax_btn_tan = plt.axes([0.6, button_y, button_width, button_height])

btn_sin = Button(ax_btn_sin, 'sin(x)')
btn_cos = Button(ax_btn_cos, 'cos(x)')
btn_tan = Button(ax_btn_tan, 'tan(x)')

# 定义按钮点击事件
def switch_function(func_name):
    global current_func
    current_func = func_name
    line.set_ydata(functions[func_name](x))
    line.set_label(func_name)
    ax.legend()
    fig.canvas.draw_idle()

btn_sin.on_clicked(lambda event: switch_function('sin'))
btn_cos.on_clicked(lambda event: switch_function('cos'))
btn_tan.on_clicked(lambda event: switch_function('tan'))

print("提示：点击按钮可以切换不同的函数")
print("关闭窗口继续下一个示例")
plt.show()

# ============ 3. 动画：数据实时更新 ============
print("\n" + "=" * 50)
print("示例 3：动画 - 数据实时更新")
print("=" * 50)

# 创建图表
fig, ax = plt.subplots(figsize=(12, 6))
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x), linewidth=2)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('动画：移动的正弦波', fontsize=14, fontweight='bold')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(True, alpha=0.3)

# 定义动画更新函数
# frame 是帧编号，从 0 开始递增
def animate(frame):
    # 每帧改变相位
    phase = frame * 0.1
    y = np.sin(x + phase)
    line.set_ydata(y)
    return line,

# 创建动画
# FuncAnimation(图表, 更新函数, frames=帧数, interval=间隔毫秒, blit=优化)
anim = FuncAnimation(fig, animate, frames=200, interval=50, blit=True)

print("提示：正弦波会持续移动")
print("关闭窗口继续下一个示例")
plt.show()

# ============ 4. 动画：财务数据增长 ============
print("\n" + "=" * 50)
print("示例 4：动画 - 财务数据增长")
print("=" * 50)

# 财务数据
months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
revenue = [450, 520, 480, 610, 580, 670, 720, 680, 750, 800, 820, 900]

# 创建图表
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar([], [], color='#2E86AB', alpha=0.8)
ax.set_xlim(-0.5, len(months) - 0.5)
ax.set_ylim(0, max(revenue) * 1.1)
ax.set_title('动画：月度营业收入增长', fontsize=14, fontweight='bold')
ax.set_xlabel('月份')
ax.set_ylabel('营业收入（万元）')
ax.grid(True, alpha=0.3, axis='y')

# 定义动画更新函数
def animate_bars(frame):
    # 清除旧的柱子
    ax.clear()

    # 绘制到当前帧的数据
    current_months = months[:frame+1]
    current_revenue = revenue[:frame+1]

    bars = ax.bar(current_months, current_revenue, color='#2E86AB', alpha=0.8)

    # 在柱子上显示数值
    for i, v in enumerate(current_revenue):
        ax.text(i, v + 10, str(v), ha='center', fontsize=10, fontweight='bold')

    # 重新设置图表属性
    ax.set_xlim(-0.5, len(months) - 0.5)
    ax.set_ylim(0, max(revenue) * 1.1)
    ax.set_title('动画：月度营业收入增长', fontsize=14, fontweight='bold')
    ax.set_xlabel('月份')
    ax.set_ylabel('营业收入（万元）')
    ax.grid(True, alpha=0.3, axis='y')

    return bars

# 创建动画
anim = FuncAnimation(fig, animate_bars, frames=len(months), interval=500, repeat=True)

print("提示：柱状图会逐月增长")
print("关闭窗口继续下一个示例")
plt.show()

# ============ 5. 保存动画为 GIF ============
print("\n" + "=" * 50)
print("示例 5：保存动画为 GIF（需要安装 pillow）")
print("=" * 50)

# 创建简单动画
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot([], [], 'b-', linewidth=2)

ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title('保存为 GIF 的动画', fontsize=14, fontweight='bold')
ax.grid(True, alpha=0.3)

def init():
    line.set_data([], [])
    return line,

def animate_save(frame):
    phase = frame * 0.2
    y = np.sin(x + phase)
    line.set_data(x, y)
    return line,

anim = FuncAnimation(fig, animate_save, init_func=init, frames=50, interval=50, blit=True)

# 保存为 GIF
# 需要安装：pip install pillow
try:
    anim.save('sine_wave_animation.gif', writer='pillow', fps=20)
    print("动画已保存为 sine_wave_animation.gif")
except Exception as e:
    print(f"保存失败（可能需要安装 pillow）：{e}")
    print("安装命令：pip install pillow")

plt.close()

# ============ 6. 实时数据监控模拟 ============
print("\n" + "=" * 50)
print("示例 6：实时数据监控模拟")
print("=" * 50)

# 模拟实时数据流
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# 初始化数据
max_points = 50
x_data = list(range(max_points))
y_data1 = [0] * max_points  # 销售额
y_data2 = [0] * max_points  # 访问量

line1, = ax1.plot(x_data, y_data1, 'b-', linewidth=2)
line2, = ax2.plot(x_data, y_data2, 'r-', linewidth=2)

ax1.set_xlim(0, max_points)
ax1.set_ylim(0, 100)
ax1.set_title('实时销售额监控', fontsize=12, fontweight='bold')
ax1.set_ylabel('销售额（万元）')
ax1.grid(True, alpha=0.3)

ax2.set_xlim(0, max_points)
ax2.set_ylim(0, 1000)
ax2.set_title('实时访问量监控', fontsize=12, fontweight='bold')
ax2.set_xlabel('时间点')
ax2.set_ylabel('访问量')
ax2.grid(True, alpha=0.3)

def animate_realtime(frame):
    # 模拟新数据
    new_sales = 50 + np.random.randn() * 10
    new_visits = 500 + np.random.randn() * 100

    # 更新数据（移除最旧的，添加最新的）
    y_data1.pop(0)
    y_data1.append(new_sales)
    y_data2.pop(0)
    y_data2.append(new_visits)

    # 更新曲线
    line1.set_ydata(y_data1)
    line2.set_ydata(y_data2)

    return line1, line2

anim = FuncAnimation(fig, animate_realtime, frames=200, interval=100, blit=True)

print("提示：模拟实时数据流，数据会持续更新")
print("关闭窗口结束示例")
plt.show()

print("\n" + "=" * 50)
print("交互式图表与动画教学完成！")
print("=" * 50)
print("\n【交互式组件】：")
print("1. Slider - 滑块控制参数")
print("2. Button - 按钮触发事件")
print("3. FuncAnimation - 创建动画")
print("4. anim.save() - 保存动画为 GIF/MP4")
print("\n【动画关键参数】：")
print("- frames：总帧数")
print("- interval：帧间隔（毫秒）")
print("- blit：优化渲染（True=只更新变化部分）")
print("- repeat：是否循环播放")
print("\n【应用场景】：")
print("- 参数调优：滑块实时调整模型参数")
print("- 数据演示：动画展示数据变化过程")
print("- 实时监控：模拟仪表盘实时数据流")
print("- 教学演示：动态展示算法过程")
