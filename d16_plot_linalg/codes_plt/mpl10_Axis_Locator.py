#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.ticker import *

'''
操作最重要的对象Axis--Locator
    |-xaxis
        |-Axes.get_xaxis()返回XAxis对象
    |-yaxis
        |-Axes.get_yaxis()返回YAxis对象
上述两个函数返回不同的对象
2.控制标签的位置
    |-AutoLocator
        |-自动定位器，大部分plot行为的默认定位器
    |-MaxNLocator
        |-计算出一个最佳的最大间隔，然后生成合适的位置.
    |-LinearLocator
        |-从最小到最大均匀计算定位
            |-set_params(numticks=None, presets=None)
            |-tick_values(vmin, vmax)
            |-view_limits(vmin, vmax)
    |-LogLocator
        |-从最小到最大按照对数计算定位.
    |-MultipleLocator
        |-按照倍数（可以整数与小数）计算定位
    |-FixedLocator
        |-固定的定位
    |-IndexLocator
        |-索引定位计算(e.g., where x = range(len(y))).
    |-NullLocator
        |-没有刻度.
    |-SymmetricalLogLocator
        |-按照对称对数计算定位
    |-LogitLocator
        |-按照分对数计算定位，计算公式log(x/1-x)
    |-OldAutoLocator
        |-选择一个乘法器，动态计算定位.
    |-AutoMinorLocator
        |-当坐标轴使线性并且主刻度是统一的空间，把大刻度按照4或者5等分均分的方式计算小刻度定位

# 注意Locator可以用于Major，也可以用于Minor。
'''
figure = plt.figure(1, figsize=(4, 6))
# -------------------------------
ax1 = figure.add_axes([0.1, 0.1, 0.8, 0.4])
# class matplotlib.ticker.LinearLocator(numticks=None, presets=None)
#   |-numticks=None 刻度个数
#   |-presets=None
# 1.LinearLocator
# from matplotlib.ticker import LinearLocator
ll = LinearLocator(numticks=6)
xaxis = ax1.get_xaxis()
xaxis.set_major_locator(ll)
# -------------------------------
# 2. AutoMinorLocator
# class matplotlib.ticker.AutoMinorLocator(n=None)
#   |-n=None 设置等分的份数；默认4，5等分
# from matplotlib.ticker import AutoMinorLocator
aml = AutoMinorLocator(5)
xaxis.set_minor_locator(aml)
# -------------------------------
# 3.MultipleLocator
# class matplotlib.ticker.MultipleLocator(base=1.0)
#   |-base=1.0 倍数
# from matplotlib.ticker import MultipleLocator
mpl = MultipleLocator(0.15)  # 按照0.15的倍数设置刻度
yaxis = ax1.get_yaxis()
yaxis.set_major_locator(mpl)
yaxis.set_minor_locator(aml)
# -------------------------------
ax2 = figure.add_axes([0.1, 0.55, 0.8, 0.4])
# 4.IndexLocator
# class matplotlib.ticker.IndexLocator(base, offset)
#    |-base
#    |-offset
# 从plot等函数的数据中抽取标签刻度,取点计算公式是： (i-offset)%base
# from matplotlib.ticker import IndexLocator
il = IndexLocator(0.2, 0.55)  # 不是按照下标计算的,而是按照data[0]~data[-1]从开始位置offset，按照base为等距计算。
xaxis = ax2.get_xaxis()
xaxis.set_major_locator(il)
ax2.plot(
    [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
    [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
)
# -------------------------------
# 5.FixedLocator
# class matplotlib.ticker.FixedLocator(locs, nbins=None)
#   |-locs 设置标签
#   |-nbins(限制抽取的标签个数)ticks <= nbins +1
#   |-其中采取的是抽样算法，从data中选取标签
yaxis = ax2.get_yaxis()
# from matplotlib.ticker import FixedLocator
fl = FixedLocator(
    locs=[0, 0.1, 0.2, 0.47, 0.48, 0.5, 0.51, 0.52, 0.53, 0.56], nbins=10)
yaxis.set_major_locator(fl)
# -------------------------------
figure.show(warn=False)
plt.show()
