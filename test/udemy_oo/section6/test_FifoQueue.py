import unittest

from py_scratch.udemy_oo.section6.FifoQueue import *


class FifoQueueTests(unittest.TestCase):

    def test_can_construct(self):
        q = FifoQueue()
        self.assertTrue(q == [])

    def test_can_construct_initialised(self):
        q = FifoQueue([1, 2, 3, 4, 5])
        self.assertTrue(q == [1, 2, 3, 4, 5])

    def test_enqueue(self):
        q = FifoQueue()
        q.enqueue(1)
        self.assertTrue(q == [1])

    def test_dequeue(self):
        q = FifoQueue()
        q.enqueue(1)
        self.assertTrue(q.dequeue() == 1)

    def test_dequeue_empty(self):
        q = FifoQueue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_dequeue_multi(self):
        q = FifoQueue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertTrue(q.dequeue() == 1)
        self.assertTrue(q.dequeue() == 2)
        self.assertTrue(q.dequeue() == 3)


if __name__ == '__main__':
    unittest.main()
