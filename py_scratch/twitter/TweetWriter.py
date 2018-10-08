from abc import ABC, abstractmethod
import json
from jsonpath_ng import jsonpath, parse


class TweetWriter(ABC):
    @abstractmethod
    def on_data(self, tweet):
        return


class LoveAndHateTweetStringWriter(TweetWriter):

    __NOT_FOUND_DEFAULT = {'NA': 'NA'}
    __TEXT_PATH = jsonpath_expr = parse('$..text')
    __FULL_TEXT_PATH = jsonpath_expr = parse('$..full_text')

    def __init__(self):
        self.__love_count = 0
        self.__hate_count = 0

    def get_love_count(self):
        return self.__love_count

    def get_hate_count(self):
        return self.__hate_count

    def on_data(self, tweet):
        j = json.loads(tweet)

        text = self._get_text(j)
        text_words = text.lower().split()
        full_text = self._get_full_text(j)
        full_text_words = full_text.lower().split()

        self._update_stats(text_words, full_text_words)

        return self._make_output_string(text, text_words, full_text, full_text_words)

    @staticmethod
    def _get_text(j):
        return [match.value for match in LoveAndHateTweetStringWriter.__TEXT_PATH.find(j)][0]

    @staticmethod
    def _get_full_text(j):
        matches = [match.value for match in LoveAndHateTweetStringWriter.__FULL_TEXT_PATH.find(j)]
        return ' '.join(matches)

    def _make_output_string(self, text, text_words, extended_tweet, extended_tweet_words):
        has_love = has_hate = '_'
        if self._is_love(text_words, extended_tweet_words):
            has_love = '*'
        if self._is_hate(text_words, extended_tweet_words):
            has_hate = '*'

        return (f'love: {self.__love_count}, {has_love}, hate: {self.__hate_count}, {has_hate}\n'
                f'text      : {text}\n'
                f'full_text : {extended_tweet}')

    def _update_stats(self, text_words, extended_tweet_words):
        if self._is_love(text_words, extended_tweet_words):
            self.__love_count += 1
        if self._is_hate(text_words, extended_tweet_words):
            self.__hate_count += 1

    @staticmethod
    def _is_love(text_words, extended_tweet_words):
        return 'love' in text_words \
               or 'love' in extended_tweet_words

    @staticmethod
    def _is_hate(text_words, extended_tweet_words):
        return 'hate' in text_words \
               or 'hate' in extended_tweet_words
