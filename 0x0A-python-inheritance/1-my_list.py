#!/usr/bin/python3
# 1-my_list.py
"""Defining an inherited list class MyList."""


class MyList(list):
    """Implementing sorted printing for the built-in list class."""

    def print_sorted(self):
        """Printing a list in sorted ascending order."""
        print(sorted(self))
