"""
Axes.hist2d(
    x,
    y,
    bins=10,
    range=None,
    normed=False,
    weights=None,
    cmin=None,        # 小于cmin的bin不被显示
    cmax=None, *,     # 大于cmax的bin不被显示
    data=None,
    **kwargs)

-----------------------
cmap使用
使用matplotlib.cm.get_cmap('颜色名')获取颜色映射，
颜色名在colors模块中，可以查找。

"""
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

# 多维数据直方图(行表示数据，列表示数据种类)
figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
# 显示图形

# ---------2维数据
x = np.random.randn(10000)
y = np.random.randn(10000)
r = ax.hist2d(
    x,
    y,
    bins=100,  # np.arange(-5, 6, 1,dtype=np.float32),  # 箱子个数
    range=[[-5, 5], [-5, 5]],
    cmap=cm.get_cmap('hot')
)
# print(r)
# ----------------------------------------------
figure.show(warn=False)
# 显式窗体
plt.show()

print(cm.get_cmap('hot'))
