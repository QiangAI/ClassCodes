import fractions
import numbers

a = 20 + 20j

print(isinstance(a, numbers.Complex))
# print(a//20)


# 代数域 = （S集合, O运算） = 代数结构
print(a.imag, a.real)
print(a.conjugate())

b = 0.75  # 实数，因为Python没有引入有理数

r = fractions.Fraction('0.75')

print(r.numerator, r.denominator)

print(isinstance(r, numbers.Rational))

add = lambda x: x

# Complex -> Real -> Rational -> Integral

c = 20
print(c.numerator, c.denominator)

print(issubclass(int, numbers.Number))
# 继承这些类实现自己的数值类型
