import random
from typing import Optional


class Organism:
    """
    Represents an evolution organism.
    """
    __health_value_for_reproduction = 10

    def __init__(self, health: int = 5) -> None:
        self.health = health

    def feed(self) -> None:
        """
        Feed the organism.
        :return:
        """
        food = random.randint(1, 5)
        self.health += food
        print(f"Health: {self.health}")

    def reproduce(self) -> Optional['Organism']:
        """
        Reproduce the organism related to health value.
        :return:
        """
        if self.health >= self.__health_value_for_reproduction:
            self.health -= 10
            print(f"New organism reproduced! Parent health value: {self.health}")
            return Organism()
