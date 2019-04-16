from statistics import *

lst = [1, 2, 3, 4, 5]
# print(mean(lst))
# print(harmonic_mean(lst))   # 6/(1/1 + 1/2 + 1/3 + 1/4 + 1/5 + 1/6)
# print(median(lst))
# print(median_low(lst))
# print(median_high(lst))
# print(median_grouped(lst))


print(pstdev(lst))  # 偏差 = 方差的平方根
print(pvariance(lst))  # 有偏方差（总体方差）  = (x-平均数 )**2  求平均数/ 数据长度
print(stdev(lst))  # 偏差
print(variance(lst))  # 无偏方差 （样本方差） = (x-平均数 )**2  求平均数 / 数据长度-1

print(pvariance(lst, mu=5))  # 指定方差计算的平均数
