import csv

import matplotlib.pyplot as plt

fields = ['工作年限', '学历', '职位', '薪水', '城市', '发布时间']
data = {}
with open('jobs.csv') as fd:
    reader = csv.DictReader(fd, fieldnames=fields, dialect='excel')
    for line in reader:
        if line['城市'] in data:
            data[line['城市']] += 1
        else:
            data[line['城市']] = 1

figure = plt.figure(1, figsize=(6, 4))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
xaxis = ax.get_xaxis()
ax.plot(data.keys(), data.values())
xaxis.grid(b=True)
plt.show()
