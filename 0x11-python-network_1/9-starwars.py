#!/usr/bin/python3
"""
9-starwars.py
"""
import requests
import sys


def request_to_star_wars(the_url, payload):
    """makes a request to input URL with q as a parameter"""
    res = requests.get(the_url, params=payload).json()
    count = res.get('count')
    print("Number of results: {}".format(count))
    if count > 0:
        results = res.get('results')
        for character in results:
            print(character.get('name'))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/"
    payload = {'search': sys.argv[1]}
    request_to_star_wars(the_url, payload)
