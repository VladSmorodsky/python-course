import sqlite3


class Database:
    """
    Class responsible for creating database and give connection
    """
    __connection: sqlite3.Connection = None

    def __init__(self, db_file: str) -> None:
        self.__connection = sqlite3.connect(db_file)

    @property
    def connection(self) -> sqlite3.Connection:
        """
        Returns sqlite3 connection
        :return:
        """
        return self.__connection

    def create_database(self) -> None:
        """
        Create database with particular tables (movies, actors, movie_cast)
        :return:
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT UNIQUE NOT NULL,
                release_year INTEGER NOT NULL,
                genre TEXT
            )
        """)
        self.__connection.commit()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS actors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                birth_year INTEGER NOT NULL
            )
        """)
        self.__connection.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS movie_cast (
                actor_id INTEGER,
                movie_id INTEGER,
                PRIMARY KEY (movie_id, actor_id),
                FOREIGN KEY (actor_id) REFERENCES actors(id),
                FOREIGN KEY (movie_id) REFERENCES movies(id) ON DELETE CASCADE
            )
        """)
        self.__connection.commit()
        cursor.close()
