#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if not x % 3 == 0 and not x % 5 == 0:
            print("{}".format(x), end='')
        if x % 3 == 0:
            print("Fizz", end='')
        if x % 5 == 0:
            print("Buzz", end='')
        print(" ", end='')
