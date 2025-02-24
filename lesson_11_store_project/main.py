import os

from dotenv import load_dotenv

from database import Database
from store_project.services.order_service import OrderService
from store_project.repositories.order_repository import OrderRepository
from store_project.models.product import Product
from store_project.repositories.product_repository import ProductRepository
from store_project.services import product_service
from store_project.services.product_service import ProductService
from store_project.repositories.customer_repository import CustomerRepository
from store_project.services.customer_service import CustomerService
from store_project.models.customer import Customer

# Setup and preparing database and infrastructure
load_dotenv()
db_name = os.getenv("DATABASE_NAME")
if db_name is None:
    raise ValueError("DATABASE_NAME environment variable is not set")
database = Database(db_name)
database.create_database()

# Repositories init
customer_repository = CustomerRepository(database.connection)
product_repository = ProductRepository(database.connection)
order_repository = OrderRepository(database.connection)

# Services init
customer_service = CustomerService(customer_repository)
product_service = ProductService(product_repository)
order_service = OrderService(order_repository)


# Client code
def create_customers():
    """
    Client function that adds test customers into db.
    :return:
    """
    customer_dataset = [
        ('John Doe', 'johndoe@example.com', '+380401231555'),
        ('Test User', 't+@example.com', '+380401231111'),  # Email is not valid
        ('Merry Merry', 'merry@example.com', '+380401231222'),
        ('Silvester Casper', 's-casper@example.com', '+380401231333'),
        ('Katty Bale', 'katty@example.com', '+380401231444'),
    ]
    for name, email, phone in customer_dataset:
        try:
            customer = Customer(name=name, email=email, phone=phone)
            customer_service.add_customer(customer)
        except ValueError as error:
            print(error)


def create_products():
    """
    Client function that adds test products into db.
    :return:
    """
    product_dataset = [
        ('Samsung A30', 20000, 40),
        ('MacBook M4', 100000, 20),
        ('Nokia', 8000, 80),
        ('Xiaomi Redmi 10', 10000, 100),
        ('Xiaomi Redmi 11', 13000, 100),
        ('Sony', 12500, 20),
        ('Acer Aspire', 23000, 50),
        ('Asus', 33000, 45),
        ('Huawei Phone', 8500, 100),
        ('Test Phone', 55000, 2),
    ]

    for name, price, stock in product_dataset:
        try:
            product = Product(name=name, price=price, stock=stock)
            product_service.add_product(product)
        except ValueError as error:
            print(error)


def create_orders():
    """
    Client function that adds test orders into db.
    :return:
    """
    order_dataset = [
        1,
        1,
        2,
        3,
        4,
        3,
        3,
        4,
        3,
        3,
    ]
    order_details_dataset_by_customer_id = [
        [(1, 1, 2), (1, 3, 1)],
        [(2, 2, 1)],
        [(3, 6, 1)],
        [(4, 9, 1)],
        [(5, 1, 1)],
        [(6, 7, 1)],
        [(7, 8, 1)],
        [(8, 9, 1)],
        [(9, 3, 1)],
        [(10, 2, 1), (10, 3, 1)],
    ]
    for index, customer_id in enumerate(order_dataset):
        try:
            customer = customer_service.get_customer_by_id(customer_id)
            order_service.create_customer_order(customer, order_details_dataset_by_customer_id[index])
        except ValueError as error:
            print(error)  # log issue


def get_available_products() -> None:
    """
    Client function that gets available products from db.
    :return:
    """
    print('Available Products:')
    for product in product_service.get_available_products():
        print(product)


def get_customer_orders(customer_id: int) -> None:
    """
    Client function that gets customer orders from db.
    :param customer_id:
    :return:
    """
    print('Customer Orders:')
    for order in order_service.get_customer_orders(customer_id):
        print(order)


def get_customer_orders_count(customer_id: int) -> None:
    """
    Client function that gets customer orders count from db.
    :param customer_id:
    :return:
    """
    print(f'Customer Orders Count: {order_service.get_customer_orders_count(customer_id)}')


def get_matched_product(title: str) -> None:
    """
    Client function that gets matched product from db.
    :param title:
    :return:
    """
    print('Matched Products from start:')
    for product in product_service.get_matched_products_from_start(title):
        print(product)

    print('Matched Products')
    for product in product_service.get_matched_products(title):
        print(product)


def get_limited_products(page: int = 1) -> None:
    """
    Client function that gets limited products from db.
    :param page:
    :return:
    """
    print('First Page:')
    for product in product_service.get_paginated_products(page):
        print(product)
    print('Next Page:')
    for product in product_service.get_paginated_products(page + 1):
        print(product)


def get_order_list_with_customers() -> None:
    """
    Client function that gets orders list from db.
    :return:
    """
    print('Orders List With Customers:')
    print('CUSTOMER_NAME | ORDER_ID | ORDER_DATE')
    for order in order_service.get_order_list_with_customers():
        print(f"{order[0]} | {order[1]} | {order[2]}")


def get_sellable_products() -> None:
    """
    Client function that gets products that was sold at least once.
    :return:
    """
    print('Sellable Products:')
    for product in product_service.get_sellable_products():
        print(product)


def get_customers_totals():
    """
    Client function that gets customers totals from db.
    :return:
    """
    print('Customers Totals:')
    for customer, total in order_service.get_customers_totals():
        print(f"{customer.name}: {total}")


def get_products_with_stock_status() -> None:
    """
    Client function that gets products with stock status.
    :return:
    """
    print('Products with Stock Status:')
    for product_name, status in product_service.get_products_with_stock_status():
        print(f"{product_name}: {status}")


def get_products_totals() -> None:
    """
    Client function that gets products totals from db.
    :return:
    """
    print('Products Totals:')
    for product_id, product_name, total in order_service.get_products_totals():
        print(f"{product_id}. {product_name}: {total}")


# Execute client code
create_customers()
create_products()
create_orders()

# Get all available products
get_available_products()
get_customer_orders(3)
get_customer_orders_count(3)

# Get matched products
get_matched_product('Xia')

# Get limiting products
get_limited_products()

get_order_list_with_customers()
get_sellable_products()
get_customers_totals()

get_products_with_stock_status()

get_products_totals()
