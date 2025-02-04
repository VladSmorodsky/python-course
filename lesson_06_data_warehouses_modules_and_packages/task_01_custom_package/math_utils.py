def factorial(number: int) -> int:
    """
    Returns sequence multiplication to number value
    :param number:
    :return int:
    """
    if number <= 1:
        return number
    return number * factorial(number - 1)


def get_greatest_denominator(number1: int, number2: int) -> int:
    """
    Returns the greatest denominator of number1 and number2
    :param number1:
    :param number2:
    :return:
    """

    if number2 % number1 == 0 or number1 % number2 == 0:
        return min(number1, number2)

    number1_list = get_all_number_multipliers(number1)
    number2_list = get_all_number_multipliers(number2)

    total_number = 1

    for value in number1_list:
        matched_element_index = find_list_index(number2_list, value)
        if matched_element_index != -1:
            total_number *= value
            number2_list = number2_list[matched_element_index + 1:]
    return total_number


def get_all_number_multipliers(number: int) -> list:
    """
    Returns dictionary with all number multipliers.
    Example: 12 = 2 * 2 * 3, returning value: [2, 2, 3]
    :param number:
    :return:
    """
    if number == 1:
        return [number]
    num = number
    denominator_list = []
    num_value = 2
    while num > 1:
        if num_value > num / 2:
            denominator_list.append(num)
            break
        if num % num_value == 0:
            denominator_list.append(num_value)
            num //= num_value
            num_value = 2
            continue
        num_value += 1
    return denominator_list


def find_list_index(number_list: list[int], element_value: int) -> int:
    """
    Returns matched element_value index
    :param number_list:
    :param element_value:
    :return:
    """
    try:
        matched_element_index = number_list.index(element_value)
    except ValueError:
        matched_element_index = -1
    return matched_element_index
