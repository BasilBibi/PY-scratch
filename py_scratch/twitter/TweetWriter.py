from abc import ABC, abstractmethod
import json


class TweetWriter(ABC):
    @abstractmethod
    def on_data(self, tweet):
        return


class LoveAndHateTweetStringWriter(TweetWriter):

    __NOT_FOUND_DEFAULT = {'NA': 'NA'}

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
        extended_tweet = self._get_extended_tweet(j)
        ext_tweet_words = extended_tweet.lower().split()

        self._update_stats(text_words, ext_tweet_words)

        return self._make_output_string(text, text_words, extended_tweet, ext_tweet_words)

    @staticmethod
    def _get_text(j):
        return j.get('text', 'NA')

    @staticmethod
    def _get_extended_tweet(j):
        not_found_default = LoveAndHateTweetStringWriter.__NOT_FOUND_DEFAULT
        et = j.get('extended_tweet', not_found_default) \
            .get('full_text', '')
        rt_ext = j.get('retweeted_status', not_found_default) \
            .get('extended_tweet', not_found_default) \
            .get('full_text', '')
        qs_ext = j.get('quoted_status', not_found_default) \
            .get('extended_tweet', not_found_default) \
            .get('full_text', '')
        rt_qs_txt = j.get('retweeted_status', not_found_default) \
            .get('quoted_status', not_found_default) \
            .get('text', '')

        if et:
            return et
        elif rt_ext:
            return rt_ext
        elif qs_ext:
            return qs_ext
        elif rt_qs_txt:
            return rt_qs_txt
        else:
            return ''

    def _make_output_string(self, text, text_words, extended_tweet, extended_tweet_words):
        has_love = has_hate = '_'
        if self._is_love(text_words, extended_tweet_words):
            has_love = '*'
        if self._is_hate(text_words, extended_tweet_words):
            has_hate = '*'

        return (f'love: {self.__love_count}, {has_love}, hate: {self.__hate_count}, {has_hate}\n'
                f'text           : {text}\n'
                f'extended_tweet : {extended_tweet}')

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
