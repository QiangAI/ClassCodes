"""
矩阵方程与逆

linalg.solve(a, b)
    |- 矩阵方程
linalg.lstsq(a, b[, rcond])
	|- 最小二乘法解
	|- rcond是解决早期的实现兼容，因为最小二乘法存在误差，
	|- 尤其系数矩阵没有矩阵逆的时候，是无法计算的。这个参数用来产生警告或者隐藏警告
	|- 取值None关闭警告，-1保持老版本兼容

	|- 返回：（解， 残差值，秩，奇异值）

linalg.inv(a)
    |- 矩阵的逆

------------
linalg.pinv(a[, rcond])
    |- 矩阵的伪逆

# ------张量暂时不掌握。
linalg.tensorsolve(a, b[, axes])
    |- 矩阵方程
linalg.tensorinv(a[, ind])
    |- 矩阵的逆

"""

import numpy.linalg as la

'''
  x + y = 5
  2*x + 4*y= 18
  
  [
    [1, 1], [ 5]
    [2, 4], [18]
  ]
  
  答案x=1与y=4
'''
a = [
    [1, 1],
    [2, 4]
]

b = [
    [5],
    [18]
]

print(la.solve(a, b))
print(la.lstsq(a, b, rcond=None))

# 逆

print(la.inv(a))
