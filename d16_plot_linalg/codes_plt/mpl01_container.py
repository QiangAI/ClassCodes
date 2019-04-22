# coding=utf-8
import matplotlib.pyplot as plt

'''
Figure的对象与构造
    FigureManager
        |-Figure
            |-Axes
                |-Artist
                    |-Line2D
                    |-Patch
                    |-Legend
                    |-Text
                    |-_BaseImage
                    |-Table
                    |-OffsetBox
                    |-AnnotationBbox
                    |-Collection
                    |-QuiverKey
'''

# Figure:Figure不建议使用构造器构造，而是使用pyplot提供的函数构造
figure = plt.figure('窗体标题')
# 坐标轴
ax = plt.Axes(
    figure,  # 坐标轴所在图形
    [0, 0, 1, 1])  # 坐标的区域
# 图形
line = plt.Line2D(
    [0, 0.25, 0.5, 0.75, 1],  # 线条的所有点的X坐标
    [0, 1, 0, 1, 0])  # 线条的所有点的Y坐标

# Figure，Axes，Artist的容器关系
ax.add_artist(line)
figure.add_axes(ax)
# 显示图形
figure.show(warn=False)
# 显式窗体
plt.show()
