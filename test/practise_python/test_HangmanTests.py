import unittest
from unittest.mock import MagicMock

from py_scratch.practise_python.Hangman import *

scabble_words = ScrabbleWords.get_sowpods()
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
        self.assertEqual(0, hangman.bad_guess_count)
        self.assertEqual(['A', 'B', 'A', 'L', 'O', 'N', 'E'], hangman.word)
        self.assertEqual(['-', '-', '-', '-', '-', '-', '-'], hangman.current_game_state)
        self.assertEqual( set(), hangman.used_letters)

    def test_input_is_a_letter(self):
        self.assertTrue( HangMan.is_valid_letter('A'))
        self.assertTrue( HangMan.is_valid_letter('Z'))

    def test_input_is_not_a_letter(self):
        self.assertFalse( HangMan.is_valid_letter('1'))
        self.assertFalse( HangMan.is_valid_letter(';'))
        self.assertFalse(HangMan.is_valid_letter(''))
        self.assertFalse(HangMan.is_valid_letter(None))

    def test_get_current_game_state_at_start(self):
        self.assertEqual('-------', hangman.get_current_game_state())

    def test_get_current_game_state(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('A')
        self.assertEqual('A-A----', hangman.get_current_game_state())

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
        self.assertEqual('ABALONE', hangman.get_current_game_state())

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
        self.assertEqual('-------', hangman.get_current_game_state())

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

    def test_incr_guess_count_bad_letter(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('Z')
        self.assertTrue(hangman.bad_guess_count == 1)

    def test_used_letters_does_not_increment_for_repeats(self):
        mock_scrabble_words = MagicMock()
        mock_scrabble_words.get_random_word.side_effect = ['ABALONE']
        hangman = HangMan(mock_scrabble_words)
        hangman.guess_letter('A')
        self.assertTrue(hangman.bad_guess_count == 0)
        hangman.guess_letter('A')
        self.assertTrue(hangman.bad_guess_count == 0)


if __name__ == '__main__':
    unittest.main()
