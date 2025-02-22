class PositiveNumberDescriptor:
    """
    Responsible for checking and setting only positive numbers.
    """

    def __get__(self, instance, owner) -> float:
        """
        Returns name value
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['number']

    def __set__(self, instance, value: float) -> None:
        """
        Validating the value and setting it
        :param instance:
        :param value:
        :return:
        """
        if value is None:
            raise ValueError("Value cannot be empty")
        if value < 0:
            raise ValueError("Value cannot be negative")
        instance.__dict__['number'] = value
