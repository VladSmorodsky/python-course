import math


class Vector:
    """Class Vector represents vector in n* dimension"""

    def __init__(self, *dimension: int) -> None:
        self.dimension = dimension

    def __add__(self, vector: 'Vector') -> 'Vector':
        """Add two vectors with the same dimension.
        :param vector: Added vector
        :return Vector:
        :raise ValueError: Two vectors have different dimensions
        """
        self.__validate_vectors_dimension(vector)
        return Vector(*(v1_dimension_item + v2_dimension_item for v1_dimension_item, v2_dimension_item in
                        zip(self.dimension, vector.dimension)))

    def __sub__(self, vector: 'Vector') -> 'Vector':
        """Add two vectors with the same dimension.
        :param vector: Subtracted vector
        :return Vector:
        :raise ValueError: Two vectors have different dimensions
        """
        self.__validate_vectors_dimension(vector)
        return Vector(*(v1_dimension_item - v2_dimension_item for v1_dimension_item, v2_dimension_item in
                        zip(self.dimension, vector.dimension)))

    def __mul__(self, scalar: int) -> 'Vector':
        """Multiply vector to scalar value
        :param scalar: integer value
        :return Vector:
        """
        return Vector(*(dimension_item * scalar for dimension_item in self.dimension))

    def __lt__(self, compared_vector: 'Vector') -> bool:
        """Compare if current vector length less than compared
        :param compared_vector: Compared vector
        :return bool:
        """
        return self.get_vector_length() < compared_vector.get_vector_length()

    def __gt__(self, compared_vector: 'Vector') -> bool:
        """Compare if current vector length greater less than compared
        :param compared_vector: Compared vector
        :return bool:
        """
        return self.get_vector_length() > compared_vector.get_vector_length()

    def __eq__(self, compared_vector: 'Vector') -> bool:
        """Compare if vectors length are equal
        :param compared_vector: Compared vector
        :return bool:
        """
        return self.get_vector_length() == compared_vector.get_vector_length()

    def __repr__(self) -> str:
        """Return vector representation"""
        return f"({', '.join([str(dimension) for dimension in self.dimension])})"

    def get_vector_length(self) -> float:
        """Get n-dimension vector length
        :return float:
        """
        return math.sqrt(sum(dimension_item ** 2 for dimension_item in self.dimension))

    def __validate_vectors_dimension(self, vector: 'Vector') -> None:
        """Validate vectors dimensions
        :param vector: Compared vector object
        :raise ValueError
        """
        if len(self.dimension) != len(vector.dimension):
            raise ValueError("Vectors must have same dimension")


v1 = Vector(0, 0, 3, 4)
v2 = Vector(0, 0, 3, 4)

v3 = v1 + v2
print(v3)

v4 = v1 - v2
print(v4)

v5 = v1 * 5
print(v5)

print(v1 == v2)
print(v1 < v3)
print(v1 > v3)
