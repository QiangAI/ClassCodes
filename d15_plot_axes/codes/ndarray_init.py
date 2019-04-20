import numpy as np

lst = (1, 2, 3, 4, 5, 6, 7, 8, 9)
bts = bytes(lst)

na = np.ndarray(shape=(3, 3), dtype=np.int8, buffer=bts, offset=0, strides=(2, 1), order='F')
print(na)

print(type(na.dtype))

dt = np.dtype('int32')  # '>i4'
print('-------------')
print('dt.type:', dt.type)
print('dt.byteorder:', dt.byteorder)
print('dt.itemsize:', dt.itemsize)
print('dt.name:', dt.name)
print('dt.shape:', dt.shape)
print('dt.fields:', dt.fields)
print('dt.flags:', dt.flags)
print('dt.str:', dt.str)
print('dt.alignment:', dt.alignment)
print('dt.base:', dt.base)
print('dt.char:', dt.char)
print('dt.descr:', dt.descr)
print('dt.kind:', dt.kind)
print('dt.names:', dt.names)
print('dt.ndim:', dt.ndim)
print('dt.num:', dt.num)
print('dt.subdtype:', dt.subdtype)
