#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve this challenge."""
import requests
import sys
if __name__ == "__main__":
    grab = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2],
        sys.argv[1]
    )
    r = requests.get(grab)
    try:
        jr = r.json()
        for i in range(10):
            print("{}: {}".format(
                jr[i]["sha"],
                jr[i]["commit"]["author"]["name"]
            ))
    except IndexError:
        pass
