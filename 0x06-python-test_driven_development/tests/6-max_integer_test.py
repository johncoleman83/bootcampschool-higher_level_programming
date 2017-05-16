#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

def real_max_integer(list=[]):
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


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        a = 77
        testslist = [
            [1, 2, 3, 4],
            [1, 3, 4, 2],
            None,
            55,
            "stringtest",
            ["hi", 6, a],
            [a, a, a],
            [1, 2, 3, [4, 5, 6], [4, 5, 6]]
            ]
        for i in testslist:
            self.assertEqual(max_integer(i), real_max_integer(i))

if __name__ == '__main__':
    unittest.main()
