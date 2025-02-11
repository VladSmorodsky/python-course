from typing import TypedDict


class User(TypedDict):
    """
    Represents user model
    """
    id: int
    name: str
    is_admin: bool
