#!/usr/bin/python3
# Author - Michael Okpako
for digit1 in range(0, 8):
    for digit2 in range(digit1 + 1, 10):
         print("{:d}{:d}".format(digit1, digit2), end=', ')
print("{:d}{:d}".format(digit1 + 1, digit2))
