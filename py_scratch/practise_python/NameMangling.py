class A:
    __clazz_var = 10

    def __init__(self, iv):
        self.__inst_var = iv

    def get_inst_var(self):
        return self.__inst_var


class B(A):
    __another_clazz_var = 100

    def __init__(self, iv, aiv):
        A.__init__(self, iv)
        self.__another_inst_var = aiv

    def get_another_inst_var(self):
        return self.__another_inst_var