# Matplotlib 教学完整指南

## 📚 教学结构

本教学包采用四层递进式教学模型，从基础到项目实战，系统学习 matplotlib 数据可视化。

### 第一层：基础语法教学（Foundation）
**目标**：掌握 matplotlib 核心语法和基本图表

**文件列表**：
- `01_basic_plotting.py` - 基本绘图（折线图、散点图、柱状图、饼图）
- `02_customization.py` - 图表美化与定制（颜色、样式、字体）
- `03_advanced_charts.py` - 高级图表类型（直方图、箱线图、热力图）
- `04_financial_charts.py` - 财务图表实战（财务三表、利润率、现金流）
- `foundation_cheatsheet.md` - 基础语法速查表

**学习时长**：2-3 小时
**知识点分类**：【必须背诵】

### 第二层：模块联合教学（Integration）
**目标**：学习 matplotlib 与其他库的集成使用

**文件列表**：
- `01_pandas_integration.py` - Matplotlib + Pandas 数据可视化
- `02_numpy_integration.py` - Matplotlib + NumPy 科学计算可视化

**学习时长**：2-3 小时
**知识点分类**：【熟悉掌握】

### 第三层：高级功能教学（Advanced）
**目标**：探索 matplotlib 的高级特性

**文件列表**：
- `01_interactive_animation.py` - 交互式图表与动画
- `02_3d_advanced_layout.py` - 3D 图表与高级布局

**学习时长**：2-3 小时
**知识点分类**：【了解即可】

### 第四层：项目规划教学（Project）
**目标**：完整的财务数据可视化系统

**项目**：`project_financial_dashboard/`
- 完整的 Python 包结构
- 专业的财务图表系统
- 可直接用于实际工作

**学习时长**：3-4 小时
**知识点分类**：【实战应用】

## 🚀 快速开始

### 1. 环境配置

```bash
# 安装依赖
pip install matplotlib pandas numpy

# 验证安装
python -c "import matplotlib; print(matplotlib.__version__)"
```

### 2. 从基础开始

```bash
# 进入基础教学目录
cd foundation

# 运行第一个示例
python 01_basic_plotting.py
```

### 3. 学习路径

**推荐学习顺序**：
1. 基础层（1-4天）→ 2. 联合层（2-3天）→ 3. 高级层（2-3天）→ 4. 项目层（3-5天）

**快速通道**（仅学核心）：
1. `01_basic_plotting.py`
2. `02_customization.py`
3. `01_pandas_integration.py`
4. 项目实战

## 📖 使用指南

### 基础层使用

每个文件都是独立的教学程序，直接运行即可：

```bash
python foundation/01_basic_plotting.py
```

每个文件包含：
- 详细的中文注释（每行代码都有解释）
- 多个示例（从简单到复杂）
- 知识点总结（文件末尾）

### 联合层使用

学习如何将 matplotlib 与 pandas、numpy 结合：

```bash
python integration/01_pandas_integration.py
```

### 高级层使用

探索交互式图表和 3D 可视化：

```bash
python advanced/01_interactive_animation.py
```

### 项目层使用

完整的财务可视化系统：

```bash
cd project_financial_dashboard
python src/financial_dashboard/dashboard.py
```

## 🎯 知识点分类

### 【必须背诵】
- `plt.plot()` - 折线图
- `plt.scatter()` - 散点图
- `plt.bar()` - 柱状图
- `plt.pie()` - 饼图
- `plt.title()` / `plt.xlabel()` / `plt.ylabel()` - 标题和标签
- `plt.legend()` - 图例
- `plt.show()` - 显示图表
- 中文显示设置

### 【熟悉掌握】
- `plt.hist()` - 直方图
- `plt.boxplot()` - 箱线图
- `plt.imshow()` - 热力图
- DataFrame.plot() - Pandas 绘图
- NumPy 数组操作

### 【了解即可】
- 3D 图表
- 交互式组件
- 动画制作
- 高级布局

## 💡 学习建议

### 1. 边学边练
每个示例都可以修改参数，观察效果变化。

### 2. 结合实际
用自己的数据（如课程成绩、消费记录）练习绘图。

### 3. 查阅速查表
`foundation_cheatsheet.md` 包含所有核心语法。

### 4. 项目驱动
最后用项目层的代码处理真实财务数据。

## 🔧 常见问题

### Q1: 中文显示为方框？
**A**: 代码中已配置 SimHei 字体，如仍有问题：
```python
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 改用微软雅黑
```

### Q2: 图表不显示？
**A**: 确保调用了 `plt.show()`，或使用 Jupyter Notebook。

### Q3: 如何保存图表？
**A**: 使用 `plt.savefig()`：
```python
plt.savefig('my_chart.png', dpi=300, bbox_inches='tight')
```

### Q4: 如何修改图表尺寸？
**A**: 使用 `figsize` 参数：
```python
plt.figure(figsize=(12, 6))  # 宽12英寸，高6英寸
```

## 📊 财务场景应用

本教学特别针对财务管理专业，包含大量财务场景：

- 营业收入趋势分析
- 利润率分析
- 成本结构分析
- 现金流分析
- 财务三表可视化
- 投资回报率计算

## 🎓 学习成果

完成本教学后，你将能够：

✅ 独立绘制各种专业图表
✅ 处理和可视化财务数据
✅ 定制图表样式和配色
✅ 集成 pandas 进行数据分析
✅ 构建完整的可视化系统
✅ 生成高质量的财务报告

## 📝 复盘与改进

### 优点
- 系统性强，从基础到项目完整覆盖
- 保姆级注释，每行代码都有解释
- 结合财务场景，实用性强
- 代码可直接运行，无需修改

### 改进空间
- 可增加更多交互式示例
- 可添加 Web 集成示例（Flask/Django）
- 可增加更多行业场景（电商、制造业等）

### 后续学习方向
1. **Seaborn**：更高级的统计可视化
2. **Plotly**：交互式图表库
3. **Dash**：构建数据可视化 Web 应用
4. **Tableau/Power BI**：商业智能工具

## 📞 反馈与支持

如有问题或建议，欢迎反馈！

---

**作者**：卢柳源
**专业**：财务管理
**版本**：v1.0
**更新日期**：2024年
