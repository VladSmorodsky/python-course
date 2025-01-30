from typing import Dict

from attack_item import AttackItem
from shop_item import ShopItem


class AttackItemCollection:
    """
    Stores attack items
    """
    __items: Dict[int, ShopItem]

    def __init__(self):
        self.__items = {}

    @property
    def items(self) -> dict[int, ShopItem]:
        """
        Get collection
        :return:
        """
        return self.__items

    def get_item(self, item_id: int) -> ShopItem:
        """
        Returns attack item if exists
        :param item_id:
        :return:
        """
        if self.__items[item_id] is None:
            raise Exception('Item not found.')
        return self.__items[item_id]

    def add_item(self, attack_item: AttackItem) -> None:
        """
        Add item to collection
        :param attack_item:
        :return:
        """
        if attack_item.id in self.__items:
            self.__items[attack_item.id]['count'] += 1
            return
        self.__items[attack_item.id] = {'item': attack_item, 'count': 1}

    def remove_item(self, attack_item: AttackItem, count: int) -> None:
        """
        Remove item from collection
        :param attack_item:
        :param count:
        :return:
        """
        if attack_item.id not in self.__items or self.__items[attack_item.id]['count'] == 0:
            raise Exception('There is no item in the shop. Check it later.')
        self.__items[attack_item.id]['count'] -= count
