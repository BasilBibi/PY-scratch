import unittest
from py_scratch.practise_python.NameMangling import B

b = B(iv='This is IV', aiv='This is AIV')


class NameManglingTests(unittest.TestCase):

    def test_name_mangling_in_A(self):
        self.assertTrue(b.clazz_var == 1)
        self.assertTrue(b._priv_clazz_var == 10)
        self.assertTrue(b._A__mangled_clazz_var == 100)

        self.assertTrue(b.inst_var == 'This is IV')
        self.assertTrue(b._priv_inst_var == 'This is IV')
        self.assertTrue(b._A__mangled_inst_var == 'This is IV')

    def test_name_mangling_in_B(self):
        self.assertTrue(b.another_clazz_var == 100)
        self.assertTrue(b._another_priv_clazz_var == 100)
        self.assertTrue(b._B__another_mangled_clazz_var == 100)

        self.assertTrue(b.another_inst_var == 'This is AIV')
        self.assertTrue(b._another_priv_inst_var == 'This is AIV')
        self.assertTrue(b._B__another_mangled_inst_var == 'This is AIV')


if __name__ == '__main__':
    unittest.main()