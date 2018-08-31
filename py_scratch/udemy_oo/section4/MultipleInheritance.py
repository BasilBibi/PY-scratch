class A:
    def __init__(self, a):
        self.a = a

    def doit(self):
        return f'A: doit: {self.a}'

    def overridden(self):
        return f'A: overridden: {self.a}'

    def overridden_2(self):
        return f'A: overridden_2: {self.a}'


class B:
    def __init__(self, b):
        self.b = b

    def doit(self):
        return f'B: doit: {self.b}'

    def overridden(self):
        return f'B: overridden: {self.b}'

    def overridden_2(self):
        return f'B: overridden_2: {self.b}'

    def only_in_b(self):
        return f'only_in_b: {self.b}'


class C(A, B):
    def __init__(self, a, b, c):
        A.__init__(self, a=a)
        B.__init__(self, b=b)
        self.c = c

    def overridden(self):
        return f'C: overridden: {self.c}'

    def overridden_2(self):
        return f'C: overridden_2: {self.c} -> ' + B.doit(self)


class D(C):
    def __init__(self, a, b, c, d):
        C.__init__(self, a, b, c)
        self.d = d

    def d_can_see_everything(self):
        return f'a: {self.a}, b: {self.b}, c: {self.c}, d: {self.d}'
