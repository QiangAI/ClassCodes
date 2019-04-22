"""
linalg.norm(x[, ord, axis, keepdims])
    |- 矩阵与向量的范数
    |- 不能计算0-范数
linalg.cond(x[, p])
    |- 矩阵条件数
linalg.det(a)
    |- 矩阵的行列式
linalg.matrix_rank(M[, tol, hermitian])
    |- 矩阵的秩（使用SVD分解方法）
# ----------------
trace(a[, offset, axis1, axis2, dtype, out])
    计算矩阵对角线上的和
linalg.slogdet(a)
    计算矩阵行列式的正负符号与自然对数。


矩阵范数说明：
    |- 范数的一个特例就是距离(比如一个点到远点的距离就是一个范数)
    |- 矩阵的范数分成0-范数，1-范数，2-范数
        |- 0范数：非0个数，对矩阵没有定义
        |- 1范数：向量：绝对值和，矩阵：列范数的最大值
        |- 2范数：向量：平方和的平方根，矩阵：A.TA的最大特征值的平方根。
矩阵的条件数说明：
    |- 矩阵A的条件数等于A的范数与A的逆的范数的乘积，即cond(A)=‖A‖·‖A^(-1)‖，
    |- 对应矩阵的3种范数，相应地可以定义3种条件数。
矩阵的行列式
    |- 矩阵的交叉积
矩阵的秩
    |- 矩阵的表示的向量空间的坐标系（不相关向量的个数）

"""
import numpy as np
import numpy.linalg as la

m = np.array([
    [1, 0, 1],
    [0, 1, 2],
    [3, 5, -1]
])
# 范数
print(la.norm(m, 1))  # m每列的范数的最大值
# 2范数
m = np.array([
    [4, 0, 0],
    [0, 8, 0],
    [0, 0, -1]
])

print(la.norm(m[0], 2))

# 条件数
m = np.array([
    [1, 0, 1],
    [0, 1, 2],
    [3, 5, -1]
])

print(la.cond(m, 2))

# 行列式
print(la.det(m))  # 使用的是子式计算方式，使用了除法，所有有小数误差

# 矩阵的秩
print(la.matrix_rank(m))
