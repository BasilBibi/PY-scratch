import unittest
from unittest.mock import MagicMock

from py_scratch.practise_python.Hangman import *

scabble_words = ScrabbleWords().load_sowpods()
mock_scrabble_words = MagicMock()
mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
hangman = HangMan(mock_scrabble_words)


class HangmanTests(unittest.TestCase):

    def test_load_scrabble_words(self):
        self.assertTrue('ABALONE' in scabble_words)

    def test_get_random_word(self):
        random_word = ScrabbleWords().get_random_word()
        self.assertTrue( random_word in scabble_words )

    def test_known_word(self):
        scrabbleWords = ScrabbleWords()
        self.assertTrue( scrabbleWords.is_known_word('ABALONE'))

    def test_fail_unknown_word(self):
        sowpods = ScrabbleWords()
        self.assertFalse( sowpods.is_known_word('RANDOM_UNNKOWN_WORD_kdfhakdhf'))

    def test_construction(self):
        self.assertEquals(0, hangman.wrong_guess_count)
        self.assertEquals(['A', 'B', 'A', 'L', 'O', 'N', 'E'], hangman.word)
        self.assertEquals([('A', '.'), ('B', '.'), ('A', '.'), ('L', '.'), ('O', '.'), ('N', '.'), ('E', '.')], hangman.current_game_state)

    def test_get_current_game_state(self):
        self.assertEquals('.......', hangman.get_current_game_state())

    def test_get_current_game_state(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('A')
        self.assertEquals('A.A....', hangman.get_current_game_state())

    def test_all_letters(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('A')
        hangman.guess_letter('B')
        hangman.guess_letter('L')
        hangman.guess_letter('O')
        hangman.guess_letter('N')
        hangman.guess_letter('E')
        self.assertEquals('ABALONE', hangman.get_current_game_state())

    def test_failed_letters(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('Z')
        hangman.guess_letter('C')
        hangman.guess_letter('W')
        hangman.guess_letter('Y')
        hangman.guess_letter('X')
        hangman.guess_letter('P')
        self.assertEquals('.......', hangman.get_current_game_state())

    def test_has_won(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('A')
        hangman.guess_letter('B')
        hangman.guess_letter('L')
        hangman.guess_letter('O')
        hangman.guess_letter('N')
        hangman.guess_letter('E')
        self.assertTrue(hangman.has_won())


if __name__ == '__main__':
    unittest.main()
