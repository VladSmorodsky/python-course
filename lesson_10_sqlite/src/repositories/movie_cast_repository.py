from sqlite3 import Connection
from typing import Tuple, List, Any


class MovieCastRepository:
    """
    Responsible for manipulating movie cast information from database
    """
    __connection: Connection = None

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_cast_to_movie(self, movie_cast_list: List[Tuple[int, int]]) -> None:
        """
        Adds a movie cast information to the database
        :param movie_cast_list:
        :return:
        """
        self.__cursor.executemany("""INSERT INTO movie_cast (movie_id, actor_id) VALUES (?, ?)""", movie_cast_list)
        self.__connection.commit()

    def get_movies_with_actors(self) -> List[Tuple[str, str]]:
        """
        Gets movies with actors
        :return:
        """
        self.__cursor.execute("""
            SELECT m.title, a.name FROM movies AS m 
            INNER JOIN movie_cast AS mc ON m.id = mc.movie_id
            INNER JOIN actors as a ON mc.actor_id = a.id 
        """)
        return self.__cursor.fetchall()
