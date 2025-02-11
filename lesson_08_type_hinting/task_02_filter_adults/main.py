from typing import Tuple


def filter_adults(people: list[Tuple[str, int]]) -> list[Tuple[str, int]]:
    """
    Returns list of people with age 18+
    :param people:
    :return:
    """
    return [person for person in people if person[1] >= 18]

people = [("Андрій", 25), ("Олег", 16), ("Марія", 19), ("Ірина", 15)]
print(filter_adults(people))