import unittest
from typing import List

from task_02_vector_numeric_like import Vector


class VectorList:
    """Class represents a list of vectors and base operations on them."""

    def __init__(self, vector_list: List[Vector]) -> None:
        self.vector_list = vector_list
        self.index = 0

    def __iter__(self):
        """Returns self object"""
        return self

    def __next__(self):
        """Returns next item in the list, otherwise raise StopIteration exception."""
        if self.index < len(self):
            result = self.vector_list[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration()


def len(vectors_list: VectorList) -> int:
    """Get VectorList's vectors count
    :param vectors_list:
    :return int:
    """
    vector_objects_count = 0

    for vector in vectors_list.vector_list:
        vector_objects_count += 1

    return vector_objects_count


def sum(vectors_list: VectorList) -> float:
    """Returns sum of VectorList's vectors length
    :param vectors_list:
    :return float:
    """
    vectors_sum = 0

    for vector in vectors_list.vector_list:
        vectors_sum += vector.get_vector_length()

    return vectors_sum


def min(vectors_list: VectorList) -> float:
    """Returns min VectorList's vector length
    :param vectors_list:
    :return float:
    """
    if len(vectors_list) <= 0:
        # Return 0 if list is empty
        return 0

    min_value = vectors_list.vector_list[0].get_vector_length()

    for index, vector in enumerate(vectors_list.vector_list):
        if index == 0:
            continue
        if min_value > vector.get_vector_length():
            min_value = vector.get_vector_length()

    return min_value


# Tests

class TaskFiveTest(unittest.TestCase):
    def test_new_len_function(self):
        """Test new len() function"""
        v1 = Vector(0, 0, 3, 4)
        v2 = Vector(0, 0, 5, 6)
        v3 = Vector(0, 0, 1, 2)

        vectors = VectorList([v1, v2, v3])

        self.assertEqual(3, len(vectors))

    def test_new_sum_function(self):
        """Test new sum() function"""
        v1 = Vector(0, 0, 3, 4)
        v2 = Vector(0, 0, 3, 4)
        v3 = Vector(0, 0, 3, 4)

        vectors = VectorList([v1, v2, v3])

        self.assertEqual(15, sum(vectors))

    def test_new_min_function(self):
        """Test new min() function"""
        v1 = Vector(0, 0, 3, 4)
        v2 = Vector(0, 0, 5, 6)
        v3 = Vector(0, 0, 7, 9)

        vectors = VectorList([v1, v2, v3])

        self.assertEqual(5, min(vectors))

    def test_iter_method(self):
        """Test VectorList's iteration"""
        v1 = Vector(0, 0, 3, 4)
        v2 = Vector(0, 0, 5, 6)
        v3 = Vector(0, 0, 7, 9)

        vectors = iter(VectorList([v1, v2, v3]))

        next(vectors)

        self.assertEqual(v2, next(vectors))

    def test_iter_raise_stop_iteration_exception(self):
        """Test raising StopIteration exception"""
        with self.assertRaises(StopIteration):
            v1 = Vector(0, 0, 3, 4)
            vectors = iter(VectorList([v1]))

            next(vectors)
            next(vectors)  # Exception
