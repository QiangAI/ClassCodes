#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
坐标轴的limits与bounds
# 这两个属性作用类似：limits还可以决定方向
|-limits:
    |-Axes.set_xlim(left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
    |-Axes.set_ylim(bottom=None, top=None, emit=True, auto=False, *, ymin=None, ymax=None)
|-bounds
    |-Axes.set_xbound(lower=None, upper=None)
    |-Axes.set_ybound(lower=None, upper=None)
'''
figure = plt.figure('Legend使用', figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# 线段
line = plt.Line2D(
    xdata=np.linspace(0, 10, 20),
    ydata=np.random.uniform(-1, 1, size=20),
    label='Line2',
    color=(1, 0, 0, 1)
)
ax.add_line(line)
# ------------------------------------------

ax.set_xlim(10, 0)  # 前大后小等同于坐标轴翻转(确定方向)
ax.set_ylim(-1, 1)
ax.set_xbound(lower=-5, upper=5)  # 范围
ax.set_ybound(lower=5, upper=-5)  # 也决定范围 不改变方向

# set_xbound设置后，会被plot等函数在绘制中改变。
# set_xlim设置后，不会被plot等函数的auto scale等参数改变。
# ------------------------------------------
figure.show(warn=False)
plt.show()
