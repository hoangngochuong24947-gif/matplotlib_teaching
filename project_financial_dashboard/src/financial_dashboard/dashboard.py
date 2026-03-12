"""
第四层：项目规划 - 财务数据可视化仪表盘
完整的财务分析可视化系统
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 设置中文字体和样式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.style.use('seaborn-v0_8-whitegrid')


class FinancialDashboard:
    """
    财务数据可视化仪表盘

    功能：
    1. 加载和处理财务数据
    2. 生成多种财务图表
    3. 导出完整的财务报告
    """

    def __init__(self, data_source=None):
        """
        初始化仪表盘

        参数:
            data_source: 数据源（DataFrame 或文件路径）
        """
        self.data = None
        self.colors = {
            'revenue': '#2E86AB',
            'profit': '#06A77D',
            'cost': '#D62246',
            'cash': '#F18F01'
        }

        if data_source is not None:
            self.load_data(data_source)

    def load_data(self, source):
        """
        加载数据

        参数:
            source: DataFrame 或 CSV 文件路径
        """
        if isinstance(source, pd.DataFrame):
            self.data = source
        elif isinstance(source, str):
            # 从 CSV 文件加载
            self.data = pd.read_csv(source)
        else:
            raise ValueError("数据源必须是 DataFrame 或文件路径")

        print(f"数据加载成功，共 {len(self.data)} 条记录")

    def generate_sample_data(self, months=12):
        """
        生成示例财务数据

        参数:
            months: 月份数量
        """
        np.random.seed(42)

        # 生成日期
        start_date = datetime(2024, 1, 1)
        dates = [start_date + timedelta(days=30*i) for i in range(months)]

        # 生成财务数据
        revenue = np.random.normal(500, 50, months).cumsum() + 5000
        cost = revenue * 0.6 + np.random.randn(months) * 50
        profit = revenue - cost
        cash_flow = profit * 0.9 + np.random.randn(months) * 30

        self.data = pd.DataFrame({
            '日期': dates,
            '营业收入': revenue,
            '营业成本': cost,
            '净利润': profit,
            '现金流': cash_flow
        })

        print(f"示例数据生成成功，共 {months} 个月")
        return self.data

    def plot_revenue_trend(self, ax=None):
        """
        绘制营业收入趋势图

        参数:
            ax: matplotlib 轴对象（可选）
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))

        # 提取数据
        x = range(len(self.data))
        y = self.data['营业收入'].values

        # 绘制折线图
        ax.plot(x, y, 'o-', linewidth=2, markersize=8,
                color=self.colors['revenue'], label='营业收入')
        ax.fill_between(x, y, alpha=0.3, color=self.colors['revenue'])

        # 添加趋势线（线性回归）
        z = np.polyfit(x, y, 1)  # 一次多项式拟合
        p = np.poly1d(z)
        ax.plot(x, p(x), '--', linewidth=2, color='red',
                alpha=0.7, label='趋势线')

        # 设置标题和标签
        ax.set_title('营业收入趋势分析', fontsize=14, fontweight='bold')
        ax.set_xlabel('月份')
        ax.set_ylabel('金额（万元）')
        ax.legend()
        ax.grid(True, alpha=0.3)

        # 在数据点上显示数值
        for i, v in enumerate(y):
            ax.text(i, v + 50, f'{v:.0f}', ha='center', fontsize=9)

        return ax

    def plot_profit_analysis(self, ax=None):
        """
        绘制利润分析图

        参数:
            ax: matplotlib 轴对象（可选）
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))

        x = range(len(self.data))
        revenue = self.data['营业收入'].values
        cost = self.data['营业成本'].values
        profit = self.data['净利润'].values

        # 绘制堆叠面积图
        ax.fill_between(x, 0, cost, alpha=0.7,
                        color=self.colors['cost'], label='营业成本')
        ax.fill_between(x, cost, revenue, alpha=0.7,
                        color=self.colors['profit'], label='净利润')

        # 绘制边界线
        ax.plot(x, revenue, 'o-', linewidth=2, markersize=6,
                color='black', label='营业收入')

        ax.set_title('收入成本利润分析', fontsize=14, fontweight='bold')
        ax.set_xlabel('月份')
        ax.set_ylabel('金额（万元）')
        ax.legend()
        ax.grid(True, alpha=0.3)

        return ax

    def plot_margin_analysis(self, ax=None):
        """
        绘制利润率分析图

        参数:
            ax: matplotlib 轴对象（可选）
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))

        # 计算利润率
        gross_margin = ((self.data['营业收入'] - self.data['营业成本']) /
                       self.data['营业收入'] * 100)
        net_margin = (self.data['净利润'] / self.data['营业收入'] * 100)

        x = range(len(self.data))

        # 绘制双折线图
        ax.plot(x, gross_margin, 'o-', linewidth=2, markersize=6,
                label='毛利率', color=self.colors['revenue'])
        ax.plot(x, net_margin, 's-', linewidth=2, markersize=6,
                label='净利率', color=self.colors['profit'])

        # 添加平均线
        ax.axhline(y=gross_margin.mean(), color=self.colors['revenue'],
                  linestyle='--', alpha=0.5, label=f'平均毛利率: {gross_margin.mean():.1f}%')
        ax.axhline(y=net_margin.mean(), color=self.colors['profit'],
                  linestyle='--', alpha=0.5, label=f'平均净利率: {net_margin.mean():.1f}%')

        ax.set_title('利润率趋势分析', fontsize=14, fontweight='bold')
        ax.set_xlabel('月份')
        ax.set_ylabel('利润率 (%)')
        ax.legend()
        ax.grid(True, alpha=0.3)

        return ax

    def plot_cash_flow(self, ax=None):
        """
        绘制现金流分析图

        参数:
            ax: matplotlib 轴对象（可选）
        """
        if ax is None:
            fig, ax = plt.subplots(figsize=(12, 6))

        x = range(len(self.data))
        cash_flow = self.data['现金流'].values

        # 根据正负值设置颜色
        colors = [self.colors['profit'] if cf > 0 else self.colors['cost']
                 for cf in cash_flow]

        # 绘制柱状图
        bars = ax.bar(x, cash_flow, color=colors, alpha=0.8)

        # 添加零线
        ax.axhline(y=0, color='black', linewidth=1)

        ax.set_title('现金流分析', fontsize=14, fontweight='bold')
        ax.set_xlabel('月份')
        ax.set_ylabel('现金流（万元）')
        ax.grid(True, alpha=0.3, axis='y')

        # 在柱子上显示数值
        for i, (bar, cf) in enumerate(zip(bars, cash_flow)):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{cf:.0f}',
                   ha='center', va='bottom' if cf > 0 else 'top',
                   fontsize=9)

        return ax

    def generate_full_report(self, save_path='financial_report.png'):
        """
        生成完整的财务报告（包含所有图表）

        参数:
            save_path: 保存路径
        """
        # 创建 2x2 子图布局
        fig, axes = plt.subplots(2, 2, figsize=(16, 12))

        # 绘制各个图表
        self.plot_revenue_trend(ax=axes[0, 0])
        self.plot_profit_analysis(ax=axes[0, 1])
        self.plot_margin_analysis(ax=axes[1, 0])
        self.plot_cash_flow(ax=axes[1, 1])

        # 添加总标题
        fig.suptitle('财务数据可视化报告', fontsize=18, fontweight='bold', y=0.995)

        plt.tight_layout()

        # 保存图表
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"完整报告已保存：{save_path}")

        plt.show()

        return fig

    def export_summary(self):
        """
        导出财务数据摘要
        """
        summary = {
            '总营业收入': self.data['营业收入'].sum(),
            '总营业成本': self.data['营业成本'].sum(),
            '总净利润': self.data['净利润'].sum(),
            '平均月收入': self.data['营业收入'].mean(),
            '平均月利润': self.data['净利润'].mean(),
            '平均毛利率': ((self.data['营业收入'] - self.data['营业成本']) /
                         self.data['营业收入'] * 100).mean(),
            '平均净利率': (self.data['净利润'] / self.data['营业收入'] * 100).mean(),
            '现金流总额': self.data['现金流'].sum()
        }

        print("\n" + "=" * 50)
        print("财务数据摘要")
        print("=" * 50)
        for key, value in summary.items():
            if '率' in key:
                print(f"{key}: {value:.2f}%")
            else:
                print(f"{key}: {value:,.2f} 万元")
        print("=" * 50)

        return summary


# ============ 使用示例 ============
if __name__ == '__main__':
    print("=" * 50)
    print("财务数据可视化仪表盘 - 使用示例")
    print("=" * 50)

    # 创建仪表盘实例
    dashboard = FinancialDashboard()

    # 生成示例数据
    print("\n1. 生成示例数据...")
    data = dashboard.generate_sample_data(months=12)
    print("\n数据预览：")
    print(data.head())

    # 生成完整报告
    print("\n2. 生成完整财务报告...")
    dashboard.generate_full_report(save_path='financial_report.png')

    # 导出摘要
    print("\n3. 导出财务摘要...")
    summary = dashboard.export_summary()

    print("\n" + "=" * 50)
    print("使用说明：")
    print("=" * 50)
    print("1. 创建仪表盘：dashboard = FinancialDashboard()")
    print("2. 加载数据：dashboard.load_data('data.csv')")
    print("3. 生成报告：dashboard.generate_full_report()")
    print("4. 单独绘图：dashboard.plot_revenue_trend()")
    print("=" * 50)
