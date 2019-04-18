import numpy as np

# n1 = np.zeros(shape=(4,3), dtype=np.float64, order='F')
# print(n1)
#
# n2 = np.zeros_like(n1, dtype=np.int8 ,order='C')
# print(n2)

# numpy.eye(N, M=None, k=0, dtype=<class 'float'>, order='C')

n3 = np.eye(4, 5, k=-2, dtype=np.int32)
print(n3)

print(np.identity(4, dtype='i4'))

print(np.ones(shape=(4, 4), dtype='i4'))
print(np.zeros(shape=(4, 4), dtype='i4'))
print(np.full(shape=(4, 4), fill_value=88, dtype='i4'))
