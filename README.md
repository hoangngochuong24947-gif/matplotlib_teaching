
# Matplotlib 教学包使用说明

## 🎯 快速开始

### 1. 安装依赖
```bash
pip install matplotlib pandas numpy
```

### 2. 运行第一个示例
```bash
cd matplotlib_teaching/foundation
python 01_basic_plotting.py
```

## 📁 目录结构

```
matplotlib_teaching/
├── foundation/                    # 第一层：基础语法
│   ├── 01_basic_plotting.py      # 基本绘图
│   ├── 02_customization.py       # 图表定制
│   ├── 03_advanced_charts.py     # 高级图表
│   ├── 04_financial_charts.py    # 财务图表
│   └── foundation_cheatsheet.md  # 语法速查表
│
├── integration/                   # 第二层：模块联合
│   ├── 01_pandas_integration.py  # Pandas 集成
│   └── 02_numpy_integration.py   # NumPy 集成
│
├── advanced/                      # 第三层：高级功能
│   ├── 01_interactive_animation.py  # 交互式与动画
│   └── 02_3d_advanced_layout.py     # 3D 与高级布局
│
├── project_financial_dashboard/   # 第四层：完整项目
│   ├── src/financial_dashboard/
│   │   ├── __init__.py
│   │   └── dashboard.py          # 核心代码
│   ├── examples/
│   │   └── basic_usage.py        # 使用示例
│   ├── configs/
│   │   └── config.yaml           # 配置文件
│   ├── README.md                 # 项目文档
│   └── requirements.txt          # 依赖列表
│
├── TEACHING_GUIDE.md             # 完整教学指南
├── SUMMARY.md                    # 系统性复盘
└── README.md                     # 本文件
```

## 📚 学习路径

### 路径 1：完整学习（推荐）
1. **第一层（2-3天）**：基础语法
   - 运行 `foundation/` 下所有文件
   - 背诵核心函数
   - 查阅速查表

2. **第二层（2-3天）**：模块联合
   - 学习 Pandas 集成
   - 学习 NumPy 集成
   - 练习数据处理

3. **第三层（2-3天）**：高级功能
   - 探索交互式图表
   - 学习 3D 可视化
   - 了解动画制作

4. **第四层（3-5天）**：项目实战
   - 研究项目结构
   - 运行示例代码
   - 用自己的数据测试

### 路径 2：快速通道（3-5天）
只学习核心内容：
1. `foundation/01_basic_plotting.py`
2. `foundation/02_customization.py`
3. `integration/01_pandas_integration.py`
4. 项目实战

## 🎓 知识点分类

### 【必须背诵】
- `plt.plot()` - 折线图
- `plt.scatter()` - 散点图
- `plt.bar()` - 柱状图
- `plt.pie()` - 饼图
- `plt.title()` / `plt.xlabel()` / `plt.ylabel()`
- `plt.legend()` - 图例
- `plt.show()` - 显示
- 中文显示设置

### 【熟悉掌握】
- `plt.hist()` - 直方图
- `plt.boxplot()` - 箱线图
- DataFrame.plot() - Pandas 绘图
- NumPy 数组操作

### 【了解即可】
- 3D 图表
- 交互式组件
- 动画制作

## 💻 运行示例

### 基础层
```bash
cd foundation
python 01_basic_plotting.py
python 02_customization.py
python 03_advanced_charts.py
python 04_financial_charts.py
```

### 联合层
```bash
cd integration
python 01_pandas_integration.py
python 02_numpy_integration.py
```

### 高级层
```bash
cd advanced
python 01_interactive_animation.py
python 02_3d_advanced_layout.py
```

### 项目层
```bash
cd project_financial_dashboard
python src/financial_dashboard/dashboard.py
python examples/basic_usage.py
```

## 🔧 常见问题

### Q: 中文显示为方框？
A: 代码中已配置 SimHei 字体，如仍有问题可改用微软雅黑：
```python
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
```

### Q: 图表不显示？
A: 确保调用了 `plt.show()`

### Q: 如何保存图表？
A: 使用 `plt.savefig('文件名.png', dpi=300, bbox_inches='tight')`

## 📊 项目实战使用

### 快速生成财务报告
```python
from financial_dashboard import FinancialDashboard

# 创建仪表盘
dashboard = FinancialDashboard()

# 生成示例数据
dashboard.generate_sample_data(months=12)

# 生成完整报告
dashboard.generate_full_report(save_path='report.png')
```

### 加载自己的数据
```python
# 从 CSV 加载
dashboard = FinancialDashboard('your_data.csv')

# 生成报告
dashboard.generate_full_report()
```

## 🎯 学习建议

1. **边学边练**：每个示例都可以修改参数观察效果
2. **用真实数据**：用自己的数据（成绩、消费等）练习
3. **查阅速查表**：`foundation_cheatsheet.md` 包含所有核心语法
4. **项目驱动**：最后用项目代码处理实际财务数据

## 📖 详细文档

- `TEACHING_GUIDE.md` - 完整教学指南
- `SUMMARY.md` - 系统性复盘与改进建议
- `foundation/foundation_cheatsheet.md` - 语法速查表
- `project_financial_dashboard/README.md` - 项目文档

## ✨ 教学特色

- ✅ 保姆级注释（每行代码都有解释）
- ✅ 财务场景导向（结合实际工作）
- ✅ 知识点分类（明确学习重点）
- ✅ 完整项目实战（可直接使用）

## 🎓 适用对象

- 财务管理专业学生
- 需要数据可视化的财务工作者
- Python 数据分析初学者
- 需要生成财务报告的从业者

---

**开始学习吧！从 `foundation/01_basic_plotting.py` 开始你的 matplotlib 之旅。**
