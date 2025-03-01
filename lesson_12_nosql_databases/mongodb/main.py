from datetime import datetime, timedelta

from create_db import clear_db
from mongodb_client import add_products, create_order, get_orders_for_one_month, delete_not_available_products
from aggregation_operations import get_sold_count_by_period_of_time, get_customer_order_count


def get_filtered_orders() -> None:
    """
    Get filtered orders from mongodb
    :return:
    """
    for order in get_orders_for_one_month():
        print(f"{order['order_number']}, created at: {order['created_at']}")


def get_sold_products_by_date_range(start_date: datetime, end_date: datetime) -> None:
    """
    Get sold products by date range
    :return:
    """
    print("Sold products:")
    for product in get_sold_count_by_period_of_time(start_date, end_date):
        print(f"{product['_id']}: {product['total_quantity']}")


def get_orders_count(name: str) -> None:
    """
    Get customer order count
    :param name:
    :return:
    """
    print("Order count:")
    for customer_order_count in get_customer_order_count(name):
        print(f"{customer_order_count['_id']}'s orders count: {customer_order_count['orders_count']}")


clear_db()
add_products()
create_order()

get_filtered_orders()
delete_not_available_products()
get_sold_count_by_period_of_time(datetime.now() - timedelta(days=30))
get_sold_products_by_date_range(datetime.now() - timedelta(days=30), datetime.now())
get_orders_count('John Doe')
