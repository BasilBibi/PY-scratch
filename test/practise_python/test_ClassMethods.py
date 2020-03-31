import unittest
from abc import ABC, abstractmethod


class MyAbstractClass(ABC):

    x = 20

    # def __init__(self, y):
    #    self.y = y

    @staticmethod
    def s_method(arg):
        print('s_method', arg)

    @classmethod
    def c_method(cls, arg):
        print('c_method called! cls.x: ', cls.x)
        print('c_method called! arg:', arg)
        return arg

    @abstractmethod
    def abs_method(self, arg):
        pass

    def method(self, arg):
        print(arg)
        print('X is ', self.__class__.x)
        return arg


class B(MyAbstractClass):
    pass


class C(B):

    class_var = 1000

    def __init__(self, x):
        self.inst_var = x

    def abs_method(self, arg):
        print(arg)
        print(self.__class__.x)
        print(self.x)
        return arg


class MyTestCase(unittest.TestCase):

    def test_cant_instantiate_abstract_class(self):
        MyAbstractClass()

    def test_cant_instantiate_B(self):
        B()

    def test_can_inst_C(self):
        c = C()
        self.assertEquals(c.abs_method(42), 42)

    def test_setting_X(self):

        c0 = C(25)
        print('c0.inst_var is :', c0.inst_var)
        print('c0.class_var is :', c0.class_var)

        c0.inst_var = 26
        print('c0.inst_var is now :', c0.inst_var)

        c00 = C(88)
        print('c00.inst_var is :', c00.inst_var)
        print('c00.class_var is :', c00.class_var)
        c00.class_var = 2000

        print('c0.class_var is :', c0.class_var)
        print('c00.class_var is :', c00.class_var)
        print('c00.__class__.class_var is :', c00.__class__.class_var)

        for k, v in c00.__dict__.items():
            print(k, v)

        self.assertEquals(c0.x, 20)

        c0.x = 50
        c0.abs_method(100)

        c0.method(0)
        print('c0.x ', c0.x)
        print('c0.__class__.x ', c0.__class__.x)

        self.assertEquals(c0.x, 50)

        c1 = C(300)
        self.assertEquals(c1.x, 20)

        c1.method(99)

    def test_showing_class_method_use(self):

        c = C(27)
        c.abs_method(c, 55)

        c.c_method(67)

        r = C.c_method(250)

        C.s_method(99)
        c.s_method(23345)

        self.assertEquals(r, 250)


if __name__ == '__main__':
    unittest.main()
