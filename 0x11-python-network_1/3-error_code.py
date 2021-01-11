#!/usr/bin/python3
"""
    a Python script that takes in a URL, sends a
    request to the URL and displays the value of
    the X-Request-Id variable found in the header
    of the response.
"""
import urllib.error
import urllib.request
import sys
try:
    with urllib.request.urlopen(sys.argv[1]) as response:
        html = response.read()
        print(html.decode("utf-8"))
except urllib.error.HTTPError as error:
    print("Error code: {}".format(error.code))
