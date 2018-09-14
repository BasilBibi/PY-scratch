class ScrabbleWords:

    def __init__(self):
        self._sowpods = self.get_sowpods()

    @staticmethod
    def get_sowpods():
        sp = ScrabbleWords.get_file_path('sowpods.txt')
        with open(sp, 'r') as fh:
            return [word.strip() for word in fh.readlines()]

    @staticmethod
    def get_file_path(file_name):
        import os
        return os.path.join(os.path.dirname(__file__), file_name)

    def get_random_word(self):
        import random
        return random.choice(self._sowpods)

    def is_known_word(self, word):
        return word in self._sowpods


# Assumes that input letter is uppercase
class HangMan:

    def __init__(self, scrabble_words, bad_guess_limit=10):
        self.word = list(scrabble_words.get_random_word())
        self.current_game_state = list('-' * len(self.word))
        self.used_letters = set()
        self.bad_guess_limit = bad_guess_limit
        self.bad_guess_count = 0

    def get_current_game_state(self):
        return ''.join(self.current_game_state)

    def guess_letter(self, letter):
        self.incr_guess_count(letter)
        self.used_letters.add(letter)

        for idx, word_letter in enumerate(self.word):
            if letter == word_letter:
                self.current_game_state[idx] = word_letter

    @staticmethod
    def is_valid_letter(letter):
        if letter is None or letter == '':
            return False
        ascii = ord(letter)
        return 65 <= ascii <= 95

    def incr_guess_count(self, letter):
        if letter not in self.used_letters and letter not in self.word:
            self.bad_guess_count += 1

    def has_won(self):
        return self.get_current_game_state() == ''.join(self.word)

    def is_game_over(self):
        return self.bad_guess_count == self.bad_guess_limit or self.has_won()
