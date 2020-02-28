import sys
from .api import yelp
import geocoder


def main():
    # uses this inaccurate api as test
    g = geocoder.ip('me')
    print(g.latlng)

    yelp.query_api("burgers", g.latlng[0], g.latlng[1])


sys.exit(main())
