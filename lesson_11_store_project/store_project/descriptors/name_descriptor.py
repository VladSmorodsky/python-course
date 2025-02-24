class NameDescriptor:
    """
    Responsible for checking and setting names values
    """

    def __get__(self, instance, owner) -> str:
        """
        Returns name value
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['name']

    def __set__(self, instance, value: str) -> None:
        """
        Validating the value and setting it
        :param instance:
        :param value:
        :return:
        """
        if value is None or value == '':
            raise ValueError("Value cannot be empty")
        instance.__dict__['name'] = value
