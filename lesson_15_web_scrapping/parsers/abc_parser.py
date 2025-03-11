from abc import ABC, abstractmethod
from datetime import datetime
from typing import Optional, List, Any

from bs4 import BeautifulSoup

NewsItem = List[dict['title': str, 'link': str, 'summary': str, 'date': datetime]]


class ABCParser(ABC):
    """
    Class defines parsing methods used by all parsers.
    """

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> Optional[List[NewsItem]]:
        """
        Method gets BeautifulSoup object and parses it.
        :param soup:
        :return:
        """
        pass
