from typing import Generator

from counter_limit_context_manager import CounterLimitContextManager


def number_generator() -> Generator[int]:
    """
    Infinite generator
    :return:
    """
    number = 0
    while True:
        yield number
        number += 1


counter = number_generator()
while True:
    try:
        with CounterLimitContextManager(next(counter)) as n:
            print(n)
    except ValueError:
        print(f"Value has limit in context manager")
        break
