import unittest
from py_scratch.udemy_oo.section6.ChattyImmutableDictionary import DelItemError, SetItemError, ChattyImmutableDictionary


class ChattyImmutableDictionaryTests(unittest.TestCase):

    def test_can_construct(self):
        cid = ChattyImmutableDictionary([('a', 1),('b', 2)])
        self.assertEqual( 1, cid['a'] )

    def test_set_a_new_key_raises_error(self):
        cid = ChattyImmutableDictionary([('a', 1),('b', 2)])
        with self.assertRaises(SetItemError):
            cid['z'] = 10

    def test_delete_a_key_raises_error(self):
        cid = ChattyImmutableDictionary([('a', 1),('b', 2)])
        with self.assertRaises(DelItemError):
            del cid['a']


if __name__ == '__main__':
    unittest.main()