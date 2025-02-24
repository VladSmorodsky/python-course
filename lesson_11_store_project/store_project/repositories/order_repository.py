from datetime import datetime
from sqlite3 import Connection
from typing import List, Tuple

from store_project.models.order import Order

from store_project.models.customer import Customer


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

    def get_order_list_with_customers(self) -> List[Tuple[str, int, datetime]]:
        """
        Get orders list with customers.
        :return:
        """
        self.__cursor.execute("""
            SELECT c.name, o.id, o.order_date FROM customers as c
            INNER JOIN orders as o ON o.customer_id = c.id
        """)
        return [customer_order for customer_order in self.__cursor.fetchall()]

    def get_customers_totals(self) -> List[Tuple[Customer, float]]:
        """
        Get customers with total spending
        :return:
        """
        self.__cursor.execute("""
            SELECT c.id, c.name, c.email, c.phone, SUM(p.price * od.quantity) as total FROM customers as c
            INNER JOIN orders as o ON o.customer_id = c.id
            INNER JOIN order_details as od ON od.order_id = o.id
            INNER JOIN products as p ON od.product_id = p.id
            GROUP BY c.id
            ORDER BY total DESC 
        """)
        return [(Customer(customer_totals[1], customer_totals[2], customer_totals[3], customer_totals[0]),
                 customer_totals[4]) for customer_totals in self.__cursor.fetchall()]

    def get_products_totals(self) -> List[Tuple[int, float]]:
        """
        Get sold products total revenue.
        :return:
        """
        self.__cursor.execute("""
             SELECT p.id, p.name, total_revenue_per_product(p.price, od.quantity) as total_revenue
             FROM products as p
             JOIN order_details as od ON od.product_id = p.id
             GROUP BY p.id
             ORDER BY total_revenue DESC
        """)
        return self.__cursor.fetchall()
