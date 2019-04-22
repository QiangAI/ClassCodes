#!/usr/bin/python
# coding=utf-8
import random

import matplotlib.pyplot as plt

'''
Artist构建与绘制--Line2D
1.构造器使用
class matplotlib.lines.Line2D(
    |-xdata, 
        |-绘制的x坐标，与下面的ydata对应形成坐标点
    |-ydata, 
        |-绘制的y坐标，与上面的xdata对应形成坐标点
    |-linewidth=None, 
        |-线条宽度
    |-linestyle=None,
        |-线条样式
            |-实线    :'-'     或者 'solid'
            |-虚线    :'--'    或者 'dashed'
            |-虚点线   :'-.'    或者 'dashdot'	
            |-点线    :':'     或者 'dotted'
            |-不绘制   :'None'	
            |-不绘制   :' '	
            |-不绘制   :''	
            |-定制虚线  :(offset, on-off-seq) 
    |-color=None, 
        |-线条颜色
    |-marker=None, 
        |-节点标记（节点就是xdata与ydata构成的点，就是线条的连接点）
        |-该值可以有很多字符串样式('.','v'等)，也可以使用整数编号(1-11)
    |-markersize=None,
        |-节点的大小 
    |-markeredgewidth=None, 
        |-节点宽度边界
    |-markeredgecolor=None, 
        |-节点边界颜色（端点边界宽度大一点才效果明显）
    |-markerfacecolor=None, 
        |-节点填充颜色（端点边界宽度大一点才效果明显）
    |-markerfacecoloralt='none', 
        |-节点的可选颜色
        |-当fillstyle填充分成2个部分的时候，可选颜色就有效果
    |-fillstyle=None,
        |-节点填充样式： {'full', 'left', 'right', 'bottom', 'top', 'none'} 
    |-antialiased=None, 
        |-控制线条的锯齿处理效果
    |-dash_capstyle=None, 
        |-虚线的端点样式(当线条很粗的时候，效果会明显点)
        |- {'butt', 'round', 'projecting'}
    |-solid_capstyle=None,
        |-实线的端点样式 (当线条很粗的时候，效果会明显点)
        |- {'butt', 'round', 'projecting'}
    |-dash_joinstyle=None,
        |- 虚线的链接样式（折线处的样式）(当线条很粗的时候，效果会明显点)
        |-{'miter', 'round', 'bevel'}
    |-solid_joinstyle=None, 
        |- 实线的链接样式（折线处的样式）(当线条很粗的时候，效果会明显点)
        |- {'miter', 'round', 'bevel'}
    |-pickradius=5, 
        |-选取的检测半径
    |-drawstyle=None,
        |-绘制样式,缺省的是直接连接节点。
        |-{'default', 'steps', 'steps-pre', 'steps-mid', 'steps-post'}
        |-steps=steps-pre,点在前steps-pre，中steps-mid，后steps-post，
    |-markevery=None,
        |-对节点的标记方式，
            |-every=None, 所有点都绘制.
            |-every=N, 0开始，整除N的点都绘制
            |-every=(start, N), 从start开始，整除N的点都绘制
            |-every=slice(start, end, N)指定区间，间隔N的点.被绘制
            |-every=[i, j, m, n], 指定位置的点被绘制.
            |-every=0.1,指定间隔距离附近的点被绘制.
            |-every=(0.5, 0.1) 从0.5开始，按照距离附件点被绘制
2.picker的使用
    |-set_picker(p)
        |-picker两种方式：
            |-True，用来交给Figure中的canvas的事件处理
            |-float作用与pickradius一样
            |-直接绑定一个处理函数，这个函数
                |- Tuple[bool, dict] callable[[Artist, Event]]
    |-set_pickradius(d)
'''
figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xticks([x for x in range(-100, 101, 20)])
# 显示图形
# ----------------------------------------------
line = plt.Line2D(
    xdata=[x for x in range(-100, 101, 20)],
    ydata=[random.random() for x in range(-100, 101, 20)],
    linewidth=1,
    linestyle=(0, (1, 2, 2, 1)),
    color=(1, 0, 0, 1),
    marker='.',
    markersize=20,
    markeredgewidth=2,
    markeredgecolor=(0, 1, 0, 1),
    markerfacecolor=(0, 0, 1, 1),
    markerfacecoloralt=(1, 0, 1, 1),
    fillstyle='bottom',
    antialiased=True,
    dash_capstyle='round',
    solid_capstyle='round',
    dash_joinstyle='bevel',
    solid_joinstyle='bevel',
    pickradius=5,
    drawstyle='steps-mid',
    markevery=0.2,
    label='Hello'
)

# 2. picker
'''
# picker方式一
def pick_line(event):
    print(event)


line.set_picker(True)
figure.canvas.mpl_connect('pick_event', pick_line)
'''


# picker方式二
def line_picker(obj, mouseevent):
    print(obj, mouseevent)
    return True, {}  # 第一只返回bool，判定是否点击了Artist，第二个是一个数据属性字典


line.set_picker(line_picker)
ax.add_artist(line)
# ----------------------------------------------
figure.show(warn=False)
# 显式窗体
plt.show()
