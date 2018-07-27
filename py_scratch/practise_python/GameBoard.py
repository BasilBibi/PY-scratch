class GameBoard:

    def __init__(self, size, init_char=' '):
        self.size = size
        self.init_char = init_char
        self.board = __class__.make_board(size, init_char)

    @staticmethod
    def make_board(size, init_char):
        b = []
        for i in range(size):
            b.append([init_char] * size)
        return b

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

    def set(self, row, col, piece=' '):
        if self.is_free(row, col):
            self.board[row][col] = piece

    def is_free(self, row, col):
        return self.board[row][col] == self.init_char