import re
from datetime import datetime
from logging import Logger
from typing import Optional, List

from bs4 import BeautifulSoup, PageElement, Tag, NavigableString

from parsers.abc_parser import ABCParser, NewsItem

from validators.validator import Validator


class DouNewsParser(ABCParser):
    """
    Parser for Dou News articles.
    """
    news_block = 'b-lenta'
    news_postcard = 'b-postcard'
    news_postcard_title = 'title'
    news_postcard_description = 'b-typo'
    news_postcard_info = 'b-info'

    def __init__(self, validator: Validator, logger: Logger) -> None:
        self._validator = validator
        self._logger = logger

    def parse(self, soup: BeautifulSoup) -> Optional[List[NewsItem]]:
        """
        Implementation of the abstract method for parsing.
        :param soup:
        :return:
        """
        news_list = []
        news_items = soup.find('div', class_=self.news_block)
        if news_items is None:
            raise ValueError("No news found.")
        for item in news_items.find_all('article', class_=self.news_postcard):
            try:
                news_item = {}
                news_item_title = item.find('h2', class_=self.news_postcard_title)
                news_item_info = item.find('div', class_=self.news_postcard_info)
                news_item['title'] = news_item_title.find('a').text.strip()
                news_item['summary'] = item.find('p', class_=self.news_postcard_description).text.strip()
                news_item['link'] = news_item_title.find('a')['href'].strip()
                news_item['date'] = self._format_date_string(news_item_info)
                self._validator.validate(news_item)  # Validate news item
                news_list.append(news_item)
            except ValueError as error:
                self._logger.error(error)  # Log error and get next news item
        return news_list

    def _format_date_string(self, postcard_info: PageElement | Tag | NavigableString) -> datetime:
        """
        Add year to date string if not exists. In DOU news there is no year for published news' date in current year.
        :return:
        """
        date_string = self._replace_ukr_month(postcard_info.find('time').text.strip())
        if re.search(r'\d{4}', date_string):
            return datetime.strptime(date_string, '%d %m %Y, %H:%M')
        current_datetime = datetime.now()
        current_year = current_datetime.year
        comma_index = date_string.index(',')
        published_date = datetime.strptime(f"{date_string[:comma_index]} {current_year}{date_string[comma_index:]}",
                                           '%d %m %Y, %H:%M')
        return published_date

    def _replace_ukr_month(self, date_string: str) -> str:
        """
        Replace Ukrainian month word with month number.
        :param date_string:
        :return:
        """
        month_mapping = {
            'січня': '01',
            'лютого': '02',
            'березня': '03',
            'квітня': '04',
            'травня': '05',
            'червня': '06',
            'липня': '07',
            'серпня': '08',
            'вересня': '09',
            'жовтня': '10',
            'листопада': '11',
            'грудня': '12'
        }
        for month_key in month_mapping:
            if month_key in date_string:
                return date_string.replace(month_key, month_mapping[month_key])
        return date_string
