import numpy as np

m = np.array([
    [9, 2, 3, 4],
    [3, 6, 2, 9],
    [5, 2, 7, 1]
])
#
# n = m.max(axis=-1,keepdims=True)
# print(n)
# n = m.argmax(axis=0)
# print(n)
# n = m.cumprod(axis=0)
# print(n)
#
# n = m.mean(axis=0)
# print(n)


n = m.var(axis=0, ddof=1)
print(n)
