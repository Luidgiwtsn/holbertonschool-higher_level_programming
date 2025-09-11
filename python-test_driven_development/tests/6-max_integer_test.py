#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        """Test a list in ascending order"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test a list in random order"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test when the max is at the beginning"""
        self.assertEqual(max_integer([9, 1, 2, 3]), 9)

    def test_max_at_middle(self):
        """Test when the max is in the middle"""
        self.assertEqual(max_integer([1, 3, 9, 2, 5]), 9)

    def test_max_at_end(self):
        """Test when the max is at the end"""
        self.assertEqual(max_integer([1, 3, 4, 10]), 10)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative_numbers(self):
        """Test a list with all negative numbers"""
        self.assertEqual(max_integer([-1, -22, -3, -4]), -1)

    def test_mixed_positive_negative(self):
        """Test a list with both positive and negative numbers"""
        self.assertEqual(max_integer([-10, 5, -2, 0]), 5)

    def test_same_elements(self):
        """Test a list with all same elements"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.1, 2.5, 3.7, 3.6]), 3.7)

    def test_mixed_ints_and_floats(self):
        """Test a list with ints and floats"""
        self.assertEqual(max_integer([1, 2.2, 3, 4.5]), 4.5)

    def test_string_input(self):
        """Test a string as input"""
        self.assertEqual(max_integer("abcde"), 'e')

    def test_list_of_strings(self):
        """Test a list of strings"""
        self.assertEqual(max_integer(["abc", "xyz", "123"]), "xyz")

    def test_list_with_none(self):
        """Test a list with None in it (should raise error)"""
        with self.assertRaises(TypeError):
            max_integer([1, None, 2])

    def test_list_with_mixed_types(self):
        """Test a list with mixed types (should raise error)"""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3])
