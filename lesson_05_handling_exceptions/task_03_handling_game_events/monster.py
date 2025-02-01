from character import Character


class Monster(Character):
    """
    Represents game's monster
    """

    def __init__(self, name: str, health: int, attack: int, experience: int) -> None:
        super().__init__(name, health, attack)
        self.__experience = experience

    @property
    def experience(self) -> int:
        """
        Returns monster's experience
        :return:
        """
        return self.__experience

    @property
    def name(self) -> str:
        """
        Returns monster's name
        :return:
        """
        return self.__name
