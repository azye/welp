import sys
import uuid
# from .api import yelp
from .api.client import Client
import geocoder
import os
import click
import pprint

@click.group()
def welp():
    pass

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
    url_params = {
        'term': term.replace(' ', '+'),
        'radius': radius,
        'categories': categories,
        'locale': locale,
        'limit': limit,
        'sort-by': sort_by,
        'price': price,
        'attributes': attributes,
    }

    client = Client()

    if location:
        url_params['location'] =  location.replace(' ', '+')

    if not location and not latitude and not longitude:
        # using google maps geolocation API if you have a key
        if 'GOOGLE_API_KEY' in os.environ:
            geo = client.geolocation.geolocate()
            url_params['latitude'] = geo['location']['lat']
            url_params['longitude'] = geo['location']['lng']
        else:
            # dont use this. just look up your lat long at this point. 
            # useful to test without using an google geolocation API key tho
            g = geocoder.ip('me')
            url_params['latitude'] = g.latlng[0]
            url_params['longitude'] = g.latlng[1]
    
    if verbose:
        print(url_params)
    
    # bus = yelp.query_api(url_params)

    # for i in range(len(bus)):
    #     # print(bus[i])
    #     print(bus[i]['id'] if verbose else '', bus[i]['name'], bus[i]['price'], bus[i]['rating'])

welp.add_command(search)
