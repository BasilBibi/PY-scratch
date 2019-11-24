import unittest
from py_scratch.hackerrank.Rangoli import make_middle_line, make_line_sub_lists, make_rangoli


class RangoliTests(unittest.TestCase):

    def test_00_make_middle_line_1(self):
        self.assertEqual('a', make_middle_line(['a']))

    def test_01_make_middle_line_2(self):
        self.assertEqual('b-a-b', make_middle_line(['a', 'b']))

    def test_02_make_middle_line_3(self):
        self.assertEqual('c-b-a-b-c', make_middle_line(['a', 'b', 'c']))

    def test_03_make_middle_line_5(self):
        self.assertEqual('e-d-c-b-a-b-c-d-e', make_middle_line(['a', 'b', 'c', 'd', 'e']))

    def test_04_make_line_sub_lists_1(self):
        self.assertEqual([['a']], make_line_sub_lists(['a']))

    def test_05_make_line_sub_lists_2(self):
        self.assertEqual([['b'], ['a', 'b']], make_line_sub_lists(['a', 'b']))

    def test_06_make_line_sub_lists_5(self):
        self.assertEqual([['e'], ['d', 'e'], ['c', 'd', 'e'], ['b', 'c', 'd', 'e'], ['a', 'b', 'c', 'd', 'e']],
                         make_line_sub_lists(['a', 'b', 'c', 'd', 'e']))

    def test_07_make_rangoli_3(self):
        self.assertEqual(
            '''----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----''', make_rangoli(3))

    def test_08_make_rangoli_5(self):
        self.assertEqual(
            '''--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------''', make_rangoli(5))

    def test_09_make_rangoli_1(self):
        self.assertEqual(
            '''a
''', make_rangoli(1))

    def test_10_make_rangoli_2(self):
        self.assertEqual(
            '''--b--
b-a-b
--b--''', make_rangoli(2))


if __name__ == '__main__':
    unittest.main()
