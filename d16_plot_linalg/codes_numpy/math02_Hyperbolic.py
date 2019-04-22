"""
sinh(x, /[, out, where, casting, order, …])
cosh(x, /[, out, where, casting, order, …])
tanh(x, /[, out, where, casting, order, …])
arcsinh(x, /[, out, where, casting, order, …])
arccosh(x, /[, out, where, casting, order, …])
arctanh(x, /[, out, where, casting, order, …])

"""

import matplotlib.pylab as plt
import numpy as np

# print(np.hypot(3, 4))  # 斜边
# print(np.unwrap([0.1, 0.5, 1, 4, 10]))
# print(np.deg2rad(360))
# print(np.radians([360], where=[False]))
figure = plt.figure('正弦', figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
x = np.linspace(-5, 5, 10000)
y = np.sinh(x)

ax.plot(x, y, label='双曲正弦')

ax.legend()
figure.show()
plt.show()
