import os
from pymongo.synchronous.cursor import Cursor
from typing import Mapping, Any

from bson.objectid import ObjectId
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

# Create connection
client = MongoClient(os.getenv("MONGO_CONNECTION"))

# Create db and collections in MongoDB
db = client[os.getenv("MONGO_DB")]
customer_collection = db['customers']


def add_customer() -> None:
    """
    Add products into collection
    :return:
    """
    customer_collection.insert_one({"name": "Test Customer", "email": "customer@example.com", "birth_year": 1999})


def read_customers() -> Cursor[Mapping[str, Any] | Any]:
    """
    Read customers from collection
    :return:
    """
    return customer_collection.find()


def update_customers(email: str, name: str) -> None:
    """
    Update customers from collection
    :return:
    """
    customer_collection.update_one({"email": email}, {"$set": {"name": name}})


def delete_customers(email: str) -> None:
    """
    Delete customers from collection
    :return:
    """
    customer_collection.delete_one({"email": email})


# Insert customer
add_customer()
# Read customer
for customer in read_customers():
    print(customer)
# Update customer
update_customers('customer@example.com', "John Doe")
# Delete customer
delete_customers('customer@example.com')
