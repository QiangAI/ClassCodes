#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
Axes坐标轴的使用与管理 ---- 之理解型add_axes
.坐标轴通常包含Axis, Tick, Line2D, Text, Polygon等对象绘制完成,
.坐标轴的创建提供了两种方式：
    |-Figure.add_axes(*args, **kwargs)  [理解型]
    |-add_subplot(*args, **kwargs)      [快捷性]
Axes坐标轴的使用与管理 ---- 之理解型add_axes
1.add_axes函数使用的两种方式：
    |-add_axes(rect, projection=None, polar=False, **kwargs)
        |-[add_axes函数利用参数构造Axes对象]
    |-add_axes(ax) 
        |-[调用者自己构造Axes对象]
    上面两种方式本质都一样，因为参数都是一样的。
注意：下面例子把Figure分成两部分
    |-下面部分：说明add_axes(ax)
    |-上面部分：说明add_axes(rect, projection=None, polar=False, **kwargs)
2.add_axes(ax)
    .class matplotlib.axes.Axes(fig, rect, facecolor=None, frameon=True, sharex=None, sharey=None, label='', xscale=None, yscale=None, **kwargs)
    .返回Axes对象
    |-fig : Figure
        |-坐标轴所属的Figure.
    |-rect : [left, bottom, width, height]
        |-坐标轴在Figure中的位置与大小
    |-facecolor: 字符串与四元元组：None
        |-周坐标轴填充色
    |-frameon：bool：True
        |-是否绘制坐标轴边框
    |-sharex：Axes：None
        |-使用sharex指定的坐标轴的属性
    |-sharey：Axes：None
        |-使用sharey指定的坐标轴的属性
    |-label：：''
        |-坐标轴的标签
    |-xscale：字符串：None
        |-x坐标比例尺的计算方式
        |-取值：{"linear", "log", "symlog", "logit", ...}
    |-yscale：字符串：None
        |-y坐标比例尺的计算方式
        |-取值：{"linear", "log", "symlog", "logit", ...}
    
    还有其他属性可以在这儿使用。请参考官方文档。
    
3.add_axes(rect, projection=None, polar=False, **kwargs)
    |-rect : 四元元组或者列表
        |-坐标轴位置与大小
    |-projection : {None, 'aitoff', 'hammer', 'lambert', 'mollweide', 'polar', 'rectilinear', str},
        |-坐标轴的类型
    |-polar : boolean
        |-使用极坐标，取值True等价于projection='polar'.
    |-sharex, sharey : Axes
        |-使用sharey指定的坐标轴的属性
    |-label : str
        |-坐标轴标签
    
    还有其他属性可以在这儿使用。请参考官方文档。
'''
figure = plt.figure(num='Axes坐标轴的使用与管理')
# ---------------------------------------------
# 坐标轴
ax1 = plt.Axes(
    fig=figure,
    rect=[0.05, 0.05, 0.9, 0.4],
    facecolor=(1, 0, 0, 1),
    frameon=True,
    label='坐标轴Axes对象',
    xscale='linear',
    yscale='symlog'
)
figure.add_axes(ax1)
figure.add_axes(
    [0.05, 0.55, 0.9, 0.4],  # 位置与大小，必须第一个指定，不能使用形式参数
    projection='polar',  # 坐标轴类型
    sharex=ax1,  # 共享ax1中的xaxis
    # sharey=ax1,            # 共享ax1中的yaxis
    label='函数构造的坐标轴Axes',
    facecolor=(1, 0, 1, 1),  # 还可以使用其他属性
    frameon=True,
)
# ---------------------------------------------
# 图形
line = plt.Line2D(
    [0.25, 0.5, 0.75],  # 线条的所有点的X坐标
    [0.5, 0.5, 0.5])  # 线条的所有点的Y坐标

# Figure，Axes，Artist的容器关系
ax1.add_artist(line)

# 显示图形
figure.show(warn=False)
# 显式窗体
plt.show()
