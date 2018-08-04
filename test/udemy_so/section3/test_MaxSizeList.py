import unittest
from py_scratch.udemy_oo.section3.MaxSizeList import MaxSizeList


class MaxSizeListTests(unittest.TestCase):

    def test_size_3(self):
        msl = MaxSizeList(3)
        msl.push('hey')
        msl.push('hi')
        msl.push("let's")
        msl.push('go')

        self.assertEqual( ['hi', "let's", 'go'], msl.get_list() )

    def test_size_1(self):
        msl = MaxSizeList(1)
        msl.push('hey')
        msl.push('hi')
        msl.push("let's")
        msl.push('go')

        self.assertEqual( ['go'], msl.get_list())

    def test_size_0(self):
        msl = MaxSizeList(0)
        msl.push('hey')
        msl.push('hi')
        msl.push("let's")
        msl.push('go')

        self.assertEqual( [], msl.get_list())

    def test_get_list_returns_copy(self):
        msl = MaxSizeList(1)
        msl.push('abc')

        copy = msl.get_list()
        copy.append('def')

        self.assertNotEqual( copy , msl.get_list())


if __name__ == '__main__':
    unittest.main()
