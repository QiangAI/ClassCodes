import numpy as np

m1 = np.diag([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], k=-1)

print(m1)

m2 = np.tri(4, 4, k=-2, dtype=np.float32)
print(m2)

# np.aamatrix等价
m3 = np.mat([1, 2, 3])
print(m3)
