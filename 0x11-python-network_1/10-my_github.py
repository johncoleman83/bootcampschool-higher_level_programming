#!/usr/bin/python3
"""
10-my_github.py
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


def request_to_github(the_url, un, pw):
    """makes a request to input URL with q as a parameter"""
    r = requests.get(the_url, auth=HTTPBasicAuth(un, pw))
    json = r.json()
    print("{}".format(json.get("id")))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = 'https://api.github.com/user'
    request_to_github(the_url, sys.argv[1], sys.argv[2])
