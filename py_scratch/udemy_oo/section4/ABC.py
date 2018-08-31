from abc import ABC, abstractmethod


class GetterSetter(ABC):

    @abstractmethod
    def set_val(self, i):
        return

    @abstractmethod
    def get_val(self):
        return


class MyClass(GetterSetter):
    def set_val(self, i):
        self.val = i

    def get_val(self):
        return self.val


class MyClassAbstract(GetterSetter):

    def get_val(self):
        return self.val


class MyClassFixed(MyClassAbstract):
    def set_val(self, i):
        self.val = i


