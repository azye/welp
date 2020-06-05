import sys
import uuid
from .api import yelp
from .api import geolocation
import geocoder



def main():
    # uses this inaccurate api as test
    g = geocoder.ip('me')
    # print(g.latlng)

    print(geolocation.geolocate())



    # geo locate me

    # try google geolocation API first. 



    # stupid way of getting a mac address
    # mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0,8*6,8)][::-1])

    
    # print(mac_address)

    # yelp.query_api("food", 37.874101, -122.456201)


# sys.exit(main())
