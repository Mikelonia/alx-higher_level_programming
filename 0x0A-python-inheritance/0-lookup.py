#!/usr/bin/python3
# 0-lookup.py
"""Defining an object attribute lookup function."""


def lookup(obj):
    """Returning a list of an object's available attributes."""
    return (dir(obj))
