import unittest
from py_scratch.practise_python.ListHeadAndTail import *


class ListHeadAndTailTests(unittest.TestCase):

    def test_with_slices(self):
        a = [5, 10, 15, 20, 25]
        expected = [5, 25]
        self.assertEqual(expected, first_and_last_element(a))

    def test_head_tail(self):
        a = [5, 10, 15, 20, 25]
        head, tail = head_and_tail(a)
        self.assertEqual(head, 5)
        self.assertEqual(tail, [10, 15, 20, 25])

    def test_head_tail_slices(self):
        a = [5, 10, 15, 20, 25]
        head, tail = head_and_tail_slices(a)
        self.assertEqual(head, 5)
        self.assertEqual(tail, [10, 15, 20, 25])


if __name__ == '__main__':
    unittest.main()
