#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return None
    roman_list = list(roman_string)
    arabic_number = 0
    roman_dict = {
        'I':1, 'IV':4, 'V':5, 'IX':9,
        'X':10, 'XL':40, 'L':50, 'XC':90,
        'C':100, 'CD':400, 'D':500, 'CM':900,
        'M':1000
    }
    x = 0
    while x < len(roman_list):
        if x < len(roman_list) - 1:
            if roman_dict[roman_list[x + 1]] > roman_dict[roman_list[x]]:
                cato = str(roman_list[x] + roman_list[x + 1])
                arabic_number += roman_dict[cato]
                x += 1
            else:
                arabic_number += roman_dict[roman_list[x]]
        else:
            arabic_number += roman_dict[roman_list[x]]
        x += 1
    return arabic_number
