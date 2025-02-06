"""
User model consists of name and age attributes
"""


class User:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        """
        Return user name
        :return:
        """
        return self._name

    def __str__(self):
        """
        Represents object
        :return:
        """
        return f"(name: {self._name}, age:{self._age})"

    def __repr__(self) -> str:
        """
        Represents object in lists
        :return:
        """
        return f"(name: {self._name}, age:{self._age})"
