from game_event_exception import GameEventException


class HealthDescriptor:
    """
    Class represents game entity health value management
    """

    def __get__(self, instance, owner) -> int:
        """
        Returns health value
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['_health']

    def __set__(self, instance, healthValue: int) -> None:
        """
        Set health value
        :param instance:
        :param healthValue:
        :return:
        :raise GameEventException
        """
        if healthValue <= 0:
            instance.__dict__['_health'] = 0
            raise GameEventException('death')
        instance.__dict__['_health'] = healthValue
