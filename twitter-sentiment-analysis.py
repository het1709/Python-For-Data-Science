# A simple example of NLP using the textblob package and Twitter API.

# Asks for a keyword from the user, finds tweets containing that keyword
# and displays the 'sentiment' as an object of:
#   - polarity: a value between -1 and 1 where -1 is most negative and 1
#               is most positive.
#   - subjectivity: a value between 0 and 1 which denotes subjectivity of
#                   the text.

import tweepy
from textblob import TextBlob

#Authentication with the Twitter API
consumer_key = 'ENTER CONSUMER KEY HERE'
consumer_sec = 'ENTER CONSUMER SECRET HERE'

access_tok = 'ENTER ACCESS TOKEN HERE'
access_tok_sec = 'ENTER ACCESS TOKEN SECRET HERE'

auth = tweepy.OAuthHandler(consumer_key, consumer_sec)
auth.set_access_token(access_tok, access_tok_sec)

api = tweepy.API(auth) #We now have access to the API and can make requests to it

#Get keyword to search for from user
keyword = input('Enter search term: ')

#Get tweets
tweets = api.search(keyword)

for tweet in tweets:
    print(tweet.text)

    #Performing sentiment analysis on tweet
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print('')