import csv

import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


#  使用plt中画布，实现绘制
class PLTCanvas(FigureCanvas):

    def __init__(self):
        self.fig = plt.figure('图像', figsize=(8, 6), dpi=100)
        super(PLTCanvas, self).__init__(self.fig)
        # 开始绘制
        self.show_jobs()

    def show_jobs(self):
        # 读取数据
        data = self.read_jobs()
        # 构造坐标系
        ax = self.fig.add_subplot(111)

        # 绘制图形
        lines = ax.plot(data.keys(), data.values(), label='岗位')
        line = lines[0]
        line.set_color((1, 0, 0, 1))
        line.set_marker('o')
        # line.color=(1,0,0,1)
        ax.legend()
        # self.fig.show()  # 不在FigureManager。所以条用存在问题

    def read_jobs(self):
        fields = ['工作年限', '学历', '职位', '薪水', '城市', '发布时间']
        data = {}
        with open('jobs.csv', 'r') as fd:
            # 1.2. 构建DictReader
            reader = csv.DictReader(fd, fieldnames=fields)
            # 1.3. 读取（顺便统计）
            for row in reader:
                if row['城市'] in data:
                    data[row['城市']] += 1
                else:
                    data[row['城市']] = 1
        return data


# 创建Qt应用+窗体，把画布添加到窗体
app = QApplication([])

widget = QWidget()
widget.setWindowTitle('职位可视化')
canvas = PLTCanvas()
canvas.setParent(widget)
widget.show()

app.exec()
