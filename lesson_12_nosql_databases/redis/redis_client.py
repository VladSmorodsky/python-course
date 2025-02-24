import json
import os
from datetime import datetime

import redis
from dotenv import load_dotenv

from customer import Customer
from customer_session import CustomerSession
from generating_functions import generate_key, generate_user_key

load_dotenv()
redis = redis.Redis(host='localhost', port=6379, db=0)


def create_session(customer: Customer) -> CustomerSession:
    """
    Create customer session id
    :return str:
    """
    login_date = datetime.now()
    ttl = os.getenv("SESSION_TTL", 1800)
    session_id = generate_key(f"{customer.id}{login_date.timestamp()}")
    user_key = generate_user_key(f"{customer.id}")
    redis.setex(user_key, ttl, json.dumps(
        {"customer_id": customer.id, "session_token": session_id, "login_date": login_date.isoformat()}))
    return CustomerSession(customer.id, session_id, login_date)


def read_session(customer: Customer) -> CustomerSession:
    """
    Get customer session from Redis
    :param customer:
    :return:
    """
    customer_session = redis.get(generate_user_key(customer.id))
    if not customer_session:
        raise ValueError('No customer session found.')
    customer_session_data = json.loads(customer_session.decode())
    return CustomerSession(customer_session_data["customer_id"], customer_session_data["session_token"],
                           customer_session_data["login_date"])


def update_session(customer: Customer) -> CustomerSession:
    """
    Update customer session
    :param customer:
    :return:
    """
    customer_session = redis.get(generate_user_key(customer.id))
    if not customer_session:
        raise ValueError('No customer session found.')
    return create_session(customer)


def delete_session(customer: Customer) -> None:
    """
    Delete customer session
    :param customer:
    :return:
    """
    redis.delete(generate_user_key(customer.id))
