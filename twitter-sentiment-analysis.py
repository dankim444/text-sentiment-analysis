import tweepy
from textblob import textblob

# authentication
consumer_key = 'enter your consumer key'
consumer_secret = 'enter your consumer secret key'

access_token = 'enter your access token'
access_token_secret = 'enter your access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# retrieves a list of tweets with specified key word
public_tweets = api.search('A24')

for tweet in public_tweets:
	print(tweet.text)

	# performs sentiment analysis on tweet
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)
    print ('Polarity: ', analysis.sentiment.polarity)
    print ('Subjectivity:', analysis.sentiment.subjectivity)