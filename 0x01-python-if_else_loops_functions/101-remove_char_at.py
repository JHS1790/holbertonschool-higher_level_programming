#!/usr/bin/env python3
def remove_char_at(str, n):
#    if n > len(str) or n < 0:
#        return(str)
#    return str.replace(str[n], '')
    cpstr = ''
    for x in range(len(str)):
        if not x == n:
            cpstr += str[x]
        else:
            pass
    return cpstr
