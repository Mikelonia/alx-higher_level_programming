#!/usr/bin/python3
# 101-locked_class.py
"""Defining a locked class."""


class LockedClass:
    """
    Preventing the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
