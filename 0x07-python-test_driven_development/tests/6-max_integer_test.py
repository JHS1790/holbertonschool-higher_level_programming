#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class for unittesting max_integer
    """

    def test_int_list(self):
        """
        tests max_integer against a list of ints
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_float_list(self):
        """
        tests max_integer against a list of floats
        """
        self.assertEqual(max_integer([1.0, 2.3, 3.4, 4.5]), 4.5)

if __name__ == '__main__':
    unittest.main()
