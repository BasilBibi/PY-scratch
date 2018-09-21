class ImmutableDict(dict):

    def __init__(self, list_of_tuples):
        dict.__init__(self)
        for k, v in list_of_tuples:
            dict.__setitem__(self, k, v)

    def __setitem__(self, key, value):
        return

    def __delitem__(self, key):
        return
