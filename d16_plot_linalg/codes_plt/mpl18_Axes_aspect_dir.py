#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
1.aspect
设置x与y的坐标单位比例
|-Axes.set_aspect(aspect, adjustable=None, anchor=None, share=False)
    |-aspect : {'auto', 'equal'} or num
        |-'auto'
            |-使用Axes的区域，自动决定绘制区域的比例。
        |-'equal'	
            |-绘制区域比例相等，等于num=1
        |-num	
            |-设置坐标轴的绘制比例
        注意：aspect与xlim与ylim是有关系的(如果不考虑adjustable)
        |-aspect=1，xlim的长度为10，ylim的长度为1，则坐标轴就是10：1的比例绘制
        |-aspect=10，xlim的长度为10，ylim的长度为1，则坐标轴就是1：1的比例绘制
    |-adjustable : None or {'box', 'datalim'}, 可选
        |-box:调整物理维度，调整绘制区域，达到aspect的值
            |-物理区域可能有空余
        |-datalim：调整x的limits或者y的limits，达到aspect的值。
            |-物理区域总是充分利用的
    |-anchor : None or str or 2-tuple of float, optional
        |-锚点：这个参数在box才有效，因为根据datalim来计算比例，物理空间永远是填充满的，锚点效果不大。
            |-'C'	中间
            |-'SW'	西南角
            |-'S'	南面中间
            |-'SE'	东南
            |-etc.  其他方向组合
    |-share : bool, optional
        |-是否使用改变到所有共享的坐标轴
|-Axes.get_aspect()
    |-返回字符串

2.坐标轴翻转
|-翻转坐标轴
|    |-Axes.invert_xaxis()
|    |-Axes.invert_yaxis()
|-判定坐标轴是否翻转
|    |-Axes.xaxis_inverted()
|    |-Axes.yaxis_inverted()
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
# 1. aspect
# get_aspect返货的是字符串的值
asp = ax.get_aspect()
print(asp, type(asp))
ax.set_xlim(
    left=0,
    right=10)
ax.set_ylim(
    bottom=0,
    top=1)
ax.set_aspect(
    aspect=10,  # x，y坐标的比例
    adjustable='datalim',  # 当使用datalim参数，总是填充整个坐标轴区域的。
    anchor=(0, 0)  # 这个参数在adjustable=box才有能看见效果。
)
# ------------------------------------------
# 2.invert axis
ax.invert_xaxis()
ax.invert_yaxis()
# ------------------------------------------
figure.show(warn=False)

plt.show()
