import os
from typing import Mapping, Any

from pymongo import MongoClient
from dotenv import load_dotenv
from pymongo.synchronous.collection import Collection

load_dotenv()

client = MongoClient(os.getenv("DATABASE_CONNECTION"))
db = client[os.getenv("DATABASE_NAME")]


def get_product_collection() -> Collection[Mapping[str, Any] | Any]:
    """
    Get a product collection.
    :return:
    """
    product_collection = db['products']
    return product_collection


def get_order_collection() -> Collection[Mapping[str, Any] | Any]:
    """
    Get an order collection.
    :return:
    """
    order_collection = db['orders']
    return order_collection


def clear_db() -> None:
    """
    Clear database
    :return:
    """
    get_product_collection().delete_many({})
    get_order_collection().delete_many({})
