import re

from arithmetic_mean_file_context_manager import ArithmeticMeanFileContextManager
from empty_file_error import EmptyFileError


def validate_allowed_symbols(file_line: str) -> None:
    """
    Validate that file's line has only allowed symbols
    :param file_line:
    :return:
    :raise ValueError
    """
    if re.search(r'[^\d\s]', file_line):
        raise ValueError


try:
    number_list = []
    with ArithmeticMeanFileContextManager('number.txt') as file:
        for line in file.readlines():
            current_line = line.strip()
            validate_allowed_symbols(current_line)
            numbers_in_line = map(int, re.findall(r'\b\d+\b', current_line))
            number_list += numbers_in_line

    if len(number_list) == 0:
        raise EmptyFileError('File is empty')

    print(sum(number_list) / len(number_list))
except (FileNotFoundError, ValueError, EmptyFileError) as e:
    print(e)
