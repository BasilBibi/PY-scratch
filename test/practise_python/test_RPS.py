import unittest
from py_scratch.practise_python.RPS import *


class RPSTests(unittest.TestCase):

    def test_rock_rock(self):
        self.assertEqual(draw, play_rps(rock, rock))

    def test_rock_paper(self):
        self.assertEqual(paper, play_rps(rock, paper))

    def test_rock_scissors(self):
        self.assertEqual(rock, play_rps(rock, scissors))

    def test_paper_paper(self):
        self.assertEqual(draw, play_rps(paper, paper))

    def test_paper_rock(self):
        self.assertEqual(paper, play_rps(paper, rock))

    def test_paper_scissors(self):
        self.assertEqual(scissors, play_rps(paper, scissors))

    def test_scissors_scissors(self):
        self.assertEqual(draw, play_rps(scissors, scissors))

    def test_scissors_rock(self):
        self.assertEqual(rock, play_rps(scissors, rock))

    def test_scissors_paper(self):
        self.assertEqual(scissors, play_rps(scissors, paper))


    def test_rock_valid_player_choice(self):
        self.assertTrue( is_valid_choice('rock'))

    def test_paper_valid_player_choice(self):
        self.assertTrue( is_valid_choice('paper'))

    def test_scissors_valid_player_choice(self):
        self.assertTrue( is_valid_choice('scissors'))

    def test_bad_player_choice(self):
        self.assertFalse( is_valid_choice('banana'))

    def test_draw_player_choice(self):
        self.assertFalse( is_valid_choice('draw'))


    def test_error_message_format(self):
        actual = '"draw" is not a valid choice. Choose from rock, paper, scissors. Try again Player 1.'
        self.assertEqual(actual, make_error_message('draw', 'Player 1'))


if __name__ == '__main__':
    unittest.main()
