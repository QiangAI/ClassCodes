import numpy as np

lst = [
    [1, 2, 3],
    [4, 5, 6]
]

m = np.array(lst, dtype=np.int_)
print(m)

lst[1][1] = 88
print(type(m))

m2 = np.asmatrix((
    (1, 2, 3),
    [4, 5, 6],
    [7, 8, 9]
), dtype=np.float)

print(type(m2))

m3 = np.asmatrix([1, 2, 3], dtype=np.float)
print(m3)

m3 = np.array([1, 2, 3], dtype=np.float)
print(m3)
