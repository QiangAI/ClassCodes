#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
操作最重要的对象Axis--Label
操作最重要的对象Axis--Locator
    |-xaxis
        |-Axes.get_xaxis()返回XAxis对象
    |-yaxis
        |-Axes.get_yaxis()返回YAxis对象

1.标签控制主要包含位置与文本（内容，文本样式等）
    |-Axis.set_label_coords	
        |-设置标签的坐标系（就是坐标变换）
    |-Axis.set_label_position	
        |-设置标签的位置
        |-取值下面两个：{'top', 'bottom'}之一
    |-Axis.set_label_text	
        |-设置标签的文本
    |-Axis.get_label_position	
        |-返回标签的位置
    |-Axis.get_label_text	
        |-返回标签的文本对象
2.tick
主刻度
    |-Axis.get_major_ticks	
    |-Axis.get_majorticklabels	
    |-Axis.get_majorticklines	
    |-Axis.get_majorticklocs	

细刻度
    |-Axis.get_minor_ticks	
    |-Axis.get_minorticklabels	
    |-Axis.get_minorticklines	
    |-Axis.get_minorticklocs	

通用属性
    |-Axis.get_offset_text	
    |-Axis.get_tick_padding	
    |-Axis.get_ticklabels	
    |-Axis.get_ticklines	
    |-Axis.get_ticklocs	
    |-Axis.get_gridlines	
    |-Axis.grid	
'''
figure = plt.figure(1, figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.3, 0.8, 0.6])
# ---------------------------------------------
# 1. labels也可以直接使用方法设置
xaxis = ax.get_xaxis()
xaxis.set_label_text(
    label='x坐标轴',
    fontdict={
        'color': (1, 0, 0, 1)
    })
xaxis.set_label_position('top')
# -------------------------------
# 可以控制刻度与坐标轴的距离
ticks = xaxis.get_major_ticks()
for tick in ticks:
    tick.set_pad(20)  # 刻度与x坐标轴的距离（单位像素）

# 控制刻度的文本样式
labels = xaxis.get_majorticklabels()
for label in labels:
    label.set_color((0, 1, 0, 1))

# 控制刻度的线条样式
lines = xaxis.get_majorticklines()
for line in lines:
    line.set_color((0, 0, 1, 1))
    line.set_marker('v')
    # 线条的长度无法改变，Line2D的数据是1个点。
# 刻度的位置再这个返回，修改影响不了位置
locs = xaxis.get_majorticklocs()
locs[0] = 0.05

# 控制坐标轴网格
# Axis.grid(b=None, which='major', **kwargs)
# |- b : bool or None
#   |- 是否显示网格线,如果设置了其他参数，默认就是True
# |- which : {'major', 'minor', 'both'}
#   |-再哪儿显示网格线
# |- **kwargs : Line2D properties
#   |-网格线的属性，与Line2D的属性一样
xaxis.grid(b=True, which='major', color='r', linestyle='--')
# -------------------------------
figure.show(warn=False)
plt.show()
