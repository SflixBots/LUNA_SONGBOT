import os
from os import environ




class Config(object):
                   BOT_TOKEN = environ['BOT_TOKEN']
                   APP_ID = int(environ['API_ID'])
                   API_HASH = environ['API_HASH']
