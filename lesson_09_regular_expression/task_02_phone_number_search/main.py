import re


def search_phone_numbers(text: str) -> list[str]:
    """
    Find all phone numbers list with patterns:
    - (123) 456-7890
    - 123-456-7890
    - 123-456-7890
    - 123.456.7890
    - 1234567890
    :param text:
    :return:
    """
    return re.findall(r'\(?\d{3}\)?[\-.\s]?\d{3}[\-.]?\d{4}', text)


print(search_phone_numbers('Test User: (034) 123-1234, Other User: 1234567890, Peter: 123.456.7890, Joe: 123-456-7890'))
