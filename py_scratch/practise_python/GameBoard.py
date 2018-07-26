def row(line):
    return f'| {line[0]} | {line[1]} | {line[2]} |\n{separator()}'


def separator():
    return f' --- --- --- '


def make_gameboard(l):
    return separator()+'\n'+'\n'.join( [row(e) for e in l] )
