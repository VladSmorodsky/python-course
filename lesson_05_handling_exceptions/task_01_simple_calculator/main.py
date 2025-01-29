from calculator import Calculator
from unknown_operator_error import UnknownOperationError

try:
    first_number = float(input('Enter first number:'))
    operator = input('Enter operation (+, -, *, /):')
    second_number = float(input('Enter second number:'))

    print('Result:', Calculator.calculate(first_number, second_number, operator))
except ZeroDivisionError as error:
    print('Error:', error)
except ValueError as error:
    print('Error:', error)
except UnknownOperationError as error:
    print('Error:', error)
