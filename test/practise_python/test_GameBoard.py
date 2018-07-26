import unittest
from py_scratch.practise_python.GameBoard import separator, row, make_gameboard


class RPSTests(unittest.TestCase):

    def test_separator(self):
        self.assertEqual(' --- --- --- ', separator())

    def test_row(self):
        line = ['X', 'X', 'X']
        self.assertEqual('| X | X | X |\n --- --- --- ', row(line))

    def test_gameboard(self):
        game = [ ['X', 'X', 'X'],
                 ['X', 'X', 'X'],
                 ['X', 'X', 'X']
        ]
        self.assertEqual(
''' --- --- --- 
| X | X | X |
 --- --- --- 
| X | X | X |
 --- --- --- 
| X | X | X |
 --- --- --- ''', make_gameboard(game))


if __name__ == '__main__':
    unittest.main()
