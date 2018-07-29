import unittest
from py_scratch.practise_python.GameBoard import TicTakToe


def make_board(size, init_char):
    b = []
    for i in range(size):
        b.append([init_char] * size)
    return b


class TicTakToeTests(unittest.TestCase):

    def test_cons(self):
        ttt3 = TicTakToe()
        self.assertEqual([[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']], ttt3.board)

    def test_get_row_sets(self):
        board = make_board(3, ' ')
        expected = [set(' '), set(' '), set(' ')]
        self.assertEqual( expected, TicTakToe().get_row_sets(board) )

    def test_get_row_sets_diffs(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [set({' ', 'X', 'O'}),
                    set({' ', 'X', 'O'}),
                    set({' ', 'X', 'O'})]

        self.assertEqual( expected, TicTakToe().get_row_sets(board))

    def test_get_col_sets(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [set({' '}),
                    set({'X'}),
                    set({'O'})]

        self.assertEqual( expected, TicTakToe().get_col_sets(board))

    def test_get_diag_sets(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        expected = [set({' '}),
                    set({' '})]

        self.assertEqual( expected, TicTakToe().get_diag_sets(board))

    def test_get_diag_sets_diff(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [set({' ', 'X', 'O'}),
                    set({' ', 'X', 'O'})]

        self.assertEqual( expected, TicTakToe().get_diag_sets(board))


if __name__ == '__main__':
    unittest.main()
