from typing import TypedDict

from item import Item


class ShopItem(TypedDict):
    """
    Represents item type in the item collection (AttackItemCollection)
    """
    item: Item
    count: int
