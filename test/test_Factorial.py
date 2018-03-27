import unittest
from py_scratch.Factorial import fact


class FactorialSpec(unittest.TestCase):

    def test_lessthan_zero(self):
        self.assertEqual(0, fact(-1))

    def test_zero(self):
        self.assertEqual(0, fact(0))

    def test_one(self):
        self.assertEqual(1, fact(1))

    def test_two(self):
        self.assertEqual(2, fact(2))

    def test_three(self):
        self.assertEqual(6, fact(3))

    def test_four(self):
        self.assertEqual(24, fact(4))

    def test_five(self):
        self.assertEqual(120, fact(5))

    def test_six(self):
        self.assertEqual(720, fact(6))

    def test_seven(self):
        self.assertEqual(5040, fact(7))

    def test_fifty(self):
        self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000,
                         fact(50))


if __name__ == '__main__':
    unittest.main()
