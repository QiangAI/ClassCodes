#!/usr/bin/python
# coding=utf-8
import matplotlib.pyplot as plt

'''
矩形图形绘制
class matplotlib.patches.Rectangle(xy, width, height, angle=0.0, **kwargs)[source]
    |-xy : (float, float)
    |-width : float
    |-height : float
    |-angle : float, optional
    |-fill : bool, optional
其他属性：
    |-hatching
        |-/   - diagonal hatching
        |-\   - back diagonal
        |-|   - vertical
        |--   - horizontal
        |-+   - crossed
        |-x   - crossed diagonal
        |-o   - small circle
        |-O   - large circle
        |-.   - dots
        |-*   - stars
'''
figure = plt.figure(1, figsize=(4, 4))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# -------------------------------
rect = plt.Rectangle(
    xy=(0.2, 0.2),
    width=0.3,
    height=0.3,
    angle=30,
    fill=True,
    hatch='/',
    snap=True)
ax.add_artist(rect)
# -------------------------------
figure.show(warn=False)
plt.show()
