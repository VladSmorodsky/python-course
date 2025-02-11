import re


def validate_email(email: str) -> None:
    """
    Validate if email is valid.
    :param email:
    :return:
    """
    if re.match(r"^(\w[\w.]+\w)@(\w+)(\.[\w]{2,6})$", email) is None:
        raise ValueError(f"Email not valid: {email}")


try:
    validate_email('test@example.com')  # Valid email (returns None)
    # validate_email('test.@example.com')  # Raises ValueError
except ValueError as e:
    print(e)
