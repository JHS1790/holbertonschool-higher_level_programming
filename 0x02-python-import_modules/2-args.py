#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argc = len(argv) - 1
    i = 1
    if argc == 0:
        print("{} arguments.".format(argc))
    elif argc == 1:
        print("{} argument:".format(argc))
        while i <= argc:
            print("{}: {}".format(i, argv[i]))
            i += 1
    else:
        print("{} arguments:".format(argc))
        while i <= argc:
            print("{}: {}".format(i, argv[i]))
            i += 1
