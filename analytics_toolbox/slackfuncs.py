# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/11_slackfuncs.ipynb (unless otherwise specified).

__all__ = ['BotUser', 'users_dataframe', 'ENDPOINT']

# Cell
"""
useful slack functions.

Use <@userid> to tag a user in a message.
"""

import os
import configparser
import pandas as pd
import slack

ENDPOINT = 'https://hooks.slack.com/services'

class BotUser:
    def __init__(self, config_file):
        self.client = self.get_bot_slack_client(config_file = config_file)

    def get_bot_slack_client(self, config_file = 'config.ini'):
        config = configparser.ConfigParser()
        config.read(config_file)
        client = slack.WebClient(config['slack']['bot_user_oauth_token'])
        return client

    def send_message(self, channel, text):
        self.client.chat_postMessage(channel = channel,
                                     text = text)

def users_dataframe(client):
    """
    Gets dataframe of User Information.
    """
    data = []
    users_list = client.users_list()
    for user in users_list['members']:
        data.append(user)
    return pd.DataFrame(data)

if __name__ == '__main__':
    bot = BotUser()
    users = users_dataframe(bot.client)
