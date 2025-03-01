import os
from typing import Tuple, List

import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Create connection.
connection = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host="localhost",
    port=os.getenv("POSTGRES_PORT"),
)

# Create a cursor object
cursor = connection.cursor()


def create_customer_table() -> None:
    """
    Create db in POSTGRES
    :return:
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            birth_year INTEGER NOT NULL
        )
    """)
    connection.commit()


def insert_customer(name: str, email: str, birth_year: int) -> None:
    """
    Insert customer into db
    :param name:
    :param email:
    :param birth_year:
    :return:
    """
    cursor.execute("""
        INSERT INTO customers (name, email, birth_year) VALUES (%s, %s, %s) ON CONFLICT (email) DO NOTHING
    """, (name, email, birth_year))
    connection.commit()


def read_customers() -> List[Tuple[int, str, str, int]]:
    """
    Read customers from db
    :return:
    """
    cursor.execute("SELECT * FROM customers")
    return cursor.fetchall()


def update_customer(customer_id: int, name: str) -> None:
    """
    Update customer from db
    :param customer_id:
    :param name:
    :return:
    """
    cursor.execute("""
        UPDATE customers SET name = %s WHERE id = %s
    """, (name, customer_id))
    connection.commit()


def delete_customer(customer_id: int) -> None:
    """
    Delete customer from db
    :param customer_id:
    :return:
    """
    cursor.execute("""
        DELETE FROM customers WHERE id = %s
    """, (customer_id,))
    connection.commit()


create_customer_table()
# Create Customer
insert_customer("Tst Customer", "customer@example.com", 1999)
# Read Customer
print(read_customers())
# Update Customer
update_customer(1, "John Doe")
# Delete Customer
delete_customer(1)
cursor.close()
connection.close()
