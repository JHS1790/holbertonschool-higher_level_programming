#!/usr/bin/python3
"""File for Task 1"""


class MyList(list):
    """class"""

    def print_sorted(self):
        """method"""
        sortList = []
        indexList = self[:]
        storeY = 0
        for i in range(len(self)):
            smallest = indexList[0]
            for y in range(len(indexList)):
                if indexList[y] <= smallest:
                    smallest = indexList[y]
                    storeY = y
            sortList.append(smallest)
            del indexList[storeY]
        print(sortList)
