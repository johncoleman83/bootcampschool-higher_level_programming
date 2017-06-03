#!/usr/bin/python3
import json
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
from sys import argv


def app():
    """adds input args to file"""
    a_list = []
    for i in range(1, len(argv)):
        a_list.append(argv[i])
    with open('./add_item.json', mode='w', encoding='utf-8') as f_io:
        f_io.write(json.dumps(a_list))
        f_io.close()


if __name__ == '__main__':
    app()
