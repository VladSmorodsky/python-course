from sqlite3 import Connection
from typing import List

from store_project.models.product import Product


class ProductRepository:
    """
    Responsible for manipulating data with customers table.
    """
    __connection: Connection

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_product(self, product: Product) -> None:
        """
        Adds a product to the table.
        :param product:
        :return:
        """
        self.__cursor.execute("""
            INSERT INTO products (name, price, stock) VALUES (?, ?, ?)
        """, (product.name, product.price, product.stock))
        self.__connection.commit()

    def get_available_products(self) -> List[Product]:
        self.__cursor.execute("""SELECT name, price, stock FROM products WHERE stock > 0""")
        product_list = self.__cursor.fetchall()
        return [Product(product[0], product[1], product[2]) for product in product_list]

    def find_by_matching_title_from_start(self, title: str) -> List[Product]:
        """
        Finds products by its title's matching.
        :param title:
        :return:
        """
        self.__cursor.execute("""SELECT name, price, stock FROM products WHERE LOWER(name) LIKE ?""",
                              (f"{title.lower()}%",))
        return [Product(product[0], product[1], product[2]) for product in self.__cursor.fetchall()]

    def find_by_matching_title(self, title: str) -> List[Product]:
        """
        Finds products by its title's matching.'
        :param title:
        :return:
        """
        self.__cursor.execute("""SELECT name, price, stock FROM products WHERE LOWER(name) LIKE ?""",
                              (f"%{title.lower()}%",))
        return [Product(product[0], product[1], product[2]) for product in self.__cursor.fetchall()]
