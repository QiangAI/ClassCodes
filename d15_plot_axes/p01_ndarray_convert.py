import numpy as np

# 一组类型相同的元素：ndarray（数据集） : 类型不同的元素：DataFrame（记录）
m = np.array([
    [1, 2, 3, 4],
    [3, 4, 5, 6],
    [5, 6, 7, 8]
])

# print(m.item(11), m[1]) #
# print(m.item(1, 1), m[1,1])
#
# m.itemset(1, 88)
# print(m)
#
# print(m.tolist())
# print(m.tobytes())
#
# print(m.astype(dtype=np.float))

# m.tofile('a.txt', sep='|',format='%08d')
# def convert(data):
#     print(data)
#     return int(data)
#
#
# n = np.loadtxt(
#     'a.txt',
#     dtype=np.int32,
#     delimiter='|',converters={1:convert})
# print(n)
# print(n.reshape((3,4)))
#
# m.fill(99)
#
# print(m)
