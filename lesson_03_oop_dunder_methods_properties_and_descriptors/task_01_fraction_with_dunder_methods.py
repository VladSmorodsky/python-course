class DenominatorDescriptor:
    """Descriptor for denominator value"""

    def __get__(self, instance: 'Fraction', owner: object) -> int:
        """Returns denominator value of Fraction instance"""
        return instance.__dict__['denominator']

    def __set__(self, instance: 'Fraction', value: int) -> 'Fraction':
        """Set denominator value
        :raise ValueError: Denominator can't be equal 0
        """
        if value == 0:
            raise ValueError("Denominator can't be 0")
        instance.__dict__['denominator'] = value

        return instance


class Fraction:
    """Class represents fraction value (numerator/denominator) and main operations on Fraction objects"""
    denominator = DenominatorDescriptor()

    def __init__(self, numerator: int, denominator: int) -> None:
        self.numerator = numerator
        self.denominator = denominator

    def __add__(self, fraction_object: 'Fraction') -> 'Fraction':
        """Returns sum of Fraction objects
        :param fraction_object: Fraction object that should be added.
        :return Fraction: New Fraction object that contains sum of 2 objects
        """
        new_denominator = self.denominator * fraction_object.denominator
        new_numerator = (self.numerator * fraction_object.denominator) + (fraction_object.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, fraction_object: 'Fraction') -> 'Fraction':
        """Returns subtraction of Fraction objects
        :param fraction_object: Fraction object that should be subtracted.
        :return Fraction: New Fraction object that contains subtraction of 2 objects.
        """
        new_denominator = self.denominator * fraction_object.denominator
        new_numerator = (self.numerator * fraction_object.denominator) - (fraction_object.numerator * self.denominator)
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, fraction_object: 'Fraction') -> 'Fraction':
        """Returns multiplication of Fraction objects
        :param fraction_object: Fraction object that should be multiplicated.
        :return Fraction: New Fraction object that contains multiplication of 2 objects.
        """
        return Fraction(self.numerator * fraction_object.numerator, self.denominator * fraction_object.denominator)

    def __truediv__(self, fraction_object: 'Fraction') -> 'Fraction':
        """Returns division of Fraction objects
        :param fraction_object: Fraction object that should be divided.
        :return Fraction: New Fraction object that contains division of 2 objects (the same as multiply reverted fraction_object).
        """
        return Fraction(self.numerator * fraction_object.denominator, self.denominator * fraction_object.numerator)

    def __repr__(self) -> str:
        """Returns Fraction representation"""
        return f"{self.numerator}/{self.denominator}"


fractionObject1 = Fraction(1, 4)
fractionObject2 = Fraction(1, 2)

fractionObject3 = fractionObject1 + fractionObject2
print(fractionObject3)

fractionObject4 = fractionObject3 - fractionObject2
print(fractionObject4)

fractionObject5 = fractionObject1 * fractionObject2
print(fractionObject5)

fractionObject6 = fractionObject1 / fractionObject2
print(fractionObject6)

# fractionObject7 = Fraction(1, 0) # ValueError: Denominator can't be 0
