#!/usr/bin/python3
"""
3-error_code.py
"""
import urllib.request
import sys


def request_error_check(the_url):
    """makes a request to input URL with checks for errors"""
    req = urllib.request.Request(the_url)
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
        print("{}".format(html.decode('utf8')))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    request_error_check(the_url)
