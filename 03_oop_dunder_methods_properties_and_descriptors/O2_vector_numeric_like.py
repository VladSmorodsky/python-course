import math


class Vector:
    """Class represents vector object
    Attributes:
        - x0 -> int: vector's start horizontal value
        - y0 -> int: vector's start vertical value
        - x1 -> int: vector's end horizontal value
        - y1 -> int: vector's end vertical value
    """

    def __init__(self, x0: int, y0: int, x1: int, y1: int) -> None:
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def __add__(self, vector: 'Vector') -> 'Vector':
        """Sum two vectors
        :param vector: Vector that should be added to vector
        :return Vector: Returns new Vector
        """
        return Vector(self.x0 + vector.x0, self.y0 + vector.y0, self.x1 + vector.x1, self.y1 + vector.y1)

    def __sub__(self, vector: 'Vector') -> 'Vector':
        """Subtract two vectors
        :param vector: Vector that should be subtracted from vector
        :return Vector: Returns new Vector
        """
        return Vector(self.x0 - vector.x0, self.y0 - vector.y0, self.x1 - vector.x1, self.y1 - vector.y1)

    def __mul__(self, number: int) -> 'Vector':
        """Multiply vector to number
        :param number: Number that vector should be multiplied by it
        :return Vector: Returns new Vector
        """
        return Vector(self.x0 * number, self.y0 * number, self.x1 * number, self.y1 * number)

    def __lt__(self, vector: 'Vector') -> bool:
        """Checks if current object length less than compared vector length
        :param vector: Compared vector
        :return bool:
        """
        return self.get_vector_length() < vector.get_vector_length()

    def __eq__(self, vector: 'Vector') -> bool:
        """Checks if current vector object equals to compared vector
        :param vector: Compared vector
        :return bool:
        """
        return (self.x0 == vector.x0
                and self.y0 == vector.y0
                and self.x1 == vector.x1
                and self.y1 == vector.y1)

    def __repr__(self) -> str:
        """Returns vector representation"""
        return f"({self.x0}, {self.y0}, {self.x1}, {self.y1})"

    def get_vector_length(self) -> float:
        """Get vector length"""
        return math.sqrt(math.pow(self.x1 - self.x0, 2) + math.pow(self.y1 - self.y0, 2))


v1 = Vector(0, 0, 3, 4)
v2 = Vector(0, 0, 3, 4)
print(v1.get_vector_length())

v3 = v1 + v2
print(v3)  # (0,0,6,8)

v4 = v1 - v2
print(v4)  # (0,0,0,0)

v5 = v1 * 5
print(v5)  # (0,0,15,20)

print(v1 < v5)  # True
print(v5 < v1)  # False

print(v1 == v2)  # True
print(v5 == v1)  # False
