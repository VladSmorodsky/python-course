import re


def validate_password(password: str) -> None:
    """
    Check if a password is secure:
    - has not less than 8 characters
    - has at least one uppercase letter and at least one lowercase letter
    - has at least one number
    - has at least one special character (@, #, $, %, &)
    :param password:
    :return:
    """
    pattern = r'(?=.*[a-z])(?=.*[A-Z])(?=.*[\d])(?=.*[@#$%&_]).{8,}'  # Use lookahead for all possible symbol groups.
    if re.search(pattern, password) is None:
        raise ValueError('Password is not secure.')


def validate_password_with_error_explanation(password: str) -> None:
    """
    Show a particular error explanation (e.g. Password must be at least 8 characters long)
    :param password:
    :return:
    """
    if len(password) < 8:
        raise ValueError('Password must be at least 8 characters long')
    if re.search(r'[A-Z]', password) is None:
        raise ValueError('Password must contain at least one uppercase letter')
    if re.search(r'[a-z]', password) is None:
        raise ValueError('Password must contain at least one lowercase letter')
    if re.search(r'[0-9]', password) is None:
        raise ValueError('Password must contain at least one number')
    if re.search(r"[@#$%&_]", password) is None:
        raise ValueError('Password must contain at least one special character')


if __name__ == '__main__':
    try:
        validate_password('PASSw#RD2d')
        print('Password is secure.')
    except ValueError as error:
        print(error)
