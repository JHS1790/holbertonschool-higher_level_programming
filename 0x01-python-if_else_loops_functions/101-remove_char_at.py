#!/usr/bin/env python3
def remove_char_at(str, n):
    cpstr = ''
    for x in range(len(str)):
        if not x == n:
            cpstr += str[x]
        else:
            pass
    return cpstr
