"""
Cover StringProcessor class
"""

import unittest
from unittest import TestCase

from ..src.string_processor import StringProcessor


class StringProcessorTest(TestCase):
    """
    Cover StringProcessor class
    """

    @unittest.skip
    def test_reversed_string_method_with_empty_string(self):
        self.assertEqual('', StringProcessor.reversed_string(''))

    def test_reversed_string_method_with_different_symbol_registry(self):
        self.assertEqual('AbC', StringProcessor.reversed_string('CbA'))

    def test_reversed_string_method_with_numbers_and_alphabet(self):
        self.assertEqual('1ab2c', StringProcessor.reversed_string('c2ba1'))

    def test_capitalize_string_method_with_empty_string(self):
        self.assertEqual(' ', StringProcessor.capitalize_string(' '))

    def test_capitalize_string_method_with_different_symbol_registry(self):
        self.assertEqual('Test', StringProcessor.capitalize_string('TeSt'))

    def test_capitalize_string_method_with_numbers_and_alphabet(self):
        self.assertEqual('Te1st', StringProcessor.capitalize_string('Te1St'))

    def test_count_vowels_method_with_empty_string(self):
        self.assertEqual(0, StringProcessor.count_vowels(' '))

    def test_count_vowels_method_with_different_symbol_registry(self):
        self.assertEqual(3, StringProcessor.count_vowels('A tEst String'))

    def test_count_vowels_method_with_numbers_and_alphabet(self):
        self.assertEqual(3, StringProcessor.count_vowels('A tE1st Stri12ng'))
