#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler

'''
循环属性：
|-Axes.set_prop_cycle(*args, **kwargs)
该属性只对数组这样的数据有效，可以按照列反复使用循环属性。
其中有三种使用方式：
    |-set_prop_cycle(cycler)
    |-set_prop_cycle(label=values[, label2=values2[, ...]])
    |-set_prop_cycle(label, values)
参数说明如下：
    |-cycler : Cycler
        |-cycler对象，可以使用函数构造
    |-label : str
        |-一个字符串，用来指定属性名
    |-values : iterable
        |-对应属性名的属性值（类型是可迭代类型）
'''
figure = plt.figure('Legend使用', figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xbound(lower=0, upper=10)  # 会被plot等函数改变
ax.set_xlim(left=-2, right=10)
# 生成a坐标（n,）
x = np.linspace(0, 2 * np.pi)
# 相位(4,)
phases = [np.pi * 0 / 2,
          np.pi * 1 / 2,
          np.pi * 2 / 2,
          np.pi * 3 / 2]
# 根据相位产生(n,4)的矩阵
y = np.transpose(
    [np.sin(x + phase) for phase in phases]
)
# ------------------------------------------
# 属性设置在前后都无所谓，在最后绘制才有效。
c = cycler(
    color=[
        (1, 0, 0, 1),
        (0, 1, 0, 1),
        (0, 0, 1, 1),
        (1, 1, 0, 1)]
)
m = cycler(
    marker=['+', 'v', '.', 'x']
)
# Cycler 支持+ * += *=等运算
# 使用方式1：使用Cycle第对象
# ax.set_prop_cycle(c+m)
# 使用方式2：使用label=值
# ax.set_prop_cycle(color=['y', 'r', 'b', 'g'])
# 使用方式3：多个label属性设置
ax.set_prop_cycle(
    color=['y', 'r', 'b', 'g'],
    marker=['.', 'v', '^', '+']
)
ax.plot(x, y)
# ax.set_xbound(lower=0, upper=10)   # 绘制后设置bound才有效
# ------------------------------------------
figure.show(warn=False)
plt.show()
