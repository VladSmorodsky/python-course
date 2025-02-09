from typing import TypeVar, List, Callable

T = TypeVar('T')


class Processor:
    """
    Represent actions between generic items
    """

    def __init__(self, items: List[T]) -> None:
        self.__items = items

    def apply(self, fn: Callable[[T], T]) -> List[T]:
        """
        Apply callable fn to list items
        :param fn:
        :return:
        """
        return [fn(item) for item in self.__items]
