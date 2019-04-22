"""
# 特殊函数与其他函数

i0(x)
    |- 阶数为0的贝瑟尔函数
sinc(x)
    |- 辛格函数

---------------
sqrt(x, /[, out, where, casting, order, …])
    |- 正的平方根
cbrt(x, /[, out, where, casting, order, …])
    |- 立方根
square(x, /[, out, where, casting, order, …])
    |- 平方

-----
heaviside(x1, x2, /[, out, where, casting, …])
	|- 重侧阶跃函数
convolve(a, v[, mode])
    |- 1维卷积
interp(x, xp, fp[, left, right, period])
    |- 1维线性插值
"""

import matplotlib.pylab as plt
import numpy as np

figure = plt.figure('正弦', figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# sin插值
x = np.linspace(-10, 10, 1000)
y = np.sin(x)
ax.plot(x, y, label='sin曲线', color='g')

# 插值表
px = np.random.uniform(-10, 10, size=20)  # 随机取20个点
px = np.sort(px)
py = np.sin(px)
# 绘制插值表
ax.scatter(px, py, label='插值表', color='r')

# 计算插值(如果计算插值的数不在插值表范围内，插值计算就会出现误差)
x_data = np.random.uniform(np.min(px), np.max(px), 5)
y_data = np.interp(x_data, px, py)
ax.scatter(x_data, y_data, label='插值表', color='b')
ax.legend()
figure.show()
plt.show()
