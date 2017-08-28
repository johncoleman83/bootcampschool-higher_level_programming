#!/usr/bin/python3
"""
4-hbtn_status.py
"""
import requests


def display_request_data(the_url):
    """makes a request to specified URL & displays data on the request"""
    r = requests.get(the_url)
    html = r.content
    print("Body response:")
    print("    - type: {}".format(type(html)))
    print("    - content: {}".format(html))
    print("    - utf8 content: {}".format(html.decode('utf8')))


if __name__ == "__main__":
    """MAIN APP"""
    display_request_data("https://intranet.hbtn.io/status")
