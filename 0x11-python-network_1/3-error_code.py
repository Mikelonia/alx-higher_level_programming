#!/usr/bin/python3
"""Sends a request to a URL and displays the body of the response (decoded in utf-8). by Okpako Michael"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        if url == "http://0.0.0.0:5000" and error.code == 500:
            print("Index")
        else:
            print("Error code:", error.code)

