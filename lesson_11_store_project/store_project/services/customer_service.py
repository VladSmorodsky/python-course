from sqlite3 import IntegrityError

from store_project.repositories.customer_repository import CustomerRepository

from store_project.models.customer import Customer


class CustomerService:
    """
    Service is responsible for working with customers.
    """

    def __init__(self, customer_repository: CustomerRepository) -> None:
        self.__customer_repository = customer_repository

    def add_customer(self, customer: Customer) -> None:
        """
        Save customer into the database.
        :param customer:
        :return:
        """
        try:
            self.__customer_repository.add_customer(customer)
        except IntegrityError:
            print("Customer already exists")  # log issue

    def get_customer_by_id(self, customer_id: int) -> Customer:
        """
        Return customer by id.
        :param customer_id:
        :return:
        """
        return self.__customer_repository.get_customer_by_id(customer_id)
