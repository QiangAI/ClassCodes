import numpy.linalg as la

"""
x + y =5
2x + 4y = 18
---------------
1, 1    5
2 ,4    18

"""
a = [
    [1, 1],
    [2, 4]
]
b = [
    [5],
    [18]
]

r = la.solve(a, b)
print(r)

r = la.lstsq(a, b, rcond=None)
print(r)

print(la.inv(a))
