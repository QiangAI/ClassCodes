# coding = utf-8

from io import BytesIO  # 存放图像的二进制数据缓冲

import matplotlib.pyplot as plt
import numpy as np


def get_plot():
    # 1. 创建图(绘制环境)
    figure = plt.figure('3D图形', figsize=(8, 6))
    # 2. 创建3D坐标系（直接创建，使用Figure中的函数创建：这里使用函数）
    ax = figure.add_axes([0.1, 0.1, 0.8, 0.8], projection='3d')
    # 使用线条绘制马鞍面
    x, y = np.mgrid[-5:5:200j, -5:5:200j];
    z = (x ** 2 - y ** 2) / 2
    # rcount=20, ccount=20 与rstride=5, cstride=5不能同时指定
    ax.plot_surface(x, y, z, label='3D曲面', cmap=plt.cm.get_cmap('cool'))
    ax.grid(b=False)  # 网格线
    buff = BytesIO()
    plt.savefig(buff, format='png')
    return buff.getvalue()
