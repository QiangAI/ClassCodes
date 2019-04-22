import numpy as np
import numpy.random as rd

a = np.arange(0, 10, 1)
print(a)
r = rd.shuffle(a)
print(r, a)

a = np.arange(0, 10, 1)
r = rd.permutation(a)
print(r, a)
