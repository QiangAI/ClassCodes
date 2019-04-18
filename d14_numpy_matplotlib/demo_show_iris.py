import matplotlib.pyplot as plt
import sklearn.datasets as ds

# 加载数据
data, target = ds.load_iris(return_X_y=True)
print(data.shape, data.dtype)
# 准备绘图环境
figure = plt.figure('iris', figsize=(8, 6), dpi=100)

ax = plt.Axes(figure, [0, 0, 1, 1])
# 直接绘制

ax.scatter(data[:, 1], data[:, 2])

# 关系
figure.add_axes(ax)

# figure.show(warn=False)
plt.show()
