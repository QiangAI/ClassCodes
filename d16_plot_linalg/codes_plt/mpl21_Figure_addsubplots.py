#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
Figure中坐标轴的创建与管理
|-add_subplot(*args, **kwargs)
该函数的所有属性基本上与add_axes一样。可以创建axes，并指定位置，坐坐标轴在figure中均匀分配，一共有三种使用方法
    |-add_subplot(nrows, ncols, index, **kwargs)
        |-nrows，坐标轴的行数（多个坐标轴）
        |-ncols，坐标轴的列数（多个坐标轴）
        |-index，坐标轴的位置（位置按照自然数计算，行：按照从上到下，列：按照从左到右）
        |-**kwargs 与add_axes函数中参数一样，可以求助于文档
    |-add_subplot(pos, **kwargs)
        |-与上一种方法一样，只是当nrows，ncols， index不超过1位数的时候，可以合并成pos来表示
    |-add_subplot(ax)     
        |-与add_axes一样  
# 可以保存成图片
    |-savefig(fname, *, frameon=None, transparent=None, **kwargs)
'''
# 构建figure对象
figure = plt.figure('Figure的坐标轴管理', (5, 4))
# ------------------------------------------
ax1 = figure.add_subplot(221, title='坐标轴1')
ax2 = figure.add_subplot(2, 2, 2, title='坐标轴2')
ax3 = figure.add_subplot(224, title='坐标轴4', position=[0.55, 0.05, 0.35, 0.3])

ax1.set_xbound(lower=0, upper=10)
ax1.set_ybound(lower=-1, upper=1)
line = plt.Line2D(
    xdata=np.linspace(0, 10, 20),
    ydata=np.random.uniform(-1, 1, size=20),
    label='Line2',
    color=(1, 0, 0, 1)
)
ax1.add_line(line)
# 下面代码报错，多个坐标轴，不能公用一个Line2D对象
# ax2.add_line(line)
# ax3.add_line(line)
# ------------------------------------------
plt.show()
