"""
prod(a[, axis, dtype, out, keepdims])
    |- 求积.
sum(a[, axis, dtype, out, keepdims])
    |- 求和
diff(a[, n, axis])
    |- 求n-th的离散差
ediff1d(ary[, to_end, to_begin])
    |- 数组中连续元素之间的差
    |- to_end：一个附加在结果后面的数组
    |- to_begin：一个附加在结构前面的数组

gradient(f, *varargs, **kwargs)
    |- 计算梯度(一维多维一样)
        |- 两个边界的元素直接用后一个减去前一个值，得到梯度；
        |- 对于中间的元素，取相邻两个元素差的一半，[1, 5, 6, 10]中第一个梯度就是5-1，第二个梯度(6-1)/2。
cross(a, b[, axisa, axisb, axisc, axis])
    |- 求交叉积
    |- 每个维度的长度是2或者3
    |- 交叉积就是矩阵的子式。
    |- x= (x1,x2,x3)  y=(y1,y2,y3)的交叉积是：
    |- (x2y2-x3y2, -(x1y3 - y1x3),x1y2-x2y1 )  具体看下面代码

trapz(y[, x, dx, axis])
    |- 求给定坐标轴的积分


下面是上面增加简单的NaN值处理。
nanprod(a[, axis, dtype, out, keepdims])
    |- Return the product of array elements over a given axis treating Not a Numbers (NaNs) as ones.
nansum(a[, axis, dtype, out, keepdims])
    |- Return the sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.
cumprod(a[, axis, dtype, out])
    |- Return the cumulative product of elements along a given axis.
cumsum(a[, axis, dtype, out])
    |- Return the cumulative sum of the elements along a given axis.
nancumprod(a[, axis, dtype, out])
    |- Return the cumulative product of array elements over a given axis treating Not a Numbers (NaNs) as one.
nancumsum(a[, axis, dtype, out])
    |- Return the cumulative sum of array elements over a given axis treating Not a Numbers (NaNs) as zero.


"""

import numpy as np

a = [
    [1, 5, 6],
    [1, 6, 10],
    [5, 6, 10]
]

# print(np.sum(a))
# print(np.prod(a))
# print(np.diff(a))
r = np.gradient(a, axis=1)
print(r)
# print(np.ediff1d(a))


b = [
    [1, 5, 6],
    [1, 5, 6],
    [1, 5, 6]
]
print(np.cross(a, b))

# cross计算的是子式
x = [1, 2]
y = [3, 4]
print(np.cross(x, y))  # = 1 * 4 - 2 * 3
x = [1, 2, 3]
y = [3, 5, 5]
print(np.cross(x, y))
"""
 +     -    +    (行数+列数 奇数为正，偶数为负）
2,3   1,3  1,2    
5,5   3,5  3,5
[-5,   4,   -1] 
"""

# 求面积，只有y参数，x默认间隔1，具体说明见下面图
print(np.trapz([1, 2, 3]))
"""
3  /|
2 / |
1|  |
 123 
上面这个图像围起来的面积就是[1,2,3]分段函数的积分
"""

# 注意梯度有一个很好的用途就是提取灰度图像的轮廓
