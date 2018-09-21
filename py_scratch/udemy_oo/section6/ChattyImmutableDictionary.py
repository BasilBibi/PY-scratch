from py_scratch.udemy_oo.section5.ImmutableDict import ImmutableDict


class SetItemError(Exception):
    pass


class DelItemError(Exception):
    pass


class ChattyImmutableDictionary(ImmutableDict):

    def __setitem__(self, key, value):
        raise SetItemError(f'Cannot add {key} {value}')

    def __delitem__(self, key):
        raise DelItemError(f'Cannot delete {key}')
