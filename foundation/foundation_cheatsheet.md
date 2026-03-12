# Matplotlib 基础语法速查表

## 必须背诵的核心函数

### 1. 图表类型
```python
plt.plot(x, y)              # 折线图
plt.scatter(x, y)           # 散点图
plt.bar(x, height)          # 柱状图
plt.barh(x, width)          # 水平柱状图
plt.pie(values, labels)     # 饼图
plt.hist(data, bins)        # 直方图
plt.boxplot(data)           # 箱线图
```

### 2. 图表装饰
```python
plt.title('标题')           # 设置标题
plt.xlabel('X轴标签')       # X轴标签
plt.ylabel('Y轴标签')       # Y轴标签
plt.legend()                # 显示图例
plt.grid(True)              # 显示网格
plt.show()                  # 显示图表
```

### 3. 样式参数
```python
# 颜色
color='red' 或 c='r'        # 单字母：r, g, b, c, m, y, k, w
color='#1f77b4'             # 十六进制
color=(0.2, 0.8, 0.2)       # RGB元组

# 线条样式
linestyle='-'               # 实线
linestyle='--'              # 虚线
linestyle='-.'              # 点划线
linestyle=':'               # 点线

# 标记样式
marker='o'                  # 圆圈
marker='s'                  # 方块
marker='^'                  # 三角形
marker='*'                  # 星号

# 其他参数
linewidth=2 或 lw=2         # 线条粗细
markersize=8 或 ms=8        # 标记大小
alpha=0.7                   # 透明度（0-1）
label='图例标签'            # 图例文字
```

### 4. 坐标轴控制
```python
plt.xlim(0, 10)             # X轴范围
plt.ylim(0, 100)            # Y轴范围
plt.xticks([0, 5, 10])      # X轴刻度位置
plt.yticks([0, 50, 100])    # Y轴刻度位置
```

### 5. 子图布局
```python
plt.figure(figsize=(10, 6)) # 创建画布（宽, 高）
plt.subplot(2, 2, 1)        # 创建子图（行, 列, 编号）
plt.tight_layout()          # 自动调整间距
```

### 6. 中文显示（必备）
```python
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

### 7. 保存图表
```python
plt.savefig('文件名.png', dpi=300, bbox_inches='tight')
```

## 组合写法速记

```python
# 颜色 + 标记 + 线型
'ro-'   # 红色圆圈实线
'bs--'  # 蓝色方块虚线
'g^-.'  # 绿色三角点划线
```

## 常用图表选择

| 数据类型 | 推荐图表 |
|---------|---------|
| 趋势变化 | 折线图 (plot) |
| 数值对比 | 柱状图 (bar) |
| 占比结构 | 饼图 (pie) |
| 数据分布 | 直方图 (hist)、箱线图 (boxplot) |
| 相关性 | 散点图 (scatter) |
| 排名 | 水平柱状图 (barh) |

## 财务图表配色方案

```python
收入/资产：'#2E86AB'  # 蓝色
利润/正向：'#06A77D'  # 绿色
成本/负向：'#D62246'  # 红色
现金流：'#F18F01'     # 橙色
```
