from datetime import datetime


class CustomerSession:
    """
    Represents a customer session object.
    """

    def __init__(self, user_id: int, session_token: str, login_time: datetime) -> None:
        self.__user_id = user_id
        self.__session_token = session_token
        self.__login_time = login_time

    @property
    def user_id(self) -> int:
        """
        Returns the user_id of the customer session.
        :return:
        """
        return self.__user_id

    @property
    def session_token(self) -> str:
        """
        Returns the session token for this customer session.
        :return:
        """
        return self.__session_token

    @property
    def login_time(self) -> datetime:
        """
        Returns the login time for this customer session.
        :return:
        """
        return self.__login_time

    def __repr__(self) -> str:
        """
        Returns a string representation of this customer session.
        :return:
        """
        return f"Customer session: {self.__login_time}"
