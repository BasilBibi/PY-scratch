class A:
    clazz_var = 1
    _priv_clazz_var = 10
    __mangled_clazz_var = 100

    def __init__(self, iv):
        self.inst_var = iv
        self._priv_inst_var = iv
        self.__mangled_inst_var = iv

class B(A):
    another_clazz_var = 100
    _another_priv_clazz_var = 100
    __another_mangled_clazz_var = 100

    def __init__(self, iv, aiv):
        A.__init__(self, iv)
        self.another_inst_var = aiv
        self._another_priv_inst_var = aiv
        self.__another_mangled_inst_var = aiv
