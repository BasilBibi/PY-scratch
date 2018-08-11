import unittest

from py_scratch.udemy_oo.section4.MultipleInheritance import *


class MultipleInheritanceTests(unittest.TestCase):

    def test_C_can_construct(self):
        c = C(a='a', b='b', c='c')
        self.assertTrue(c.a == 'a' and c.b == 'b' and c.c == 'c')

    def test_C_doit_from_A(self):
        c = C(a='a', b='b', c='c')
        self.assertEqual('A: doit: a', c.doit())

    def test_C_overridden(self):
        c = C(a='a', b='b', c='c')
        self.assertEqual('C: overridden: c', c.overridden())

    def test_C_overridden_with_directed_base_call(self):
        c = C(a='a', b='b', c='c')
        self.assertEqual('C: overridden_2: c -> B: doit: b', c.overridden_2())

    def test_C_only_in_b_call(self):
        c = C(a='a', b='b', c='c')
        self.assertEqual('only_in_b: b', c.only_in_b())

    def test_D_can_construct(self):
        d = D(a='a', b='b', c='c', d='d')
        self.assertTrue(d.a == 'a' and d.b == 'b' and d.c == 'c' and d.d == 'd')

    def test_D_doit_from_A(self):
        d = D(a='a', b='b', c='c', d='d')
        self.assertEqual('A: doit: a', d.doit())

    def test_D_overridden(self):
        d = D(a='a', b='b', c='c', d='d')
        self.assertEqual('C: overridden: c', d.overridden())

    def test_D_can_see_everything(self):
        d = D(a='a', b='b', c='c', d='d')
        self.assertEqual('a: a, b: b, c: c, d: d', d.d_can_see_everything())

    def test_D_can_cast_to_B(self):
        d = D(a='a', b='b', c='c', d='d')
        self.assertEqual('B: doit: b', B.doit(d))


if __name__ == 'main':
    unittest.main()
