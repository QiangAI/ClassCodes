import numpy as np

# 一组类型相同的元素：ndarray（数据集） : 类型不同的元素：DataFrame（记录）
m = np.array([
    [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [5, 6, 7, 8]
    ],
    [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [5, 6, 7, 8]
    ],
    [
        [1, 2, 3, 4],
        [3, 4, 5, 6],
        [5, 6, 7, 8]
    ],
])

# n = m.reshape((6,2))
# print(n)

# n = m.resize((6,7))
# print(n)
# print(m)

# 矩阵转置
# print(m.shape)
# print(m.transpose(2,0,1).shape)  # 按照指定的维度改变形状

print(m.swapaxes(0, 2))  # 维度不能重复使用
print(m.flatten())  # 返回拷贝
n = m.ravel()  # 共享内存
n[3] = 88

print(m)

m = np.array([[[3]]])
n = m.squeeze()  # np.nexaxis :压缩维数

print(n)
