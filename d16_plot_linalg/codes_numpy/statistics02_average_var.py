"""

median(a[, axis, out, overwrite_input, keepdims])
    |- 中间值
average(a[, axis, weights, returned])
    |- 平均值（可以去加权）
mean(a[, axis, dtype, out, keepdims])
    |- 算术平均数
std(a[, axis, dtype, out, ddof, keepdims])
    |- 标准差
var(a[, axis, dtype, out, ddof, keepdims])
    |- 方差

nanmedian(a[, axis, out, overwrite_input, …])	Compute the median along the specified axis, while ignoring NaNs.
nanmean(a[, axis, dtype, out, keepdims])	Compute the arithmetic mean along the specified axis, ignoring NaNs.
nanstd(a[, axis, dtype, out, ddof, keepdims])	Compute the standard deviation along the specified axis, while ignoring NaNs.
nanvar(a[, axis, dtype, out, ddof, keepdims])	Compute the variance along the specified axis, while ignoring NaNs.
"""
import numpy as np

a = [1, 2, 3, 4, 5, 9]
print(np.median(a))
print(np.average(a))
print(np.mean(a))
print(np.std(a))
print(np.var(a))
