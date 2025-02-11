from typing import Union


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


print(parse_input(42))  # 42
print(parse_input("100"))  # 100
print(parse_input("hello"))  # None
