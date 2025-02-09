from typing import final, TypedDict


@final
class Config(TypedDict):
    """
    Stores database configuration
    """
    database_name: str
    product_table_name: str
