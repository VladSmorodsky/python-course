from sqlite3 import Connection
from typing import List, Tuple

from store_project.models.product import Product


class ProductRepository:
    """
    Responsible for manipulating data with customers table.
    """
    __connection: Connection
    __products_count_per_page = 5

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    @property
    def products_count_per_page(self) -> int:
        """
        Returns the number of products count per page.
        :return:
        """
        return self.__products_count_per_page

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

    def get_paginated_products(self, offset: int = 0) -> List[Product]:
        """
        Gets a paginated list of products.
        :param offset:
        :return:
        """
        self.__cursor.execute("""SELECT name, price, stock FROM products LIMIT ? OFFSET ?""",
                              (self.products_count_per_page, offset,))
        return [Product(product[0], product[1], product[2]) for product in self.__cursor.fetchall()]

    def get_sellable_products(self) -> List[Product]:
        """
        Get products that were sold at least once.
        :return:
        """
        self.__cursor.execute("""
            SELECT DISTINCT name, price, stock FROM products
            INNER JOIN order_details ON products.id = order_details.product_id
        """)
        return [Product(product[0], product[1], product[2]) for product in self.__cursor.fetchall()]

    def get_products_with_stock_status(self) -> List[Tuple[str, str]]:
        """
        Get products with stock status.
        :return:
        """
        self.__cursor.execute("""
            SELECT name, 'Available' AS status FROM products WHERE stock > 0
            UNION ALL
            SELECT name, 'Out of stock' FROM products WHERE stock = 0;
        """)
        return self.__cursor.fetchall()
