from __future__ import print_function

import argparse
import json
import pprint
import sys
import urllib
import os
import requests

from urllib.error import HTTPError
from urllib.parse import quote
from urllib.parse import urlencode

API_KEY= os.environ['YELP_API_KEY'] 
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.
SEARCH_LIMIT = 20

def request(host, path, api_key, url_params=None):
    url_params = url_params or {}
    url = f"{host}{quote(path.encode('utf8'))}"
    headers = {
        'Authorization': 'Bearer %s' % api_key,
    }

    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers=headers, params=url_params)

    return response.json()


def search(api_key, term, latitude, longitude):
    url_params = {
        'term': term.replace(' ', '+'),
        'latitude': latitude,
        'longitude': longitude,
        'radius': 5000,
        'limit': SEARCH_LIMIT,
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)


def get_business(api_key, business_id):
    """Query the Business API by a business ID.

    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    business_path = BUSINESS_PATH + business_id

    return request(API_HOST, business_path, api_key)

def query_api(term, latitude, longitude):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    response = search(API_KEY, term, latitude, longitude)

    businesses = response.get('businesses')

    if not businesses:
        # print(u'No businesses for {0} in {1} found.'.format(term, location))
        return
    for b in businesses:
        print(b)
        # pprint.pprint(b['name'], indent=2)
        