import numpy as np
# import __future__
m1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

m2 = np.array([
    [9, 8, 7],
    [6, 5, 4]
])

m3 = 4

# print(m1 <= m2)
# print(4 == m1)

if m1.any():  # all(m1)
    print(True)

print(+m1)
print(-m1)
print(~m1)
print(abs(m1))

print(m1 + m2)
print(m1 + 4)

print(pow(m1, m2))
print(pow(m1, 4))

m1 += m2
m2 += m3
print(m1)
print(m2)

# @ 运算符号的使用：Python是个内置运算符，实际没有实现
# numpy重载运算符实现 @ 运算符重载是def __matmul__(self, value);
# @ 在数组中运算需要条件：内积：

p1 = np.array([1, 2, 3], dtype=np.int32)
p2 = np.array([4, 5, 6], dtype=np.int32)
print(p1 @ p2)

# shape = (m,n) = (4,3)
q1 = np.array([
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7],
    [8, 9, 10]
])

# shape=(n, k) = (3, 2)
q2 = np.array([
    [0.1, 0.3],
    [0.2, 0.4],
    [0.7, 0.3],
])
print(q1 @ q2)  # (m.n) (n.k) = (m.k)
"""
[[ 14  29]   14 = w0*a0+w1*a1+w2*a2(加权求和)  29 = 1*3+2*4+3*6
 [ 26  55]
 [ 38  81]
 [ 56 120]]
"""

# 0.2 * 100 +  0.8 * 99  = （0.2, 0.8）@  (100, 99)） = 加权乘积
"""
（0.1, 0.9）@  (100, 99)  数学
（0.2, 0.8）@  (88, 100)  物理 
（0.3, 0.7）@  (65, 75)  英语 

w =[
    [0.1,0.9],
    [0.2,0.8],
    [0.3,0.7]
] （3，2）） （2  3）

score= [
    [100,88,65]
    [99, 100,75]    3 *  3
]

w @ score = 最终综合乘积

"""

# 乘积的计算方式（权重系数）
w = np.array([  # 3*2
    [0.1, 0.9],
    [0.2, 0.8],
    [0.3, 0.7]
])

score = np.array([  # 2*3
    [100, 88, 65],
    [99, 100, 75]
])

print(w @ score)
print(2 @ score)
