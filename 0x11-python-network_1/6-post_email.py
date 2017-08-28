#!/usr/bin/python3
"""
6-post_email.py
"""
import requests
import sys


def request_with_parameter(the_url, the_email):
    """makes a request to input URL with email as a parameter"""
    payload = {'email': the_email}
    r = requests.post(the_url, data=payload)
    print("{}".format(r.text))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = sys.argv[1]
    the_email = sys.argv[2]
    request_with_parameter(the_url, the_email)
