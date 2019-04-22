import numpy as np
import numpy.random  as rd

"""
# 随机小数
rand:[0, 1)之间随机数；
randn:(-inf, inf) 每个数字取到的概率满足正态分布。 numpy.NaN, numpy.inf

# 随机整数
randint
random_integers

#  备选[0，1）
random
ranf
sample
random_sample

# 
choice(a[, size, replace, p])
    |- repalce：a中的值是否重复选择

"""

print(rd.rand(3, 4))
print(rd.randn(3, 4))

print(rd.randint(1, 5, dtype=np.int, size=(3, 4)))
print(rd.random_integers(1, 5, size=(3, 4)))

print(rd.random(size=(3, 4)))
print(rd.ranf(size=(3, 4)))
print(rd.sample(size=(3, 4)))
print(rd.random_sample(size=(3, 4)))

a = [1, 2, 3, 4, 5, 6, 6, 23, 13, 41, 1, 5, 7, 8, 3]
m = rd.choice(a, size=(3, 4), replace=False)
print(m)
