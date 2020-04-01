class SetItemError(Exception):
    pass


class LowercaseKeysOnlyDict(dict):

    def __init__(self, *args, **kw):
        super(LowercaseKeysOnlyDict, self).__init__(*args, **kw)

    def __setitem__(self, key, value):
        if key.lower() != key:
            raise SetItemError(f'Key contains uppercase characters. Cannot add {key} {value}')

        super(LowercaseKeysOnlyDict, self).__setitem__(key, value)
