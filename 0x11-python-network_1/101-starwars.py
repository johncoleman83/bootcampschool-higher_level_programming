#!/usr/bin/python3
"""
101-starwars.py
"""
import requests
import sys


def request_to_star_wars(the_url, payload):
    """makes a request to input URL with q as a parameter"""
    r = requests.get(the_url, params=payload)
    r_json = r.json()
    name_list = []
    count = r_json.get('count')
    if count > 0:
        results = r_json.get('results')
        for character in results:
            name_list.append(character.get('name'))
    while r_json.get('next'):
        r = requests.get(r_json.get('next'))
        r_json = r.json()
        results = r_json.get('results')
        for character in results:
            name_list.append(character.get('name'))
    print("Number of result: {}".format(count))
    for name in name_list:
        print(name)

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/"
    payload = {'search': sys.argv[1]}
    request_to_star_wars(the_url, payload)
