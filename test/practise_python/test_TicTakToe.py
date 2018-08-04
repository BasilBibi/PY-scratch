import unittest
from py_scratch.practise_python.GameBoard import TicTakToe, RowPopulation, ColPopulation, DiagPopulation


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
        expected = [RowPopulation(0, set(' ')),
                    RowPopulation(1, set(' ')),
                    RowPopulation(2, set(' '))]
        self.assertEqual( expected, TicTakToe().get_row_sets(board) )

    def test_get_row_sets_diffs(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [RowPopulation(0, set({' ', 'X', 'O'})),
                    RowPopulation(1, set({' ', 'X', 'O'})),
                    RowPopulation(2, set({' ', 'X', 'O'}))]

        self.assertEqual( expected, TicTakToe().get_row_sets(board))

    def test_get_col_sets(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [ColPopulation(0, set({' '})),
                    ColPopulation(1, set({'X'})),
                    ColPopulation(2, set({'O'}))]

        self.assertEqual( expected, TicTakToe().get_col_sets(board))

    def test_get_diag_sets(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        expected = [DiagPopulation('FwdSlash', set({' '})),
                    DiagPopulation('BkSlash', set({' '}))]

        self.assertEqual( expected, TicTakToe().get_diag_sets(board))

    def test_get_diag_sets_diff(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [DiagPopulation('FwdSlash', set({' ', 'X', 'O'})),
                    DiagPopulation('BkSlash', set({' ', 'X', 'O'}))]

        self.assertEqual( expected, TicTakToe().get_diag_sets(board))

    def test_is_validPopulation_len_not_ok(self):
        ttt=TicTakToe()
        pop = set({'a', 'b'})
        self.assertFalse( ttt.is_valid_population(pop) )

    def test_is_validPopulation_len_ok(self):
        ttt=TicTakToe()
        pop = set('a')
        self.assertTrue( ttt.is_valid_population(pop) )

    def test_is_validPopulation_len_ok_character_ok(self):
        ttt=TicTakToe()
        pop = set('a')
        self.assertTrue( ttt.is_valid_population(pop) )

    def test_is_validPopulation_len_ok_character_not_ok(self):
        ttt = TicTakToe()
        pop = set(ttt.init_char)
        self.assertFalse( ttt.is_valid_population(pop) )

    def test_winning_row_set(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        expected = []

        self.assertEqual(expected, TicTakToe().winning_row_set(board))

    def test_winning_row_set_empty(self):
        board = [['X', 'X', 'X'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [RowPopulation(0, set({'X'}))]

        self.assertEqual(expected, TicTakToe().winning_row_set(board))

    def test_winning_row_set_no_result(self):
        board = [[' ', 'X', 'O'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = []

        self.assertEqual( expected, TicTakToe().winning_row_set(board) )

    def test_winning_col_set(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]

        expected = []

        self.assertEqual(expected, TicTakToe().winning_col_set(board))

    def test_winning_col_set_empty(self):
        board = [['X', 'X', 'X'],
                 [' ', 'X', 'O'],
                 [' ', 'X', 'O']]

        expected = [ColPopulation(1, set('X'))]

        self.assertEqual(expected, TicTakToe().winning_col_set(board))

    def test_winning_col_set_no_result(self):
        board = [[' ', 'X', 'O'],
                 ['X', ' ', 'X'],
                 ['O', 'O', ' ']]

        expected = []

        self.assertEqual( expected, TicTakToe().winning_col_set(board) )


if __name__ == '__main__':
    unittest.main()
