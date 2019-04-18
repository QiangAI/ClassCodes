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
