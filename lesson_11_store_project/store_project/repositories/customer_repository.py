from sqlite3 import Connection

from store_project.models.customer import Customer


class CustomerRepository:
    """
    Responsible for manipulating data with customers table.
    """
    __connection: Connection

    def __init__(self, connection: Connection) -> None:
        self.__connection = connection
        self.__cursor = self.__connection.cursor()

    def add_customer(self, customer: Customer) -> None:
        """
        Adds a customer to the table.
        :param customer:
        :return:
        """
        self.__cursor.execute("""
            INSERT INTO customers (name, email, phone) VALUES (?, ?, ?)
        """, (customer.name, customer.email, customer.phone))
        self.__connection.commit()
