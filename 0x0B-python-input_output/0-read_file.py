#!/usr/bin/python3
"""read_file methode"""


def read_file(filename=""):
    """reads a text file and prints it to the stdout"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_d = f.read()
    print(read_d)
