draw, rock, paper, scissors = (-1, 0, 1, 2)

rps_tokens = {'rock': rock, 'paper': paper, 'scissors': scissors}

result_lookup = {v:k for k, v in rps_tokens.items()}


def get_player_choice(player_name):
    while True:
        c = input(f'{player_name} : ').lower()
        if is_valid_choice(c):
            return rps_tokens[c]
        else:
            print( make_error_message(c, player_name) )
            continue


def is_valid_choice(c):
    return c != 'draw' and c in rps_tokens


def make_error_message(c, player_name):
    keys = ', '.join( rps_tokens.keys() )
    return f'"{c}" is not a valid choice. Choose from {keys}. Try again {player_name}.'


def rps_math(p1, p2):
    outcome = [draw, p1, p2]
    return outcome[(p1 - p2) % 3]





