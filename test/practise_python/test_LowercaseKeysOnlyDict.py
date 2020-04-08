import pytest
from py_scratch.practise_python.LowercaseKeysOnlyDict import LowercaseKeysOnlyDict, SetItemError


def test_set_a_new_key_lowercase():
    d = LowercaseKeysOnlyDict()
    d['z'] = 10
    assert d['z'] == 10


def test_set_a_new_key_uppercase_raises_error():
    with pytest.raises(SetItemError):
        d = LowercaseKeysOnlyDict()
        d['Z'] = 10


def test_can_construct_with_values():

    d = dict( [('a', 1), ('b', 2)] )
    d = LowercaseKeysOnlyDict( [('a', 123), ('b', 222)] )
    assert d['a'] == 123
