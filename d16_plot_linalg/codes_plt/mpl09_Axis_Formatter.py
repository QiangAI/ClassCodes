#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.ticker import EngFormatter
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import PercentFormatter

'''
操作最重要的对象Axis--Formatter
    |-xaxis
        |-Axes.get_xaxis()返回XAxis对象
    |-yaxis
        |-Axes.get_yaxis()返回YAxis对象
上述两个函数返回不同的对象
1.控制标签的格式化
    |-NullFormatter
        |-没有标签
    |-IndexFormatter
        |-从labels列表中取标签
    |-FixedFormatter
        |-从labels手动设置字符串
    |-FuncFormatter
        |-用函数的返回值设置标签
    |-StrMethodFormatter
        |-使用字符串format方法.
    |-FormatStrFormatter
        |-使用sprintf格式化方法.
    |-ScalarFormatter
        |-缺省的标量格式化
    |-LogFormatter
        |-log坐标的格式化
    |-LogFormatterExponent
        |-对数坐标格式化值指数为 exponent = log_base(value).
    |-LogFormatterMathtext
        |-对数坐标格式化值指数为 exponent = log_base(value)，使用数学文本
    |-LogFormatterSciNotation
        |-科学记数法的对数坐标值
    |-LogitFormatter
        |-概率格式化
    |-EngFormatter
        |-工程记号表示的标签格式化
        |-前缀符号：
            |-ENG_PREFIXES = {-24: 'y', -21: 'z', -18: 'a', -15: 'f', -12: 'p', -9: 'n', -6: 'μ', -3: 'm', 0: '', 3: 'k', 6: 'M', 9: 'G', 12: 'T', 15: 'P', 18: 'E', 21: 'Z', 24: 'Y'}
    |-PercentFormatter
        |-百分格式化
'''
figure = plt.figure(1, figsize=(4, 4))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.4])
# -------------------------------
# 1.PercentFormatter
# |-class matplotlib.ticker.PercentFormatter(xmax=100, decimals=None, symbol='%', is_latex=False)
xaxis = ax.get_xaxis()
pfx = PercentFormatter(
    xmax=10,  # 百分比的计算分母：输出值计算方式：x / xmax * 100. 比如千分比，使用10
    decimals=2,  # 小数点维数：精度
    symbol='‰$a^2$',  # 符号
    is_latex=True)  # 符号支持Latex语法
xaxis.set_major_formatter(pfx)
# 2.EngFormatter
# |-class matplotlib.ticker.EngFormatter(unit='', places=None, sep=' ')[source]
yaxis = ax.get_yaxis()
pfy = EngFormatter(
    unit='Hz',  # 单位（后缀）
    places=1,  # 小数位数
    sep='*')  # 前缀（常用符号见上面说明与文档说明）
print(pfy.format_eng(0.1))  # 100m
yaxis.set_major_formatter(pfy)

ax2 = figure.add_axes([0.1, 0.55, 0.8, 0.4])
# 3.FuncFormatter
# class matplotlib.ticker.FuncFormatter(func)
xaxis = ax2.get_xaxis()


def my_x_formatter_func(x, pos):
    if x and pos:
        print(type(x), x, type(pos), pos)
        return 'L:%5.2f(%d)' % (x, pos)
    else:
        return "o"


ff = FuncFormatter(my_x_formatter_func)
xaxis.set_major_formatter(ff)

# -------------------------------
figure.show(warn=False)
plt.show()
