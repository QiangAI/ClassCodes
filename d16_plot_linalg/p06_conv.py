import numpy as np

x = [1, 2, 3, 4, 5, 6]  # 原始数据
y = [6, 5, 4, 3, 2, 1]  # 核

# r[0] = x0y0
# r[1] = x0y1 + x1y0
# r[1] = x0y2 + x1y1 + x2y0


print(np.convolve(x, y, mode=''))
