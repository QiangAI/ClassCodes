"""
矩阵的相关性

corrcoef(x[, y, rowvar, bias, ddof])
    |- 相关系数(皮尔逊积矩相关系数)
    |- bias, ddof没有效果，已经不推荐使用
correlate(a, v[, mode])
    |- 两个1维向量的互相关.
cov(m[, y, rowvar, bias, ddof, fweights, …])
    |- 协方差矩阵
    |-  bias, ddof用来设置是否做无偏估计还是有偏估计。

协方差说明：
    |- 协方差计算公式：cov(X,Y)=E(XY)-E(X)E(Y)=E[(X-E(X))(Y-E(Y))]


相关系数：
    |- 相关系数是最早由统计学家卡尔·皮尔逊设计的统计指标，是研究变量之间线性相关程度的量，一般用字母 r 表示。由于研究对象的不同，相关系数有多种定义方式，较为常用的是皮尔逊相关系数。
    |- 计算公式：cov(X,Y)/(var(X)var(Y))^(1/2)

互相关：
    |-
"""

import numpy as np

x = np.random.uniform(0, 1, size=(3,))

y = np.random.uniform(0, 1, size=(3,))

print(np.corrcoef(x, y))

print(np.cov(x, y))

x = np.random.uniform(0, 1, size=(3,))
y = np.random.uniform(0, 1, size=(3,))

print(np.correlate(x, y))
