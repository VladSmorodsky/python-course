from processor import Processor


def double(item: int) -> int:
    """
    Returns double item
    :param item:
    :return:
    """
    return item * 2


def to_upper(item: str) -> str:
    """
    Returns upper string
    :param item:
    :return:
    """
    return item.upper()


p1 = Processor([1, 2, 3])
print(p1.apply(double))  # [2, 4, 6]

p2 = Processor(["hello", "world"])
print(p2.apply(to_upper))  # ["HELLO", "WORLD"]
