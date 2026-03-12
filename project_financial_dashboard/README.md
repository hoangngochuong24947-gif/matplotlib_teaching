# 财务数据可视化仪表盘

一个基于 matplotlib 的专业财务数据可视化系统，适用于财务分析、报表生成和数据展示。

## 功能特性

- 📊 多种财务图表类型（趋势图、利润分析、利润率分析、现金流分析）
- 🎨 专业的财务配色方案
- 📈 自动趋势线拟合
- 💾 高清图表导出（300 DPI）
- 📋 财务数据摘要统计
- 🔧 灵活的数据加载方式（CSV、DataFrame）

## 快速开始

### 安装依赖

```bash
pip install matplotlib pandas numpy
```

### 基本使用

```python
from financial_dashboard import FinancialDashboard

# 创建仪表盘
dashboard = FinancialDashboard()

# 生成示例数据
dashboard.generate_sample_data(months=12)

# 生成完整报告
dashboard.generate_full_report(save_path='report.png')

# 导出财务摘要
summary = dashboard.export_summary()
```

### 加载自己的数据

```python
# 方式 1：从 CSV 文件加载
dashboard = FinancialDashboard('data.csv')

# 方式 2：从 DataFrame 加载
import pandas as pd
df = pd.read_excel('financial_data.xlsx')
dashboard = FinancialDashboard(df)
```

## 数据格式要求

CSV 或 DataFrame 需要包含以下列：

| 列名 | 说明 | 类型 |
|------|------|------|
| 日期 | 日期 | datetime |
| 营业收入 | 营业收入金额 | float |
| 营业成本 | 营业成本金额 | float |
| 净利润 | 净利润金额 | float |
| 现金流 | 现金流金额 | float |

示例数据：

```csv
日期,营业收入,营业成本,净利润,现金流
2024-01-01,5000,3000,1800,1600
2024-02-01,5200,3100,1900,1700
2024-03-01,5400,3200,2000,1800
```

## 图表类型

### 1. 营业收入趋势图
- 折线图 + 面积填充
- 自动趋势线拟合
- 数据点标注

### 2. 利润分析图
- 堆叠面积图
- 展示收入、成本、利润关系

### 3. 利润率分析图
- 毛利率和净利率双折线
- 平均值参考线

### 4. 现金流分析图
- 柱状图
- 正负值颜色区分

## 高级用法

### 单独绘制图表

```python
import matplotlib.pyplot as plt

# 创建画布
fig, ax = plt.subplots(figsize=(12, 6))

# 绘制单个图表
dashboard.plot_revenue_trend(ax=ax)

plt.show()
```

### 自定义配色

```python
dashboard.colors = {
    'revenue': '#1E88E5',  # 蓝色
    'profit': '#43A047',   # 绿色
    'cost': '#E53935',     # 红色
    'cash': '#FB8C00'      # 橙色
}
```

### 导出数据摘要

```python
summary = dashboard.export_summary()

# 访问具体指标
total_revenue = summary['总营业收入']
avg_margin = summary['平均净利率']
```

## 项目结构

```
project_financial_dashboard/
├── src/
│   └── financial_dashboard/
│       ├── __init__.py
│       └── dashboard.py          # 核心仪表盘类
├── examples/
│   ├── basic_usage.py            # 基本使用示例
│   └── custom_charts.py          # 自定义图表示例
├── tests/
│   └── test_dashboard.py         # 单元测试
├── docs/
│   └── api_reference.md          # API 文档
├── configs/
│   └── config.yaml               # 配置文件
├── README.md
└── requirements.txt
```

## 配置文件

在 `configs/config.yaml` 中可以配置默认参数：

```yaml
# 图表配置
chart:
  figsize: [12, 6]
  dpi: 300
  style: seaborn-v0_8-whitegrid

# 颜色配置
colors:
  revenue: '#2E86AB'
  profit: '#06A77D'
  cost: '#D62246'
  cash: '#F18F01'

# 字体配置
font:
  family: SimHei
  size: 12
```

## 常见问题

### Q: 中文显示为方框？
A: 确保安装了中文字体（如 SimHei），代码中已自动配置。

### Q: 如何修改图表尺寸？
A: 在调用绘图方法时传入 `figsize` 参数：
```python
fig, ax = plt.subplots(figsize=(14, 8))
dashboard.plot_revenue_trend(ax=ax)
```

### Q: 如何保存为 PDF 格式？
A: 修改保存路径的扩展名：
```python
dashboard.generate_full_report(save_path='report.pdf')
```

## 扩展开发

### 添加新图表类型

```python
def plot_custom_chart(self, ax=None):
    """自定义图表"""
    if ax is None:
        fig, ax = plt.subplots(figsize=(12, 6))

    # 你的绘图代码
    # ...

    return ax
```

### 集成到 Web 应用

```python
import io
import base64

# 生成图表并转换为 base64
fig = dashboard.generate_full_report()
buf = io.BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
img_base64 = base64.b64encode(buf.read()).decode()

# 在 HTML 中使用
html = f'<img src="data:image/png;base64,{img_base64}">'
```

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## 联系方式

- 作者：卢柳源
- 专业：财务管理
- 用途：财务数据分析与可视化
