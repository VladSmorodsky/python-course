"""
Module is responsible for string processing
"""
import re


class StringProcessor:
    """
    Responsible for working with strings operations.
    """

    @staticmethod
    def reversed_string(text: str) -> str:
        """
        Revert text string
        :param text:
        :return:
        """
        return text[::-1]

    @staticmethod
    def capitalize_string(s: str) -> str:
        """
        Capitalize string
        :param s:
        :return:
        """
        return s.capitalize()

    @staticmethod
    def count_vowels(s: str) -> int:
        """
        Return vowels count in the s string
        :param s: 
        :return: 
        """
        return len(re.findall('[aeyuio]', s.lower()))
