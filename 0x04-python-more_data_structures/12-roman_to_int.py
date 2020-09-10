#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return None
    roman_list = list(roman_string)
    arabic_number = 0
    roman_dict = {
        'I':1, 'IV':4, 'V':5, 'IX':9,
        'X':10, 'L':50, 'C':100, 'D':500,
        'M':1000
    }
    x = 0
    while x < len(roman_list):
        if roman_list[x] is not 'I':
            arabic_number += roman_dict[roman_list[x]]
        else:
            if x == len(roman_list) - 1 or roman_list[x + 1] == 'I':
                arabic_number += 1
            else:
                cato = str(roman_list[x] + roman_list[x + 1])
                arabic_number += roman_dict[cato]
                x += 1
        x += 1
    return arabic_number
