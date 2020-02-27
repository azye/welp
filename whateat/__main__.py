import sys
from .api import yelp
import geocoder



# Defaults for our simple example.
DEFAULT_TERM = 'asian'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3

def main():
    # print("yo")
    # g = geocoder.ip('me')

    # print(g.latlng)

    
    try:
        yelp.query_api(DEFAULT_TERM, 37.773251, -122.484431)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

sys.exit(main())
