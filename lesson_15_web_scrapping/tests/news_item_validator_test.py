import datetime

import pytest

from validators.news_item_validator import NewsItemValidator


@pytest.fixture
def validator():
    return NewsItemValidator()


class TestNewsItemValidator:
    @pytest.mark.parametrize("item, expected_error_text", [
        (
                {
                    'link': 'https://dou.ua/lenta/news/test-title/',
                    'summary': 'Test summary',
                    'date': datetime.datetime(2025, 3, 7, 13, 46)
                },
                'title is not defined'
        ),
        (
                {
                    'title': '',
                    'link': 'https://dou.ua/lenta/news/test-title/',
                    'summary': 'Test summary',
                    'date': datetime.datetime(2025, 3, 7, 13, 46)
                },
                'Value of title cannot be empty'
        ),
        (
                {
                    'title': 'Test title',
                    'summary': 'Test summary',
                    'date': datetime.datetime(2025, 3, 7, 13, 46)
                },
                'link is not defined'
        ),
        (
                {
                    'title': 'Test title',
                    'link': 'https://dou.ua/lenta/news/test-title/',
                    'date': datetime.datetime(2025, 3, 7, 13, 46)
                },
                'summary is not defined'
        ),
        (
                {
                    'title': 'Test title',
                    'link': 'https://dou.ua/lenta/news/test-title/',
                    'summary': 'Test summary',
                },
                'date is not defined'
        )
    ])
    def test_validate_method_throws_exception(self, validator, item, expected_error_text):
        """
        Test raising error if validation fails.
        :param validator:
        :param item:
        :param expected_error_text:
        :return:
        """
        with pytest.raises(ValueError, match=expected_error_text):
            validator.validate(item)
