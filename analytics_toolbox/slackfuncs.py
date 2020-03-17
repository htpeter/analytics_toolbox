#AUTOGENERATED! DO NOT EDIT! File to edit: dev/11_slackfuncs.ipynb (unless otherwise specified).

__all__ = ['SlackClient', 'ENDPOINT', 'users_dataframe', 'add_slack_user_ids_to_message']

#Cell

import os
import configparser
import pandas as pd
import slack

ENDPOINT = 'https://hooks.slack.com/services'

class SlackClient:
    def __init__(self, config_file, config_section):
        self.client = self.get_bot_slack_client(config_file = config_file)

    def get_bot_slack_client(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)
        client = slack.WebClient(config[config_section]['bot_user_oauth_token'])
        return client

    def send_message(self, channel, text):
        self.client.chat_postMessage(
                channel = channel,
                text = text)


#Cell

def users_dataframe(client):
    """
    Gets dataframe of User Information.

    """
    data = []
    users_list = client.users_list()
    for user in users_list['members']:
        data.append(user)
    return pd.DataFrame(data)


#Cell

def add_slack_user_ids_to_message(msg: str, slack_user_map: dict) -> str:
    for replacable_name, slack_username in slack_user_map.items():
        msg = msg.replace(replacable_name, '<@'+ slack_username + '>')
    return msg