class GameEventException(Exception):
    """
    Custom exception when fighting ends
    """

    def __init__(self, event: str, details=None) -> None:
        super().__init__(f"GameEventException: {event}")
        self.__event = event
        self.__details = details

    def __str__(self) -> str:
        """
        Represent exception message
        :return:
        """
        return f"Event: {self.__event}. Details: {self.__details}"

    def __repr__(self) -> str:
        """
        Represent exception message
        :return:
        """
        return f"Event: {self.__event}. Details: {self.__details}"
