import logging
import argparse

from tweepy import Stream
from tweepy import OAuthHandler

from py_scratch.twitter.LoveAndHateListener import LoveAndHateListener
from py_scratch.twitter.TweetWriter import LoveAndHateTweetStringWriter

parser = argparse.ArgumentParser(description='Subscribes to Twitter with terms "love" and "hate"')
parser.add_argument('--log', default='warning', help='Set the logging level: debug, info, warning, error, fatal')
parser.add_argument('-verbose', '-v', help='Output full tweet information and counts', action='store_true')

args = parser.parse_args()

numeric_level = getattr(logging, args.log.upper(), None)

logging.basicConfig(level=numeric_level,
                    format="%(asctime)s:%(levelname)s:%(message)s")

CONSUMER_API_KEY = 'i1uJqq2m07rocMK5x0UxfZjCt'
API_SECRET_KEY = 'oUfnCvkFHhgEHOsoXNWUN9TIuMhCOyP50mKDBjtihKJDtGHxQI'
ACCESS_TOKEN = '1176837962-yAxywVlI8S9e41zzIOBcbmWnjs4RhlZM0yImVbj'
ACCESS_TOKEN_SECRET = 'PNp71qntFDdRDOk7C6XpAhJsKyMBu11Y7a3L6fm5MUOo0'

auth = OAuthHandler(CONSUMER_API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listener = LoveAndHateListener(
                LoveAndHateTweetStringWriter(verbose=args.verbose),
                tweet_count_limit=1000
           )

twitterStream = Stream(auth, listener)
twitterStream.filter(track=listener.TERMS)
