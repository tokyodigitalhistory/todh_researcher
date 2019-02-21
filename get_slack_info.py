from slackclient import SlackClient
from secret_info import slack_token
from pprint import pprint

sc = SlackClient(slack_token)


def get_slack_user_id():
    """
    Get your Slack user id from auth.test API
    :return: Your Slack user id
    :rtype: str
    """
    response = sc.api_call('auth.test')
    if not response['ok']:
        pprint(response)
        return None
    return response['user_id']


def find_slack_direct_message_id(user_id):
    """
    Get the id of direct message between you and bot user from your user id.
    :param str user_id: Your Slack user id
    :return: Direct message ID
    :rtype: str
    """

    response = sc.api_call('im.list')
    if not response['ok']:
        pprint(response)
        return None
    im_list = response['ims']
    for im in im_list:
        if im['user'] == user_id:
            return im['id']
    return None


def main():
    user_id = get_slack_user_id()
    if not user_id:
        print('abort')
        return False
    im_id = find_slack_direct_message_id(user_id)
    if not im_id:
        print('abort')
        return False
    print('slack_direct_message_id is', im_id)


if __name__ == '__main__':
    main()
