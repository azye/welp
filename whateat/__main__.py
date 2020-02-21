import sys
from .api import yelp



# Defaults for our simple example.
DEFAULT_TERM = 'dinner'
DEFAULT_LOCATION = 'San Francisco, CA'
SEARCH_LIMIT = 3

def main():
    print("yo")
    try:
        yelp.query_api(DEFAULT_TERM, DEFAULT_LOCATION)
    except HTTPError as error:
        sys.exit(
            'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                error.code,
                error.url,
                error.read(),
            )
        )

sys.exit(main())
