# coding = utf-8
import sys

import matplotlib as  mpl
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


class DataVCanvas(FigureCanvas):
    # 创建pyplot的Figure对象

    def __init__(self):
        self.figure = plt.figure(figsize=(4, 3))
        # FigureCanvas的初始化需要依赖Figure对象
        super(DataVCanvas, self).__init__(self.figure)
        self.iris_visual()

    # 鸢尾花的数据逻辑回归分类效果Qt可视化
    def iris_visual(self):
        X, y = load_iris(return_X_y=True)
        X = X[0:100, 0:2]
        y = y[50:150]

        clf = LogisticRegression(random_state=0, solver='lbfgs').fit(X, y)
        # clf = LogisticRegression().fit(X, y)
        # 预测结果
        r = clf.predict(X)

        # 权重系数
        coef = clf.coef_
        intercept = clf.intercept_
        print('权重系数：', coef)
        print('权重截距：', intercept)
        score = clf.score(X, y)
        print(score)

        # 可视化
        x1 = X[:, 0]
        x2 = X[:, 1]

        # 生成网格
        x1_min, x1_max = x1.min(), x1.max()  # 第0列的范围
        x2_min, x2_max = x2.min(), x2.max()  # 第1列的范围

        x1_min = x1_min - 0.25
        x1_max = x1_max + 0.25

        x2_min = x2_min - 0.25
        x2_max = x2_max + 0.25

        x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点
        grid_plane = np.stack((x1.flat, x2.flat), axis=1)

        z = clf.predict(grid_plane)
        # 控制区域颜色
        colors = mpl.colors.ListedColormap([(0.2, 0.8, 0.8, 1), (0.8, 0.6, 0.5, 1)])
        # 样本数据分开
        label_1 = y[0:50]
        label_2 = y[50:100]

        # 创建坐标轴
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8], label='数据集图示')
        ax.set_xbound(x1_min, x1_max)
        ax.set_ybound(x2_min, x2_max)

        ax.pcolormesh(x1, x2, z.reshape(x1.shape), cmap=colors)

        ax.scatter(X[0:50:, 0], X[0:50, 1], marker='.', color=(1, 0, 0, 1), label='A类')
        ax.scatter(X[50:100:, 0], X[50:100, 1], marker='x', color=(0, 0, 1, 1), label='B类')

        plt.legend()


# 显示图形的窗体
class DataVWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('数据可视化：Qt + Pyplot')

        self.data_v = DataVCanvas()
        self.data_v.setParent(self)
        self.show()


app = QApplication(sys.argv)

widget = DataVWidget()

sys.exit(app.exec())
