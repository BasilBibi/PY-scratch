import json

from tweepy.streaming import StreamListener

# The on_* methods are the way Twitter calls back onto our code
class LoveAndHateTweetPrinter(StreamListener):

    TWEET_COUNT = 0
    TWEET_COUNT_LIMIT = 10
    LOVE_COUNT = 0
    HATE_COUNT = 0
    NOT_FOUND_DICT = {'NA': 'NA'}

    def on_limit(self, track):
        print(f'on_limit {track}')

    def on_data(self, data):
        print(data)
        j = json.loads(data)
        text = j.get('text', 'NA').lower()
        print(self._get_stats(text, self._get_extended_tweet(j)))
        return self._is_limit_reached()

    def on_error(self, status):
        print(status)

    def _get_stats(self, text, extended_tweet):
        has_love, has_hate = (' ', ' ')
        if self._is_love(text, extended_tweet):
            self.LOVE_COUNT += 1
            has_love = '*'
        if self._is_hate(text, extended_tweet):
            self.HATE_COUNT += 1
            has_hate = '*'

        return(f'{self.LOVE_COUNT}, {has_love}, {self.HATE_COUNT}, {has_hate}, {self.TWEET_COUNT}\n'
               f'text           : {text}\n'
               f'extended_tweet : {extended_tweet}\n'
               '-------------------------------------------------------')

    def _get_extended_tweet(self, j):
        et = j.get('extended_tweet', self.NOT_FOUND_DICT) \
            .get('full_text', '') \
            .lower()
        rt_ext = j.get('retweeted_status', self.NOT_FOUND_DICT) \
            .get('extended_tweet', self.NOT_FOUND_DICT) \
            .get('full_text', '') \
            .lower()

        if et:
            return et
        else:
            return rt_ext

    @staticmethod
    def _is_love(text, extended_tweet):
        return 'love' in text.split() \
               or 'love' in extended_tweet.split()

    @staticmethod
    def _is_hate(text, extended_tweet):
        return 'hate' in text.split() \
               or 'hate' in extended_tweet.split()

    def _is_limit_reached(self):
        self.TWEET_COUNT += 1
        return self.TWEET_COUNT > self.TWEET_COUNT_LIMIT
