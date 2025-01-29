from health_descriptor import HealthDescriptor
from game_event_exception import GameEventException


class Character:
    """
    Class represents game player
    """
    __health = HealthDescriptor()

    def __init__(self, name: str, health: int, attack: int) -> None:
        """
        :param name:
        :param health:
        :param attack:
        """
        self.__name = name
        self.__health = health
        self.__attack = attack

    @property
    def health(self) -> int:
        """
        Returns health value
        :return int:
        """
        return self.__health

    @health.setter
    def health(self, healthValue: int) -> None:
        """
        Set health value
        :param healthValue:
        :return:
        """
        self.__health = healthValue

    @property
    def attack(self) -> int:
        """
        Get character's attack value
        :return int:
        """
        return self.__attack

    @attack.setter
    def attack(self, attackValue: int) -> None:
        """
        Set character's attack value
        :param attackValue:
        :return:
        """
        self.__attack = attackValue

    def hit(self, attackedCharacter: 'Character') -> None:
        """
        Attack character
        :param attackedCharacter:
        :return:
        """
        try:
            attackedCharacter.__health -= self.__attack
        except GameEventException:
            raise GameEventException('death', f"You was killed by {self.__name}")

    def __repr__(self) -> str:
        return f"{self.__name}: ({self.__health})"
