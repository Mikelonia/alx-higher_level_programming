#!/usr/bin/python3
# 7-save_to_json_file.py
"""Defining a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """Writing an object to a text file using JSON representation."""
    with open(filename, "w") as m:
        json.dump(my_obj, m)
