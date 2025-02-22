from typing import List

from store_project.models.order_item import OrderItem


class Order:
    """
    Represents an order
    """

    def __init__(self, order_id: int, customer_id: int, order_date: int,
                 order_items: List[OrderItem] | None = None) -> None:
        self.__order_id = order_id
        self.__customer_id = customer_id
        self.__order_date = order_date
        self.__order_items = order_items

    @property
    def order_id(self) -> int:
        """
        Get order id
        :param self:
        :return:
        """
        return self.__order_id

    @property
    def order_items(self) -> List[OrderItem]:
        """
        Get products from order
        :param self:
        :return:
        """
        return self.__order_items

    def __repr__(self) -> str:
        """
        :param self:
        :return:
        """
        return f"Order id: {self.__order_id}"
