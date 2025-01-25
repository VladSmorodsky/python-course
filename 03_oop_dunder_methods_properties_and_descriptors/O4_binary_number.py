import re
import unittest


class BinaryDescriptor:
    """Descriptor for binary number"""

    def __get__(self, instance: 'BinaryNumber', owner) -> 'BinaryNumber':
        """Returns binary number"""
        return instance.__dict__['binary_number']

    def __set__(self, instance: 'BinaryNumber', value: str) -> 'BinaryNumber':
        """Set binary number
        :raise ValueError: If value is empty or consists of not only 1 and 0 characters
        :return BinaryNumber:
        """
        if not value.strip():
            raise ValueError("value can's be empty")
        if not re.match(r'^[0,1]+$', value):
            raise ValueError("value can consists of sequence of 0 and 1")
        instance.__dict__['binary_number'] = value.strip()

        return instance


class BinaryNumber:
    """Class represents binary number"""
    binary_code = BinaryDescriptor()

    def __init__(self, binary_code: str) -> None:
        self.binary_code = binary_code

    def __and__(self, binary_number: 'BinaryNumber') -> 'BinaryNumber':
        """Use operation AND between two BinaryNumber objects.
        If both binary object's has 1 on the same position, it'll return 1, otherwise 0.
        :param binary_number: BinaryNumber object
        :return BinaryNumber:
        """
        new_binary_code = ''

        max_length = max([len(self.binary_code), len(binary_number.binary_code)])
        self.__optimize_binary_number_length(max_length)
        binary_number.__optimize_binary_number_length(max_length)

        for index, character in enumerate(binary_number.binary_code):
            if self.binary_code[index] == '1' and binary_number.binary_code[index] == '1':
                new_binary_code += '1'
                continue
            new_binary_code += '0'

        return BinaryNumber(new_binary_code)

    def __or__(self, binary_number: 'BinaryNumber') -> 'BinaryNumber':
        """Use operation OR between two BinaryNumber objects.
        If both binary object's has 0 on the same position, it'll return 0, otherwise 1.
        :param binary_number: BinaryNumber object
        :return BinaryNumber:
        """
        new_binary_code = ''

        max_length = max([len(self.binary_code), len(binary_number.binary_code)])
        self.__optimize_binary_number_length(max_length)
        binary_number.__optimize_binary_number_length(max_length)

        for index, character in enumerate(binary_number.binary_code):
            if self.binary_code[index] == '0' and binary_number.binary_code[index] == '0':
                new_binary_code += '0'
                continue
            new_binary_code += '1'

        return BinaryNumber(new_binary_code)

    def __xor__(self, binary_number: 'BinaryNumber') -> 'BinaryNumber':
        """Use operation XOR between two BinaryNumber objects.
        If both binary object's has the same value on the same position, it'll return 0, otherwise 1.
        :param binary_number: BinaryNumber object
        :return BinaryNumber:
        """
        new_binary_code = ''

        max_length = max([len(self.binary_code), len(binary_number.binary_code)])
        self.__optimize_binary_number_length(max_length)
        binary_number.__optimize_binary_number_length(max_length)

        for index, character in enumerate(binary_number.binary_code):
            if self.binary_code[index] == binary_number.binary_code[index]:
                new_binary_code += '0'
                continue
            new_binary_code += '1'

        return BinaryNumber(new_binary_code)

    def __invert__(self):
        """Invert BinaryNumber object
        :return BinaryNumber:
        """
        inverted_value = ''
        for index, binary_character in enumerate(self.binary_code):
            if binary_character == '1':
                inverted_value += '0'
            else:
                inverted_value += '1'

        return BinaryNumber(inverted_value)

    def __repr__(self) -> str:
        """Represents binary number"""
        return f"{self.binary_code}"

    def format_binary_number(self) -> None:
        """Format binary code value (remove leading zero's)"""
        self.binary_code = self.binary_code.lstrip('0')
        print(self.binary_code)

    def __optimize_binary_number_length(self, binary_number_length: int) -> None:
        """Add 0 characters on the start of binary number to easily manipulate with other numbers"""
        additional_characters = (binary_number_length - len(self.binary_code)) * '0'
        self.binary_code = additional_characters.join(["", self.binary_code])


# Tests
class TestBinaryNumber(unittest.TestCase):
    def test_setting_binary_number(self):
        """Test BinaryNumber instance is created"""
        expected_value = '1001'
        result = BinaryNumber('1001')

        self.assertEqual(expected_value, result.binary_code)

    def test_setting_binary_number_throws_value_error(self):
        """Check setting binary number validations"""
        test_cases = [
            ('12000', "value can consists of sequence of 0 and 1"),  # wrong sequence of characters provided
            ('     ', "value can's be empty"),  # empty string provided
        ]

        for incorrect_binary_number, error_message in test_cases:
            with self.subTest(incorrect_binary_number=incorrect_binary_number, error_message=error_message):
                with self.assertRaises(ValueError) as error_context:
                    BinaryNumber(incorrect_binary_number)

                self.assertEqual(str(error_context.exception), error_message)

    def test_operation_and_with_binary_number_objects(self):
        """Check binary AND logic"""
        test_cases = [
            (BinaryNumber('10010'), BinaryNumber('0110'), BinaryNumber('00010')),
            (BinaryNumber('1001'), BinaryNumber('0110'), BinaryNumber('0000'))
        ]

        for binary, added_binary, expected_binary in test_cases:
            with self.subTest(binary=binary, added_binary=added_binary, expected_binary=expected_binary):
                result = binary & added_binary
                self.assertEqual(expected_binary.binary_code, result.binary_code)

    def test_operation_or_with_binary_number_objects(self):
        """Check binary OR logic"""
        test_cases = [
            (BinaryNumber('10010'), BinaryNumber('0110'), BinaryNumber('10110')),
            (BinaryNumber('1001'), BinaryNumber('0110'), BinaryNumber('1111'))
        ]

        for binary, added_binary, expected_binary in test_cases:
            with self.subTest(binary=binary, added_binary=added_binary, expected_binary=expected_binary):
                result = binary | added_binary
                self.assertEqual(expected_binary.binary_code, result.binary_code)

    def test_operation_xor_with_binary_number_objects(self):
        """Check binary XOR logic"""
        test_cases = [
            (BinaryNumber('10010'), BinaryNumber('0110'), BinaryNumber('10100')),
            (BinaryNumber('10011'), BinaryNumber('01101'), BinaryNumber('11110'))
        ]

        for binary, added_binary, expected_binary in test_cases:
            with self.subTest(binary=binary, added_binary=added_binary, expected_binary=expected_binary):
                result = binary ^ added_binary
                self.assertEqual(expected_binary.binary_code, result.binary_code)

    def test_invert_operation(self):
        """Check binary XOR logic"""
        test_cases = [
            (BinaryNumber('10010'), BinaryNumber('01101')),
            (BinaryNumber('10011'), BinaryNumber('01100'))
        ]

        for binary, expected_binary in test_cases:
            with self.subTest(binary=binary, expected_binary=expected_binary):
                result = ~binary
                self.assertEqual(expected_binary.binary_code, result.binary_code)

    def test_format_binary_number_method(self):
        """Check format binary code value"""
        binary = BinaryNumber('00110')
        binary.format_binary_number()

        self.assertEqual('110', binary.binary_code)


if __name__ == '__main__':
    unittest.main()
