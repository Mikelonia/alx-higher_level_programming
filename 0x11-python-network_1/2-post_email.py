#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in
the header of the response. By Okpako Michael
"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    value = {"email": argv[2]}
    request = Request(argv[1], urlencode(value).encode("ascii"))

    with urlopen(request) as response:
        head = response.headers.get('X-Request-Id')
        print(response.read().decode('utf-8'))

