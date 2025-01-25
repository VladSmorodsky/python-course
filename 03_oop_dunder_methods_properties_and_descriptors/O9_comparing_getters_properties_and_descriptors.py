"""
Summary:

- Getter/Setter: separate functions, the easiest way to get access to attribute.
But validation should be added on every set action (__init__ and set method individually)
- Property: needs less code to define property.
The same thing about validation, it should be provided individually in setter and __init__ method
- Descriptor: it's great to make reusable functionality, also great idea for validation,
because it observes setting value in the __init__ method and setting directly as well.
But it's possible to have name mangling issues with private attributes
(it's possible to see it in unit tests)

In particular case, the best idea to use descriptor for validating
and using @property to get and set values for private attributes.
"""

import unittest


############### ProductWithGetSet
class ProductWithGetSet:
    """Represents product with getters and setters"""

    def __init__(self, name: str, price: float) -> None:
        self.__validate_product_price(price)  # price should be checked before initializing

        self.name = name
        self.__price = price

    def get_price(self):
        """Return product price
        :return float
        """
        return self.__price

    def set_price(self, price: float) -> None:
        """
        Set product price value.
        :param price:
        :param value: new price value
        :return:
        """
        self.__validate_product_price(price)
        self.__price = price

    def __validate_product_price(self, price: float) -> None:
        """
        Check is product price not less than 0
        :return:
        :raise ValueError:
        """
        if price < 0:
            raise ValueError("Product price can't be less than 0")


################### ProductWithProperty
class ProductWithProperty:
    """Class represents product with property annotation"""

    def __init__(self, name: str, price: float) -> None:
        self.__validate_product_price(price)  # price should be checked before initializing

        self.name = name
        self.__price = price

    @property
    def price(self) -> float:
        """Returns product price"""
        return self.__price

    @price.setter
    def price(self, value: float):
        """
        Set new price value
        :param value:
        :return:
        """
        self.__validate_product_price(value)
        self.__price = value

    def __validate_product_price(self, price: float) -> None:
        """
        Check is product price not less than 0
        :return:
        :raise ValueError:
        """
        if price < 0:
            raise ValueError("Product price can't be less than 0")


################### ProductWithDescriptor
class PriceDescriptor:
    """Represents price descriptor"""

    def __get__(self, instance: 'ProductWithDescriptor', owner) -> float:
        """
        Return ProductWithDescriptor instance price value
        :param instance:
        :param owner:
        :return:
        """
        return instance.__dict__['_price']

    def __set__(self, instance: 'ProductWithDescriptor', value: float) -> None:
        """
        Validate product price and set it to the ProductWithDescriptor instance
        :param instance:
        :param value:
        :return ProductWithDescriptor:
        """
        if value < 0:
            raise ValueError("Product price can't be less than 0")
        instance.__dict__['_price'] = round(value, 2)


class CurrencyDescriptor:
    """Class represents Currency changes and price exchange"""
    EUR_TO_USD = 1.0418
    USD_TO_EUR = 0.96

    def __get__(self, instance: 'ProductWithDescriptor', owner) -> str:
        """Get currency
        :param instance:
        :return str:
        """
        return instance.__dict__.get('currency')

    def __set__(self, instance: 'ProductWithDescriptor', value: str) -> None:
        """Set currency value and make changes in the price due to the currency exchange"""
        self.__is_empty(value)
        self.__is_currency_not_supported(value)

        if 'currency' in instance.__dict__:
            if instance.__dict__['currency'] == value.strip().upper():
                return

            if value.strip().upper() == "USD":
                instance.__dict__['_price'] = round(instance.__dict__['_price'] * self.EUR_TO_USD, 2)
            elif value.strip().upper() == "EUR":
                instance.__dict__['_price'] = round(instance.__dict__['_price'] * self.USD_TO_EUR, 2)
        instance.__dict__['currency'] = value.strip().upper()

    def __is_empty(self, value: str) -> None:
        """Throw ValueError if value is empty
        :param value:
        """
        if value.strip() is None:
            raise ValueError("Currency name can't be empty.")

    def __is_currency_not_supported(self, value: str) -> None:
        """
        Throw ValueError if not supported currency provided
        :param value:
        :return:
        """
        if value.strip().upper() != "EUR" and value.strip().upper() != "USD":
            raise ValueError(f"Currency {value} is not supported")


class ProductWithDescriptor:
    """Represent product with price descriptor"""
    _price = PriceDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name: str, price: float, currency: str) -> None:
        self.name = name
        self._price = price
        self.currency = currency

    def __repr__(self):
        """Product into representation"""
        return f"(price: {self._price}, currency: {self.currency})"


################## Unit tests

class ProductTest(unittest.TestCase):
    """Test different product classes"""

    def test_get_price_value(self):
        """Test get values"""
        product_with_get_and_set = ProductWithGetSet('Cup', 2)
        self.assertEqual(2, product_with_get_and_set.get_price())

        product_with_property = ProductWithProperty('Tea', 22)
        self.assertEqual(22, product_with_property.price)

        # For getting value in the unit tests property should be provided
        product_with_descriptor = ProductWithDescriptor('Coffee', 22, 'EUR')
        self.assertEqual(22, product_with_descriptor._price)

    def test_set_price_value(self):
        """Test set values"""
        product_with_get_and_set = ProductWithGetSet('Cup', 2)
        product_with_get_and_set.set_price(3)
        self.assertEqual(3, product_with_get_and_set.get_price())

        product_with_property = ProductWithProperty('Tea', 22)
        product_with_property.price = 4
        self.assertEqual(4, product_with_property.price)

        # For setting value in the unit tests property should be provided
        product_with_descriptor = ProductWithDescriptor('Coffee', 22, 'EUR')
        product_with_descriptor._price = 23
        self.assertEqual(23, product_with_descriptor._price)

    def test_set_raise_value_error_in_product_with_descriptor(self):
        with self.assertRaises(ValueError):
            product_with_descriptor = ProductWithDescriptor('Coffee', 22, 'EUR')
            product_with_descriptor._price = -11

    def test_set_raise_value_error_in_product_with_property(self):
        with self.assertRaises(ValueError):
            product_with_property = ProductWithProperty('Coffee', 22)
            product_with_property.price = -22

    def test_set_raise_value_error_in_product_with_set_and_get(self):
        with self.assertRaises(ValueError):
            product_with_get_set = ProductWithGetSet('Coffee', 22)
            product_with_get_set.set_price(-22)


################### Programming call

product_with_get_and_set = ProductWithGetSet('Cup', 2)
print('product_with_get_and_set:', product_with_get_and_set.get_price())
try:
    product_with_get_and_set.set_price(-22)
except ValueError as error:
    print('product_with_get_and_set error:', error.__str__())

product_with_property = ProductWithProperty('Tea', 22)
print('product_with_property:', product_with_property.price)
try:
    product_with_property.price = -22
except ValueError as error:
    print('product_with_property error:', error.__str__())

product_with_descriptor = ProductWithDescriptor('Coffee', 22, 'EUR')
print('product_with_descriptor:', product_with_descriptor._price)
try:
    product_with_descriptor._price = -22
except ValueError as error:
    print('product_with_descriptor error:', error.__str__())

print('---- Currency Exchange ----')

print(product_with_descriptor)
product_with_descriptor.currency = 'USD'
print(product_with_descriptor)
product_with_descriptor.currency = 'EUR'
print(product_with_descriptor)
