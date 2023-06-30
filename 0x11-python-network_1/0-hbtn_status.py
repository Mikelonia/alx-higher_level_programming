#!/usr/bin/python3
'''Script that fetches my https://alx-intranet.htbn.io/status'''

import urllib.request

if __name__ == '__main__':
    text = '''Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'''
    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        result = response.read()

    print(text.format(type(result), result, str(result)[2:-1]))

