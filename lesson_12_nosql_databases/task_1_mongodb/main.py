from datetime import datetime, timedelta

from create_db import clear_db
from crud_operations import add_products, create_order, get_orders_for_one_month, delete_not_available_products
from aggregation_operations import get_sold_count_by_period_of_time


def get_filtered_orders() -> None:
    """
    Get filtered orders from mongodb
    :return:
    """
    for order in get_orders_for_one_month():
        print(f"{order['order_number']}, created at: {order['created_at']}")


clear_db()
add_products()
create_order()

get_filtered_orders()
delete_not_available_products()
get_sold_count_by_period_of_time(datetime.now() - timedelta(days=30))
