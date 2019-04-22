"""
matmul
"""
import numpy as np

# x = [1, 2, 3, 4, 5]
# y = [3, 4, 5, 6, 7]

# # 内积：dot，inner，matmul
# print(np.dot(x, y))    # 向量，矩阵
# print(np.inner(x, y))  # 向量
# print(np.matmul(x, y))  # 矩阵积


x = np.array([[1, 2, 3, 4, 5]])
y = np.array([[3, 4, 5, 6, 7]])

print(np.dot(x, y.T))  # 向量，矩阵
print(np.inner(x, y))  # 向量
print(np.matmul(x, y.T))  # 矩阵积
