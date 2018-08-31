class A:
    def do_this(self):
        return 'doing this in A'


class B(A):
    pass


class C(A):
    def do_this(self):
        return 'doing this in C'


class D(B,C):
    pass


class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


class DD(BB, CC):
    pass
