import unittest
from py_scratch.udemy_oo.section4.InheritanceDiamond import *
import re


def get_class_names_in_mro(clazz):
    return [ extract_last_non_period( str(s) ) for s in clazz.mro() if(str(s) != "<class 'object'>")]


def extract_last_non_period(s):
    pattern = re.compile(r'([^.]+)\'>$')
    return pattern.search(s).group(1)


class InheritanceDiamondTests(unittest.TestCase):

    def test_remove_earlier_occurence_of_A(self):
        d = D()
        self.assertEqual('doing this in C', d.do_this())

    def test_mro_uses_BBB_despite_diamond(self):
        ddd = DDD()
        self.assertEqual('doing this in BBB as shown in mro', ddd.do_this())

    def test_compare_Python_3_mro_output(self):
        mro_output = get_class_names_in_mro(D)
        self.assertEqual(['D', 'B', 'C', 'A'], mro_output)

    def test_compare_Python_3_mro_non_diamond_output(self):
        mro_output = get_class_names_in_mro(DD)
        self.assertEqual(['DD', 'BB', 'AA', 'CC'], mro_output)


if __name__ == 'main':
    unittest.main()
