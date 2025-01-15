class RectangleSideException(Exception):
    def __init__(self, message):
        self.__message = message
        super().__init__(self.__message)

    def __str__(self):
        return self.__message


class Rectangle:
    def __init__(self, width, height):
        self.__validate_rectangle_values(width, height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        return 2 * (self.__height + self.__width)

    def is_square(self):
        return self.__width == self.__height

    def resize(self, new_width, new_height):
        self.__validate_rectangle_values(new_width, new_height)
        self.__width = new_width
        self.__height = new_height

    def __validate_rectangle_values(self, width_value, height_value):
        if not isinstance(width_value, (int, float)) or not isinstance(height_value, (int, float)):
            raise RectangleSideException('Incorrect rectangle width or height values.')


rectangle = Rectangle(4, 5)
print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())
print(rectangle.resize(4.5, 4.5))

print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())
