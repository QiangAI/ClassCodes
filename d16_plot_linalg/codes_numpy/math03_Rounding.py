"""

around(a[, decimals, out])
round_(a[, decimals, out])
    |- 四舍五入
    |- decimals保留的小数点位数
rint(x, /[, out, where, casting, order, …])
    |- 四舍五入取整
fix(x[, out])
    |- 向0方向取整
floor(x, /[, out, where, casting, order, …])
    |- 向下取整
ceil(x, /[, out, where, casting, order, …])
    |- 向上取整
trunc(x, /[, out, where, casting, order, …])
    |- 去掉小数
"""

import numpy as np

a = np.random.uniform(-5, 5, size=(5,))
print(a)
print(np.around(a, 3))
print(a)
print(np.round_(a, 3))
print(a)

print(np.rint(5.495))
