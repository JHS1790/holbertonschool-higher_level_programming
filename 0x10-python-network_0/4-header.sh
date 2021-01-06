#!/bin/bash
#takes in a URL as an argument, sends a GET request to
curl -X GET -s -H "X-HolbertonSchool-User-Id: 98" $1
