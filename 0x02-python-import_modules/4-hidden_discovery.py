#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    strlist = dir(hidden_4)
    i = 0
    while i < len(strlist):
        if not strlist[i].startswith('__'):
            print("{}".format(strlist[i]))
        i += 1
