import matplotlib.pyplot as plt
import numpy.random as rd

# x = rd.laplace(loc=100, scale=100,size=(100000,))
# x = rd.normal(loc=0, scale=1,size=(100000,))
x = rd.standard_normal(size=(100000,))

figure = plt.figure(1, figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])

ax.hist(
    x=x,
    bins=1000
)

plt.show()
