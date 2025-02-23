import sqlite3

from total_revenue_per_product_aggregator import TotalRevenuePerProductAggregator


class Database:
    """
    Class responsible for creating database and give connection
    """
    __connection: sqlite3.Connection

    def __init__(self, db_file: str) -> None:
        self.__connection = sqlite3.connect(db_file)
        self.__connection.create_aggregate('total_revenue_per_product', 2, TotalRevenuePerProductAggregator)

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
        self.connection.execute('PRAGMA foreign_keys = ON;')
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT UNIQUE NOT NULL
            )
        """)
        self.__connection.commit()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock REAL NOT NULL
            )
        """)
        self.__connection.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_date DEFAULT CURRENT_TIMESTAMP NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers (id) ON DELETE CASCADE
            )
        """)
        self.__connection.commit()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_details (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity REAL NOT NULL,
                FOREIGN KEY (product_id) REFERENCES products (id) ON DELETE CASCADE,
                FOREIGN KEY (order_id) REFERENCES orders (id) ON DELETE CASCADE
            )
        """)
        self.__connection.commit()
        cursor.execute("""
            CREATE TRIGGER IF NOT EXISTS update_stock AFTER INSERT ON order_details
            BEGIN
                 UPDATE products
                 SET stock = stock - NEW.quantity
                 WHERE id = NEW.product_id;
            END;
        """)
        self.__connection.commit()
        cursor.execute("""CREATE INDEX IF NOT EXISTS idx_customers_email ON customers(email);""")
        self.__connection.commit()
        cursor.close()
