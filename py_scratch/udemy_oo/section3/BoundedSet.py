from math import inf

class BoundedSet:
    def __init__(self, lower=-inf, upper=inf):
        self.__lower = lower
        self.__upper = upper
        self.__internal_set = set()

    def get_set(self):
        return self.__internal_set.copy()

    def add(self, e):
        if self.__lower <= e <= self.__upper:
            self.__internal_set.add(e)