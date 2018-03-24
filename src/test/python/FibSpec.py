import unittest
from src.main.python.Fibonacci import fib


class FibSpec(unittest.TestCase):

    def test_lessthan_zero(self):
        self.assertEqual(0, fib(-1))

    def test_zero(self):
        self.assertEqual(0, fib(0))

    def test_one(self):
        self.assertEqual(1, fib(1))

    def test_two(self):
        self.assertEqual(1, fib(2))

    def test_three(self):
        self.assertEqual(2, fib(3))

    def test_four(self):
        self.assertEqual(3, fib(4))

    def test_five(self):
        self.assertEqual(5, fib(5))


if __name__ == '__main__':
    unittest.main()