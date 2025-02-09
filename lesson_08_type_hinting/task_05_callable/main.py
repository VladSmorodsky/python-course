from typing import Callable


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


print(apply_operation(5, square))  # 25
print(apply_operation(5, double))  # 10
