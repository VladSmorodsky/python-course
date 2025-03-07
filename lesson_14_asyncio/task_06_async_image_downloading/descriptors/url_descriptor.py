import re


class UrlDescriptor:
    """
    Validates, gets and sets url value
    """

    def __get__(self, instance, owner) -> str:
        return instance.__dict__['url']

    def __set__(self, instance, value: str) -> None:
        """
        Validates and sets url value
        :param instance:
        :param value:
        :return:
        """
        if value is None or value == '':
            raise ValueError('Url value cannot be empty')
        if re.match(r"(?:https?://|www\.)[\w.\-_]+[\w/?=]+", value) is None:
            raise ValueError(f'Invalid url value: {value}')
        instance.__dict__['url'] = value
