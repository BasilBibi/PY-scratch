import unittest
import re
from test.TestBase import *


class GeneralTests(unittest.TestCase):


    def test_find_longest_word_in_macbeth(self):
        macbeth = get_file_contents('Macbeth.txt')
        lines = macbeth.split()
        lines.sort(key=len, reverse=True)
        self.assertEqual('Waiting-Gentlewoman]', lines[0])


    def test_find_longest_word_in_macbeth_using_regex(self):
        macbeth = get_file_contents('Macbeth.txt').lower()
        lines = re.findall('[a-z]+', macbeth)
        lines.sort(key=len, reverse=True)
        self.assertEqual('northumberland', lines[0])

    def test_get_longest_word_with_dict(self):
        import re
        macbeth = get_file_contents('Macbeth.txt').upper()
        word_histo = {}
        words = re.findall('[A-Z]+', macbeth)
        words.sort(key=len, reverse=True)
        longest_word = words[0]
        for word in words:
            if word is None: continue
            count_of_word = word_histo.get(word, 0)
            word_histo[word] = count_of_word + 1

        print(longest_word, word_histo[longest_word])


if __name__ == '__main__':
    unittest.main()
