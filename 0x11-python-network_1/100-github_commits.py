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
    results = []
    c_range = 10 if len(the_json) >= 10 else len(the_json)
    for i in range(c_range):
        c = the_json[i]
        c_sha = c.get('sha')
        c_author = c.get('commit').get('author').get('name')
        # print('{}: {}'.format(c_sha, c_author))
        c_date = c.get('commit').get('author').get('date')
        results.append([c_date, c_sha, c_author])
    results = list(reversed(sorted(results)))
    for i in range(10):
        c = results[i]
        print('{}: {}'.format(c[1], c[2]))

if __name__ == "__main__":
    """MAIN APP"""
    the_url = ('https://api.github.com/repos/{}/{}/commits'
               .format(sys.argv[2], sys.argv[1]))
    request_to_github(the_url)
