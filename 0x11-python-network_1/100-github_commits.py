#!/usr/bin/python3
"""
100-github_commits.py
"""
import requests
import sys


def request_to_github(the_url):
    """makes a request for commits from input url"""
    r = requests.get(the_url)
    the_json = r.json()
    for i in range(10):
        c = the_json[i]
        c_id = c.get('sha')
        c_author = c['commit']['author']['name']
        print('{}: {}'.format(c_id, c_author))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = ('https://api.github.com/repos/{}/{}/commits'
               .format(sys.argv[2], sys.argv[1]))
    request_to_github(the_url)
