import sys
from .api import yelp
# import geocoder


def main():
    # uses this inaccurate api as test
    # g = geocoder.ip('me')
    # print(g.latlng)

    yelp.query_api("food", 37.874101, -122.456201)


sys.exit(main())
