from attack_item import AttackItem
from item import Item
from attack_item_collection import AttackItemCollection
from insufficient_resources_exception import InsufficientResourcesException


class Shop:
    """
    Represents shop with items
    """
    __attack_items: (AttackItemCollection, [])

    def __init__(self):
        self.__attack_items = AttackItemCollection()

    def add_to_shop(self, item: Item) -> None:
        """
        Add item into shop's collection
        :param item:
        :return:
        """
        if isinstance(item, AttackItem):
            self.__attack_items.add_item(item)
        else:
            raise Exception('Insufficient item.')

    @property
    def attack_items(self) -> (AttackItemCollection, []):
        """
        Returns attack items
        :return:
        """
        return self.__attack_items

    def remove_item(self, item: Item, count: int) -> None:
        """
        Remove item from the shop
        :param count:
        :param item:
        :return:
        """
        if isinstance(item, AttackItem):
            selected_item_count = self.attack_items.get_item(item.id)['count']
            if count > selected_item_count:
                raise InsufficientResourcesException(item.name, count, selected_item_count)
            self.attack_items.remove_item(item, count)
        raise Exception('Insufficient item')
