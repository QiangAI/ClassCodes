"""
- 最小最大与范围
amin(a[, axis, out, keepdims])
    |- 数组最小值
amax(a[, axis, out, keepdims])
    |- 数组最大值
nanmin(a[, axis, out, keepdims])
    |- 数组最小值（忽略NaN）
nanmax(a[, axis, out, keepdims])
    |- 数组最大值（忽略NaN）
ptp(a[, axis, out])
    |- 取值=maximum - minimum
percentile(a, q[, axis, out, …])
    |- 计算qth的百分比位数，这个维数把数组分成2个部分。小的占q/100,大的占（100-q）/100
nanpercentile(a, q[, axis, out, …])
    |- 计算qth的百分比位数（忽略NaN）

说明：
    axis指定按照那个维度来计算,默认为None值，就是把数组reshape为1为计算。
"""

import numpy as np

a = np.random.uniform(1, 20, size=(3, 4))
print(a)
print(np.amin(a))
print(np.amax(a))
print('-----------------')
print(np.ptp(a))
print(np.percentile(a, 3))
print('-----------------')
a[1, 1] = np.NaN
print(np.nanmin(a))
print(np.nanmax(a))

a = np.array([
    [10, 7, 4],
    [3, 2, 1]
])

print(np.percentile(a, 95))  # 7是一个分界点 大的20%，小的80%，按照线性分。
# 10-7 (15/20)
print((10 - 7) * 15 / 20)
# 因为线性，最后百分之20中按照比例分。因为7是80%分界点，95-80=15，剩下20%在10-7之间分。
