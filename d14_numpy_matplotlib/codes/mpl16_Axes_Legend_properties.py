#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
操作并管理Axes中的Legend。
1、绘制主题：
    |-Axes.legend(*args, **kwargs)
    返回matplotlib.legend.Legend对象
        |-handles : sequence of Artist, optional
        |-labels : sequence of strings, optional
        |-loc : int or string or pair of floats, : rcParams["legend.loc"] 
            指定主题的位置，可以使用字符串：codes代码。也可以使用二元的绝对坐标
                |-loc='lower right'
                |-loc=4
                |-loc=(0.9,0.1)
                上述三种方式都在下右位置
                当使用坐标形式的时候，bbox_to_anchor失效。
            |-('best' for axes, 'upper right' for figures)
            |-'best'	0
            |-'upper right'	1
            |-'upper left'	2
            |-'lower left'	3
            |-'lower right'	4
            |-'right'	5
            |-'center left'	6
            |-'center right'	7
            |-'lower center'	8
            |-'upper center'	9
            |-'center'	10
        |-bbox_to_anchor : BboxBase, 2-tuple, or 4-tuple of floats
            |-绝对控制主题的位置，前提是loc不要使用浮点数坐标形式
            |-loc用来控制在一个区域中的位置方式
            |-bbox_to_anchor用来确定一个区域，默认是axis或者figure的坐标系
            |-loc='upper center', bbox_to_anchor=(0.5,0.5),表示以（0.5，0.5）为锚点的上中位置（既主题的下中点就在（0.5，0.5））
            |-loc与锚点之间略有一点间隔
        |-ncol : integer
            |-控制列数
        |-prop : None or matplotlib.font_manager.FontProperties or dict
            |-字体控制
                |-family: A list of font names in decreasing order of priority. The items may include a generic font family name, either 'serif', 'sans-serif', 'cursive', 'fantasy', or 'monospace'. In that case, the actual font to be used will be looked up from the associated rcParam.
                |-style: Either 'normal', 'italic' or 'oblique'.
                |-variant: Either 'normal' or 'small-caps'.
                |-stretch: A numeric value in the range 0-1000 or one of 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded' or 'ultra-expanded'
                |-weight: A numeric value in the range 0-1000 or one of 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'
                |-size: Either an relative value of 'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large' or an absolute font size, e.g., 12
        |-fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
        |-numpoints : None or int
            |-在主题中控制marker的显示格式（就是主题中的图形也显示marker，如果线条设置了marker得话）也可以使用参数设置：rcParams["legend.numpoints"]
        |-scatterpoints : None or int
            |-在主题中显示散点的marker数量：，可以使用rcParams["legend.scatterpoints"]设置
        |-scatteryoffsets : iterable of floats
            |-控制散点在主题中的垂直偏离位置，缺省值是[0.375, 0.5, 0.3125]
            |-0与主题文本对齐，1上对齐，0.5同一高度
        |-markerscale : None or int or float
            |-marker的方法比例，可以使用rcParams["legend.markerscale"]设置
        |-markerfirst : bool
            |-控制marker绘制的啥位置，True在左，False在右
        |-frameon : None or bool
            |-控制边框的绘制，True就绘制
            |-可以使用 rcParams["legend.frameon"].设置
        |-fancybox : None or bool
            |-与frameon一起使用才有效果，就是控制是否圆角矩形
            |- rcParams["legend.fancybox"].
        |-shadow : None or bool
            |-rcParams["legend.shadow"]
        |-framealpha : None or float
            |-控制主题的背景透明度
            |-rcParams["legend.framealpha"]
        |-facecolor : None or "inherit" or a color spec
            |-rcParams["legend.facecolor"]
            |-因为继承，也会从rcParams["axes.facecolor"]获取
        |-edgecolor : None or "inherit" or a color spec
            |-rcParams["legend.edgecolor"],也可以设置 rcParams["axes.edgecolor"]
        |-mode : {"expand", None}
            |-绘制的区域模式,在水平方向填充
        |-bbox_transform : None or matplotlib.transforms.Transform
            |-bbox_to_anchor的坐标系
        |-title : str or None
            |-标题
        |-title_fontsize: str or None
            |-标题的字体
        |-borderpad : float or None
            |-边界空白(单位按照字体大小度量,1表示一个字符宽度或者高度)
            |- rcParams["legend.borderpad"]
        |-labelspacing : float or None
            |-主题中标签的间隔(单位按照字体大小度量,1表示一个字符宽度或者高度)
            |-rcParams["legend.labelspacing"]
        |-handlelength : float or None
            |-rcParams["legend.handlelength"]
            |-handle的长度（单位按照字体大小度量）
        |-handletextpad : float or None
            |-rcParams["legend.handletextpad"].
            |-控制handle与标签文本间的距离（单位按照字体大小度量）
        |-borderaxespad : float or None
            |-rcParams["legend.borderaxespad"].
            |-坐标轴与主题之间的距离（单位按照字体大小度量）
        |-columnspacing : float or None
            |-rcParams["legend.columnspacing"]
            |-多列之间的距离（单位按照字体大小度量）
        |-handler_map : dict or None
            |-可以使用其他对象映射到handle，产生不同的handle效果
