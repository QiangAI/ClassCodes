import pk1.pk2.mod2
from pk1.pk2.mod2 import _v2

print(dir(pk1.pk2.mod2))
print(pk1.pk2.mod2.v1)
print(pk1.pk2.mod2._v2)
print(pk1.pk2.mod2.__v3)

print(pk1.pk2.mod2.Cls1.cv1)
print(pk1.pk2.mod2.Cls1._cv2)
# print(pk1.pk2.mod2.Cls1.__cv3)

obj = pk1.pk2.mod2.Cls1()
print(obj.iv1)
print(obj._iv2)
# print(obj.__iv3)
print(_v2)


class Cls2:
    def __init__(self):
        self.o = pk1.pk2.mod2.Cls1()
        print(dir(self.o))


oo = Cls2()

print(pk1.pk2.mod2.Cls1.__dict__)
print(obj.__dict__)
print(obj._Cls1__iv3)
