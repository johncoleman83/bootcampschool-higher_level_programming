#!/usr/bin/python3
"""
1-btcp_header.py
"""
import urllib.request
import sys


def value_request_id(the_url):
    """makes a request to input URL & displays value of X-Request-Id"""
    with urllib.request.urlopen(the_url) as response:
        headers = response.info()
    print("{}".format(headers.get("X-Request-Id")))


if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    value_request_id(the_url)
