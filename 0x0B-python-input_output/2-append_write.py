#!/usr/bin/python3
"""append_write method that appends a sting at
the end of a text file"""


def append_write(filename="", text=""):
    """appends string at the end of a text file (UTF8)
    and returns the number of characters added:"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
