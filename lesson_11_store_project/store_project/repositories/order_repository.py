from sqlite3 import Connection
from typing import List, Tuple

from store_project.models.order import Order


class OrderRepository:
    """
    Responsible for manipulating data with orders table.
    """
    __connection: Connection

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_customer_order(self, customer_id: int) -> None:
        self.__cursor.execute("""
            INSERT INTO orders (customer_id) VALUES (?)
        """, (customer_id,))
        self.__connection.commit()

    def add_order_details(self, order_item_list: List[Tuple[int, int, float]]) -> None:
        """
        Add order items info.
        :param order_item_list:
        :return:
        """
        self.__cursor.executemany("""INSERT INTO order_details (order_id, product_id, quantity) VALUES (?, ?, ?)""",
                                  order_item_list)
        self.__connection.commit()

    def get_latest_customer_order(self, customer_id: int) -> Order:
        """
        Get latest customer order.
        :param customer_id:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM orders WHERE customer_id = ? ORDER BY order_date DESC""", (customer_id,))
        order_id, customer_id, order_date = self.__cursor.fetchone()
        return Order(order_id, customer_id, order_date)

    def get_customer_orders(self, customer_id: int) -> List[Order] | None:
        """
        Get customer orders.
        :param customer_id:
        :return:
        """
        self.__cursor.execute("""SELECT * FROM orders WHERE customer_id = ?""", (customer_id,))
        return [Order(order[0], order[1], order[2]) for order in self.__cursor.fetchall()]

    def get_customer_orders_count(self, customer_id: int) -> int:
        """
        Get customer orders count.
        :param customer_id:
        :return:
        """
        self.__cursor.execute("""SELECT COUNT(*) FROM orders WHERE customer_id = ?""", (customer_id,))
        return self.__cursor.fetchone()[0]
