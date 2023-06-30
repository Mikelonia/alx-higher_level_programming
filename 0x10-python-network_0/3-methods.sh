#!/bin/bash
# Takes in a URL and displays all HTTP methods the server will accept..by  Okpako Michael
curl -sI "$1" | grep "Allow" | cut -d " "  -f2-
