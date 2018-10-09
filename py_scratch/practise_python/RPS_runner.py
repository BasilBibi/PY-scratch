from py_scratch.practise_python.RPS import *


def get_player_choice(player_name):
    while True:
        c = input(f'{player_name} : ').lower()
        if is_valid_choice(c):
            return rps_tokens[c]
        else:
            print( make_error_message(c, player_name) )
            continue


while True:

    p1 = get_player_choice('Player 1')
    p2 = get_player_choice('Player 2')

    winning_choice = result_lookup[
        play_rps(p1, p2)
    ]

    print(f'Winning choice is {winning_choice}\n')
