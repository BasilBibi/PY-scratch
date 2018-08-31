import unittest

from py_scratch.udemy_oo.section4.ABC import *


class ABC_Tests(unittest.TestCase):

    def test_can_construct_MyClass(self):
        mc = MyClass()
        mc.set_val(100)
        self.assertEqual(100, mc.get_val())

    def test_cannot_construct_MyClassAbstract(self):
        with self.assertRaises(Exception):
            MyClassAbstract()

    def test_can_construct_MyClassFixed(self):
        mcf = MyClassFixed()
        mcf.set_val(200)
        self.assertEqual(200, mcf.get_val())


if __name__ == 'main':
    unittest.main()
