class RectangleSideException(Exception):
    """
    Custom rectangle side assigning exception class
    """

    def __init__(self, message):
        self.__message = message
        super().__init__(self.__message)

    def __str__(self) -> str:
        return self.__message


class Rectangle:
    """
    Class represents rectangle object with possible operations with it

    Attributes:
        __width (float): Rectangle width
        __height (float): Rectangle height
    """
    __width = 0
    __height = 0

    def __init__(self, width: float, height: float):
        self.__validate_rectangle_values(width, height)
        self.__width = width
        self.__height = height

    def area(self) -> float:
        """
        Method calculates a rectangle area

        Returns:
            float: rectangle area value
        """
        return self.__width * self.__height

    def perimeter(self) -> float:
        """
        Method calculates a rectangle perimeter

        Returns:
            float: rectangle perimeter value
        """
        return 2 * (self.__height + self.__width)

    def is_square(self) -> bool:
        """
        Method checks if rectangle has the same width and height

        Returns:
            bool: if rectangle has the same width and height (true) or not (false)
        """
        return self.__width == self.__height

    def resize(self, new_width: float, new_height: float) -> None:
        """
        Method changes rectangle's width and height

        Parameters:
            new_width (float): New rectangle width
            new_height (float): New rectangle height
        """
        self.__validate_rectangle_values(new_width, new_height)
        self.__width = new_width
        self.__height = new_height

    def __validate_rectangle_values(self, width_value, height_value):
        """
        Method validates rectangle's width and height

        Parameters:
            width_value (float):
                New rectangle width
            height_value (float):
                New rectangle height

        Raises:
            RectangleSideException: If width or height has incorrect value
        """
        if (isinstance(width_value, (int, float)) is not True
                or isinstance(height_value, (int, float)) is not True):
            raise RectangleSideException('Incorrect rectangle width or height values.')


rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())
print(rectangle.resize(4.5, 4.5))

print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())
