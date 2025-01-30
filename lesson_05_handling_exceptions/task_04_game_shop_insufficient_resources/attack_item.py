from item import Item


class AttackItem(Item):
    """Represents attack items"""

    def __init__(self, item_id: int, name: str, price: float, attack_value: float) -> None:
        super().__init__(item_id, name, price)
        self.__attack_value = attack_value

    @property
    def attack_value(self) -> float:
        """
        Return attack value
        :return:
        """
        return self.__attack_value

    @attack_value.setter
    def attack_value(self, attack_value: float) -> None:
        """Set attack value"""
        self.__attack_value = attack_value

    def __repr__(self) -> str:
        """
        Represents attack item info
        :return:
        """
        return f"{self.name}: ATK {self.__attack_value}"
