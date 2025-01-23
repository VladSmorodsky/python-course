import re


class User:
    """Class represents user with first name, last name and email"""

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        self.__validate_not_empty_value(first_name)
        self.__validate_not_empty_value(last_name)
        self.__validate_not_empty_value(email)
        self.__validate_email(email)

        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @property
    def first_name(self) -> str:
        """Return __first_name"""
        return self.__first_name

    @first_name.setter
    def first_name(self, value: str) -> None:
        """Set first name if it's not empty"""
        self.__validate_not_empty_value(value)

        self.__first_name = value.strip()

    @property
    def last_name(self) -> str:
        """Return __last_name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, value: str) -> None:
        """Set last name if it's not empty"""
        self.__validate_not_empty_value(value)

        self.__last_name = value.strip()

    @property
    def email(self) -> str:
        """Return __email"""
        return self.__email

    @email.setter
    def email(self, value: str) -> None:
        """Set email if it's not empty
        :param value
        """
        self.__validate_not_empty_value(value)
        self.__validate_email(value)

        self.__email = value.strip()

    def __repr__(self):
        """Return user representation"""
        return f"{self.first_name} {self.last_name}: {self.email}"

    def __validate_not_empty_value(self, value):
        if not value.strip():
            raise ValueError("Value can't be empty")

    def __validate_email(self, email_value: str) -> None:
        """Validate email address
        :param email_value
        """
        if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email_value):
            raise ValueError("Incorrect email format.")


user = User('Test', 'User', 'test@example.com')
print(user)

user.first_name = 'Tom'
print(user)

user2 = User('T', 'T', 'T@ee.tt')
print(user2)
