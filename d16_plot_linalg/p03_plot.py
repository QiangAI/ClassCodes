import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(1, figsize=(8, 6))

ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-2 * np.pi, 2 * np.pi)
# x = np.linspace(-2 * np.pi, 2*np.pi, 10)
x = np.linspace(-5, 5, 100)
y = np.sinh(x)  # 按位运算 element-wise

ax.plot(x, y)

plt.show()

# p = [0,1,2,6, 10]
# print(np.unwrap(p))
