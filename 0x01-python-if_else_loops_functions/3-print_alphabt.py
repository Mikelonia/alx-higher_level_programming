#!/usr/bin/python3
# Author - Michael Okpako
for i in range(97, 123):
    if chr(i) == 'q' or chr(i) == 'e':
        continue
    print(chr(i).format(i), end='')
