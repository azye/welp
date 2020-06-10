import sys
import uuid
from .api import yelp
from .api import geolocation
import geocoder
import os
import click
import time
# from blessings import Terminal
from pydoc import pipepager
from termcolor import colored, cprint
from colorama import Fore, Back, Style

@click.command()
@click.option('--lat', default=None)
@click.option('--lng', default=None)
@click.option('--term', default='Restaurants')
def whateat(lat, lng, term):
    # pager('hello world\n' * 20 + 'hello world2\n' * 20)
    # pager()
        # time.sleep(10)


    # if there is latlong addes as arguments
    if not lat and not lng:
        # using google maps geolocation API if you have a key
        if 'GOOGLE_API_KEY' in os.environ:
            print('using Google API')
            geo = geolocation.geolocate()
            print(geo)
            lat = geo['location']['lat']
            lng = geo['location']['lng']
        else:
            # uses this inaccurate api as test
            print('using geocoder')
            g = geocoder.ip('me')
            print(g.latlng)

    bus = yelp.query_api(term, lat, lng)
    
    # for i in range(len(businesses)):
    #     # print(businesses[i])
    #     pprint.pprint(businesses[i], indent=2)

    pipepager(Fore.RED + str(bus), cmd='less -R')
