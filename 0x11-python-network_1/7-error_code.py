#!/usr/bin/python3
"""
7-error_code.py
"""
import requests
import sys


def request_error_check(the_url):
    """makes a request to input URL with checks for errors"""
    r = requests.get(the_url)
    if r.status_code > 200:
        print("Error code: {}".format(r.status_code))
    else:
        print("{}".format(r.text))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    request_error_check(the_url)
