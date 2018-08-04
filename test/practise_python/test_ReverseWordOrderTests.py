import unittest
from py_scratch.practise_python.ReverseList import *


class PrimalityTests(unittest.TestCase):

    def test_example_list(self):
        self.assertEqual( ['this', 'is', 'correct'], reverse_list_from_string('correct is this'))


if __name__ == '__main__':
    unittest.main()
