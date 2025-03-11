import datetime
from typing import Optional, List
from unittest.mock import Mock

import pytest
from bs4 import BeautifulSoup

from parsers.abc_parser import NewsItem
from parsers.dou_news_parser import DouNewsParser
from validators.news_item_validator import NewsItemValidator


@pytest.fixture
def dou_news_parser() -> DouNewsParser:
    validator = NewsItemValidator()
    logger_mock = Mock()
    return DouNewsParser(validator, logger_mock)


def get_test_content() -> str:
    return """<div class="b-lenta">
		<article class="b-postcard ">
			<h2 class="title">
				<a href="https://dou.ua/lenta/news/test-title/">
                    Test title
				</a>
			</h2>
			<div class="b-info">
				<time class="date">7 березня<span class="m-hide">, 13:46</span></time>
			</div>
			<p class="b-typo">
                Test summary
			</p>
			</div>
		</article></div>"""


def get_expected_result() -> Optional[List[NewsItem]]:
    return [{
        'title': 'Test title',
        'link': 'https://dou.ua/lenta/news/test-title/',
        'summary': 'Test summary',
        'date': datetime.datetime(2025, 3, 7, 13, 46)
    }]


class TestDouNewsParser:
    @pytest.mark.parametrize("content, expected_result", [
        (get_test_content(), get_expected_result()),
    ])
    def test_parser_method_executes_successfully(self, dou_news_parser, content, expected_result) -> None:
        soup = BeautifulSoup(content, features="lxml")
        result = dou_news_parser.parse(soup)
        assert expected_result == result

    @pytest.mark.parametrize("content, expected_exception, expected_text", [
        ('', ValueError, 'No news found.'),
    ])
    def test_parser_method_raises_exception(self, dou_news_parser, content, expected_exception, expected_text) -> None:
        """
        Check raised exception when parsing fails.
        :param dou_news_parser:
        :param content:
        :param expected_exception:
        :return:
        """
        with pytest.raises(expected_exception, match=expected_text):
            soup = BeautifulSoup(content, features="lxml")
            dou_news_parser.parse(soup)
