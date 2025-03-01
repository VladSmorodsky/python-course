import hashlib
import os

from dotenv import load_dotenv


load_dotenv()


def generate_key(payload: str) -> str:
    """
    Generate customer session key
    :return:
    """
    salt = os.getenv("SALT")
    if not salt:
        raise ValueError("Salt not set.")
    sha256_hash = hashlib.sha256()
    sha256_hash.update(f"{payload}{salt}".encode('utf-8'))
    return sha256_hash.hexdigest()


def generate_user_key(payload: str | int) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(f"{payload}".encode('utf-8'))
    return generate_key(md5_hash.hexdigest())
