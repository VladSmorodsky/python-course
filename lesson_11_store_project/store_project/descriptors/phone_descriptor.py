import re


class PhoneDescriptor:
    """
    A descriptor class that describes a phone number.
    """

    def __get__(self, instance, owner) -> str:
        """
        Returns the phone number value.
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__["phone"]

    def __set__(self, instance, value) -> None:
        """
        Sets the phone number value and validates the value.
        :param instance:
        :param value:
        :return:
        """
        if value is None or value == '':
            raise ValueError("Phone is required.")
        if re.match(r"^(\+?\d{1,3}[-.\s]?(\(?\d{2,3}?\)?[-.\s]?|\d{2,3})?[-.\s]?\d{3,4}[-.\s]?\d{4})$", value) is None:
            raise ValueError("Phone is not valid.")
        instance.__dict__["phone"] = value
