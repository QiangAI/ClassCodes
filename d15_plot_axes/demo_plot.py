import csv

import matplotlib.pyplot as plt

# 1. 读取数据，并计算出每个城市的岗位数量的总和
# 1.1. 打开文件
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

# 2. 构建坐标系
figure = plt.figure('岗位信息分布图', figsize=(8, 6), dpi=100)

ax = figure.add_subplot(111)

# 3. 绘制图形
lines = ax.plot(data.keys(), data.values(), label='岗位')
line = lines[0]
line.set_color((1, 0, 0, 1))
line.set_marker('o')
# line.color=(1,0,0,1)
ax.legend()
plt.show()
