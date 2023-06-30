#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response. By Okpako Michael
"""

import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    value = {"email": email}

    r = requests.post(url, data=value)
    print(r.text)

