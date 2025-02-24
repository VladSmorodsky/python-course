from datetime import datetime, timedelta

from bson.objectid import ObjectId
from typing import Mapping, Any, Dict

from pymongo.synchronous.cursor import Cursor
from create_db import get_product_collection, get_order_collection


def add_products() -> None:
    """
    Add products into collection
    :return:
    """
    product_collection = get_product_collection()
    product_dataset = [
        {"name": "orange", "price": 22.0, "category": "fruits", "quantity": 100},
        {"name": "apple", "price": 15.0, "category": "fruits", "quantity": 50},
        {"name": "broccoli", "price": 30.0, "category": "vegetables", "quantity": 75},
        {"name": "chicken", "price": 120.0, "category": "meat", "quantity": 40},
    ]
    product_collection.insert_many(product_dataset)


def find_product_by_name(name: str) -> Dict[str, Any] | None:
    """
    Find products by name
    :param name:
    :return:
    """
    product_collection = get_product_collection()
    return product_collection.find_one({"name": name})


def update_product_count(product_id: ObjectId, sold_quantity: float) -> None:
    """
    Update product quantity
    :param product_id:
    :param sold_quantity:
    :return:
    """
    product_collection = get_product_collection()
    product_collection.update_one({"_id": product_id},
                                  {"$inc": {"quantity": -sold_quantity}})


def create_order() -> None:
    """
    Create order, count total_price and update products' quantity
    :return:
    """
    order_collection = get_order_collection()
    order_dataset = [
        {
            "order_number": "123456",
            "client": "John Doe",
            "products": [
                {"name": "orange", "quantity": 100},
                {"name": "apple", "quantity": 2}
            ],
            "total_price": 0,
            "created_at": datetime(year=2025, month=1, day=15, hour=10, minute=30)
        },
        {
            "order_number": "123456",
            "client": "John Doe",
            "products": [
                {"name": "chicken", "quantity": 3},
                {"name": "apple", "quantity": 2}
            ],
            "total_price": 0,
            "created_at": datetime(year=2025, month=2, day=23, hour=10, minute=30)
        },
        {
            "order_number": "234567",
            "client": "Test Name",
            "products": [
                {"name": "broccoli", "quantity": 2},
                {"name": "chicken", "quantity": 2}
            ],
            "total_price": 0,
            "created_at": datetime.now()
        }
    ]
    for order in order_dataset:
        total_price = 0
        for product_item in order["products"]:
            # Get product
            product = find_product_by_name(product_item["name"])
            if product["quantity"] < product_item["quantity"]:
                raise ValueError(f"Insufficient product {product_item['name']} quantity.")
            total_price += product["price"] * product_item["quantity"]
            # Update product's count
            update_product_count(product['_id'], product_item["quantity"])
        order["total_price"] = total_price
    order_collection.insert_many(order_dataset)


def get_orders_for_one_month() -> Cursor[Mapping[str, Any] | Any]:
    """
    Get orders for one month
    :return:
    """
    order_collection = get_order_collection()
    print(datetime.now() - timedelta(days=30))
    return order_collection.find({"created_at": {"$gte": datetime.now() - timedelta(days=30)}})


def delete_not_available_products() -> None:
    """
    Delete products not available
    :return:
    """
    product_collection = get_product_collection()
    product_collection.delete_many({"quantity": 0})
