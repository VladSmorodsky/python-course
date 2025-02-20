import os

from dotenv import load_dotenv

from database import Database
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

# Services init
customer_service = CustomerService(customer_repository)

# Client code
def create_customers():
    """
    Add test clients into db.
    :return:
    """
    customer_dataset = [
        ('John Doe', 'johndoe@example.com', '+380401231555'),
        ('Test User', 't+@example.com', '+380401231111'), # Email is not valid
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


# Execute client code
create_customers()