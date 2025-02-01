from character import Character
from game_event_exception import GameEventException
from monster import Monster


class Player(Character):
    """
    Represents game's monster
    """

    def __init__(self, name: str, health: int, attack: int) -> None:
        super().__init__(name, health, attack)
        self.__experience = 0
        self.__level = 1

    @property
    def experience(self) -> int:
        """
        Monster's experience
        :return:
        """
        return self.__experience

    @experience.setter
    def experience(self, value: int) -> None:
        """
        :param value:
        :return:
        """
        self.__experience += value

    def hit(self, attackedMonster: 'Monster') -> None:
        """
        Overridden method for play to set win message
        :param attackedMonster:
        :return:
        """
        try:
            super().hit(attackedMonster)
        except GameEventException:
            self.__experience += attackedMonster.experience
            self.__level += 1
            raise GameEventException('levelUp',
                                     f"New level: {self.__level}. Given experience: {attackedMonster.experience}")
