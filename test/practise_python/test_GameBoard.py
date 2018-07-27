import unittest
from py_scratch.practise_python.GameBoard import GameBoard


class GameBoardTests(unittest.TestCase):

    def test_1x1_construction(self):
        g1x1 = GameBoard(1, 'X')
        self.assertEqual(1, g1x1.size)
        self.assertEqual([['X']], g1x1.board)

    def test_3x3_construction(self):
        g3x3 = GameBoard(3, 'X')
        self.assertEqual(3, g3x3.size)
        self.assertEqual([['X', 'X', 'X'],
                          ['X', 'X', 'X'],
                          ['X', 'X', 'X']], g3x3.board)

    def test_separator_str(self):
        g3x3 = GameBoard(3, 'X')
        self.assertEqual(' --- --- ---', g3x3.separator_str())

    def test_cell_str(self):
        g1x1 = GameBoard(1, 'X')
        self.assertEqual('| X ', g1x1.cell_str('X'))

    def test_row_str(self):
        g3x3 = GameBoard(3, 'X')
        line = ['X', 'X', 'X']
        self.assertEqual('''| X | X | X |
 --- --- ---''', g3x3.row_str(line))

    def test_make_board(self):
        g = GameBoard(2)
        self.assertEqual( [['X', 'X'], ['X','X']] , GameBoard.make_board(2, 'X'))

    def test_get_current_board(self):

        g3x3 = GameBoard(3, 'X')

        self.assertEqual('''
 --- --- ---
| X | X | X |
 --- --- ---
| X | X | X |
 --- --- ---
| X | X | X |
 --- --- ---
''', g3x3.get_current_board())

    def test_set(self):
        g3x3 = GameBoard(3)
        g3x3.set(0, 0, 'X')
        self.assertEqual( [['X', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']], g3x3.board)
        g3x3.set(2, 1, 'Y')
        self.assertEqual([['X', ' ', ' '], [' ', ' ', ' '], [' ', 'Y', ' ']], g3x3.board)

    def test_is_free(self):
        g3x3 = GameBoard(3)
        self.assertTrue(g3x3.is_free(0, 0))
        g3x3.set(0, 0, 'X')
        self.assertFalse(g3x3.is_free(0, 0))


if __name__ == '__main__':
    unittest.main()
