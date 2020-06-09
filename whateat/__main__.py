import sys
import uuid
from .api import yelp
from .api import geolocation
import geocoder
import os
import click
import time
from blessings import Terminal

@click.command()
@click.option('--lat', default=None)
@click.option('--lng', default=None)
@click.option('--term', default='Restaurants')
def whateat(lat, lng, term):
    term = Terminal()
    with term.fullscreen() and term.hidden_cursor():
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        print(term.red_on_green('Red on green? Ick!'))
        print(term.yellow('I can barely see it.'))
        # time.sleep(10)


    # if there is latlong addes as arguments
    # if not lat and not lng:
    #     # using google maps geolocation API if you have a key
    #     if 'GOOGLE_API_KEY' in os.environ:
    #         print('using Google API')
    #         geo = geolocation.geolocate()
    #         print(geo)
    #         lat = geo['location']['lat']
    #         lng = geo['location']['lng']
    #     else:
    #         # uses this inaccurate api as test
    #         print('using geocoder')
    #         g = geocoder.ip('me')
    #         print(g.latlng)

    # yelp.query_api(term, lat, lng)
