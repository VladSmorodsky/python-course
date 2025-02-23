from datetime import datetime

from lesson_12_nosql_databases.task_1_mongodb.create_db import get_order_collection


def get_sold_count_by_period_of_time(start_date: datetime, end_date: datetime = datetime.now()) -> float:
    """
    Get products' sold count by period of time
    :param start_date:
    :param end_date:
    :return:
    """
    order_collection = get_order_collection()
    count = order_collection.aggregate([
        {"$match": {"date": {"$gte": start_date, "$lte": end_date}}, },
        {"$unwind": "$products"},
        {"$group": {
            "_id": "$products.name",
            "total_quantity": {"$sum": "$products.quantity"},
        }}
    ])

    return count
