"""
numpy随机模块的排列运算
    shuffle(x)
        |- 对x的数据进行直接洗牌。
    permutation(x)
        |- 利用x的数据洗牌产生新的拷贝数据。
"""

import numpy as np
import numpy.random as rd

a = np.arange(0, 10)
r = rd.shuffle(a)  # 没有返回值，a被洗牌
print('shuffle:', a, r)

a = np.arange(0, 10)
r = rd.permutation(a)  # 返回洗牌的结果
print('permutation:', a, r)
