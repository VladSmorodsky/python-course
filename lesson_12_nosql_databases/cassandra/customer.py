import uuid


class Customer:
    """
    Represents a customer session object.
    """

    def __init__(self, customer_id: uuid.UUID, customer_name: str) -> None:
        self.__id = customer_id
        self.__name = customer_name

    @property
    def id(self) -> uuid.UUID:
        """
        Returns the id of the customer.
        :return:
        """
        return self.__id
