
import geocoder
import argparse
import json
import pprint
import uuid
import sys
import urllib
import os
import requests

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode


# API constants, you shouldn't have to change these.
API_HOST = 'https://www.googleapis.com'
SEARCH_PATH = '/geolocation/v1/geolocate'

# def geolocate():
#     url_params = {
#         'key': API_KEY,
#     }

#     body = {
#         'macAddress': ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]),
#     }

#     url_params = url_params or {}
#     url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))

#     response = requests.request('POST', url, params=url_params, data=body)

#     return response.json()


class Geolocation:
    def __init__(self, client):
        self.client = client
    
    def geolocate(self):
        try:
            API_KEY = os.environ['GOOGLE_API_KEY']
            print('google api key...')
            url_params = {
                'key': API_KEY,
            }
            
            body = {
                'macAddress': ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1]),
            }

            url_params = url_params or {}
            url = '{0}{1}'.format(API_HOST, quote(SEARCH_PATH.encode('utf8')))

            response = self.client.session.request('POST', url, params=url_params, data=body)
            return response['location']['lat'], response['location']['lng']

        except KeyError:
                # dont use this irl. just look up your lat long at this point. 
                # useful to test without using an google geolocation API key tho
                print('no google api key, try geocoder...')
                g = geocoder.ip('me')
                return g.latlng[0], g.latlng[1]
