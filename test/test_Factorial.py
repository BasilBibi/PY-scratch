import unittest
from py_scratch.Factorial import fact


class FactorialSpec(unittest.TestCase):

    def test_lessthan_zero_term(self):
        self.assertEqual(0, fact(-1))

    def test_first_Factorial_term(self):
        self.assertEqual(0, fact(0))

    def test_second_Factorial_term(self):
        self.assertEqual(1, fact(1))

    def test_third_Factorial_term(self):
        self.assertEqual(2, fact(2))

    def test_fourth_Factorial_term(self):
        self.assertEqual(6, fact(3))

    def test_fifth_Factorial_term(self):
        self.assertEqual(24, fact(4))

    def test_sixth_Factorial_term(self):
        self.assertEqual(120, fact(5))

    def test_seventh_Factorial_term(self):
        self.assertEqual(720, fact(6))

    def test_eighth_Factorial_term(self):
        self.assertEqual(5040, fact(7))

    def test_fifty_first_Factorial_term(self):
        self.assertEqual(30414093201713378043612608166064768844377641568960512000000000000,
                         fact(50))


if __name__ == '__main__':
    unittest.main()
