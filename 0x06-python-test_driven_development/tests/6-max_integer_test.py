#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):


    def test_variable(self):
        a = 77
        self.assertEqual(max_integer([a]), a)


    def test_multiple_variables(self):
        a = 99
        self.assertEqual(max_integer([a, a, a]), a)


    def test_regular_ints(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)


    def test_unsorted_ints(self):
        self.assertEqual(max_integer([2, 1, 4, 3]), 4)


    def test_large_int(self):
        self.assertEqual(max_integer([999999999999999]), 999999999999999)


    def test_large_small(self):
        self.assertEqual(max_integer([1, 999999999999999]), 999999999999999)


if __name__ == '__main__':
    unittest.main()
