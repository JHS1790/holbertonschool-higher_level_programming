#!/usr/bin/python3

for x in range(26, 0, -1):
    if x % 2 == 0:
        y = 96
    else:
        y = 64
    print("{}".format(chr(x + y)), end='')
