#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
属性太多，我们分成几个部分说明
Axes坐标轴的使用与管理 ---- 之坐标轴外观属性
下列属性使用方式
    |-（1）可以在构造器
    |-（2）创建函数参数
    |-（3）属性访问（部分）
    |-（4）set/get方法
    |-（5）matplotlib.rcParams['xxxx']  这个是全局，影响所有坐标轴
1.外观基本属性
    |-facecolor：color
        |-填充颜色
    |-fc：color
        |与facecolor一样
    |-figure：Figure
        |-所在Figure容器
    |-frame_on：bool
        |-是否绘制边框
    |-label：object
        |-坐标轴的标签
    |-position：[left, bottom, width, height] or Bbox
        |-坐标轴的位置，大小
    |-title：str
        |-坐标轴标题
    |-visible：bool
        |-是否显示坐标轴
2.外观x-坐标轴属性
    下面属性控制这坐标轴的范围，刻度的方式，标签，其中控制坐标轴的范围分成三组，相互之间有影响；
    （xbound）（xlim）（xmargin+xscale）（xticks，xticklabels）
    
    |-xbound：unknown
        |-坐标轴范围
    |-xlabel：str
        |-坐标轴标签
    |-xlim：(left: float, right: float)
        |-坐标轴限制
    |-xmargin：float greater than -0.5
        |-坐标轴边界（中心点）
    |-xscale：{"linear", "log", "symlog", "logit", ...}
        |-坐标轴比例尺
    |-xticklabels：List[str]
        |-刻度标签
    |-xticks：list
        |-刻度
3.外观y-坐标轴属性（与x-坐标轴一样）
    |-ybound：unknown
    |-ylabel：str
    |-ylim：(bottom: float, top: float)
    |-ymargin：float greater than -0.5
    |-yscale：{"linear", "log", "symlog", "logit", ...}
    |-yticklabels：List[str]
    |-yticks：list
'''
figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.2, 0.2, 0.6, 0.3])

# 1.外观基本属性
# ---------------------------------------------
ax.set_fc((1, 0, 0))
# 控制标题
# Axes.set_title(label, fontdict=None, loc='center', pad=None, **kwargs)
ax.set_title(
    label='坐标轴标题',  # 显示的标题内容
    fontdict={  # 可以使用Text所有的字体属性，也可以附加在kwargs参数后面。
        'fontsize': 10,
        'fontweight': 900,
        'fontstyle': 'italic',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center'},  # 字体的相关属性
    loc='center',  # 取值{'center', 'left', 'right'}
    pad=10)  # 与坐标轴的间隔距离(单位是点 )
# **kwargs 其他的文本属性（参考官方文档）
'''
字体
    fontfamily	{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
    fontname	{FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
    fontproperties	font_manager.FontProperties
    fontsize	{size in points, 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
    fontstretch	{a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
    fontstyle	{'normal', 'italic', 'oblique'}
    fontvariant	{'normal', 'small-caps'}
    fontweight	{a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
'''
ax.set_visible(True)  # 设置坐标轴不可见
# Axes.set_position(pos, which='both')
ax.set_position(
    pos=[0.05, 0.25, 0.9, 0.5],  # 新的位置[left, bottom, width, height] or Bbox
    which='original'  # {'both', 'active', 'original'} 原来位置，还是绘制位置
)
# print(ax.get_position(original=True))   # which通常下active与original都是一样的，除非使用set_aspect改变方向
# ---------------------------------------------

# 2.外观x-坐标轴属性
# ---------------------------------------------
# Axes.set_ylabel(ylabel, fontdict=None, labelpad=None, **kwargs)[source]
ax.set_xlabel(
    xlabel='X坐标',  # 标签的内容
    fontdict={  # 控制标签的字体、位置等参数
        'fontsize': 12,
        'fontweight': 'bold',
        'fontstyle': 'italic',
        'verticalalignment': 'baseline',
        'horizontalalignment': 'center',
        'color': (1, 0, 0, 1)
    },
    labelpad=30  # 标签与x坐标轴的距离
)

# Axes.set_xbound(lower=None, upper=None)

ax.set_xbound(
    lower=-1,  # 坐标取值的范围（缺省是0-1）
    upper=1)

# Axes.set_xlim(left=None, right=None, emit=True, auto=False, *, xmin=None, xmax=None)
# 设置坐标轴的范围，效果与xbound一样，只是使用方式的区别
r = ax.set_xlim(
    left=-10,
    right=10,
    emit=False,  # 是否发出信号，告诉观察器，left与right参数是否改变
    auto=True  # ,
)  # xmin=-1, xmax=1) 这两个参数未来会取消，与left与right作用一样
print(r)

# 下面两个属性结合在一起使用有效
# Axes.set_xmargin(m)
# 设置边的大小: [0, 2],设置 0.1的结果是[-0.2, 2.2]，如果-0.1，则结果是[0.2, 1.8]
ax.set_xmargin(0.2)
# Axes.set_xscale(value, **kwargs)
ax.set_xscale("linear")
# print(ax.get_xlim())

# Axes.set_xticks(ticks, minor=False)
ax.set_xticks(
    ticks=[0, 2, 3.5, 5, 7],
    minor=False
)
# Axes.set_xticklabels(labels, fontdict=None, minor=False, **kwargs)
ax.set_xticklabels(
    labels=['|', 'x', 'y', 'z', 'w'],
    fontdict={
        'color': (0, 0, 1, 1)
    }
)

# ---------------------------------------------
# 图形
line = plt.Line2D(
    [0.25, 0.5, 0.75],  # 线条的所有点的X坐标
    [0.5, 0.5, 0.5])  # 线条的所有点的Y坐标

# Figure，Axes，Artist的容器关系
ax.add_artist(line)

# 显示图形
figure.show(warn=False)
# 显式窗体
plt.show()
