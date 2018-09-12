import unittest
from py_scratch.udemy_oo.section3.FilteredSet import FilteredSet


class FilteredSetTests(unittest.TestCase):

    def test_can_construct(self):
        filter_condition = lambda e: e % 2 == 0
        fs = FilteredSet(filter_condition)
        self.assertTrue(fs._FilteredSet__filter_condition == filter_condition)
        self.assertTrue(fs.get_set() == set())

    def test_evens_only_set_can_add_2(self):
        fs = FilteredSet(lambda e: e % 2 == 0)
        fs.add(2)
        self.assertTrue( 2 in fs.get_set() )

    def test_evens_only_set_cannot_add_3(self):
        fs = FilteredSet(lambda e: e % 2 == 0)
        fs.add(3)
        self.assertFalse( 3 in fs.get_set() )

    def test_internal_set_is_encapsulated(self):
        fs = FilteredSet(lambda e: e % 2 == 0)
        fs.add(2)
        copy = fs.get_set()
        copy.add(15)
        self.assertFalse( 15 in fs.get_set())

    def test_odds_only_set_can_add_2(self):
        fs = FilteredSet(lambda e: e % 2 != 0)
        fs.add(2)
        self.assertFalse(2 in fs.get_set())

    def test_bounds_set_can_add_in_range(self):
        fs = FilteredSet(lambda e: 3 <= e <= 5)
        fs.add(3)
        fs.add(5)
        self.assertTrue(3 in fs.get_set())
        self.assertTrue(5 in fs.get_set())

    def test_bounds_set_cannot_add_out_of_range(self):
        fs = FilteredSet(lambda e: 3 <= e <= 5)
        fs.add(2)
        fs.add(10)
        self.assertFalse(2 in fs.get_set())
        self.assertFalse(10 in fs.get_set())


if __name__ == '__main__':
    unittest.main()