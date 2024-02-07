#!/usr/bin/python3
"""defining save_to_json_file function"""


import json


def save_to_json_file(my_obj, filename):
    """writes an object to a text file using json"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
