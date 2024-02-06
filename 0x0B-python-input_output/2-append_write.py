#!/usr/bin/python3
"""defining append_write function"""


def append_write(filename="", text=""):
    """appends text in filename"""
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
