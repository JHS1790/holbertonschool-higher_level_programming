#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for y in range(list_length):
        try:
            new_list.append(my_list_1[y] / my_list_2[y])
        except TypeError:
            print("wrong type".format())
            new_list.append(0)
            pass
        except ZeroDivisionError:
            print("division by 0".format())
            new_list.append(0)
            pass
        except IndexError:
            print("out of range".format())
            new_list.append(0)
            pass
        finally:
            pass
    return(new_list)
