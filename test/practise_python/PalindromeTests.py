import unittest
from py_scratch.practise_python.palindrome import *


class GeneralTests(unittest.TestCase):

    def test_non_palindrome(self):
        self.assertEqual( False, is_palindrome('This is not a Palindrome') )

    def test_palindrome(self):
        self.assertEqual( True, is_palindrome('abba') )

    def test_palindrome_with_mixed_caps(self):
        self.assertEqual( True, is_palindrome('aBba') )

    def test_palindrome_empty_str(self):
        self.assertEqual( True, is_palindrome('') )


if __name__ == '__main__':
    unittest.main()
