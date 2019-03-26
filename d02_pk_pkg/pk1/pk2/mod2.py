v1 = 10
_v2 = 20
__v3 = 30


class Cls1(object):
    cv1 = 40
    _cv2 = 50
    __cv3 = 60

    def __init__(self):
        self.iv1 = 70
        self._iv2 = 80
        self.__iv3 = 90

    def m1(self):
        print('m1')

    def _m2(self):
        print('m2')

    def __m3(self):
        print('m3')


oi = Cls1()
print(oi._iv2)
print(oi.iv1)
print(Cls1._cv12)
oi._m2()
