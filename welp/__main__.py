import sys
import uuid
# from .api import yelp
from .api.client import Client
import geocoder
import os
import click
import pprint
import curses
import math
import pickle

from .menus import CursesWindow

@click.group()
def welp():
    pass


class ClickData:
    def __init__(self, term, location, latitude, longitude, radius, categories, locale, limit, sort_by, price, attributes, verbose):
        self.term = term.replace(' ', '+')
        self.location = location.replace(' ', '+') if location else None
        self.latitude = latitude
        self.longitude = longitude
        self.term = term
        self.radius = radius
        self.categories = categories
        self.locale = locale
        self.limit = limit
        self.sort_by = sort_by
        self.price = price
        self.attributes = attributes
        self.verbose = verbose

@click.command()
@click.option('--term', default='Restaurants', type=click.STRING)
@click.option('--location', type=click.STRING)
@click.option('--latitude', type=click.FLOAT)
@click.option('--longitude', type=click.FLOAT)
@click.option('--radius', default=5000, type=click.INT)
@click.option('--categories', default="", type=click.STRING)
@click.option('--locale', default="en_US", type=click.STRING)
@click.option('--limit', default=20, type=click.INT)
@click.option('--sort-by', default='best_match', type=click.STRING)
@click.option('--price', default='1,2,3', type=click.STRING)
@click.option('--attributes', default='', type=click.STRING)
@click.option('--verbose', default=False, type=click.BOOL)
def search(term, location, latitude, longitude, radius, 
categories, locale, limit, sort_by, price, attributes, verbose):


    dd = ClickData(term, location, latitude, longitude, radius, categories, locale, limit, sort_by, price, attributes, verbose)
    print(dd.__dict__)

    client = Client()

    # if location:
    #     dd.location =  location.replace(' ', '+')

    if not location and not latitude and not longitude:
        # using google maps geolocation API if you have a key
        if 'GOOGLE_API_KEY' in os.environ:
            geo = client.geolocation.geolocate()
            dd.latitude = geo['location']['lat']
            dd.longitude = geo['location']['lng']
        else:
            # dont use this. just look up your lat long at this point. 
            # useful to test without using an google geolocation API key tho
            g = geocoder.ip('me')
            dd.latitude = g.latlng[0]
            dd.longitude = g.latlng[1]
    
    if dd.verbose:
        print(dd)
    
    bus = client.yelp.query_api(dd)
    # print(bus.__dict__)
    
    c = CursesWindow(['{} {} {}'.format(x['name'], x['price'], x['rating']) for x in bus])
    c.open_screen()

welp.add_command(search)
