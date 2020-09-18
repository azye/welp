import sys
import uuid
import geocoder
import os
import click
import pprint
import curses
import math
from .welp import Welp
from .click_data import ClickData


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
    welp = Welp()

    click_data = ClickData(
        term,
        location,
        latitude,
        longitude,
        radius,
        categories,
        locale,
        limit,
        sort_by,
        price,
        attributes,
        verbose)

    if not click_data.latitude and not click_data.longitude:
        print('geolocating...')
        lat, ln = welp.api_client.geolocation.geolocate()
        click_data.set_location(lat, ln)

    bus = welp.api_client.yelp.query_api(click_data)
    welp.ui.set_data(
        ['{} {} {}'.format(x['name'], x['price'], x['rating']) for x in bus])
    welp.ui.open_curses_ui()


welp.add_command(search)
