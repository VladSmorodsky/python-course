from sqlite3 import Connection
from typing import Any, Tuple


class ActorRepository:
    """
    Responsible for manipulating actors information from database
    """
    __connection: Connection = None

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_actor(self, name: str, year: int) -> None:
        """
        Adds an actor to the database.
        :param name:
        :param year:
        :return:
        """
        self.__cursor.execute("""INSERT INTO actors (name, birth_year) VALUES (?, ?)""",
                              (name, year))
        self.__connection.commit()

    def find_by_id(self, actor_id: int) -> Any:
        """
        Retrieves an actor by id.
        :param actor_id:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors WHERE id = ?""", (actor_id,))
        return self.__cursor.fetchone()

    def find_by_name(self, actor_name: str) -> Any:
        """
        Retrieves a actor by name.
        :param actor_name:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors WHERE name = ?""", actor_name)
        return self.__cursor.fetchone()

    def find_all(self) -> list[Any]:
        """
        Retrieves all actors.
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors""")
        return self.__cursor.fetchall()

    def find_all_in_list(self, actor_ids: Tuple[int, ...]) -> list[Any]:
        """
        Retrieves all actors.
        :return:
        """
        placeholders = ', '.join('?' for _ in actor_ids)
        query = f'SELECT * FROM actors WHERE id IN ({placeholders})'
        self.__cursor.execute(query, actor_ids)
        return self.__cursor.fetchall()
