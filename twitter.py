from tweepy import OAuthHandler, API
from secret_info import twitter_keys
import re


def get_api(consumer_key,
            consumer_secret,
            access_token,
            access_token_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return API(auth)


api = get_api(**twitter_keys)


def search_tweets(query, since_id=1):
    found_tweets = api.search(q=query, since_id=since_id)
    returned_tweets = []
    for tweet in found_tweets:
        if not re.search('^RT @', tweet.text):
            returned_tweets.append(tweet)
    return returned_tweets
