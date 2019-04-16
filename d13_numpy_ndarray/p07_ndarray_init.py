import numpy as np

# 构造一个指定形状与类型的数组(空的数组的数据是随机：没有初始化的数据)
# na = np.ndarray(shape=(3, 3), dtype=np.int8)
# print(na)

# 使用缓存构造有数据的数组
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
buffer = bytes(lst)
print(buffer)

# na = np.ndarray(
#     shape=(3, 3),
#     dtype=np.int8,
#     buffer=buffer,
#     offset=1,   # 缓冲的偏移位置
#     strides=(2, 1))   # strides单位是字节，取值的步长（第一维，第二维，第三维，...）
na = np.ndarray(
    shape=(3, 3),
    dtype=np.int8,
    buffer=buffer,
    offset=0,
    order='F')

print(na)
