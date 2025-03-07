class NameDescriptor:
    """
    Validates, gets and sets name value
    """

    def __get__(self, instance, owner) -> str:
        return instance.__dict__['name']

    def __set__(self, instance, value: str) -> None:
        """
        Validates and sets url value
        :param instance:
        :param value:
        :return:
        """
        if value is None or value == '':
            raise ValueError('Url value cannot be empty')
        instance.__dict__['name'] = value
