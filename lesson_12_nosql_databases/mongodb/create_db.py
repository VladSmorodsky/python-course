import os
from typing import Mapping, Any

from pymongo import MongoClient, TEXT
from dotenv import load_dotenv
from pymongo.synchronous.collection import Collection

load_dotenv()

client = MongoClient(os.getenv("DATABASE_CONNECTION"))
db = client[os.getenv("DATABASE_NAME")]
product_collection = db['products']
order_collection = db['orders']

# Create index for category field for faster search result
product_collection.create_index([("category", TEXT)])


def get_product_collection() -> Collection[Mapping[str, Any] | Any]:
    """
    Get a product collection.
    :return:
    """
    return product_collection


def get_order_collection() -> Collection[Mapping[str, Any] | Any]:
    """
    Get an order collection.
    :return:
    """
    return order_collection


def clear_db() -> None:
    """
    Clear database
    :return:
    """
    get_product_collection().delete_many({})
    get_order_collection().delete_many({})
