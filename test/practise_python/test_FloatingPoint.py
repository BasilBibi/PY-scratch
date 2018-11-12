import unittest
from decimal import *


class FloatingPointTests(unittest.TestCase):

    def test_half_is_ok(self):
        self.assertEqual(0.5, 1.0/2.0)

    def test_0_75_is_ok(self):
        self.assertEqual(0.75, 1.5/2.0)

    def test_currency_addition(self):
        pence = Decimal('0.01')
        dec = Decimal(200.21).quantize(pence, ROUND_HALF_UP)
        r = Decimal(100.10) + Decimal(100.11)
        result = r.quantize(pence, ROUND_HALF_UP)

        self.assertEqual( dec, result )


if __name__ == '__main__':
    unittest.main()
