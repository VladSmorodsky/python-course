from logging import Logger
from typing import Optional, List

from bs4 import BeautifulSoup

from parsers.abc_parser import ABCParser, NewsItem


def parse_news(parser: ABCParser, soup: BeautifulSoup, logger: Logger) -> Optional[List[NewsItem]]:
    """
    Parse news page and get each news item: title, url, description, published_at
    :param parser: News parser
    :param soup: BeautifulSoup object that appropriate to parser.
    :param logger:
    :return:
    """
    try:
        return parser.parse(soup)
    except ValueError as error:
        logger.error(error)
    except Exception as error:
        logger.error(error)
