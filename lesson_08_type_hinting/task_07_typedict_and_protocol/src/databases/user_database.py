from typing import Protocol, Optional

from ..models.user import User


class UserDatabase(Protocol):
    """
    Represents database with operations between user models
    """

    def get_user(self, user_id: int) -> Optional[User]:
        """
        Get user by id
        :return:
        """

    def save_user(self, user: User) -> None:
        """
        Save user into database
        :return:
        """
