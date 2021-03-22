from TwitterAPI import TwitterAPI
import os
from os import environ

#from auth import (
#    consumer_key,
#    consumer_secret,
#    access_token_key,
#    access_token_secret
#)
consumer_key = environ['CONSUMER_KEY']
consumer_secret = environ['CONSUMER_SECRET']
access_token_key = environ['ACCESS_KEY']
access_token_secret = environ['ACCESS_SECRET']

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

def sendTweet(message):
	r = api.request('statuses/update', {'status': message} )
	print(r.status_code)

#sendTweet("test")
#def sendtweet():
	#r = api