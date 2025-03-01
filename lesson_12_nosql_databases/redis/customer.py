from typing import Optional


class Customer:
    """
    Represents a customer session object.
    """

    def __init__(self, customer_id: int, customer_name: str, session_token: Optional[str] = None) -> None:
        self.__id = customer_id
        self.__name = customer_name
        self.__session_token = session_token

    @property
    def id(self) -> int:
        """
        Returns the id of the customer.
        :return:
        """
        return self.__id

    @property
    def session_token(self) -> Optional[str]:
        """
        Returns the session token of the customer.
        :return:
        """
        return self.__session_token

    @session_token.setter
    def session_token(self, session_token: str) -> None:
        """
        Sets the session token of the customer.
        :param session_token:
        :return:
        """
        self.__session_token = session_token
