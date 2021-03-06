#!/usr/bin/python3
"""
    a Python script that takes your Github credentials
    (username and password) and uses the Github API to
    display your id
"""
import requests
import sys
if __name__ == "__main__":
    name = str(sys.argv[1])
    pswd = str(sys.argv[2])
    r = requests.get(
        "https://api.github.com/user",
        auth=(requests.auth.HTTPBasicAuth(name, pswd))
    )
    try:
        jr = r.json()
        print(jr.get("id"))
    except:
        print("None")
