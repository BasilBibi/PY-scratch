import unittest
from py_scratch.practise_python.WordDictionary import *
from test.TestBase import *

onlineoxford_pear_json = get_file_contents('Oxford_Pear.json')


class HangmanTests(unittest.TestCase):

    def test_OnlineOxford_can_parse_its_own_json(self):
        oxford = OnlineOxfordDictionary()
        definitions = oxford.extract_definition_from_result(onlineoxford_pear_json)
        self.assertEqual( ["1 : sweet yellowish- or brownish-green edible fruit which is narrow at stalk",
                           "2 : Eurasian tree which bears pear"], definitions )

    def test_LocalDictionary_making_internal_dict(self):
        internal_dict = LocalDictionary._make_internal_dict('LocalDictionary.csv')
        self.assertTrue('doe' in internal_dict.keys())

    def test_LocalDictionary_lookup_known_word(self):
        localDict = LocalDictionary('LocalDictionary.csv')
        self.assertEqual( ['1 : A deer a female deer'], localDict.lookup('doe'))

    def test_LocalDictionary_lookup_UNKNOWN_word(self):
        localDict = LocalDictionary('LocalDictionary.csv')
        self.assertEqual( ['UNKNOWN not found in LocalDictionary'], localDict.lookup('UNKNOWN'))


if __name__ == '__main__':
    unittest.main()
