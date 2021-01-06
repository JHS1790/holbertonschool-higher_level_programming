#!/bin/bash
#takes in a URL, sends a POST request to the
curl $1 -s -X POST --data "email=hr@holbertonschool.com&subject=I will always be here for PLD"
