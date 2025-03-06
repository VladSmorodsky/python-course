import logging
from typing import Optional, List

import requests
import pandas as pd
from bs4 import BeautifulSoup

from validators.validator import Validator
from parsers.dou_news_parser import DouNewsParser
from parsers.abc_parser import ABCParser, NewsItem

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def get_page(url: str) -> Optional[BeautifulSoup]:
    """
    Get page content from url
    :param url: site url
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Custom User Agent'  # Sites can return 403 error if User-Agent header not defined (e.g. DOU).
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        if response.text == '' or response.text is None:
            raise ValueError(f'Content is empty: {url}')
        return BeautifulSoup(response.text, 'lxml')
    except requests.exceptions.ConnectionError as error:
        logging.error("Connection Error: {}".format(error))
    except requests.exceptions.HTTPError as error:
        logging.error("HTTP Error: {}".format(error))
    except ValueError as error:
        logging.error("ValueError: {}".format(error))
    except Exception as error:
        logging.error(error)


def parse_news(parser: ABCParser, soup: BeautifulSoup) -> Optional[List[NewsItem]]:
    """
    Parse news page and get each news item: title, url, description, published_at
    :param parser: News parser
    :param soup: BeautifulSoup object that appropriate to parser.
    :return:
    """
    try:
        return parser.parse(soup)
    except ValueError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


def save_to_csv(news_list: List[NewsItem]) -> None:
    """
    Save news list to csv
    :param news_list:
    :return:
    """
    try:
        if not news_list:
            logging.error('No news items to save.')
            return
        df = pd.DataFrame(news_list)
        df.to_csv('news.csv', index=False)
    except PermissionError as error:
        logging.error(error)
    except FileNotFoundError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


def main():
    site_url = 'https://dou.ua/lenta/news'
    soap_object = get_page(site_url)
    if soap_object:
        news_validator = Validator()  # Create Validator instance
        dou_news_parser = DouNewsParser(news_validator, logger)  # Create DouNewsParser instance
        data = parse_news(dou_news_parser, soap_object)
        save_to_csv(data)


if __name__ == '__main__':
    main()
