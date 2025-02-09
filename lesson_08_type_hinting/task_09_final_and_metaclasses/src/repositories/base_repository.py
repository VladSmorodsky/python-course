import os
from abc import ABC, abstractmethod
from typing import Dict, Any
from dotenv import load_dotenv

from config import Config

load_dotenv()


class BaseRepository(ABC):
    """
    Represents template for other repositories
    """
    __config: Config = {
        'database_name': os.getenv('DATABASE_NAME') if os.getenv('DATABASE_NAME') else 'db',
        'product_table_name': os.getenv('PRODUCT_TABLE_NAME') if os.getenv('PRODUCT_TABLE_NAME') else 'products'
    }

    @property
    def config(self) -> Config:
        return self.__config

    @abstractmethod
    def save(self, data: Dict[str, Any]) -> None:
        """
        Represents template method that other repositories have to implement
        :return:
        """
