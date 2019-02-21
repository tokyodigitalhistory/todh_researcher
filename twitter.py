from tweepy import OAuthHandler, API
from secret_info import twitter_keys
from const import excluded_patterns
import re


def get_api(consumer_key,
            consumer_secret,
            access_token,
            access_token_secret):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    return API(auth)


api = get_api(**twitter_keys)


def check_tweet_is_excluded(tweet):
    """
    Check whether the tweet include the specified patterns.
    If it has the pattern, this function returns True, otherwise False.
    :param Status tweet: Checked tweet
    :return: Exclude or not
    :rtype: boolean
    """
    for pattern in excluded_patterns:
        if re.search(pattern, tweet.text):
            return True
    return False


def search_tweets(query, since_id=1):
    """
    Query tweets and exclude the tweets which have the specified patterns.
    e.g.> A tweet which starts with "RT @" is retweeted status.
          We exclude it because we don't need retweeted tweets.
    :param str query: Query string
    :param int since_id: Search tweets which have larger than this id.
    :return: List of tweets
    :rtype: list of Status
    """
    found_tweets = api.search(q=query, since_id=since_id)
    returned_tweets = []
    for tweet in found_tweets:
        excluded = check_tweet_is_excluded(tweet)
        if not excluded:
            returned_tweets.append(tweet)
    return returned_tweets
