class GameBoard:

    def __init__(self, size, init_char=' '):
        self.size = size
        self.places = [[init_char] * size] * size

    def row_str(self, line):
        l = [self.cell_str(e) for e in line]
        return ''.join(l) + '|' + '\n' + self.separator_str()

    def cell_str(self, e):
        return f'| {e} '

    def separator_str(self):
        return ' ---' * self.size

    def get_current_board(self):
        board = [self.row_str(line) for line in self.places]
        return '\n' \
               + self.separator_str()+'\n' \
               + '\n'.join(board)\
               + '\n'
