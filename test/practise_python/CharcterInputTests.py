import unittest
from py_scratch.practise_python.Centenary import calculate_year_of_centenary


class GeneralTests(unittest.TestCase):

    def test_for_newborn(self):
        self.assertEqual( 2118, calculate_year_of_centenary(2018, 0) )

    def test_for_sufi(self):
        self.assertEqual( 2095, calculate_year_of_centenary(2018, 22) )

    def test_for_basil(self):
        self.assertEqual( 2063, calculate_year_of_centenary(2018,54) )


if __name__ == '__main__':
    unittest.main()
