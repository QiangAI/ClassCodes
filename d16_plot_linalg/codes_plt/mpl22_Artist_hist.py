#!/usr/bin/python
# coding=utf-8
import csv

import matplotlib.pyplot as plt

'''
- 直方图，也称频率图或者密度图，用来显示频率统计。
Axes.hist(
    x, 
        |- (n,) array or sequence of (n,) arrays
            |- 直方图数据（用来统计），类型是一维数组与一维数组序列
            |- 直方图数据表示x位置,如果是数组序列，每个数组的长度可以不同。
    bins=None, 
        |- int or sequence or str, optional
            |- 整数表示箱子个数，类型可以是整数与序列或者字符串
        
    range=None, 
        |- 绘制的范围，用来调整箱子的绘制范围，这个范围最好根据x坐标的范围一致。
    density=None, 
        |- 类型True与False或者None,True表示概率，False使用统计计数表示
    weights=None, 
        |- 每个数据的权重，类型与x一样，可以用来控制统计的结果,形状与x对应，weights与x的形状必须一致
    cumulative=False, 
        |- 是否累加，类型是True与False，或者None
    bottom=None, 
        |- 每个箱子的底边高度,类型是标量（统一高度）或者数组（对应每个箱子）
        |- 注意：标量也要采用数组。比如[1]
    histtype='bar', 
        |- 直方图类型,取值为：{'bar', 'barstacked', 'step', 'stepfilled'}, 
    align='mid', 
        | -对齐方式，bar在箱子中的对齐方式,取值为：{'left', 'mid', 'right'}, 
    orientation='vertical', 
        |- 直方图的绘制方向，取值为 {'horizontal', 'vertical'}, 
    rwidth=None, 
        |- bar在箱子中的相对宽度，数据类型是：scalar or None，histtype类型为step与stepfilled无效
    log=False, 
        |- x坐标采用log类型的scale,取值类型：bool, optional
    color=None, 
        |- 颜色
    label=None,
        |- 显示在legend中的信息 ，类型维字符串
    stacked=False, 
        |- 堆叠方式，类型是True与False
    normed=None, 
        |- 已经不推荐使用，等价于density
    *, 
    data=None, 
    **kwargs)
    
返回值：
    n : 
        返回：array or list of arrays,表示统计数据列表
    bins : 
        返回：array，箱子的边界位置
    patches : 
        返回：list or list of lists，创建的Patch Artist(Bar)对象列表
'''
figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(0, 12)
# 显示图形
# ----------------------------------------------
fields = ['工作年限', '学历', '职位', '薪水', '城市', '发布时间']

data = []
city = set()
with open('jobs.csv', 'r') as fd:
    # 1.2. 构建DictReader
    reader = csv.DictReader(fd, fieldnames=fields)
    next(reader)
    # 1.3. 读取（顺便统计）
    for row in reader:
        data.append(row['城市'])
        city.add(row['城市'])

r = ax.hist(
    x=data,
    bins=len(city),  # 箱子个数
    density=False,
    label='直方图',
    range=(0, 12),  # 与城市个数相同，用来调整箱子绘制的宽度，最好与坐标范围一致ax.set_xlim(0,12)
    cumulative=False,  # 累加
    bottom=[-1],  # 箱子的底边高,-1 表示绘制到y的-1位置,注意不能使用-1，必须是[]
    histtype='bar',  # {'bar', 'barstacked', 'step', 'stepfilled'},
    align='left',  # 微调bar的位置
    orientation='vertical',  # {'horizontal', 'vertical'}   一般没有必要使用horizontal横过来
    rwidth=0.5,  # histtype类型为step与stepfilled无效
    color='r',
    stacked=True,  # 多个数据才有效果
)
print(r)
ax.legend()
# ----------------------------------------------
figure.show(warn=False)
# 显式窗体
plt.show()
