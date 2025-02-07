"""
Doctest usage
"""

import doctest


def is_even(number: int) -> bool:
    """
    Checking if n is even
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    return number % 2 == 0


def factorial(number: int) -> int:
    """
    Returns factorial from n values
    >>> factorial(5)
    120
    >>> factorial(6)
    720
    >>> factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError
    """
    if number < 0:
        raise ValueError
    return number if number == 1 else number * factorial(number - 1)


if __name__ == "__main__":
    doctest.testmod(verbose=True)
