class Item:
    """
    Represents game's item
    """

    def __init__(self, item_id: int, name: str, cost: float) -> None:
        self.__id = item_id
        self.__name = name
        self.__cost = cost

    @property
    def id(self) -> int:
        """
        Get item id
        :return int:
        """
        return self.__id

    @id.setter
    def id(self, value: int) -> None:
        """
        Set item id
        :param value:
        :return:
        """
        self.__id = value

    @property
    def name(self) -> str:
        """
        Get item name
        :return str:
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Get item cost
        :param value:
        :return:
        """
        self.__name = value

    @property
    def cost(self) -> float:
        """
        Get item cost
        :return str:
        """
        return self.__cost

    @cost.setter
    def cost(self, value: float) -> None:
        """
        Set item cost
        :param value:
        :return:
        """
        self.__cost = value
