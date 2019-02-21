from slackclient import SlackClient
from secret_info import slack_token
from secret_info import slack_direct_message_id

sc = SlackClient(slack_token)


def read_last_id():
    """
    Read the newest tweet which was already posted to use it since_id.
    NOTE: "The newest" means the largest tweet ID.
    Not last posted tweet into a Slack channel.
    :return: The last text posted by the administrator to the bot user.
    :rtype: str
    """

    latest_messages = sc.api_call(
        'im.history',
        channel=slack_direct_message_id,
        count=1,
    )['messages']
    return latest_messages[0]['text']


def post_message(text, channel_id):
    """
    Post a message to a Slack channel
    :param str text: Text to post
    :param str channel_id: Id of channel to post
    :return: None
    """
    sc.api_call(
        'chat.postMessage',
        channel=channel_id,
        text=text,
    )
