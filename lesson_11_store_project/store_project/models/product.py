from store_project.descriptors.name_descriptor import NameDescriptor

from store_project.descriptors.positive_number_descriptor import PositiveNumberDescriptor


class Product:
    """
    Represents a product in the store.
    """
    __name = NameDescriptor()
    __price = PositiveNumberDescriptor()
    __stock = PositiveNumberDescriptor()

    def __init__(self, name: str, price: float, stock: float) -> None:
        self.__name = name
        self.__price = price
        self.__stock = stock

    @property
    def name(self) -> str:
        """
        The name of the product.
        :return:
        """
        return self.__name

    @property
    def price(self) -> float:
        """
        The price of the product.
        :return:
        """
        return self.__price

    @property
    def stock(self) -> float:
        """
        The stock of the product.
        :return:
        """
        return self.__stock

    def __repr__(self) -> str:
        """
        The string representation of the product.
        :return:
        """
        return f"- Product: {self.__name}, Price: {self.__price}, Stock: {self.__stock}"
