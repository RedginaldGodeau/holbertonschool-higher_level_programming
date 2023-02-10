#!/usr/bin/python3
""" DOCUMENTATION """

class MyList:
    """ DOCUMENTATION """
    
    def __init__(self):
        self.__list = []

    def print_sorted(self):
        """ FUNCTION """
        list = self.__list.copy()
        list.sort()
        print(str(list))
 
    def append(self, number):
        """ FUNCTION """
        self.__list.append(number)
    
    def __str__(self):
        return (str(self.__list))
