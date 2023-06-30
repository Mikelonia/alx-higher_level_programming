#!/bin/bash
# Takes in URL, send a POST request to the passed URL, and displays the body of the response, by Okpako Michael
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
