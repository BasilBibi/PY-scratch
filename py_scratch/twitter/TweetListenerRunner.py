import logging

from tweepy import Stream
from tweepy import OAuthHandler

from py_scratch.twitter.LoveAndHateListener import LoveAndHateListener
from py_scratch.twitter.TweetWriter import LoveAndHateTweetStringWriter

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s:%(levelname)s:%(message)s")

CONSUMER_API_KEY = 'i1uJqq2m07rocMK5x0UxfZjCt'
API_SECRET_KEY = 'oUfnCvkFHhgEHOsoXNWUN9TIuMhCOyP50mKDBjtihKJDtGHxQI'
ACCESS_TOKEN = '1176837962-yAxywVlI8S9e41zzIOBcbmWnjs4RhlZM0yImVbj'
ACCESS_TOKEN_SECRET = 'PNp71qntFDdRDOk7C6XpAhJsKyMBu11Y7a3L6fm5MUOo0'

auth = OAuthHandler(CONSUMER_API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

listener = LoveAndHateListener(
                LoveAndHateTweetStringWriter()
           )

twitterStream = Stream(auth, listener)
twitterStream.filter(track=listener.TERMS)
