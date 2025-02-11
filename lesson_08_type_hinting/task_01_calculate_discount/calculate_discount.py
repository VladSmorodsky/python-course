def calculate_discount(price: float, discount: float) -> float:
    """
    Return price with applied discount. If discount nore or equal 100%, returns 0.
    :param price:
    :param discount:
    :return:
    """
    return 0 if discount >= 100 else price - price * discount / 100


print(calculate_discount(100, 20))
