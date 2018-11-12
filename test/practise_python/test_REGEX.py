import unittest
import re

pattern = re.compile('^[^"]*"[^"]*$')


class RegexTests(unittest.TestCase):

    def test_search_finds_single_doublequote(self):
        self.assertTrue( pattern.search('this should "match') )

    def test_search_finds_multiple_doublequotes(self):
        self.assertFalse(pattern.search('this should not "matc"h'))

    def test_find_multiple_adjacent_dots(self):
        s = "this....has"
        multiple_dot_pattern = re.compile('.*[.]{2,}.*')
        self.assertTrue(multiple_dot_pattern.search(s))


if __name__ == '__main__':
    unittest.main()
