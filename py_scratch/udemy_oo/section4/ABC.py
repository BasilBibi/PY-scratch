from abc import ABC, abstractmethod


class GetterSetter(ABC):
    def __init__(self):
        self._val = None

    @abstractmethod
    def set_val(self, i):
        pass

    @abstractmethod
    def get_val(self):
        pass


class MyClass(GetterSetter):
    def set_val(self, i):
        self._val = i

    def get_val(self):
        return self._val


class MyClassAbstract(GetterSetter):
    def get_val(self):
        return self._val


class MyClassFixed(MyClassAbstract):
    def set_val(self, i):
        self._val = i


