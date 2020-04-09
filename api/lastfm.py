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
    
    def format_query_string(self, lastfm_object, method, user, *params):
        self.query_string = '?method={lastfm_object}.{method}&user={user}&api_key={key}&format=json'.format(
            lastfm_object=lastfm_object,
            method=method,
            user=user,
            key=self.lastfm_key
        )

        if params:
            final_query = ''
            for param in params:
                final_query += param

            return self.url_base + self.query_string + final_query
        else:
            query = self.url_base + self.query_string
            return query

    def get_recent_tracks(self, user):
        pass

fm = Lastfm()
q_s = fm.format_query_string('user', 'getrecenttracks', 'Spacesh1p', '&limit=5', '&test=1')
print(q_s)