"""
频率统计计算
histogram(a[, bins, range, normed, weights, …])
    |- 分段统计
histogram2d(x, y[, bins, range, normed, weights])
    |- 计算两个数据样本的二维直方图。
    |- 二维直方图是指落在矩形区域内的频率计算
histogramdd(sample[, bins, range, normed, …])
    |- 多维直方图

    
bincount(x[, weights, minlength])
    |- 计数非负整数数组中每个值的出现次数。
    |- minlength指定返回的最小箱子数
digitize(x, bins[, right])
    |- 返回输入数组中每个值所属的箱子的索引。
"""

import numpy as np

# a = np.random.uniform(-1,1,size=100)
# # r = np.histogram(a, 10, (-1, 1))
# # print(r)
x = np.random.uniform(-1, 1, size=1000)
y = np.random.uniform(-1, 1, size=1000)
r = np.histogram2d(x, y, 10, [[-1, 1], [-1, 1]])
print(r)
