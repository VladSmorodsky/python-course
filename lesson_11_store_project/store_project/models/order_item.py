from store_project.descriptors.positive_number_descriptor import PositiveNumberDescriptor


class OrderItem:
    """
    Represents an order details
    """
    __quantity = PositiveNumberDescriptor

    def __init__(self, product_id: int, quantity: float, order_id: int | None = None, ) -> None:
        self.__order_id = order_id
        self.__product_id = product_id
        self.__quantity = quantity

    @property
    def product_id(self) -> int:
        """
        Returns the product id of the order
        :return:
        """
        return self.__product_id

    @property
    def quantity(self) -> float:
        """
        Get the quantity of the order item
        :return:
        """
        return self.__quantity
