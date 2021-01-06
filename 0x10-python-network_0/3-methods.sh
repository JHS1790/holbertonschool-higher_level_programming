#!/bin/bash
#takes in a URL and displays all HTTP
curl -i -s -X OPTIONS $1 | grep "Allow:" | cut -b 8-
