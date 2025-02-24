from datetime import datetime
from typing import Any, Mapping, Optional

from pymongo.command_cursor import CommandCursor

from create_db import get_order_collection


def get_sold_count_by_period_of_time(start_date: datetime, end_date: datetime = datetime.now()) -> Optional[
    CommandCursor[
        Mapping[str, Any]]]:
    """
    Get products' sold count by period of time.
    :param start_date:
    :param end_date:
    :return:
    """
    if start_date > end_date:
        raise ValueError('Start date must be less than end date')
    order_collection = get_order_collection()
    sold_product_data = order_collection.aggregate([
        {"$match": {"created_at": {"$gte": start_date, "$lte": end_date}}, },  # filter by date range
        {"$unwind": {"path": "$products"}},  # unwind products array of objects
        {"$group": {
            "_id": "$products.name",  # group by product name
            "total_quantity": {"$sum": "$products.quantity"},  # count sold products
        }},
        {"$sort": {"total_quantity": -1}},  # order by sold product count in desc order
    ])
    return sold_product_data


def get_customer_order_count(customer_name: str) -> Optional[CommandCursor[Mapping[str, Any]]]:
    """
    Get products' customer order count.'
    :param customer_name:
    :return:
    """
    order_collection = get_order_collection()
    orders = order_collection.aggregate([
        {"$match": {"client": customer_name}},
        {"$group": {
            "_id": "$client", # grouping all documents together into a single group
            "orders_count": {"$sum": 1}, #
        }}
    ])
    return orders
