from abc import ABC, abstractmethod
from typing import Optional, List, Any

from bs4 import BeautifulSoup


class ABCParser(ABC):
    """
    Class defines parsing methods used by all parsers.
    """

    @abstractmethod
    def parse(self, soup: BeautifulSoup) -> Optional[List[dict[str, Any]]]:
        """
        Method gets BeautifulSoup object and parses it.
        :param soup:
        :return:
        """
        pass
