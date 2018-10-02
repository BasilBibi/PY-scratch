import unittest
from py_scratch.udemy_oo.section6.LifoStack import LifoStack


class LifoStackTests(unittest.TestCase):

    def test_can_construct(self):
        s = LifoStack()
        self.assertEqual(s, [])

    def test_can_construct_initialised(self):
        s = LifoStack([1, 2, 3, 4, 5])
        self.assertTrue(s == [1,2,3,4,5])

    def test_push(self):
        s = LifoStack()
        s.push(1)
        self.assertTrue(s == [1])

    def test_pop(self):
        s = LifoStack()
        s.push(1)
        self.assertTrue(s.pop() == 1)

    def test_pop_empty(self):
        s = LifoStack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_push_pop_multi(self):
        s = LifoStack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertTrue(s.pop() == 3)
        self.assertTrue(s.pop() == 2)
        self.assertTrue(s.pop() == 1)

    def test_peek(self):
        s = LifoStack()
        s.push(1)
        self.assertTrue(s.peek() == 1)
        self.assertTrue(s == [1])


if __name__ == '__main__':
    unittest.main()
