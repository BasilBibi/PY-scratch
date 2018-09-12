class FilteredSet:
    def __init__(self, filter_condition):
        self.__filter_condition = filter_condition
        self.__internal_set = set()

    def get_set(self):
        return self.__internal_set.copy()

    def add(self, e):
        if self.__filter_condition(e):
            self.__internal_set.add(e)