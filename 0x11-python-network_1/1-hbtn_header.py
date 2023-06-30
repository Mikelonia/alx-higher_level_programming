#!/usr/bin/python3
''' Takes in URL, send a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response by Okpako Michael'''

import urllib.request
import sys

if __name__ == '__main__':
    try:
        url = sys.argv[1]
        with urllib.request.urlopen(url) as response:
            headers = response.headers
            x_request_id = headers.get('X-Request-Id')
            print(x_request_id)
    except Exception:
        pass

