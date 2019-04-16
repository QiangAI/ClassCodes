import decimal
import math

# 实现精度更高的算法，请不要直接使用int，float，请使用Decimal高精度类型
# flgs = {}
# ctx = decimal.Context(
#     prec=4,
#     rounding=decimal.ROUND_CEILING,
#     Emax=100,
#     Emin=-100,
#     capitals=1,
#     clamp=True,
#     traps={decimal.InvalidOperation: True}, flags=flgs)
#
# decimal.setcontext(ctx)

with decimal.localcontext() as ctx:
    ctx.prec = 4
    ctx.traps[decimal.DivisionByZero] = True
    a = decimal.Decimal('12.13424354324233546464674746447474747647')
    # print(a)
    b = decimal.Decimal('33.13424353646474744747474747474747')
    print(a + b)
    print(a / decimal.Decimal('0'))

n = decimal.Decimal('0.49999999999999999999999')
# print(n/0)
# Python 提供规范，接口，满足接口，您的类型可以在传统的函数中使用，Decimal与float一样的方便
print(math.asin(n))
# numpy

# print(isinstance(b, numbers.Number))
#
# ctx = decimal.getcontext()
# print(ctx.prec)
# print(ctx.rounding)
# print(ctx.flags)  # 每次运算产生的标记
# print(ctx.traps)  # 设置的标记
# print(ctx.Emin)
# print(ctx.Emax)
# print(ctx.clamp)   # 指数是否包含精度
# print(ctx.capitals) # 0,1表示科学记数法的e的大小写
