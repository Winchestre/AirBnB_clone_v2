#!/usr/bin/python3
"""Module doc"""
import unittest
import console


class test_Console(unittest.TestCase):
    """Test doc"""

    def test_doc(self):
        """Test function"""
        self.assertIsNotNone(console.__doc__)
