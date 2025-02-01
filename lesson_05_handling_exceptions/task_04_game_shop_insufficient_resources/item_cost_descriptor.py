from price_error import PriceError


class ItemCostDescriptor:
    """
    Descriptor for setting and getting item price
    """

    def __get__(self, instance, owner) -> float:
        """
        Returns item price
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['item_price']

    def __set__(self, instance, value: float) -> None:
        """
        Set item price
        :param instance:
        :param value:
        :return:
        """
        if value < 0:
            raise PriceError("Item's cost can't be less than 0")
        instance.__dict__['item_price'] = value
