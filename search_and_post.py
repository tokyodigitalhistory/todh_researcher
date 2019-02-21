from twitter import search_tweets
from slack import read_last_id, post_message
from const import post_message_template, result_header_format, query_strings
from secret_info import slack_channel_id, slack_direct_message_id
from jinja2 import Template


def search_tweets_by_query(query, since_id):
    found_tweets = search_tweets(query=query,since_id=since_id)
    return found_tweets


def post_tweets_to_slack(tweets):
    """
    :param tweets: status
    :return: the id of the latest tweet among the tweets
    :rtype: int
    """
    max_id = 0
    for tw in tweets:
        tw_template = Template(post_message_template)
        post_text = tw_template.render(tweet=tw)
        post_message(post_text, slack_channel_id)
        if tw.id > max_id:
            max_id = tw.id
    return max_id


def main():
    since_id = read_last_id()
    if not since_id.isdigit():
        since_id = 1
    last_id = int(since_id)

    for q in query_strings:
        tweets = search_tweets(q, since_id)
        if len(tweets) > 0:
            post_message(result_header_format.format(query=q), slack_channel_id)
            max_id = post_tweets_to_slack(tweets)
            if max_id > last_id:
                last_id = max_id

    post_message(last_id, slack_direct_message_id)


if __name__ == '__main__':
    main()
