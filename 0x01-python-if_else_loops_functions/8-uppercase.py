#!/usr/bin/python3
def uppercase(str):
    cpstr = ""
    for x in range(0, len(str)):
        oldascval = ord(str[x])
        if oldascval >= 97 and oldascval <= 122:
            newascval = oldascval - 32
            cpstr = cpstr + chr(newascval)
        else:
            cpstr = cpstr + chr(oldascval)
    print(cpstr)
