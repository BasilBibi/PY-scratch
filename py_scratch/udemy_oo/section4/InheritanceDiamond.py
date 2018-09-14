class A:
    def do_this(self):
        return 'This does not get called because it is inherited by B in a diamond'


class B(A):
    pass


class C(A):
    def do_this(self):
        return 'doing this in C'


class D(B, C):
    pass


########################################
  
class AA:
    pass


class BB(AA):
    pass


class CC:
    pass


class DD(BB, CC):
    pass


########################################

class AAA:
    pass


class BBB(AAA):
    def do_this(self):
        return 'doing this in BBB as shown in mro'


class CCC(AAA):
    def do_this(self):
        return 'doing this in CCC'


class DDD(BBB, CCC):
    pass
