import re
from datetime import datetime
from typing import Optional, List

from bs4 import BeautifulSoup, PageElement, Tag, NavigableString

from parsers.abc_parser import ABCParser


class DouNewsParser(ABCParser):
    """
    Parser for Dou News articles.
    """
    news_block = 'b-lenta'
    news_postcard = 'b-postcard'
    news_postcard_title = 'title'
    news_postcard_description = 'b-typo'
    news_postcard_info = 'b-info'

    def parse(self, soup: BeautifulSoup) -> Optional[List[dict[str, str]]]:
        """
        Implementation of the abstract method for parsing.
        :param soup:
        :return:
        """
        news_list = []
        news_items = soup.find('div', class_=self.news_block)
        for news_item in news_items.find_all('article', class_=self.news_postcard):
            news_item_title = news_item.find('h2', class_=self.news_postcard_title)
            news_item_description = news_item.find('p', class_=self.news_postcard_description).text.strip()
            news_item_info = news_item.find('div', class_=self.news_postcard_info)

            news_item_link = news_item_title.find('a')['href'].strip()
            news_item_title_text = news_item_title.find('a').text.strip()
            # news_item_info_date = news_item_info.find('time').text.strip()
            news_list.append(
                {
                    'title': news_item_title_text,
                    'link': news_item_link,
                    'summary': news_item_description,
                    'date': self._format_date_string(news_item_info)
                }
            )
        return news_list

    def _format_date_string(self, postcard_info: PageElement | Tag | NavigableString) -> str:
        """
        Add year to date string if not exists
        :return:
        """
        date_string = postcard_info.find('time').text.strip()
        if re.search(r'\d{4}', date_string):
            return date_string
        current_datetime = datetime.now()
        current_year = current_datetime.year
        comma_index = date_string.index(',')
        return f"{date_string[:comma_index]} {current_year}{date_string[comma_index:]}"
