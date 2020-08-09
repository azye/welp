import geocoder
import os

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

    def set_location(self, geo):
        if not self.location and not self.latitude and not self.longitude:
        # using google maps geolocation API if you have a key
            if 'GOOGLE_API_KEY' in os.environ:
                self.latitude = geo['location']['lat']
                self.longitude = geo['location']['lng']
            else:
                # dont use this. just look up your lat long at this point. 
                # useful to test without using an google geolocation API key tho
                g = geocoder.ip('me')
                self.latitude = g.latlng[0]
                self.longitude = g.latlng[1]
    
