import re


def format_date(date: str) -> str:
    """
    Format date from template DD/MM/YYYY to YYYY-MM-DD
    :param date:
    :return:
    """
    validate_date_value(date)
    parsed_date = re.split(r'\D', date)

    return f"{parsed_date[2]}-{parsed_date[1]}-{parsed_date[0]}"


def validate_date_value(date: str) -> None:
    """
    Validate date value. Use this pattern: DD/MM/YYYY
    :param date:
    :return:
    """
    if re.match(r'^\d{2}/\d{2}/\d{4}$', date) is None:
        raise ValueError('Invalid date format')
    parsed_date = re.split(r'\D', date)
    day = int(parsed_date[0])
    month = int(parsed_date[1])
    year = int(parsed_date[2])
    month_list_with_31_days = [1, 3, 5, 7, 8, 10, 12]
    month_list_with_30_days = [4, 6, 9, 11]
    if month > 12:
        raise ValueError('There are 12 month in year.')
    if month in month_list_with_31_days:
        if day > 31:
            raise ValueError(f"Day value can't be more than 31 days for month {month}")
        return
    if month in month_list_with_30_days:
        if day > 30:
            raise ValueError(f"Day value can't be more than 30 days for month {month}")
        return
    if month == 2:  # Check February day value
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            if day > 29:
                raise ValueError(f"Day value can't be more than 29 days for month {month}")
        elif day > 28:
            raise ValueError(f"Day value can't be more than 28 days for month {month}")


if __name__ == '__main__':
    print(format_date('29/02/2020'))
