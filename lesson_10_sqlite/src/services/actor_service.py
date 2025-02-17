from typing import Any, Tuple, List

from ..repositories.actor_repository import ActorRepository
from ..exceptions.not_found_error import NotFoundError


class ActorService:
    """
    Service class to manage actors related operations.
    """

    def __init__(self, actor_repository: ActorRepository) -> None:
        self.__actor_repository = actor_repository

    def add_actor(self, name: str, birth_year: int) -> None:
        """
        Add an actor to the database.
        :param name:
        :param birth_year:
        :return:
        """
        self.__actor_repository.add_actor(name, birth_year)

    def get_all(self) -> list[Any]:
        """
        Get all actors.
        :return:
        :raises NotFoundError:
        """
        actors = self.__actor_repository.find_all()
        if len(actors) == 0:
            raise NotFoundError(f"No actors in database. Please add actors first.")
        return actors

    def get_actor_by_name(self, actor_name: str) -> Any:
        """
        Get actor by name.
        :param actor_name:
        :return:
        """
        return self.__actor_repository.find_by_name(actor_name)

    def get_actors_by_ids(self, actor_ids: Tuple[int, ...]) -> list[Any]:
        """
        Get actors by ids.
        :param actor_ids:
        :return:
        """
        return self.__actor_repository.find_all_in_list(actor_ids)
