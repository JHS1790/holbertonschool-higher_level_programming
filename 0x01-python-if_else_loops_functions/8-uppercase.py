#!/usr/bin/python3
#def uppercase(str):
#    cpstr = ""
#    for x in range(0, len(str)):
#        oldascval = ord(str[x])
#        if oldascval >= 97 and oldascval <= 122:
#            newascval = oldascval - 32
#            cpstr = cpstr + chr(newascval)
#        else:
#            cpstr = cpstr + chr(oldascval)
#    print(cpstr)
def uppercase(str):
    for letter in str:
        if ord(letter) >= ord('a') and ord(letter) <= ord('z'):
            letter = ord(letter) - 32
            letter = chr(letter)
        print("{}".format(letter), end='')
    print('')
