#!/usr/bin/python3
"""defining to_json_string"""


import json


def to_json_string(my_obj):
    """returns representation of an object"""
    return json.dumps(my_obj)
