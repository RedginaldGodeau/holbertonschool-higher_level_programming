#!/usr/bin/python3
""" Doc """
import unittest

def max_integer(list=[]):
    """Function to find and return the max integer in a list of integers
        If the list is empty, the function returns None
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result

class FonctionTest(unittest.TestCase):
    def test1(self):
        print(max_integer([1, 2, 3, 4]))
    def test2(self):
        print(max_integer([]))
    def test3(self):
        print(max_integer([1, "A", 3, 4]))
    def test4(self):
        print(max_integer([5.524, 2.532, 0, -5]))
    

if __name__ == '__main__':
    unittest.main()
