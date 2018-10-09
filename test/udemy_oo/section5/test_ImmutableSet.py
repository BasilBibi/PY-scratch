import unittest
from py_scratch.udemy_oo.section5.ImmutableSet import ImmutableSet


class ImmutableSetTests(unittest.TestCase):

    def test_can_construct(self):
        s = ImmutableSet( (1, 2, 3, 4) )
        self.assertTrue( 1 in s )

    def test_add_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.add(5)
        self.assertFalse( 5 in s)

    def test_clear_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.clear()
        self.assertTrue( 1 in s)

    def test_discard_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.discard(1)
        self.assertTrue( 1 in s)

    def test_pop_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.pop(1)
        self.assertTrue( 1 in s)

    def test_remove_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.remove(1)
        self.assertTrue( 1 in s)

    def test_update_does_not_change_set(self):
        s = ImmutableSet((1, 2, 3, 4))
        s.update(5)
        self.assertFalse( 5 in s)


if __name__ == '__main__':
    unittest.main()