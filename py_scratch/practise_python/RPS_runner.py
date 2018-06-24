from py_scratch.practise_python.RPS import *


while True:

    p1 = get_player_choice('Player 1')
    p2 = get_player_choice('Player 2')

    winning_choice = result_lookup[
        play_rps(p1, p2)
    ]

    print(f'Winning choice is {winning_choice}\n')
