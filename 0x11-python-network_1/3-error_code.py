#!/usr/bin/python3
"""Displays the value of the X-Request-Id variable found in
the header of the response. By Okpako Michael
"""

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as error:
        print('Error code:', error.code)

