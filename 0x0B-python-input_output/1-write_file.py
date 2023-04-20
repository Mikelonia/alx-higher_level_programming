#!/usr/bin/python3
# 3-write_file.py
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Writing a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as m:
        return m.write(text)
