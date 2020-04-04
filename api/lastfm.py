import os
import sys
import configparser
import logging
import requests
import json

log = logging.getLogger(__name__)

class Lastfm:

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.environ['D_BOT_CFG'] + 'main.ini')

        self.lastfm_key = self.config['lastfm']['api_key']
        self.lastfm_secret = self.config['lastfm']['shared_secret']
        self.url_base = 'http://ws.audioscrobbler.com/2.0/'

    def get_recent_tracks(self, user):
        pass