from twitter import search_tweets
from slack import read_last_id, post_message
from const import post_message_template, result_header_template, query_strings
from secret_info import slack_channel_id, slack_direct_message_id
from jinja2 import Template


def post_tweets_to_slack(tweets):
    """
    Search tweets and post them to a Slack channel
    :param Status tweets: Status object (tweet) to post to Slack
    :return: the id of the latest tweet among the tweets
    :rtype: int
    """
    max_id = 0
    for tw in tweets:
        tw_template = Template(post_message_template)
        post_text = tw_template.render(tweet=tw)
        post_message(post_text, slack_channel_id)
        # Update max_id when the tweet has larger ID than current one.
        if tw.id > max_id:
            max_id = tw.id
    return max_id


def main():
    since_id_str = read_last_id()
    # Initialize since_id
    since_id = 1
    if since_id_str.isdigit():
        since_id = int(since_id)
    # Initialize largest_id which will be new since_id
    largest_id = since_id

    for q in query_strings:
        tweets = search_tweets(q, since_id)
        if len(tweets) > 0:
            # Post a header
            header_template = Template(result_header_template)
            header_text = header_template.render(
                query=q, num_tweets=len(tweets)
            )
            post_message(header_text, slack_channel_id)
            max_id = post_tweets_to_slack(tweets)
            # Update largest_id when one of tweets has larger ID than the
            # current.
            if max_id > largest_id:
                largest_id = max_id

    post_message(largest_id, slack_direct_message_id)


if __name__ == '__main__':
    main()
