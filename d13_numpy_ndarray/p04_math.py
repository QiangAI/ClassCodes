import math

f1 = float('NaN')
f2 = float('Inf')

print(math.isinf(f2))  # 无穷大：累加，累乘 + 除以0
print(math.isnan(f1))
print(math.isfinite(20))

print(math.exp(10))  # 自然指数
print(math.log(10, 10))
print(math.hypot(1, -1))
print(math.sinh(1))
print((math.exp(1) - math.exp(-1)) / 2)

print(math.erf(1), 1 - math.erfc(1))
print(math.erfc(1))

print(math.e)
