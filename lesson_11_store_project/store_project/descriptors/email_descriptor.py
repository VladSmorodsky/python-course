import re


class EmailDescriptor:
    """
    Represent an email address and validation
    """

    def __get__(self, instance, owner) -> str:
        """
        Return the email address
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__["email"]

    def __set__(self, instance, value: str) -> None:
        """
        Set the email address and validation
        :param instance:
        :param value:
        :return:
        """
        if value is None or value == '':
            raise ValueError("Email address is required.")
        if re.match(r"^(\w[\w.+\-_]+\w)@(\w+)(\.[\w]{2,6})$", value) is None:
            raise ValueError("Email address is not valid.")
        instance.__dict__["email"] = value
