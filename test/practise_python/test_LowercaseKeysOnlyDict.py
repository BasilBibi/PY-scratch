import pytest
from py_scratch.practise_python.LowercaseKeysOnlyDict import SetItemError, LowercaseKeysOnlyDict


def test_can_construct():
    d = LowercaseKeysOnlyDict()
    with pytest.raises(KeyError):
        d['a']


def test_set_a_new_key_lowercase():
    d = LowercaseKeysOnlyDict()
    d['z'] = 10
    assert 10 == d['z']


def test_set_a_new_key_uppercase_raises_error():
    d = LowercaseKeysOnlyDict()
    with pytest.raises(SetItemError):
        d['Z'] = 10

