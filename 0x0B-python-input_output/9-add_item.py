#!/usr/bin/python3
from sys import argv
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file


def app():
    """adds input args to file"""
    try:
        a_list = load_from_json_file('./add_item.json')
    except:
        a_list = []
    for i in range(1, len(argv)):
        a_list.append(argv[i])
    save_to_json_file(a_list, './add_item.json')


if __name__ == '__main__':
    app()
