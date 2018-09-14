from py_scratch.practise_python.Hangman import HangMan,ScrabbleWords
from py_scratch.practise_python.WordDictionary import LocalDictionary, OnlineOxfordDictionary

clear_screen = '\033[H\033[J'

oxford_dictionary = OnlineOxfordDictionary()
local_dictionary = LocalDictionary('LocalDictionary.csv')


def print_definitions(word):
    print(f'\n{word} :')
    print('\n'.join(oxford_dictionary.lookup(word)))


while True:
    hangman = HangMan(ScrabbleWords())
    cg = hangman.get_current_game_state()
    print(f'\n\nHangman word\n{cg} : {len(cg)} letters\n')
    while True:
        guess = input(f'{hangman.get_current_game_state()} : {hangman.bad_guess_count} : ').upper()
        if hangman.is_valid_letter(guess):
            hangman.guess_letter(guess)
            if hangman.is_game_over():
                if hangman.has_won():
                    print(f'{hangman.get_current_game_state()} : {hangman.bad_guess_count}')
                    word = ''.join(hangman.word)
                    print_definitions(word)
                    print(f'You win!')
                    break
                else:
                    word = ''.join(hangman.word)
                    print_definitions(word)
                    print(f'You lose ;( {hangman.bad_guess_count} bad guesses.')
                    break
        else:
            print(f'{hangman.get_current_game_state()} : {hangman.bad_guess_count}\n')

    if input('Play again ? [y/n] : ').upper() != 'Y':
        break
    else:
        print(clear_screen)
