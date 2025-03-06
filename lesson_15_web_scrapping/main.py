import logging
import re
from datetime import datetime
from typing import Optional, List

import requests
import pandas as pd
from bs4 import BeautifulSoup

from parsers.dou_news_parser import DouNewsParser
from parsers.abc_parser import ABCParser

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def get_page(url: str) -> Optional[BeautifulSoup]:
    """
    Get page content from url
    :param url: site url
    :return:
    """
    try:
        headers = {
            'User-Agent': 'Custom User Agent'
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


def parse_news(parser: ABCParser, soup: BeautifulSoup) -> Optional[List[dict[str, str]]]:
    """
    Parse news page and get each news item: title, url, description, published_at
    :param parser: News parser
    :param soup: BeautifulSoup object that appropriate to parser.
    :return:
    """
    try:
        return parser.parse(soup)
        # news_block = 'b-lenta'
        # news_postcard = 'b-postcard'
        # news_postcard_title = 'title'
        # news_postcard_description = 'b-typo'
        # news_postcard_info = 'b-info'
        # news_list = []
        # news_items = soup.find('div', class_=news_block)
        # for news_item in news_items.find_all('article', class_=news_postcard):
        #     news_item_title = news_item.find('h2', class_=news_postcard_title)
        #     news_item_link = news_item_title.find('a')['href'].strip()
        #     news_item_title_text = news_item_title.find('a').text.strip()
        #     news_item_description = news_item.find('p', class_=news_postcard_description).text.strip()
        #     news_item_info = news_item.find('div', class_=news_postcard_info)
        #     news_item_info_date = news_item_info.find('time').text.strip()
        #     news_list.append(
        #         {
        #             'title': news_item_title_text,
        #             'link': news_item_link,
        #             'summary': news_item_description,
        #             'date': _format_date_string(news_item_info_date)
        #         }
        #     )
        # return news_list
    except Exception as error:
        logging.error(error)


# def _format_date_string(date_string: str) -> str:
#     """
#     Add year to date string if not exists
#     :param date_string:
#     :return:
#     """
#     if re.search(r'\d{4}', date_string):
#         return date_string
#     current_datetime = datetime.now()
#     current_year = current_datetime.year
#     comma_index = date_string.index(',')
#     return f"{date_string[:comma_index]} {current_year}{date_string[comma_index:]}"


def save_to_csv(news_list: List[dict[str, str]]) -> None:
    """
    Save news list to csv
    :param news_list:
    :return:
    """
    df = pd.DataFrame(news_list)
    df.to_csv('news.csv', index=False)


def main():
    site_url = 'https://dou.ua/lenta/news'
    soap_object = get_page(site_url)
    dou_news_parser = DouNewsParser()
    if soap_object:
        data = parse_news(dou_news_parser, soap_object)
        save_to_csv(data)


if __name__ == '__main__':
    main()
