"""
矩阵与向量的乘积
# ------------------------
dot(a, b[, out])
    |- 点积:一般对向量而言
inner(a, b)
    |- 内积就是点击
matmul(a, b[, out])
    |- 矩阵的内积
linalg.matrix_power(M, n)
    |- 矩阵的幂（n是整数）
linalg.multi_dot(arrays)
    |- 点积（多个向量一起计算）
vdot(a, b)
    |- 两个向量的点积
# ------------------------
outer(a, b[, out])
    |- 两个矩阵的外积
# ------------------------暂时不掌握
kron(a, b)
    |- 克罗内克（Kronecker）积,也称张量积与直积
tensordot(a, b[, axes])
    |- 张量积

# ------------------------
einsum(subscripts, *operands[, out, dtype, …])
    |- 爱因斯坦和
einsum_path(subscripts, *operands[, optimize])
    |- Evaluates the lowest cost contraction order for an einsum expression by considering the creation of intermediate arrays.


说明：
    我们使用dot与matmul即可。
"""

import numpy as np

a = [1, 2, 3]
b = [4, 5, 6]
print(np.dot(a, b))
print(np.inner(a, b))
print(np.matmul(a, b))
print(np.vdot(a, b))

a = np.array([[1, 2, 3]])
b = np.array([[4, 5, 6]])

print(np.dot(a, b.T))  # 向量与矩阵都计算
print(np.inner(a, b))  # 内积只争对向量
print(np.matmul(a, b.T))  # 与dot一样
print(np.vdot(a, b))  # 结果为标量

a = np.array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
])
b = np.array([
    [1, 2],
    [1, 2],
    [1, 2],
])
print(np.dot(a, b))
print(np.inner(a, b.T))  # 列数相同即可
print(np.matmul(a, b))

# print(np.vdot(a, b)) # 转换为一维在做向量积

# 张量积
print(np.tensordot(a, b, axes=1))
