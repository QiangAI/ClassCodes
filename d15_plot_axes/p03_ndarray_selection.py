import numpy as np

m = np.array([
    [1, 2, 3, 4],
    [3, 0, 0, 6],
    [5, 6, 7, 8]
])

# print(m.take([1,0,2,1], axis=1))

# print(m.take([[1], [1]]))
#
# print(m.repeat(2))

# print(m.compress([True,False,True]))
# print(m.diagonal(-1))
# print(m.nonzero())

# out = np.empty_like(m, dtype=np.int32) # 预先分配空间
#
# n = m.choose(np.array([11,22,33,44,55,66,77,88,99,100]),out=out)
# print(n)
# print(out)

# m = np.array([1, 7, 5, 2, 9])
# print(m.searchsorted(3))

m = np.array([
    [9, 2, 3, 4],
    [3, 6, 2, 9],
    [5, 2, 7, 1]
])
# print(m)
# print(m.sort(axis= 0))  # 没有返回，直接在原数组操作
# print(m)
# print(m)
# print(m.argsort(axis= 0))  #返回排序后的元素的原来下标
# print(m)
m = np.array([1, 5, 7, 2, 4, 9, 6, 8])
n = m.argpartition(1)  # 部分排序：0,1,2
print(m)
print(n)
