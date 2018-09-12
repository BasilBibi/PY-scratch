import unittest
from py_scratch.udemy_oo.section3.BoundedSet import BoundedSet


class BoundedSetTests(unittest.TestCase):

    def test_can_construct(self):
        s = BoundedSet(3, 5)
        self.assertTrue(s._BoundedSet__lower == 3)
        self.assertTrue(s._BoundedSet__upper == 5)
        self.assertTrue(s.get_set() == set())

    def test_can_add_in_lower_range(self):
        s = BoundedSet(3, 5)
        s.add(3)
        self.assertTrue(3 in s.get_set())

    def test_cannot_add_below_lower_range(self):
        s = BoundedSet(3, 5)
        s.add(1)
        self.assertFalse(1 in s.get_set())

    def test_can_add_in_upper_range(self):
        s = BoundedSet(3, 5)
        s.add(5)
        self.assertTrue(5 in s.get_set())

    def test_can_add_above_upper_range(self):
        s = BoundedSet(3, 5)
        s.add(10)
        self.assertFalse(10 in s.get_set())

    def test_internal_set_is_encapsulated(self):
        s = BoundedSet(3, 5)
        s.add(3)

        copy = s.get_set()
        copy.add(15)

        self.assertFalse( 15 in s.get_set())

    def test_default_arg_are_infinite(self):
        s = BoundedSet()
        s.add(-2_000_000)
        self.assertTrue( -2_000_000 in s.get_set() )


if __name__ == '__main__':
    unittest.main()