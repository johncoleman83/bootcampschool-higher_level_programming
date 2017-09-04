#!/usr/bin/python3
"""
103-search_twitter.py
"""
import requests
import sys
import base64


def base_64_encode(key, secret):
    """encodes key and secret in base 64 for the auth credential"""
    conversion_string = "{}:{}".format(key, secret).encode('ascii')
    auth_credential = base64.b64encode(conversion_string)
    auth_credential = auth_credential.decode()
    return auth_credential


def get_bearer_token(auth_credential):
    """gets bearer token from twitter OAuth"""
    oauth_url = "https://api.twitter.com/oauth2/token"
    the_header = {
        "Authorization": "Basic {}".format(auth_credential),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"
        }
    the_data = {
        "grant_type": "client_credentials"
        }
    res = requests.post(
        oauth_url,
        headers=the_header,
        data=the_data
    )
    res = res.json()
    if res.get("token_type") == "bearer":
        bearer_token = res.get("access_token")
        return bearer_token
    else:
        raise Exception("ERROR, no bearer token returned")


def make_query(query_param, bearer_token):
    """makes a request to twitter search api using the input values:
    the query, and the bearer token"""
    query_url = 'https://api.twitter.com/1.1/search/tweets.json'
    payload = {
        'q': query_param
        }
    the_header = {
        'Authorization': 'Bearer {}'.format(bearer_token)
        }
    res = requests.get(
        query_url,
        params=payload,
        headers=the_header
    )
    return res.json()


def print_five_tweets(response):
    """prints five tweets from response of twitter API request
    FORMAT: [<Tweet ID>] <Tweet text> by <Tweet owner name>"""
    statuses = response.get('statuses')
    the_range = 5 if len(statuses) > 5 else len(statuses)
    for i in range(the_range):
        tweet = statuses[i]
        tweet_id = tweet.get('id_str')
        tweet_text = tweet.get('text')
        tweet_user_name = tweet.get('user').get('name')
        print("[{}] {} by {}".format(tweet_id, tweet_text, tweet_user_name))


def query_twitter_api_run_app():
    """main application: authenticates credentials from user input,
    then searches twitter api from input search terms"""
    key = sys.argv[1]
    secret = sys.argv[2]
    query_param = sys.argv[3]
    auth_credential = base_64_encode(key, secret)
    bearer_token = get_bearer_token(auth_credential)
    response = make_query(query_param, bearer_token)
    print_five_tweets(response)

if __name__ == "__main__":
    """MAIN APP"""
    query_twitter_api_run_app()
