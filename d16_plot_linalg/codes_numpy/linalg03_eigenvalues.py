"""
矩阵特征值
linalg.eig(a)
    |- 计算一个方阵的特征值和右特征向量。

linalg.eigvals(a)
    |- 计算一般矩阵的特征值。(与上面测差别就是没有返回特征向量)
--------------------
linalg.eigh(a[, UPLO])
    |-返回厄米特矩阵或对称矩阵的特征值和特征向量。
linalg.eigvalsh(a[, UPLO])
    |- 计算厄米特矩阵或实对称矩阵的特征值。

矩阵特征值说明(矩阵必须是方阵)
    |- 设A是n阶方阵，如果存在数m和非零n维列向量x，使得 Ax=mx 成立，
    |- 则称m是矩阵A的一个特征值或本征值（eigenvalue)。
    |- x称为特征右向量

"""

import numpy as np
import numpy.linalg as la

m = np.random.uniform(1, 10, size=(4, 4))

r = la.eig(m)
print('M:\n', r[0])
print('X:\n', r[1])

r = la.eigvals(m)
print(r)
