"""
构建矩阵：
    |- mat(data[, dtype])
        |- 构建矩阵
    |- matrix(data[, dtype, copy])
        |- 可以使用字节字流构建

    |- asmatrix(data[, dtype])
        |- 把数组转换为矩阵
创建特殊矩阵的函数
    empty(shape[, dtype, order])
        |- 空矩阵
    zeros(shape[, dtype, order])
        |- 0矩阵
    ones(shape[, dtype, order])	Matrix of ones.
        |- 值位1的矩阵
    eye(n[, M, k, dtype, order])
        |- 对角线为1的矩阵
    identity(n[, dtype])
        |- 单位方阵
    rand(*args)
        |- 随机矩阵，取值范围(0-1)
    randn(*args)
        |- 服从标准正态分布的矩阵，取值范围(-inf, inf)

"""

import numpy.matlib as mb

print(mb.mat([1, 2, 3]))
print(mb.matrix([1, 2, 3]))

print(mb.rand(3, 3))
print(mb.randn(3, 3))
