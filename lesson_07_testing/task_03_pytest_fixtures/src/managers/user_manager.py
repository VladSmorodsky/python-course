from lesson_07_testing.task_03_pytest_fixtures.src.models.user import User


class UserManager:
    """
    Class is responsible for user management operations
    """

    def __init__(self):
        self.__users = []

    def add_user(self, user: User) -> None:
        """
        Add user to the system
        :param user:
        :return:
        """
        self.__users.append(user)

    def remove_user(self, name: str) -> None:
        """
        Remove user from list
        :param user:
        :return:
        """
        for user_index, user in enumerate(self.__users):
            if user.name == name:
                del self.__users[user_index]
                break

    def get_all_users(self) -> list:
        """
        Get all users
        :return:
        """
        return self.__users
