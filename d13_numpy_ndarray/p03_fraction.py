import fractions
import numbers

# 分式运算
a = fractions.Fraction(0.75)
b = fractions.Fraction(numerator=3, denominator=4)

print(a.numerator, a.denominator)
print(b)

print(a + b)

print(fractions.gcd(12, 8))
print(isinstance(a, numbers.Integral))
