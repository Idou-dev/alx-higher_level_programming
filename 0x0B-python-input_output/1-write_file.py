#!/usr/bin/python3
"""defining write_file function"""


def write_file(filename="", text=""):
    """writes in filename with utf-8"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
