import os
import sys
import configparser
import logging
import requests
import json

log = logging.getLogger(__name__)

class LastFm:

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

    def now_playing(self, lastfm_username):
        fm = LastFm()
        query_string = fm.format_query_string('user', 'getrecenttracks', lastfm_username, '&limit=4')
        try:
            response = requests.get(query_string).json()
        except:
            log.error('Invalid response from API')
            return None

        recent_tracks = response['recenttracks']['track']
        
        return_tracks = []

        for track in recent_tracks:
                track_item = {}
    
                track_item.update({
                    'artist':track['artist']['#text'],
                    'album':track['album']['#text'],
                    'song':track['name']
                })
    
                if '@attr' in track:
                    track_item.update({
                        'nowplaying':track['@attr']['nowplaying']
                    })
    
                else:
                    pass
    
                return_tracks.append(track_item)
        
        return return_tracks

# fm = LastFm()
# q_s = fm.format_query_string('user', 'getrecenttracks', 'Spacesh1p', '&limit=5', '&test=1')
# print(q_s)