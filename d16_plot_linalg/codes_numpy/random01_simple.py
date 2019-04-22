"""
随机模块 - 简单随机取值

    rand(d0, d1, …, dn)
        |- 返回shape=(d0, d1, …, dn)的随机数组,取值区间[0.0, 1.0)。
    randn(d0, d1, …, dn)
        |- 返回shape=(d0, d1, …, dn)的随机数组，随机值在0左右出现的概率服从标准正态分布。
    randint(low[, high, size, dtype])
        |- 返回shape=size的随机整数数组，取值为范围[low,high)，可以使用dtype指定类型,类型必须是整数，但字节数可以不同。
    random_integers(low[, high, size])
        |- 返回shape=size的随机整数数组，取值为范围[low,high]，整数类型为np.int
    random_sample([size])
        |- 返回shape=size的随机浮点数数组，取值区间[0.0, 1.0)
    random([size])
        |- 返回shape=size的随机浮点数数组，取值区间[0.0, 1.0)
    ranf([size])
        |- 返回shape=size的随机浮点数数组，取值区间[0.0, 1.0)
    sample([size])
        |- 返回shape=size的随机浮点数数组，取值区间[0.0, 1.0)
    choice(a[, size, replace, p])
        |- 从数组a（1维数组）中随机采样生成大小为size的数组。
        |- replace取值True与False，用来指名，是否可以重复采样取值，如果False，则size的大小必须小于等于a的长度。
        |- p是一个与一样shape的1维概率数组，用来指定a中元素被选择的概率，不指定就使用均匀分布的概率
    bytes(length)
        |- 返回长度为length的字节数组

说明：
    1. 上面size默认值为None，返回一个标量随机值。
    2. randn是与其他随机取值的函数不用，他的取值范围是(-inf, +inf)，取值概率满足正态分布

"""
import matplotlib.pyplot as plt
import numpy.random as rd

# print(rd.rand(3, 4))
# print(rd.randn(3, 4))
# print(rd.randint(0, 10, (3, 4), dtype=np.int8))
# print(rd.random_integers(0, 10, (3, 4)))
# print(rd.random_sample((3,4)))
# print(rd.random((3,4)))
# print(rd.ranf((3,4)))
# print(rd.sample((3,4)))
# a = np.arange(0, 10)
#
# print(rd.choice(a, size=[3, 4], replace=True))
# ----下面是randn函数随机取值的可视化结果

figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-10, 10)
data = rd.randn(1000000)
r = ax.hist(
    x=data,
    bins=100,  # 箱子个数
    density=True,
    label='直方图',
    range=(-10, 10),  # 与城市个数相同，用来调整箱子绘制的宽度，最好与坐标范围一致ax.set_xlim(0,12)
    cumulative=False,  # 累加
    bottom=[0],  # 箱子的底边高,-1 表示绘制到y的-1位置,注意不能使用-1，必须是[]
    histtype='bar',  # {'bar', 'barstacked', 'step', 'stepfilled'},
    align='left',  # 微调bar的位置
    orientation='vertical',  # {'horizontal', 'vertical'}   一般没有必要使用horizontal横过来
    rwidth=0.5,  # histtype类型为step与stepfilled无效
    color='r',
    stacked=True,  # 多个数据才有效果
)
ax.legend()
# ----------------------------------------------
figure.show(warn=False)
# 显式窗体
plt.show()
