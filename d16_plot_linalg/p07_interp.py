"""
插值算法：
    曲线没有函数表示。
    能够得到曲线上的一些点。根据这些点，可以计算出，某个x值得y结果
"""
import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(1, (8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])

# 1.
# x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
# y = np.sin(x)
# ax.plot(x, y)

# 2. 使用已知点，
xp = np.arange(-2 * np.pi, 2 * np.pi, np.pi / 4)
fp = np.sin(xp)
ax.scatter(xp, fp, color=(1, 0, 0, 1))

# 3. 根据已知点，计算某个x的y
# 求pi/6
x = [np.pi / 6, np.pi / 8, np.pi / 9]
r = np.interp(x, xp, fp)
ax.scatter(x, r, color=(0, 1, 0, 1))

plt.show()
