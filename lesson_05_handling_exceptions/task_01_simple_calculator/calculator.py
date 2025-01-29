from unknown_operator_error import UnknownOperationError


class Calculator:
    """
    Class makes arithmetic actions between 2 numbers
    """

    @staticmethod
    def calculate(number1: float, number2: float, operation: str) -> float:
        """
        Calculates arithmetic result between two numbers with related operation
        :param number1:
        :param number2:
        :param operation:
        :return float:
        :raise UnknownOperationError
        """
        match operation:
            case '+':
                return number1 + number2
            case '-':
                return number1 - number2
            case '*':
                return number1 * number2
            case '/':
                return number1 / number2
            case default:
                raise UnknownOperationError(f"Unknown operation: {operation}")
