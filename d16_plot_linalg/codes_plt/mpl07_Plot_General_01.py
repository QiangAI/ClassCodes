#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt
from matplotlib.markers import MarkerStyle

'''
矩形图形绘制--Axes除了使用add_artist添加构造好的图形外，还可以使用一系列函数直接绘制
    |-Axes.plot(*args, scalex=True, scaley=True, data=None, **kwargs)
        |-返回：line数组
        |-x, y : 标量或者向量
            |-绘制线段的点坐标
            |-不使用x=，或者y=的参数名字
        |-fmt : str
            |-用来控制线段的颜色与样式，格式是：fmt = '[color][marker][line]'
            |-其中color，marker，line的取值可以参考官方文档
            |-如果fmt只有颜色，颜色增加了16进制表示:#RRGGBBAA
        |-data : 索引类型，通常是字典
            |-设置data就会替代x，y（x，y就用来作为线条的标签）
            |-data字典的key是x，y指定的标签
        |-scalex, scaley : bool: True
            |-设置为True，会根据x，y属性设置limits。
            |-设置为False不会自动scale。（观察x，y轴随x、y参数改变的变化）
        |-**kwargs : Line2D的属性
    |-Axes.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, verts=None, edgecolors=None, *, data=None, **kwargs)
        返回paths
        |-x, y : 形状为 (n, )的数组,
        |-s : 标量 或者 形状为(n, )数组,
            |-marker的大小，一般是点的2次方，缺省是rcParams['lines.markersize'] ** 2.
        |-c : 颜色或者颜色序列,
        |-marker : MarkerStyle(包含marker与markerstyle)
        |-cmap : Colormap: None
            |-颜色空间
        |-norm : Normalize: None
            |-当c是浮点数数组的时候使用，一把使用缺省值： colors.Normalize
        |-vmin, vmax : scalar: None
            |-与norm一起使用
        |-alpha : scalar: None
        |-linewidths : scalar 或者 array_like: None
            |-marker边界的线条宽度
        |-edgecolors : color or sequence of color: 'face'
            |-'face': 边界颜色与face颜色相同.
            |-'none': 不绘制边界.
            |-颜色与颜色序列.
    |-Axes.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)
        返回：container : BarContainer
        |-x : sequence of scalars
        |-height : scalar or sequence of scalars
        |-width : scalar or array-like:0.8
        |-bottom : scalar or array-like
        |-align : {'center', 'edge'}: 'center'
        |-tick_label : string or array-like
        |-orientation : {'vertical', 'horizontal'}, optional
            |-内部使用，如果使用horizontal，则请使用barh函数。
        |-color : scalar or array-like
        |-edgecolor : scalar or array-like
        |-linewidth : scalar or array-like(像素)
        |-xerr, yerr : scalar or array-like of shape(N,) or shape(2,N), optional
        |-log : bool, optional, default: False
'''
figure = plt.figure(1, figsize=(4, 4))
ax = figure.add_axes([0.05, 0.05, 0.9, 0.4])
# 1.plot
# -------------------------------
lines1 = ax.plot(
    [0.2, 0.7],
    [0.5, 0.5],
    '#FF0000',
    scalex=False,
    scaley=False,
)
lines2 = ax.plot(
    'x标签',
    'y标签',
    '#FF0000',
    data={
        'x标签': [0.2, 0.7],
        'y标签': [0.7, 0.7]
    },

    scalex=False,
    scaley=False,
)
# -------------------------------
# 2.scatter
# -------------------------------
ax2 = figure.add_axes([0.05, 0.55, 0.9, 0.4])
ax2.set_autoscale_on(False)
ax2.scatter(
    x=[0.3, 0.7],
    y=[0.5, 0.8],
    s=[100, 50],
    c=[(1, 0, 0, 1), (0, 0, 1, 1)],
    marker=MarkerStyle('v', 'full'),
)
# 3.bar
br = ax2.bar(
    x=[0.2, 0.5, 0.8],
    height=[0.2, 0.3, 0.4],
    width=0.05,
    bottom=[0.5, 0.1, 0.3],
    align='edge',
    tick_label=['x', 'y', 'z'],
    color=[(1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)],
    edgecolor=[(1, 1, 0, 1), (0, 1, 1, 1), (1, 0, 1, 1)],
    linewidth=[1, 2, 3],
    xerr=[0.05, -0.05, 0.05],
    yerr=[
        [0.05, 0.1, -0.05],
        [0.1, 0.2, 0.2]
    ],
    ecolor='b'
)
print(br)
# -------------------------------
figure.show(warn=False)
plt.show()
