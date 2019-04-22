import matplotlib.pyplot as plt
import numpy as np

figure = plt.figure(1, figsize=[8, 6])
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])

x = np.linspace(-10, 10, 100)
# y = np.i0(x)
y = np.sinc(x)

ax.plot(x, y)

plt.show()
