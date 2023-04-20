#!/usr/bin/python3
# 100-my_int.py
"""Defining a class MyInt that inherits from int."""


class MyInt(int):
    """Inverting int operators == and !=."""

    def __eq__(self, value):
        """Override == operator with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
