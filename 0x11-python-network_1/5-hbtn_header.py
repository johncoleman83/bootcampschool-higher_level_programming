#!/usr/bin/python3
"""
5-hbtn_header.py
"""
import requests
import sys


def value_request_id(the_url):
    """makes a request to input URL & displays value of X-Request-Id"""
    r = requests.get(the_url)
    print("{}".format(r.headers.get("X-Request-Id")))


if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    value_request_id(the_url)
