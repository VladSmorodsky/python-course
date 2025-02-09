from typing import List, TypeVar, Union

T = TypeVar('T')


def get_first(items: List[T]) -> Union[T, None]:
    """
    Returns the first item from the list
    :param items:
    :return:
    """
    return items[0] if len(items) > 0 else None


print(get_first([1, 2, 3]))  # 1
print(get_first(["a", "b", "c"]))  # "a"
print(get_first([]))  # None
