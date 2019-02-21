from slackclient import SlackClient
from secret_info import slack_token
from secret_info import slack_direct_message_id

sc = SlackClient(slack_token)


def read_last_id():
    """
    :return: The text posted by administrator to the bot user.
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
    :param text: str
    :param channel_id: str
    :return: None
    """
    sc.api_call(
        'chat.postMessage',
        channel=channel_id,
        text=text,
    )
