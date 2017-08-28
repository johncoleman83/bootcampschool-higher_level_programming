#!/usr/bin/python3
"""
8-json_api.py
"""
import requests
import sys


def request_with_parameter(the_url, q):
    """makes a request to input URL with q as a parameter"""
    payload = {'q': q}
    r = requests.post(the_url, data=payload)
    c_type = r.headers.get('content-type')
    if c_type == 'application/json':
        json = r.json()
        if len(json) > 0:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    else:
        print("Not a valid JSON")

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "http://0.0.0.0:5000/search_user"
    try:
        q = sys.argv[1]
    except:
        q = ""
    request_with_parameter(the_url, q)
