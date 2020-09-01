#!/usr/bin/env python3
def remove_char_at(str, n):
#    if n > len(str) or n < 0:
#        return(str)
#    return str.replace(str[n], '')
    cp1str = str[:]
    cpstr = ''
    for x in range(len(cp1str)):
        if not x == n:
            cpstr += cp1str[x]
        else:
            pass
    return cpstr
