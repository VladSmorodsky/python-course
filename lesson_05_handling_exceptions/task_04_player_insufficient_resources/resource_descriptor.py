from insufficient_resources_exception import InsufficientResourcesException


class ResourceDescriptor:
    """
    Responsible for setting and getting resource amount
    """

    def __get__(self, instance, owner) -> float:
        """
        Get resource amount
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['resource_amount']

    def __set__(self, instance, value: float) -> None:
        """
        Set resource amount
        :param instance:
        :param value:
        :return:
        """
        if value < 0:
            raise InsufficientResourcesException
        instance.__dict__['resource_amount'] = value
