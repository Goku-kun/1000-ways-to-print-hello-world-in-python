import math
from urllib.parse import urlencode
import random
import asyncio
import functools
import itertools
import requests
import base64
import datetime


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        Returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret == None or client_secret == None:
            raise Exception('You must set client_ID and client_secret')
        client_creds = f'{client_id}:{client_secret}'
        client_creds_base64 = base64.b64encode(client_creds.encode())
        return client_creds_base64.decode()

    def get_token_headers(self):
        client_creds_base64 = self.get_client_credentials()
        return {
            'Authorization': f'Basic {client_creds_base64}'
        }

    def get_token_data(self):
        return {
            'grant_type': 'client_credentials'
        }

    def perfom_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)
        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client.")
        now = datetime.datetime.now()
        data = r.json()
        access_token = data['access_token']
        expires_in = data['expires_in']
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        self.access_token = access_token
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perfom_auth()
            return self.get_access_token()
        elif token == None:
            self.perfom_auth()
            return self.get_access_token()
        return token

    def spotify_track(self, link):
        access_token = self.get_access_token()
        id = link[31:53]
        headers = {
            'Authorization': f'Bearer {access_token}'
        }
        endpoint = 'https://api.spotify.com/v1/tracks'

        lookup_url = f"{endpoint}/{id}"
        r = requests.get(lookup_url, headers=headers)
        if r.status_code in range(200, 299):
            data = r.json()
            track_name = data['name']
            artist_name = data['artists'][0]['name']
            return [track_name,artist_name]

client_id = '9f31c31d0a4c40178302ff79ccfc59df'
client_secret = '87ed19e8b607442e9a871ec4f183a499'
spotify = SpotifyAPI(client_id, client_secret)
# print(''.join(x for x in str(spotify.spotify_track('https://open.spotify.com/track/21AUdfi6fLFDp9JuNcHsfS')[0]) if x not in [',']))
print(str(spotify.spotify_track('https://open.spotify.com/track/21AUdfi6fLFDp9JuNcHsfS')[0])+'!')
