"""
File contains all implemented tasks for checking with mypy util
"""

from typing import Callable, Tuple, Union, TypeVar, List


# Task 1
def calculate_discount(price: float, discount: float) -> float:
    """
    Return price with applied discount. If discount nore or equal 100%, returns 0.
    :param price:
    :param discount:
    :return:
    """
    return 0 if discount >= 100 else price - price * discount / 100


# Task 2
def filter_adults(people: list[Tuple[str, int]]) -> list[Tuple[str, int]]:
    """
    Returns list of people with age 18+
    :param people:
    :return:
    """
    return [person for person in people if person[1] >= 18]


# Task 3
def parse_input(value: Union[int, str]) -> Union[int, None]:
    """
    Return number if value or converted is number, else return None
    :param value:
    :return:
    """
    try:
        return int(value)
    except ValueError:
        return None


# Task 4
T = TypeVar('T')


def get_first(items: List[T]) -> Union[T, None]:
    """
    Returns the first item from the list
    :param items:
    :return:
    """
    return items[0] if len(items) > 0 else None


# Task 5
def apply_operation(number: int, fn: Callable[[int], int]) -> int:
    """
    Apply fn with number parameter
    :param number:
    :param fn:
    :return:
    """
    return fn(number)


def square(number: int) -> int:
    """
    Returns square of number
    :param number:
    :return:
    """
    return number ** 2


def double(number: int) -> int:
    """
    Returns double number value
    :param number:
    :return:
    """
    return number * 2
