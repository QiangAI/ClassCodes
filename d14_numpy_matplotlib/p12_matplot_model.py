import matplotlib.pyplot as plt
import numpy as np

# 对象创建两种方式
#   |- 直接构造对象
#   |- plt中的函数直接创建

# 创建一个 Figure(Figure最好不要自己创建)
figure = plt.figure('绘图', figsize=(8, 6), dpi=100)

# 创建Axes
ax = plt.Axes(figure, [0.1, 0.1, 0.8, 0.8], label='我的坐标系')
# 创建Artist
x = np.linspace(0, 1, 11)
y = np.array([0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.2, 0.7, 0.5])
# line = plt.Line2D(x, y)

# 维护关系
# ax.add_artist(line)

# 直接使用坐标系的绘制
ax.scatter(x, y)
figure.add_axes(ax)
# 显示/保存
figure.show(warn=False)  # 图显示
figure.savefig('figure.png')
plt.show()  # 窗体显示
