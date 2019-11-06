import unittest
from py_scratch.practise_python.Centenary import calculate_year_of_centenary


class CalculateYearOfCentenaryTests(unittest.TestCase):

    def test_for_newborn(self):
        self.assertEqual(2118, calculate_year_of_centenary(current_year=2018, current_age=0))

    def test_for_sufi(self):
        self.assertEqual(2095, calculate_year_of_centenary(current_year=2018, current_age=22))

    def test_for_basil(self):
        self.assertEqual(2063, calculate_year_of_centenary(current_year=2018, current_age=54))

    def test_for_bill(self):
        self.assertEqual(2064, calculate_year_of_centenary(current_year=2019, current_age=54))

    def test_for_negative_value_age(self):
        with self.assertRaises(Exception) as context:
            calculate_year_of_centenary(current_year=2019, current_age=-20)
            self.assertTrue('Bad input -20 < 0' == context.exception)

    def test_for_negative_value_year(self):
        with self.assertRaises(Exception) as context:
            calculate_year_of_centenary(current_year=-2019, current_age=20)
            self.assertTrue('Bad input -20 < 0' == context.exception)


if __name__ == '__main__':
    unittest.main()
