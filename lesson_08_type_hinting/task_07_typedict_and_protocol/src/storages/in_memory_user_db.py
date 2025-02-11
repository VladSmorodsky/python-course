from typing import List, Optional

from lesson_08_type_hinting.task_07_typedict_and_protocol.src.databases.user_database import UserDatabase
from lesson_08_type_hinting.task_07_typedict_and_protocol.src.models.user import User


class InMemoryUserDB(UserDatabase):
    """
    Represents users database storage
    """
    __users: List[User] = []

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Return user by id
        :param user_id:
        :return:
        """
        for user in self.__users:
            if user['id'] == user_id:
                return user
        return None

    def save_user(self, user: User) -> None:
        """
        Save user
        :param user:
        :return:
        """
        self.__users.append(user)
