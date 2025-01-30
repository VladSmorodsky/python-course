from attack_item import AttackItem
from item import Item
from insufficient_resources_exception import InsufficientResourcesException
from shop import Shop
from resource_descriptor import ResourceDescriptor


class Player:
    """
    Represents game's player
    """
    __money = ResourceDescriptor()
    __weapon: (AttackItem, None)

    def __init__(self, name: str, money: float, health: int = 100) -> None:
        self.__name = name
        self.__attack = 10
        self.__health = health
        self.__money = money
        self.__weapon = None

    @property
    def money(self) -> float:
        """
        Get player's money value
        :return:
        """
        return self.__money

    @money.setter
    def money(self, value: int) -> None:
        """
        :param value:
        :return:
        """
        self.__money = value

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

    @property
    def weapon(self) -> (AttackItem, None):
        """
        Returns player's weapon
        :return AttackItem:
        """
        return self.__weapon

    @weapon.setter
    def weapon(self, new_weapon: AttackItem) -> None:
        """
        Set new weapon for player
        :param new_weapon:
        :return:
        """
        if self.__weapon is not None:
            self.__attack -= self.__weapon.attack_value
        self.__weapon = new_weapon
        self.__attack += new_weapon.attack_value

    def buy(self, shop: Shop, item: Item, count: int = 1) -> None:
        """
        Adding item for player from the shop
        :param count:
        :param shop:
        :param item:
        :return:
        """
        if isinstance(item, AttackItem):
            purchasable_item = shop.attack_items.get_item(item.id)
            price = purchasable_item['item'].cost * count
            if count > purchasable_item['count']:
                raise InsufficientResourcesException(item.name, count, purchasable_item.count)
            if self.__money < price:
                raise InsufficientResourcesException(item.name, price, self.__money,
                                                     'price')
            self.__money -= price
            self.weapon = item
            shop.remove_item(item, count)
        else:
            raise Exception('Item not found')

    def __repr__(self) -> str:
        """Represents player info"""
        return f"{self.__name}:\n ATK: {self.__attack}\n HP: {self.__health}\n Money:{self.__money}"
