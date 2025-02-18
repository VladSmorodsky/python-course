from sqlite3 import Connection
from typing import Any, Tuple


class ActorRepository:
    """
    Responsible for manipulating actors information from database
    """
    __connection: Connection

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
        self.__cursor.execute("""INSERT OR IGNORE INTO actors (name, birth_year) VALUES (?, ?)""",
                              (name, year))
        self.__connection.commit()
        self.__connection.close()

    def find_by_id(self, actor_id: int) -> tuple:
        """
        Retrieves an actor by id.
        :param actor_id:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors WHERE id = ?""", (actor_id,))
        actor = self.__cursor.fetchone()
        self.__connection.close()
        return actor

    def find_by_name(self, actor_name: str) -> Any:
        """
        Retrieves a actor by name.
        :param actor_name:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors WHERE name = ?""", actor_name)
        actor = self.__cursor.fetchone()
        self.__connection.close()
        return actor

    def find_all(self) -> list[tuple]:
        """
        Retrieves all actors.
        :return:
        """
        self.__cursor.execute("""SELECT * FROM actors""")
        actors = self.__cursor.fetchall()
        self.__connection.close()
        return actors

    def find_all_in_list(self, actor_ids: Tuple[int, ...]) -> list[tuple]:
        """
        Retrieves all actors.
        :return:
        """
        placeholders = ', '.join('?' for _ in actor_ids)
        query = f'SELECT * FROM actors WHERE id IN ({placeholders})'
        self.__cursor.execute(query, actor_ids)
        actors = self.__cursor.fetchall()
        self.__connection.close()
        return actors
