from abc import ABC, abstractmethod
from collections import Counter
import json
from jsonpath_ng import jsonpath, parse


class TweetWriter(ABC):
    @abstractmethod
    def on_data(self, tweet):
        return


class LoveAndHateTweetStringWriter(TweetWriter):

    __TEXT_PATH = jsonpath_expr = parse('$..text')
    __FULL_TEXT_PATH = jsonpath_expr = parse('$..full_text')

    def __init__(self, verbose=False):
        self._verbose = verbose
        self._counts = Counter()

    def get_love_count(self):
        return self._counts['love']

    def get_hate_count(self):
        return self._counts['hate']

    def on_data(self, tweet):
        j = json.loads(tweet)

        text = self._get_text(j)
        text_words = text.lower().split()
        full_text = self._get_full_text(j)
        full_text_words = full_text.lower().split()

        self._update_stats(text_words, full_text_words)

        return self._make_output_message(text, text_words, full_text, full_text_words)

    @staticmethod
    def _get_text(j):
        return [match.value for match in LoveAndHateTweetStringWriter.__TEXT_PATH.find(j)][0]

    @staticmethod
    def _get_full_text(j):
        matches = [match.value for match in LoveAndHateTweetStringWriter.__FULL_TEXT_PATH.find(j)]
        return ' '.join(matches)

    def _make_output_message(self, text, text_words, full_text, full_text_words):
        has_love = has_hate = '_'
        if self._is_love(text_words, full_text_words):
            has_love = '*'
        if self._is_hate(text_words, full_text_words):
            has_hate = '*'

        if self._verbose :
            msg = f'love: {self.get_love_count()}, {has_love}, hate: {self.get_hate_count()}, {has_hate}\n'\
                f'text      : {text}\n' \
                f'full_text : {full_text}'
        else:
            msg = f'love: {self.get_love_count()} hate: {self.get_hate_count()}'

        return msg

    def _update_stats(self, text_words, full_text_words):
        if self._is_love(text_words, full_text_words):
            self._counts['love'] += 1
        if self._is_hate(text_words, full_text_words):
            self._counts['hate'] += 1

    @staticmethod
    def _is_love(text_words, full_text_words):
        return 'love' in text_words \
               or 'love' in full_text_words

    @staticmethod
    def _is_hate(text_words, full_text_words):
        return 'hate' in text_words \
               or 'hate' in full_text_words
