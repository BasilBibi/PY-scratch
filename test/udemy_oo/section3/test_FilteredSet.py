import unittest
from py_scratch.udemy_oo.section3.FilteredSet import FilteredSet


class FilteredSetTests(unittest.TestCase):

    def test_can_construct(self):
        filter_condition = lambda e: e % 2 == 0
        fs = FilteredSet(filter_condition)
        self.assertTrue(fs._FilteredSet__filter_condition == filter_condition)
        self.assertTrue(fs.get_set() == set())

    def test_evens_only_set_can_add_2(self):
        even_ints = FilteredSet(lambda e: e % 2 == 0)
        even_ints.add(2)
        self.assertTrue( 2 in even_ints.get_set() )

    def test_evens_only_set_cannot_add_3(self):
        even_ints = FilteredSet(lambda e: e % 2 == 0)
        even_ints.add(3)
        self.assertFalse( 3 in even_ints.get_set() )

    def test_internal_set_is_encapsulated(self):
        even_ints = FilteredSet(lambda e: e % 2 == 0)
        even_ints.add(2)
        copy = even_ints.get_set()
        copy.add(15)
        self.assertFalse( 15 in even_ints.get_set())

    def test_odds_only_set_can_add_2(self):
        odd_ints = FilteredSet(lambda e: e % 2 != 0)
        odd_ints.add(2)
        self.assertFalse(2 in odd_ints.get_set())

    def test_bounds_set_can_add_in_range(self):
        odd_ints = FilteredSet(lambda e: 3 <= e <= 5)
        odd_ints.add(3)
        odd_ints.add(5)
        self.assertTrue(3 in odd_ints.get_set())
        self.assertTrue(5 in odd_ints.get_set())

    def test_bounds_set_cannot_add_out_of_range(self):
        bounded_ints_3_5 = FilteredSet(lambda e: 3 <= e <= 5)
        bounded_ints_3_5.add(2)
        bounded_ints_3_5.add(10)
        self.assertFalse(2 in bounded_ints_3_5.get_set())
        self.assertFalse(10 in bounded_ints_3_5.get_set())


if __name__ == '__main__':
    unittest.main()