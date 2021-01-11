#!/usr/bin/python3
"""
    a Python script that takes in a letter and
    sends a POST request to
    http://35c54c3227ed.7b77981b.hbtn-cod.io:5000/search_user with the
    letter as a parameter.
"""
import requests
import sys
if __name__ == "__main__":
    boi = 'jangles'
    try:
        q = sys.argv[1]
    except IndexError:
        q = ""
    r = requests.post(
        'http://35c54c3227ed.7b77981b.hbtn-cod.io:5000/search_user',
        data={"q": q}
        )
    try:
        jr = r.json()
        boi = 'howdy'
    except:
        print("Not a valid JSON")
    if boi == 'howdy':
        if jr != {}:
            print("[{}] {}".format(jr.get("id"), jr.get("name")))
        else:
            print("No result")
