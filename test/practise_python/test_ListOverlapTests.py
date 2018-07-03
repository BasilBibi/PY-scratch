import unittest
from py_scratch.practise_python.ListOverlap import *

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

class GeneralTests(unittest.TestCase):

    def test_with_self_rolled(self):
        expected = {1, 2, 3, 5, 8, 13}
        self.assertEqual( expected, get_list_overlap(a, b) )

    def test_with_list_intersection_1(self):
        expected = {1, 2, 3, 5, 8, 13}
        self.assertEqual(expected, list_intersection(a, b))

    def test_with_list_intersection_2(self):
        expected = {1, 2, 3, 5, 8, 13}
        self.assertEqual(expected, list_intersection_with_ampersand(a, b))

    def test_list_difference(self):
        expected = {21, 34, 55, 89}
        self.assertEqual(expected, list_difference(a, b))

    def test_list_union(self):
        expected = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 21, 89, 34, 55}
        self.assertEqual(expected, list_union(a, b))

    def test_list_sym_diff(self):
        expected = {34, 4, 6, 7, 9, 10, 11, 12, 21, 55, 89}
        self.assertEqual(expected, list_sym_diff(a, b))


if __name__ == '__main__':
    unittest.main()
