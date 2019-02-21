from slackclient import SlackClient
from secret_info import slack_token
from secret_info import slack_direct_message_id

sc = SlackClient(slack_token)


def get_my_user_id():
    auth_data = sc.api_call('auth.test')
    return auth_data['user_id']


def read_last_id():
    latest_messages = sc.api_call(
        'im.history',
        channel= slack_direct_message_id,
        count=1,

    )['messages']
    return latest_messages[0]['text']


def post_message(text, channel_id):
    sc.api_call(
        'chat.postMessage',
        channel=channel_id,
        text=text,
    )
