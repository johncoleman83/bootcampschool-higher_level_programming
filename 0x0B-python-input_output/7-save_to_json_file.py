#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """saves JSON to file"""
    with open(filename, mode='w', encoding='utf-8') as f_io:
        f_io.write(json.dumps(my_obj))
        f_io.close()
