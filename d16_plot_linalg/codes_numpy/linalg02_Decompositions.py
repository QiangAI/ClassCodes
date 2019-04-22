"""


linalg.qr(a[, mode])
    |- QR因子计算
    |-  QR方法是Francis于1961年发表的用于求解所有特征值的算法呢。
    |- 该算法对对称矩阵和非对称矩阵都适用，都可以分解成正交矩阵Ｑ和上三角矩阵Ｒ乘机的形式。
linalg.svd(a[, full_matrices, compute_uv])
    |- 奇异值分解

这个函数不掌握
linalg.cholesky(a)
    |- 柯列斯基(Cholesky)分解

SVD分解收说明：
    SVD也是对矩阵进行分解，但是和特征分解不同，SVD并不要求要分解的矩阵为方阵。假设我们的矩阵A是一个m×n
    的矩阵，那么我们定义矩阵A的SVD为：A=UΣVT
        其中U是一个m×m的矩阵，
        Σ是一个m×n的矩阵，除了主对角线上的元素以外全为0，主对角线上的每个元素都称为奇异值，
        V是一个n×n的矩阵。

        U和V都是酉矩阵，即满足UTU=I,VTV=I
PCA降维
    左奇异矩阵可以用于行数的压缩
    右奇异矩阵可以用于列数即特征维度的压缩

# --------------------
QR分解说明：
    如果非奇异矩阵A能够分解成正交（酉）矩阵Q与非奇异上三角矩阵R的乘积，即A=QR，
    则称其为A的QR分解。
"""

import numpy as np
import numpy.linalg as la

m = np.random.uniform(1, 10, size=(4, 5))

r = la.svd(m)
print('U:\n', r[0])
print('Σ:\n', r[1])
print('V:\n', r[2])

r = la.qr(m)
print('Q:\n', r[0])
print('R:\n', r[1])
