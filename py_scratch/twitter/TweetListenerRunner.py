from tweepy import Stream
from tweepy import OAuthHandler

from py_scratch.twitter.LoveAndHateTweetPrinter import LoveAndHateTweetPrinter


CONSUMER_API_KEY = 'i1uJqq2m07rocMK5x0UxfZjCt'
API_SECRET_KEY = 'oUfnCvkFHhgEHOsoXNWUN9TIuMhCOyP50mKDBjtihKJDtGHxQI'
ACCESS_TOKEN = '1176837962-yAxywVlI8S9e41zzIOBcbmWnjs4RhlZM0yImVbj'
ACCESS_TOKEN_SECRET = 'PNp71qntFDdRDOk7C6XpAhJsKyMBu11Y7a3L6fm5MUOo0'

auth = OAuthHandler(CONSUMER_API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

twitterStream = Stream(auth, LoveAndHateTweetPrinter())
twitterStream.filter(track=["love", "hate"])
