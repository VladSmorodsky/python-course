from typing import List, Tuple

from store_project.repositories.order_repository import OrderRepository

from store_project.models.customer import Customer

from store_project.models.order import Order


class OrderService:
    """
    Service is responsible for working with orders.
    """

    def __init__(self, order_repository: OrderRepository) -> None:
        self.__order_repository = order_repository

    def create_customer_order(self, customer: Customer, order_item_list: List[Tuple[int, int, float]]) -> None:
        """
        Create customer order
        :param customer:
        :param order_item_list:
        :return:
        """
        try:
            if customer.customer_id is None:
                raise ValueError('Customer is not exists. Please create a new customer first.')
            self.__order_repository.add_customer_order(customer.customer_id)
            customer_order = self.__order_repository.get_latest_customer_order(customer.customer_id)
            if customer_order is None:
                raise ValueError('Order is not exists.')
            self.__order_repository.add_order_details(order_item_list)
        except ValueError as error:
            print(error)  # log issue

    def get_customer_orders(self, customer_id: int) -> List[Order]:
        """
        Get customer orders list
        :param customer_id:
        :return:
        """
        return self.__order_repository.get_customer_orders(customer_id)

    def get_customer_orders_count(self, customer_id: int) -> int:
        """
        Get customer orders count
        :param customer_id:
        :return:
        """
        return self.__order_repository.get_customer_orders_count(customer_id)
