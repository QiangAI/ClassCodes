import numpy as np

m = np.array([
    [1, 2, 3, 4],
    [3, 0, 0, 6],
    [5, 6, 7, 8]
])

# print(m.take([1,0,2,1], axis=1))

# print(m.take([[1], [1]]))
#
# print(m.repeat(2))

# print(m.compress([True,False,True]))
# print(m.diagonal(-1))
print(m.nonzero())
