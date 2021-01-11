#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a
    request to the URL and displays the value of
    the X-Request-Id variable found in the header
    of the response.
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
