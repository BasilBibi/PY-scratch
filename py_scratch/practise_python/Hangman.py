import random


class ScrabbleWords:

    def __init__(self):
        self.sowpods = self.load_sowpods()

    @staticmethod
    def get_file_path(file_name):
        import os
        return os.path.join(os.path.dirname(__file__), file_name)

    def load_sowpods(self):
        sp = self.get_file_path('sowpods.txt')
        with open(sp, 'r') as fh:
            return [word.strip() for word in fh.readlines()]

    def get_random_word(self):
        return random.choice(self.sowpods)

    def is_known_word(self, word):
        return word in self.sowpods


class HangMan:

    def __init__(self, scrabbleWords):
        self.scrabbleWords = scrabbleWords
        self.word = [letter for letter in scrabbleWords.get_random_word()]
        self.wrong_guess_count = 0
        blank = ['.' for l in self.word]
        self.current_game_state = list(zip(self.word, blank))

    def get_current_game_state(self):
        guess = [b for a,b in self.current_game_state]
        return ''.join(guess)

    def guess_letter(self, letter):
        if letter not in self.word:
            self.wrong_guess_count += 1

        def rep(a,b):
            if a == letter: return a
            else: return b

        self.current_game_state = [(a, rep(a, b)) for a, b in self.current_game_state]
        return self.get_current_game_state()

    def has_won(self):
        return self.get_current_game_state() == ''.join(self.word)
