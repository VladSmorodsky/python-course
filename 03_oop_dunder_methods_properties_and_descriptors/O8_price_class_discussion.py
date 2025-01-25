class PriceDescriptor:
    """Class represents Price value descriptor"""

    def __get__(self, instance: 'Price', owner) -> 'Price':
        """Get Price object
        :return Price:
        """
        return instance.__dict__['value']

    def __set__(self, instance: 'Price', value: float) -> 'Price':
        """
        Set value to Price object and round it up to 2 simbols after dot.
        :param instance:
        :param value:
        :return Price:
        """
        instance.__dict__['value'] = round(value, 2)
        return instance


class Price:
    """Class represents price object"""
    __value = PriceDescriptor()

    def __init__(self, value: float) -> None:
        self.__value = value

    def __add__(self, price: 'Price') -> 'Price':
        """Add price and return new Price object
        :param price:
        :return Price
        """
        return Price(self.__value + price.__value)

    def __sub__(self, price: 'Price') -> 'Price':
        """Subtract price and return new Price object
        :param price:
        :return Price:
        """
        return Price(self.__value - price.__value)

    def __lt__(self, compared_price: 'Price') -> bool:
        """Check if current price less than compared price
        :param compared_price:
        :return bool:
        """
        return self.__value < compared_price.__value

    def __gt__(self, compared_price: 'Price') -> bool:
        """Check if current price greater than compared price
        :param compared_price:
        :return bool:
        """
        return self.__value > compared_price.__value

    def __eq__(self, compared_price: 'Price') -> bool:
        """Check if both price values are equal
        :param compared_price:
        :return bool:
        """
        return self.__value == compared_price.__value

    def __repr__(self) -> str:
        """Return Price value"""
        return f"{self.__value}"


######## The idea of how to use Price class

class PaymentGateway:
    """Class represents payment gateway object"""
    __price = Price(0)

    @classmethod
    def set_price(cls, price: Price) -> None:
        """Set new price
        :param price: New price
        """
        cls.__price = price

    @classmethod
    def get_price(cls) -> Price:
        """Return Price object"""
        return cls.__price

    def __repr__(self):
        """Return payment gateway info"""
        return f"{self.__price}"


class Paypal(PaymentGateway):
    pass


price1 = Price(5.6333)
print(price1)

price2 = Price(2.367)

price3 = price1 + price2
print(price3)

price4 = price3 - price2
print(price4)

print(price1 > price2)
print(price1 < price2)
print(price1 == price2)

#####################

items_price = Price(50.99)
shipping_price = Price(3.99)

PaymentGateway.set_price(items_price + shipping_price)
print('Base PaymentGateway price:', PaymentGateway.get_price())  # 54.98

payment_method = Paypal()
print('Paypal method price: ', payment_method)  # 54.98
