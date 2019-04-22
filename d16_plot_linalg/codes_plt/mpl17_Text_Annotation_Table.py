#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np

'''
操作并管理Text与Annotations。
|-Axes.annotate
    |-使用文本标注点xy.
|-Axes.text
    |-添加文本到坐标轴
|-Axes.table
    |-添加表格到坐标轴
|-Axes.arrow	
    |-添加箭头到坐标轴
|-Axes.inset_axes
    |-添加内部子坐标轴到坐标轴	
|-Axes.indicate_inset
    |-添加内部标示器到坐标轴	
|-Axes.indicate_inset_zoom
    |-添加内部标示器到坐标轴，标示器被限制在一个内部坐标轴
1.annotate
|-Axes.annotate(s, xy, *ags, **kwargs)
    |-s : str
        |-标注的文本
    |-xy : (float, float)
        |- 标注目标的位置
    |-xytext : (float, float), optional
        |-标准文本的位置
    |-xycoords : str, Artist, Transform, callable or tuple, optional
        |-xy所在的坐标系
    |-textcoords : str, Artist, Transform, callable or tuple, optional
        |-文本所在坐标系
    |-arrowprops : dict, optional
        |-从xytext到xy的箭头属性，该属性存在，箭头就存在
        |-如果在arrowprops中使用arrowstyle，下面几个属性失效:
            |-width	箭头线条宽度
            |-headwidth	头部宽度
            |-headlength 头部长度	
            |-shrink	端点之间总长度的收缩因子
    |-annotation_clip : bool or None, optional
        |-标注是否裁剪
    |-**kwargs
        |-其他文本属性
----------------------
可思议使用 FancyArrowPatch 的属性：
    |-arrowstyle	the arrow style
    |-connectionstyle	the connection style
    |-relpos	default is (0.5, 0.5)
    |-patchA	default is bounding box of the text
    |-patchB	default is None
    |-shrinkA	default is 2 points
    |-shrinkB	default is 2 points
    |-mutation_scale	default is text size (in points)
    |-mutation_aspect	default is 1.
    |-还可以使用matplotlib.patches.PathPatch的属性（参考文档）
----------------------
arrowstyle
    |-'-'	None
    |-'->'	head_length=0.4,head_width=0.2
    |-'-['	widthB=1.0,lengthB=0.2,angleB=None
    |-'|-|'	widthA=1.0,widthB=1.0
    |-'-|>'	head_length=0.4,head_width=0.2
    |-'<-'	head_length=0.4,head_width=0.2
    |-'<->'	head_length=0.4,head_width=0.2
    |-'<|-'	head_length=0.4,head_width=0.2
    |-'<|-|>'	head_length=0.4,head_width=0.2
    |-'fancy'	head_length=0.4,head_width=0.4,tail_width=0.4
    |-'simple'	head_length=0.5,head_width=0.5,tail_width=0.2
    |-'wedge'	tail_width=0.3,shrink_factor=0.5
2.Text
|-Axes.text(x, y, s, fontdict=None, withdash=False, **kwargs)
    |-x, y : scalars    
        |-文本位置
    |-s : str
        |-文本内容
    |-fontdict : dictionary, optional, default: None
        |-文本的字体控制
    |-withdash : boolean, optional, default: False
        |-使用dash
    |-**kwargs : Text properties.
3. Arrow:
|-Axes.arrow(x, y, dx, dy, **kwargs)
    |-**kwargs
        |- FancyArrow 对象的构造器参数都可以使用,Patch的属性等，参考文档
4.table
返回 matplotlib.table.Table 对象
|-Axes.table(**kwargs)
    该函数调用的是matplotlib.table.table函数
    |-class matplotlib.table.Table(ax, loc=None, bbox=None, **kwargs)
    |-matplotlib.table.table(cellText=None, cellColours=None, cellLoc='right', colWidths=None, rowLabels=None, rowColours=None, rowLoc='left', colLabels=None, colColours=None, colLoc='center', loc='bottom', bbox=None, edges='closed')
        |-必须提供cellText or cellColours
        |-loc取值
            |-best
            |-upper right
            |-upper left
            |-lower left
            |-lower right
            |-center left
            |-center right
            |-lower center
            |-upper center
            |-center
            |-top right
            |-top left
            |-bottom left
            |-bottom right
            |-right
            |-left
            |-top
            |-bottom	
5.inset Axes
# 该函数在matplotlib3.0使用的，请更新下matplotlib模块
    |-pip install matplotlib -U
|-Axes.inset_axes(bounds, *, transform=None, zorder=5, **kwargs)[source]
    |-bounds : [x0, y0, width, height]
    |-transform : Transform
    |-zorder : number
    |-**kwargs
        |-axes.Axes的属性，用来控制位置
'''

figure = plt.figure('Legend使用', figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_ylim(-1, 1)
line = plt.Line2D(
    xdata=np.linspace(0, 1, 20),
    ydata=np.random.uniform(-1, 1, size=20),
    label='Line1',
    color=(1, 0, 0, 1)
)
ax.add_line(line)
ax.legend()
# ---------------------------------------------
# 1. Annotation
ax.annotate(
    s='标注',  # 标注的文本内容:必须
    xy=(0.9, 0.5),  # 坐标位置：必须参数，单位按照坐标单位
    xytext=(0.1, 0.1),
    arrowprops={
        'width': 2,  # 箭头线条粗细
        'headwidth': 5,
        'headlength': 5,
        'shrink': 0.1,  # 头尾的收缩因子(0-1之间)，该因子会改变线段长度
        'connectionstyle': 'angle3'  # 如果要定制链接类型，可以使用ConnectionStyle对象
    }
)
ax.annotate(
    s='标注',  # 标注的文本内容:必须
    xy=(0.9, 0.1),  # 坐标位置：必须参数，单位按照坐标单位
    xytext=(0.1, 0.9),
    arrowprops={
        'arrowstyle': 'wedge',  # 使用该属性，就不能使用width等几个属性。
        'connectionstyle': 'angle3'
    },
    color=(0, 1, 0, 1)
)
# ---------------------------------------------
# 2 .Text
t1 = ax.text(
    x=0.5,
    y=0.5,
    s='Hello World',
    fontdict={
        'size': 20
    },
    withdash=True  # 使用Line2D绘制字体,返回TextWithDash(0.5,0.5,'Hello')对象
)
t1.set_dashlength(30)  # 像素单位
t1.set_dashdirection(0)  # dash的方向0在前，1在后
t1.set_dashrotation(45)  # 旋转，单位是度。  (以文本中心旋转)
t1.set_dashpad(100)  # dash 与文本间宽度
print(t1)

# ---------------------------------------------
# 4. table
ax.table(
    cellText=[
        ['1', '2'],
        ['3', '4']],
    cellColours=[
        ['r', 'b'],
        ['g', 'w']],
    loc='bottom left',  # 位置，
    bbox=[0.5, 0.5, 0.3, 0.3]  # 配合loc使用控制表格的位置
)
# ---------------------------------------------
# 5. inset Axes(坐标轴中嵌套坐标轴)
in_ax = ax.inset_axes(
    bounds=[0.8, 0.1, 0.15, 0.15]
)
in_ax.plot(
    [0.1, 0.9],
    [0.5, 0.5],
    color='r'
)
# ---------------------------------------------
figure.show(warn=False)
plt.show()
