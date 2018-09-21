class ImmutableSet(set):
    def __iter__(self, elements):
        set.update(elements)

    def add(self, *args, **kwargs):  # real signature unknown
        return

    def clear(self, *args, **kwargs):  # real signature unknown
        return

    def discard(self, *args, **kwargs):  # real signature unknown
        return

    def pop(self, *args, **kwargs):  # real signature unknown
        return

    def remove(self, *args, **kwargs):  # real signature unknown
        return

    def update(self, *args, **kwargs): # real signature unknown
        return

    def difference_update(self, *args, **kwargs):  # real signature unknown
        return

    def symmetric_difference_update(self, *args, **kwargs): # real signature unknown
        return
