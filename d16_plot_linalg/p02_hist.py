"""
Axes.hist(
    x,   # 显示的数据
    bins=None,  # 箱子的数量
    range=None,  # 范围
    density=None, # True，统计的百分比（概率） False统计次数
    weights=None,  # 统计次数的权重
    cumulative=False, # 累加
    bottom=None,
    histtype='bar',  'bar', 'barstacked', 'step', 'stepfilled
    align='mid',
    orientation='vertical',
    rwidth=None,
    log=False,
    color=None,
    label=None,
    stacked=False,
    normed=None, *,  //不推荐使用。等价于density
    data=None,
    **kwargs)
"""
import matplotlib.pyplot as plt
import numpy.random as rd

# x = [1, 2, 3, 2, 3, 2, 4, 2, 1, 5, 6, 1, 3, 5, 4, 3, 2, 3, 4]
x = rd.randn(1000000)

# 创建图
figure = plt.figure('随机频率直方图', figsize=(8, 6))
# 创建坐标系
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-5, 5)
# ax.set_ylim(0, 10)
# 画图
r = ax.hist(
    x=x,
    bins=1000,
    range=[-5, 5],
    density=True,
    cumulative=False,
    bottom=[0],
    histtype='bar',
    align='mid',
    # rwidth=0.5,
    color='r',
    label='职位统计'
)

print(r)
ax.legend()
figure.show()
plt.show()
