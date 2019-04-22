"""
随机分布：
    beta(a, b[, size])
        |- 贝塔分布
    binomial(n, p[, size])
        |- 二项式分布
    chisquare(df[, size])
        |- 卡方分布
    dirichlet(alpha[, size])
        | 迪里克莱(Dirichlet)分布
    exponential([scale, size])
        |- 指数分布
    f(dfnum, dfden[, size])
        | -F 分布
    gamma(shape[, scale, size])
        |- Gamma分布.
    geometric(p[, size])
    	|- 几何分布
    gumbel([loc, scale, size])
        |- 耿贝尔(Gumbel)分布
    hypergeometric(ngood, nbad, nsample[, size])
        |- 超几何分布
    laplace([loc, scale, size])
        |- 拉普拉斯（Laplace）分布
    logistic([loc, scale, size])
        |- 逻辑分布
    lognormal([mean, sigma, size])
        |- 对数正态分布
    logseries(p[, size])
        |- 对数级数分布.
    multinomial(n, pvals[, size])
        |- 多项式分布
    multivariate_normal(mean, cov[, size, …)
    	|- 多元正态分布
    negative_binomial(n, p[, size])
        |- 负二项分布
    noncentral_chisquare(df, nonc[, size])
        |- 非中心卡方分布.
    noncentral_f(dfnum, dfden, nonc[, size])
        |- 非中心F分布.
    normal([loc, scale, size])
        |- 正态分布
    pareto(a[, size])
        |- Pareto II或Lomax分布.
    poisson([lam, size])
        |- 泊松(Poisson)分布
    power(a[, size])
        | -指数分布 ，取值为[0, 1] ，指数为a - 1.
    rayleigh([scale, size])
        |- 瑞利(Rayleigh)分布
    standard_cauchy([size])
        |- 标准柯西( Cauchy)分布
    standard_exponential([size])
    	|- 标准指数分布
    standard_gamma(shape[, size])
        |- 标准Gamma.分布
    standard_normal([size])
        |- 标准正态分布
    standard_t(df[, size])
        | - 标准t分布
    triangular(left, mode, right[, size])
        |- 三角形分布
    uniform([low, high, size])
        |- 均匀分布
    vonmises(mu, kappa[, size])
        |- 冯·米塞斯(von Mises)分布
    wald(mean, scale[, size])
        |- 瓦尔德(Wald)分布(逆高斯分布)
    weibull(a[, size])
        | 韦布(Weibull)分布.
    zipf(a[, size])
        |- Zipf分布.


掌握如下几种分布：
    - 均匀分布：
        |- uniform([low, high, size])
            |- 在区间[low, high)均匀概率取值，得到shape=size的数组
    - 高斯分布（正态分布）/标准高斯分布（标准正态分布）
        |- standard_normal([size])
            |- 在区间[-inf, +inf)按照标准正态分布概率取值，得到shape=size的数组
        |- normal([loc, scale, size])
            |- 在区间[-inf, +inf)按照正态分布概率取值，得到shape=size的数组
    - 拉普拉斯分布
        |- laplace([loc, scale, size])
            |- 在区间[-inf, +inf)按照拉普拉斯概率取值，得到shape=size的数组

说明：
    - 这组函数返回x坐标上的值，取得这些值的概率满足上述分布。
"""
import matplotlib.pyplot as plt
import numpy.random as rd

# print(rd.uniform(0, 1, size=(3, 4)))
# print(rd.normal(0, 2, size=(3, 4)))
# print(rd.standard_normal(size=(3, 4)))
# print(rd.laplace(0, 5, size=(3, 4)))

# 下面是拉普拉斯的分布
figure = plt.figure(num='Axes坐标轴的属性')
# 坐标轴
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
ax.set_xlim(-10, 10)

data = rd.laplace(0, 1, 1000000)
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
