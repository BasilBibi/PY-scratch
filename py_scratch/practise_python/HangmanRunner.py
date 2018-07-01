from py_scratch.practise_python.Hangman import HangMan,ScrabbleWords

hangman = HangMan(ScrabbleWords())
cg = hangman.get_current_game_state()
print(f'\n\nHangman word : {cg} {len(cg)} letters\n')

while True:
    guess = input('Guess : ').upper()
    current_game_state = hangman.guess_letter(guess)
    print(f'{current_game_state} : {hangman.bad_guess_count}\n')
    if hangman.is_game_over():
        if hangman.has_won():
            print(f'You win! {hangman.bad_guess_count} bad guesses.')
            break
        else:
            print(f'You lose ;( {hangman.bad_guess_count} bad guesses.')
            print(''.join(hangman.word))
            break
