import numpy as np

"""
- 数据类型
    - python内置类型
    - numpy内置类型
    - 字符表示方式一
        - 可以指定长度
        - （维度）类型+长度   (2,2)i4
    - 字符表示方式二
        - 不需要指定长度（指定字节序）'>I'
    - 字段
        ('U', 10)  字段
        ('name', 'U', 10) 带字段名
        
"""

# 创建空的数组

a1 = np.ndarray(shape=(3, 3), dtype=np.int32)
print(a1)

# 使用缓冲创建数组
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bts = bytes(lst)

a2 = np.ndarray(shape=(3, 3), dtype=np.int8, buffer=bts, offset=0, order='F')
print(a2)
