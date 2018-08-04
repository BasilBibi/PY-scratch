class GameBoard:

    @property
    def ascii_offset(self): return 65

    def __init__(self, size, init_char=' '):
        self.size = size
        self.init_char = init_char
        self.board = GameBoard.make_board(size, init_char)
        self.column_names = GameBoard.make_cols(size)

    @staticmethod
    def make_board(size, init_char):
        b = []
        for i in range(size):
            b.append([init_char] * size)
        return b

    @staticmethod
    def make_cols(size):
        cols = []
        for i in range(size):
            cols.append(chr(65+i))
        return cols

    def header(self):
        return

    def row_str(self, line):
        l = [self.cell_str(e) for e in line]
        return ''.join(l) + '|' + '\n' + self.separator_str()

    def cell_str(self, e):
        return f'| {e} '

    def separator_str(self):
        return ' ---' * self.size

    def get_current_board(self):
        current_board_as_str = [self.row_str(line) for line in self.board]
        return '\n' \
               + self.separator_str()+'\n' \
               + '\n'.join(current_board_as_str)\
               + '\n'

    def set(self, col, row, piece=' '):
        col_index = ord(col) - self.ascii_offset
        self.board[row][col_index] = piece

    def is_free(self, col, row):
        col_index = ord(col) - self.ascii_offset
        return self.board[row][col_index] == self.init_char

    def is_valid_coords(self, col, row):

        def is_valid_col(ci):
            return 0 <= ci < self.size

        def is_valid_row(r):
            return 0 <= r < self.size

        col_index = ord(col) - self.ascii_offset
        return is_valid_col(col_index) and is_valid_row(row)


from collections import namedtuple

RowPopulation = namedtuple('RowPopulation', 'row population')
ColPopulation = namedtuple('ColPopulation', 'col population')
DiagPopulation = namedtuple('DiagPopulation', 'diag population')


class TicTakToe(GameBoard):

    def __init__(self):
        super().__init__(size=3)

    def winning_row_set(self, board):
        row_pops = self.get_row_sets(board)
        return [rp for rp in row_pops if self.is_valid_population(rp.population)]

    @staticmethod
    def get_row_sets(board):
        return [RowPopulation(i, set(e)) for i, e in enumerate(board)]

    def is_valid_population(self, pop):
        return len(pop) == 1 and pop != set(self.init_char)

    def winning_col_set(self, board):
        col_pops = self.get_col_sets(board)
        return [cp for cp in col_pops if self.is_valid_population(cp.population)]

    @staticmethod
    def get_col_sets(board):
        zipped = list(zip(board[0], board[1], board[2]))
        return [ColPopulation(i, set(e)) for i, e in enumerate(zipped)]

    def get_winning_diag_set(self, board):
        diagPops = self.get_diag_sets(board)
        return [diag for diag in diagPops if self.is_valid_population(diag.population)]

    @staticmethod
    def get_diag_sets(board):
        fwd_slash = {board[0][2], board[1][1], board[2][0]}
        fwd = DiagPopulation('FwdSlash', fwd_slash)
        back_slash ={board[0][0], board[0][1], board[0][2]}
        bk = DiagPopulation('BkSlash', back_slash)
        return [fwd, bk]
