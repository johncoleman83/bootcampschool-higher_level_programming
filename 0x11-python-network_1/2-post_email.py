#!/usr/bin/python3
"""
2-post_email.py
"""
import urllib.request
import urllib.parse
import sys


def request_with_parameter(the_url, the_email):
    """makes a request to input URL with email as a parameter"""
    values = {'email': the_email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(the_url, data)
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print("{}".format(html.decode('utf8')))


if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    the_email = sys.argv[2]
    request_with_parameter(the_url, the_email)
