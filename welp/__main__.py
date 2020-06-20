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

# from .menus import CursesWindow

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
    
    bus = client.yelp.query_api(url_params)

    for i in range(len(bus)):
        # print(bus[i])
        print(bus[i]['id'] if verbose else '', bus[i]['name'], bus[i]['price'], bus[i]['rating'])

    print_window()
    # cw = CursesWindow()
    # cw.render_screen()


# class CursesWindow:
#     def __init__(self):
#         b = curses.initscr()
#         self.curse = curses.newpad(100, 100)
#         curses.noecho()
#         curses.cbreak()
#         b.keypad(True)


#     def render_screen(self):
#         self.curse.clear()
#         for y in range(0, 99):
#             for x in range(0, 99):
#                 self.curse.addch(y,x, ord('a') + (x*x+y*y) % 26)
#         self.curse.refresh( 0,0, 5,5, 20,75)

    
def print_window():
    screen = curses.initscr()
    curses.noecho()
    curses.cbreak()
    curses.start_color()
    screen.keypad( 1 )
    curses.init_pair(1,curses.COLOR_BLACK, curses.COLOR_CYAN)
    highlightText = curses.color_pair( 1 )
    normalText = curses.A_NORMAL
    screen.border( 0 )
    curses.curs_set( 0 )
    max_row = 10 #max number of rows
    box = curses.newwin( max_row + 2, 64, 1, 1 )
    box.box()


    strings = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n" ] #list of strings
    row_num = len( strings )

    pages = int( math.ceil( row_num / max_row ) )
    position = 1
    page = 1
    for i in range( 1, max_row + 1 ):
        if row_num == 0:
            box.addstr( 1, 1, "There aren't strings", highlightText )
        else:
            if (i == position):
                box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
            else:
                box.addstr( i, 2, str( i ) + " - " + strings[ i - 1 ], normalText )
            if i == row_num:
                break

    screen.refresh()
    box.refresh()

    x = screen.getch()
    while x != 27:
        if x == curses.KEY_DOWN:
            if page == 1:
                if position < i:
                    position = position + 1
                else:
                    if pages > 1:
                        page = page + 1
                        position = 1 + ( max_row * ( page - 1 ) )
            elif page == pages:
                if position < row_num:
                    position = position + 1
            else:
                if position < max_row + ( max_row * ( page - 1 ) ):
                    position = position + 1
                else:
                    page = page + 1
                    position = 1 + ( max_row * ( page - 1 ) )
        if x == curses.KEY_UP:
            if page == 1:
                if position > 1:
                    position = position - 1
            else:
                if position > ( 1 + ( max_row * ( page - 1 ) ) ):
                    position = position - 1
                else:
                    page = page - 1
                    position = max_row + ( max_row * ( page - 1 ) )
        if x == curses.KEY_LEFT:
            if page > 1:
                page = page - 1
                position = 1 + ( max_row * ( page - 1 ) )

        if x == curses.KEY_RIGHT:
            if page < pages:
                page = page + 1
                position = ( 1 + ( max_row * ( page - 1 ) ) )
        if x == ord( "\n" ) and row_num != 0:
            screen.erase()
            screen.border( 0 )
            screen.addstr( 14, 3, "YOU HAVE PRESSED '" + strings[ position - 1 ] + "' ON POSITION " + str( position ) )

        box.erase()
        screen.border( 0 )
        box.border( 0 )

        for i in range( 1 + ( max_row * ( page - 1 ) ), max_row + 1 + ( max_row * ( page - 1 ) ) ):
            if row_num == 0:
                box.addstr( 1, 1, "There aren't strings",  highlightText )
            else:
                if ( i + ( max_row * ( page - 1 ) ) == position + ( max_row * ( page - 1 ) ) ):
                    box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], highlightText )
                else:
                    box.addstr( i - ( max_row * ( page - 1 ) ), 2, str( i ) + " - " + strings[ i - 1 ], normalText )
                if i == row_num:
                    break



        screen.refresh()
        box.refresh()
        x = screen.getch()

        


welp.add_command(search)
