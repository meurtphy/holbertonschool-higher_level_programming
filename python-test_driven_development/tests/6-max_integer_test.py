#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
import sys
import os

# Ajoutez le chemin parent au sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Importez la fonction max_integer
from six_max_integer import max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_single_element(self):
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 15, 0, -3, 8]), 15)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_mixed_types(self):
        self.assertEqual(max_integer([1, 2.2, 3, 4.4]), 4.4)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c", "d"]), "d")

    def test_mixed_strings_and_numbers(self):
        with self.assertRaises(TypeError):
            max_integer([1, "a", 2, "b"])

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == "__main__":
    unittest.main()
