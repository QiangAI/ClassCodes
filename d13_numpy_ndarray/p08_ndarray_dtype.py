import numpy as np

# Python的内置类型，python的类型的缺陷：不存在大小写
na = np.ndarray((3, 3), dtype=bool)

# Numpy的内置类型(使用numpy的内置类型)
na = np.ndarray((3, 3), dtype=np.int32)

# numpy.dtype()
# Numpy的内置类型
na = np.ndarray((3, 3), dtype=np.dtype(int))

print(type(na.dtype))
dt = np.dtype('I')
na = np.ndarray((3, 3), dtype=dt)
na = np.ndarray((3, 3), dtype='I')
print(na.dtype)

na = np.ndarray((3, 3), dtype='(2,2)i4')  # 数据类型是int32，数组元素也是数组（2，2）

print(na.dtype)

na = np.ndarray((3, 3), dtype='U10')
na[1, 1] = 'Louis Young,Hello,good boy'
print(na)

na = np.ndarray((3, 3), dtype='U10,i4,f8')
na[1, 1][0] = 'Jack'
na[1, 1][1] = 20
na[1, 1][2] = 88.88
print(na)

na = np.ndarray(
    shape=(3, 3),
    dtype=np.dtype([('name', ('U', 10)), ('age', 'i4')]))

na[0, 0]['name'] = 'Louis'
na[0, 0]['age'] = 20
print(na)

na = np.ndarray(
    shape=(3, 3))
print(na)
