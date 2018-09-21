import unittest
from py_scratch.udemy_oo.section5.ImmutableDict import ImmutableDict


class ImmutableDictTests(unittest.TestCase):

    def test_can_construct(self):
        imd = ImmutableDict([('a', 1)])
        self.assertEqual(1, imd['a'])

    def test_setitem_is_immutable(self):
        imd = ImmutableDict([('a', 1)])
        imd['a'] = 10
        self.assertEqual(1, imd['a'])

    def test_delitem_is_immutable(self):
        imd = ImmutableDict([('a', 1)])
        del imd['a']
        self.assertEqual(1, imd['a'])

    def test_cannot_add_a_new_kv(self):
        imd = ImmutableDict([('a', 1)])
        imd['z'] = 100
        with self.assertRaises(KeyError):
            imd['z']


if __name__ == '__main__':
    unittest.main()
