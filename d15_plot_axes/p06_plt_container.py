import matplotlib.pyplot as plt

# 应该有FigureManager（全局，在plt内部管理）


# 创建Figure图像（显示一个图像：当前图像，激活图像）
#    |- Figure创建（自己创建的Figure没有被管理）
#    |- plt的函数创建
# figure = plt.Figure() 这种创建方式，可以使用，但需要使用FigureManager纳入管理
"""
figure(
    num=None, 整数，字符串（使用字符串）
    figsize=None, 
    dpi=None, 
    facecolor=None, 
    edgecolor=None, 
    frameon=True, 
    FigureClass=<class 'matplotlib.figure.Figure'>, 
    clear=False, **kwargs)
"""
# figure = matplotlib.figure.Figure()
figure = plt.figure(
    num='我的图形',
    figsize=(8, 6),  # 图像的高度与宽度
    dpi=100,
    facecolor="xkcd:sky blue",
    edgecolor='red',
    frameon=True
)
figure.linewidth = 10

# 创建坐标系Axes:图中可以有做个坐标系（同时显示，需要指定位置与大小）
#       | - Axis 坐标轴（XAxis，YAxis）
#              |- 刻度，标签，格式化器
# Figure.add_axes(axes对象 | 参数 )
# 使用函数构建
ax = plt.Axes(
    figure,
    rect=[0.1, 0.5, 0.8, 0.3],
    label='坐标系2',
    facecolor=(0, 0, 1, 1),
    frameon=True,
    xscale='log',
    yscale='linear'

)
figure.add_axes(ax)

figure.add_axes(
    [0.1, 0.1, 0.8, 0.3],
    projection='polar',
    label='坐标系1',
    facecolor=(0, 1, 0, 1),
    frameon=True,
    sharex=ax,
    sharey=ax,
    xscale='linear',
    yscale='log'
)

# 绘制图形Artist（分成很多类型：线条，矩形，文本，图像）


# 显示Figure（被FigureManager管理的Figure才能显示）

# 显示窗体（当前Figure自动显示）
figure.show(warn=True)
plt.show()
