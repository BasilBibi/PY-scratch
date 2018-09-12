import unittest
from py_scratch.practise_python.NameMangling import B

b = B(iv='This is IV', aiv='This is AIV')


class NameManglingTests(unittest.TestCase):

    def test_name_mangling_in_A(self):
        self.assertTrue(b._A__clazz_var == 10)
        self.assertTrue(b._A__inst_var == 'This is IV')

    def test_name_mangling_in_B(self):
        self.assertTrue(b._B__another_clazz_var == 100)
        self.assertTrue(b._B__another_inst_var == 'This is AIV')


if __name__ == '__main__':
    unittest.main()