2、返回主题：
    |-Axes.get_legend()
        |-返回Legend对象
    |-Axes.get_legend_handles_labels(legend_handler_map=None)
        |-返回Legend句柄与标签
'''

figure = plt.figure('Legend使用', figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_ylim(-1, 1)
ax.set_xlim(-1, 1)
line1 = plt.Line2D(
    xdata=np.linspace(-1, 1, 20),
    ydata=np.random.uniform(-1, 1, size=20),
    label='Line1',
    color=(1, 0, 0, 1),
    marker='.'
)
line2 = plt.Line2D(
    xdata=np.linspace(-1, 1, 20),
    ydata=np.random.uniform(-1, 1, size=20),
    label='Line2',
    color=(0, 1, 0, 1),
    marker='v'
)
ax.add_artist(line1)
ax.add_line(line2)

# ---------------------------------------------
# 用法一：自动映射标签（根据添加的顺序自动映射）
# lg1 = ax.legend(labels=['x', 'y'])
# 用法二：定制映射标签
# lg2 = ax.legend(handles=[line1, line2], labels=['x', 'y'])

# 常见属性使用：
lg2 = ax.legend(
    handles=[line1, line2],
    labels=['x', 'y'],  # 定制标签，默认是Artist的label属性提供的标签，调用get_label获取
    loc='upper left',  # 标签的为位置，三种方式4, 'lower right'  (0.85, 0.00)
    bbox_to_anchor=(0.5, 0.5, 0.5, 0.5),  # 控制位置的锚点与区域，位置：(x, y)说明loc以改点为锚点，位置与大小：(x, y, width, height)说明loc再该区域来设置位置。
    ncol=1,  # 主题的列数(默认一列，行数自动计算)
    prop={  # 控制主题的字体
        'size': 9
    },
    numpoints=3,  # 主题中显示marker的个数，前提是Line2D需要设置marker
    markerfirst=False,  # marker在右，默认在左
    frameon=True,
    fancybox=True,  # 与frameon一起使用才有效果，就是控制是否圆角矩形
    mode=None,  # "expand",     # x方向扩展填充整个区域
    title='主题',
    borderpad=1,  # 边界宽度，以一个字大小为单位
    labelspacing=2,  # 显示内容见的间隔,以一个字大小为单位
    handletextpad=4,  # 控制handle与text的距离
    borderaxespad=0  # 控制坐标轴与主题之间的间距
)
ax.grid(b=True, which='both')  # 为了更好显示loc与bbox_to_anchor的结合控制位置
# ---------------------------------------------
figure.show(warn=False)
plt.show()
