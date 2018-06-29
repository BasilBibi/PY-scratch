from py_scratch.practise_python.Hangman import HangMan,ScrabbleWords

hangman = HangMan(ScrabbleWords())
cg = hangman.get_current_game_state()
print(f'\n\nHangman word : {cg} {len(cg)} letters\n')

while True:
    guess = input('Guess : ').upper()
    current_state = hangman.guess_letter(guess)
    print(f'{current_state} : {hangman.wrong_guess_count}\n')
    if hangman.has_won():
        print(f'You win! {hangman.wrong_guess_count} wrong guesses.')
        break
    if hangman.wrong_guess_count > 10:
        print(''.join(hangman.word))
        break