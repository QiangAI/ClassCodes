#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
操作并管理Axes中的Legend。
1、绘制主题：
    |-Axes.legend(*args, **kwargs)
    返回matplotlib.legend.Legend对象
        |-handles : sequence of Artist, optional
        |-labels : sequence of strings, optional
        |-loc : int or string or pair of floats, default: rcParams["legend.loc"] ('best' for axes, 'upper right' for figures)
        |-bbox_to_anchor : BboxBase, 2-tuple, or 4-tuple of floats
        |-ncol : integer
        |-prop : None or matplotlib.font_manager.FontProperties or dict
        |-fontsize : int or float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
        |-numpoints : None or int
        |-scatterpoints : None or int
        |-scatteryoffsets : iterable of floats
        |-markerscale : None or int or float
        |-markerfirst : bool
        |-frameon : None or bool
        |-fancybox : None or bool
        |-shadow : None or bool
        |-framealpha : None or float
        |-facecolor : None or "inherit" or a color spec
        |-edgecolor : None or "inherit" or a color spec
        |-mode : {"expand", None}
        |-bbox_transform : None or matplotlib.transforms.Transform
        |-title : str or None
        |-title_fontsize: str or None
        |-borderpad : float or None
        |-labelspacing : float or None
        |-handlelength : float or None
        |-handletextpad : float or None
        |-borderaxespad : float or None
        |-columnspacing : float or None
        |-handler_map : dict or None
2、返回主题：
    |-Axes.get_legend()
        |-返回Legend对象
    |-Axes.get_legend_handles_labels(legend_handler_map=None)
        |-返回Legend句柄与标签
'''

figure = plt.figure('Legend使用', figsize=(5, 4))
# 可以直接在add_axes函数中设置
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])

pie = ax.pie([2, 3, 4], labels=['X', 'Y', 'Z'])
# ---------------------------------------------
lg = ax.legend()
# ---------------------------------------------
figure.show(warn=False)
plt.show()
