#!/usr/bin/python3
"""
9-starwars.py
"""
import requests
import sys


def request_to_star_wars(the_url):
    """makes a request to input URL with q as a parameter"""
    r = requests.get(the_url)
    json = r.json()
    count = json.get('count')
    print("Number of result: {}".format(count))
    if count > 0:
        results = json.get('results')
        for character in results:
            print(character.get('name'))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/?search={}".format(sys.argv[1])
    request_to_star_wars(the_url)
