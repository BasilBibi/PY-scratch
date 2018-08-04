import unittest

from py_scratch.practise_python.SecondRank import *


class SecondRankTests(unittest.TestCase):

    def test_normal_list(self):
        l = [1,3,4,7,9,8]
        self.assertEqual(8, get_second_largest(l))

    def test_normal_list_with_negatives(self):
        l = [1,-3,-4,-7,-9,-8]
        self.assertEqual(-3, get_second_largest(l))

    def test_list_all_equal(self):
        l = [1,1]
        self.assertEqual( None, get_second_largest(l))

    def test_pass_none(self):
        self.assertEqual( None, get_second_largest(None) )

    def test_pass_empty(self):
        self.assertEqual( None, get_second_largest(None) )


if __name__ == '__main__':
    unittest.main()
