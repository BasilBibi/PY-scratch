import logging

from tweepy.streaming import StreamListener


# The on_* methods are the way Twitter calls back onto our code
class LoveAndHateListener(StreamListener):

    def __init__(self, tweet_writer, tweet_count_limit=10):
        self.__tweet_writer = tweet_writer
        self.__tweet_count = 1
        self.__tweet_count_limit = tweet_count_limit

    def on_limit(self, track):
        logging.warning(f'on_limit {track}')

    def on_error(self, status):
        logging.error(f'on_error {status}')

    def on_data(self, data):
        logging.info(data)
        writer_output = self.__tweet_writer.on_data(data)
        if writer_output:
            print(f'{writer_output}\n')

        print(f'Number of tweets processed : {self.__tweet_count}\n'
              '------------------------------------')
        return not self._is_count_limit_reached()

    def _is_count_limit_reached(self):
        self.__tweet_count += 1
        return self.__tweet_count > self.__tweet_count_limit
