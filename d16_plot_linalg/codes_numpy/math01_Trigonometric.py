"""
讲解numpy三角函数的使用
sin(x, /[, out, where, casting, order, …])
    |- 正弦
cos(x, /[, out, where, casting, order, …])
    |- 余弦
tan(x, /[, out, where, casting, order, …])
    |- 正切
arcsin(x, /[, out, where, casting, order, …])
    |- 反正弦
arccos(x, /[, out, where, casting, order, …])
    |- 反余弦
arctan(x, /[, out, where, casting, order, …])
    |- 反正切
hypot(x1, x2, /[, out, where, casting, …])
    |- 返回x,y的斜边
arctan2(x1, x2, /[, out, where, casting, …])
    |- 使用x1,x2计算反正切
degrees(x, /[, out, where, casting, order, …])
    |- 弧度转化为角度
radians(x, /[, out, where, casting, order, …])
    |- 角度转换为弧度
unwrap(p[, discont, axis])
    |- Unwrap by changing deltas between values to 2*pi complement.
deg2rad(x, /[, out, where, casting, order, …])
    |- Convert angles from degrees to radians.
rad2deg(x, /[, out, where, casting, order, …])
    |-Convert angles from radians to degrees.


说明：
1. 这里难以理解的函数式unwrap函数
    numpy.unwrap(p, discont=3.141592653589793, axis=-1)
        |- unwrap函数检测相邻的两个值a和b,如果abs(p[i]-p[i-1]) > discont, 那么现在要对p[i]进行修正
        |- 修正方式：通过对p[i](修正后面一个元素)增加或者减少2pi；
        |- 这个函数的背景是因为角度变化的，比如：角度-pi/4 ，逆时针变化（增加）到-pi/4的时候，角度变成7*pi/4, 实际从循环来讲，应该是-pi/4,为了恢复到-pi/4，这就是unwrap。
        |- unwrap对数组才有效，因为需要比较前后两个值。
        |- axis是指按照那个维度开始unwrap。
2. 上面函数中的where是指运算的条件，where往往是一个函授，返回True就计算，否则不计算
3. casting='same_kind',表示是否做
3. 上面计算数据可以是标量
"""

import matplotlib.pylab as plt
import numpy as np

# print(np.hypot(3, 4))  # 斜边
# print(np.unwrap([0.1, 0.5, 1, 4, 10]))
# print(np.deg2rad(360))
# print(np.radians([360], where=[False]))
figure = plt.figure('正弦', figsize=(8, 6))
ax = figure.add_axes([0.1, 0.1, 0.8, 0.8])
x = np.linspace(-4 * np.pi, 4 * np.pi, 1000)
y = np.sin(x)

ax.plot(x, y, label='正弦')

ax.legend()
figure.show()
plt.show()
