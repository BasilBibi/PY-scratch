import unittest
from py_scratch.practise_python.Primality import *


class PrimalityTests(unittest.TestCase):

    def test_negative_numbers(self):
        self.assertFalse( is_prime(-1) )

    def test_zero(self):
        self.assertFalse( is_prime(0) )

    def test_2(self):
        self.assertTrue( is_prime(2) )

    def test_3(self):
        self.assertTrue( is_prime(3) )

    def test_evens(self):
        self.assertFalse( is_prime(8) )

    def test_5939(self):
        self.assertTrue( is_prime(5939) )

    def test_16769023(self):
        self.assertTrue( is_prime(16769023))

    def test_16769024(self):
        self.assertFalse( is_prime(16769024))

    @unittest.skip("Runs for over a minute")
    def test_large_prime_1073676287(self):
        self.assertTrue( is_prime(1073676287))

    def test_very_large_even_number_1298074214633706835075030044377088(self):
        self.assertFalse( is_prime(1298074214633706835075030044377088))


if __name__ == '__main__':
    unittest.main()
