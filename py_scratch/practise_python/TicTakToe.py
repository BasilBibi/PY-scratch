from py_scratch.practise_python import GameBoard


class TicTakToe(GameBoard):

    def __init__(self):
        super().__init__(size=3, init_char='0')

    def get_row_sets(self, board):
        return [set(e) for e in board]

    def get_col_sets(self, board):
        return zip(zip(board[0], board[1]), board[2])
