import numpy as np

m = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [3, 6, 8, 5]
])

# 下标是整数
print(type(m[1]), m[1])
print(m[1][1], type(m[1][1]))

# 多个整数(数组中的维度中索引)
print(m[1, 2])  # 多个整数表述的元素的坐标位置

m[1] = [0, 0, 0, 0]
print(m)

# 下标是切片
# 切片对象
# sl = slice(2)
sl = slice(-1, -3, -1)
print(m[sl])

# 切片表达式
print(m[::])
print(m[1::])
print(m[::-1])

# 多个切片（切片个数与维度一致）
print(m)
print(m[..., np.newaxis, 1:3:])

# ...= ::
