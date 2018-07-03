class ScrabbleWords:

    def __init__(self):
        self.sowpods = self.get_sowpods()

    @staticmethod
    def get_file_path(file_name):
        import os
        return os.path.join(os.path.dirname(__file__), file_name)

    @staticmethod
    def get_sowpods():
        sp = ScrabbleWords.get_file_path('sowpods.txt')
        with open(sp, 'r') as fh:
            return [word.strip() for word in fh.readlines()]

    def get_random_word(self):
        import random
        return random.choice(self.sowpods)

    def is_known_word(self, word):
        return word in self.sowpods


class HangMan:

    def __init__(self, scrabbleWords, allowed_guesses=10):
        self.scrabbleWords = scrabbleWords
        self.word = [letter for letter in scrabbleWords.get_random_word()]
        self.current_game_state = list('-' * len(self.word))
        self.used_letters = set()
        self.allowed_guesses = allowed_guesses
        self.bad_guess_count = 0

    def get_current_game_state(self):
        return ''.join(self.current_game_state)

    def guess_letter(self, letter):
        self.incr_guess_count(letter)
        self.used_letters.add(letter)

        for idx, l in enumerate(self.word):
            if l == letter:
                self.current_game_state[idx] = l

        return self.get_current_game_state()

    def incr_guess_count(self, letter):
        if letter not in self.used_letters and letter not in self.word:
            self.bad_guess_count += 1

    def has_won(self):
        return self.get_current_game_state() == ''.join(self.word)

    def is_game_over(self):
        return self.bad_guess_count == self.allowed_guesses or self.has_won()

