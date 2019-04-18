#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
1.构造Figure对象需要的属性
pyplot.figure函数需要的参数：
    matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
    |- num : 整数或者字符串: None
        |-Figure的内部标示ID，如果是字符串也会作为窗体标题
        |-如果没有设置num，或者是整数，figure的ID会自动按序生成。
    |- figsize : 2元小数元组: rcParams["figure.figsize"] = [6.4, 4.8]
        |-窗体大小(英寸为单位)
    |- dpi : 整数类型: rcParams["figure.dpi"] = 100
        |-分辨率，每英寸的像素个数
    |- facecolor :字符串或者4元元组: rcParams["figure.facecolor"] = 'w'
        |-Figure的主体颜色
    |- edgecolor :字符串或者4元元组: rcParams["figure.edgecolor"] = 'w'
        |-Figure的边界颜色
    |- frameon : bool:True
        |-是否绘制Frame边框
    |- FigureClass : Figure子类：Figure
        |-一般指定figure函数创建Figure对象的类（必须是Figure的子类），默认是Figure
    |- clear : bool: False
        |-如果num指定的Figure存在，则清除。
Figure类构造器参数:
    class matplotlib.figure.Figure(figsize=None, dpi=None, facecolor=None, edgecolor=None, linewidth=0.0, frameon=None, subplotpars=None, tight_layout=None, constrained_layout=None)
    |-figsize : 2元小数元组: rcParams["figure.figsize"]
        |-英寸为单位的元组表示(width, height).
    |-dpi : float: rcParams["figure.dpi"]
        |-没英寸的点数（像素）
    |-facecolor : 字符与4元元组: rcParams["figure.facecolor"]
        |-设置的是Figure的patch(小区域块)的填充颜色facecolor.
    |-edgecolor : 字符与4元元组: rcParams["figure.edgecolor"]
        |-设置的是Figure的patch(小区域块)的边界颜色edgecolor.
    |-linewidth : float
        |-边框的线条宽度.
    |-frameon : bool: rcParams["figure.frameon"]
        |-True就绘制边框.
    |-subplotpars : SubplotParams：rcParams["figure.subplot.*"]
        |-Subplot子图的参数.
    |-tight_layout : bool或者字典: rcParams["figure.autolayout"]
        |-If False 就使用subplotpars. 
        |-If True 使用缺省的padding实现tight_layout. 
        |-字典：使用key参数：pad, w_pad, h_pad, and rect实现tight_layout.
    |-constrained_layout : bool：rcParams["figure.constrained_layout.use"]
        |-True：实现 constrained layout. 与tight_layout类似,但比tight_layout灵活.
        |-该参数对subplot()与 subplot2grid()无效.
2.上面的参数只有三个提供属性模式访问
    |-number
    |-dpi
    |-frameon
3.Figure的属性都提供set/get函数设置与获取
    set_xxxx(value)
    value=get_xxxx()
    |-get_dpi()
        |-set_dpi(val)
    |-get_edgecolor()
        |-set_edgecolor(color)
    |-get_facecolor()
        |-set_facecolor(color)
    |-get_figheight()
        |-set_figheight(val, forward=True)  
            |-#forward用来控制：当设置尺寸过大，窗体是否自动调整大小。
    |-get_figwidth()
        |-set_figwidth(val, forward=True)
            |-#forward用来控制：当设置尺寸过大，窗体是否自动调整大小。
    |-get_size_inches()
        |-set_size_inches(w, h=None, forward=True)
            |-#forward用来控制：当设置尺寸过大，窗体是否自动调整大小。
    |-get_frameon()
        |-set_frameon(b)
    |-get_tight_layout()
        |-set_tight_layout(tight)
    |-get_constrained_layout()
        |-set_constrained_layout(constrained)
    |-get_constrained_layout_pads(relative=False）
        |-set_constrained_layout_pads(**kwargs)
4.Figure参数的rcParams设置：
    Figure的参数还可以通过matplotlib.rcParams['xxxx']来设置
5.注意：
    除了在构造器外，Figure没有提供title，linewidth的设置方式
    阅读源代码知道，对窗体标题的处理有下面代码完成
        |-figManager.set_window_title(figLabel)
        |-figManager.canvas.figure.set_label(figLabel)  #这个是Figure的标签,来自Artist类
    获取figmanager可以使用pyplot函数实现
        FigureManager=plt.get_current_fig_manager()
            |-返回对象类型：NSWindow
        如果不存在Figure，会自动返回，plt.figure一般会创建一个新的。所以该函数最好在Figure创建后调用
'''
# ---------------------------------------------
# Figure
figure = plt.figure(
    num='Figure使用与管理',  # 窗体ID，字符串也是窗体标题
    figsize=(6.4, 4.8),  # 窗体大小（英寸）
    dpi=150,  # 分辨率
    facecolor=(1, 0, 0, 1),  # 填充色
    edgecolor='b',  # 边界色
    frameon=True,  # 是否绘制边框
    linewidth=5  # 来自Figure构造器的绘制变量的线条宽度
)
FigureManager = plt.get_current_fig_manager()
FigureManager.set_window_title('换一个窗体标题')
# 当坐标轴填满Figure,上面的某些属性看不见效果，比如facecolor与edgecolor，linewidth
# 属性方式访问
figure.dpi = 50
figure.frameon = False
figure.number = 2
# set/get方式访问
figure.set_dpi(60)
figure.set_figheight(8)
figure.set_size_inches(8, 8)
# ---------------------------------------------
# 坐标轴
ax = plt.Axes(
    figure,  # 坐标轴所在图形
    [0.1, 0.1, 0.8, 0.8])  # 坐标的区域
# 图形
line = plt.Line2D(
    [0.25, 0.5, 0.75],  # 线条的所有点的X坐标
    [0.5, 0.5, 0.5])  # 线条的所有点的Y坐标

# Figure，Axes，Artist的容器关系
ax.add_artist(line)
figure.add_axes(ax)
# 显示图形
figure.show(warn=False)
# 显式窗体
plt.show()
