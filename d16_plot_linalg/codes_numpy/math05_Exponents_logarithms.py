"""
# 指数与对数函数

exp(x, /[, out, where, casting, order, …])
    |- 自然指数函数
expm1(x, /[, out, where, casting, order, …])
	|- exp(x) - 1 f
exp2(x, /[, out, where, casting, order, …])
    |-  计算2**p
log(x, /[, out, where, casting, order, …])
    |- 自然对数
log10(x, /[, out, where, casting, order, …])
    |- 常用对数
log2(x, /[, out, where, casting, order, …])
    |- 2为底的对数
log1p(x, /[, out, where, casting, order, …])
    |-x + ln(x)
logaddexp(x1, x2, /[, out, where, casting, …])
    |- ln(exp(x1) + exp(x2))
logaddexp2(x1, x2, /[, out, where, casting, …])
    |- log2(exp(x1) + exp(x2))
"""

import numpy as np

print(np.exp(1))
print(np.logaddexp(1, 1))

import matplotlib.pylab as plt

figure = plt.figure('正弦', figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
x = np.linspace(0, 2, 10000)
y1 = np.exp(x[1:])
y2 = np.log(x[1:])

ax.plot(x[1:], y1, label='自然指数', color='r')
ax.plot(x[1:], y2, label='自然对数', color='g')

ax.legend()
figure.show()
plt.show()
