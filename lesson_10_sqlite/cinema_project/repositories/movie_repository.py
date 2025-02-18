from sqlite3 import Connection
from typing import Tuple, List


class MovieRepository:
    """
    Responsible for manipulating movie information from database
    """
    __connection: Connection
    __movies_count_by_page: int = 2  # set default page size

    @property
    def movie_count_by_page(self) -> int:
        """
        Returns movies count by page value.
        :return:
        """
        return self.__movies_count_by_page

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_movie(self, movie_title: str, year: int, genre: str = '') -> None:
        """
        Adds a movie to the database.
        :param movie_title:
        :param year:
        :param genre:
        :return:
        """
        self.__cursor.execute("""INSERT OR IGNORE INTO movies (title, release_year, genre) VALUES (?, ?, ?)""",
                              (movie_title, year, genre))
        self.__connection.commit()

    def find_all(self) -> list:
        """
        Retrieves all movies from the database.
        :return:
        """
        self.__cursor.execute("""SELECT * FROM movies""")
        return self.__cursor.fetchall()

    def find_by_id(self, movie_id: int) -> dict:
        """
        Retrieves a movie by id.
        :param movie_id:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM movies WHERE id = ?""", (movie_id,))
        return self.__cursor.fetchone()

    def find_one_by_title(self, movie_title: str) -> list:
        """
        Retrieves a movie by title.
        :param movie_title:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM movies WHERE title = ?""", (movie_title,))
        return self.__cursor.fetchone()

    def find_by_title(self, movie_title: str) -> List[Tuple[str, int]]:
        """
        Retrieve movies by title matching.
        :param movie_title:
        :return:
        """
        self.__cursor.execute("""SELECT title, release_year FROM movies WHERE LOWER(title) LIKE ?""",
                              (f"%{movie_title.lower()}%",))
        return self.__cursor.fetchall()

    def find_all_genres(self) -> List[Tuple[str]]:
        """
        Retrieves all genres from the database.
        :return:
        """
        self.__cursor.execute("""SELECT DISTINCT genre FROM movies WHERE genre IS NOT NULL """)
        return self.__cursor.fetchall()

    def get_movie_count_by_genres(self) -> List[Tuple[str, int]]:
        """
        Retrieves movies count by genre from the database.
        :return:
        """
        self.__cursor.execute(
            """SELECT genre, COUNT(genre) as movie_count FROM movies WHERE genre IS NOT NULL GROUP BY genre ORDER BY movie_count DESC""")
        return self.__cursor.fetchall()

    def get_movies_count(self) -> int:
        """
        Retrieves movies count from the database.
        :return:
        """
        self.__cursor.execute("""SELECT COUNT(*) FROM movies""")
        return self.__cursor.fetchone()[0]

    def get_movies_by_page(self, page: int = 1) -> List[Tuple[str, int]]:
        """
        Retrieves movies paginated result from the database.
        :param page:
        :return:
        """
        self.__cursor.execute("""SELECT title, release_year FROM movies LIMIT ? OFFSET ?""",
                              (self.__movies_count_by_page, self.__movies_count_by_page * (page - 1)))
        return self.__cursor.fetchall()
