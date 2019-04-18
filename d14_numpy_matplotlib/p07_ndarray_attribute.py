import cv2
import numpy as np

"""
- 数组的内存信息
ndarray.shape	形状：每个维度的长度
ndarray.ndim	Number of array dimensions.
ndarray.size	Number of elements in the array.
ndarray.itemsize	Length of one array element in bytes.


ndarray.flags	C语言中的内存信息
ndarray.strides	Tuple of bytes to step in each dimension when traversing an array.
ndarray.data	Python buffer object pointing to the start of the array’s data.
ndarray.nbytes	Total bytes consumed by the elements of the array.
ndarray.base	Base object if memory is from some other object.

- 数组的数据类型
ndarray.dtype	Data-type of the array’s elements.

- 数组的其他属性

ndarray.T	Same as self.transpose(), except that self is returned if self.ndim < 2.
ndarray.flat	A 1-D iterator over the array.

ndarray.real	The real part of the array.
ndarray.imag	The imaginary part of the array.

ndarray.ctypes	An object to simplify the interaction of the array with the ctypes module.

"""

m = cv2.imread('bea.jpg')
print(m.shape)
print(m.ndim)
print(m.size)
print(m.itemsize)
print(m.base)
# print(m.dtype.descr)  # 只适用numpy的内置类型

print(m.T.shape)  # 维度逆序
print(m.flat)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
bts = bytes(lst)

n = np.ndarray(shape=(3, 3), dtype=np.int8, buffer=bts)
print(n)
print(n.base)
print(n.T)
for i in n.flat:
    print(i, type(i))
