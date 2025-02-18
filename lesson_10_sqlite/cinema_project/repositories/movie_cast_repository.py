from sqlite3 import Connection
from typing import Tuple, List


class MovieCastRepository:
    """
    Responsible for manipulating movie cast information from database
    """
    __connection: Connection

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_cast_to_movie(self, movie_cast_list: List[Tuple[int, int]]) -> None:
        """
        Adds a movie cast information to the database
        :param movie_cast_list:
        :return:
        """
        self.__cursor.executemany("""INSERT OR IGNORE INTO movie_cast (movie_id, actor_id) VALUES (?, ?)""",
                                  movie_cast_list)
        self.__connection.commit()
        self.__connection.close()

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
        movies_with_actors = self.__cursor.fetchall()
        self.__connection.close()
        return movies_with_actors

    def get_average_birth_year_for_actors_in_movie_genre(self, movie_genre: str) -> float:
        """
        Get average actors' birth year for movie genre
        :param movie_genre:
        :return:
        """
        self.__cursor.execute("""
            SELECT AVG(birth_year) FROM actors
            INNER JOIN movie_cast ON movie_cast.actor_id = actors.id    
            INNER JOIN movies ON movies.id = movie_cast.movie_id
            WHERE movies.genre = ?
        """, (movie_genre,))
        avg_birth_year = self.__cursor.fetchone()[0]
        self.__connection.close()
        return avg_birth_year

    def get_movies_and_actors_names(self) -> List[Tuple[str]]:
        """
        Get movies' and actors' names
        :return:
        """
        self.__cursor.execute("""
            SELECT title FROM movies
            UNION 
            SELECT name FROM actors
        """)
        names = self.__cursor.fetchall()
        self.__connection.close()
        return names
