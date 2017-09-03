#!/usr/bin/python3
"""
101-starwars.py
"""
import requests
import sys


def request_to_star_wars(the_url, payload):
    """makes a request to input URL with q as a parameter"""
    res = requests.get(the_url, params=payload).json()
    name_list = []
    count = res.get('count')
    if count > 0:
        results = res.get('results')
        for character in results:
            name_list.append(character.get('name'))
    next_page = res.get('next')
    while next_page:
        res = requests.get(next_page).json()
        results = res.get('results')
        for character in results:
            name_list.append(character.get('name'))
        next_page = res.get('next')
    print("Number of results: {}".format(count))
    for name in name_list:
        print(name)

if __name__ == "__main__":
    """MAIN APP"""
    the_url = "https://swapi.co/api/people/"
    payload = {'search': sys.argv[1]}
    request_to_star_wars(the_url, payload)
