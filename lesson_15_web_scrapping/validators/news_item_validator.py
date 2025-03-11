from parsers.abc_parser import NewsItem


class NewsItemValidator:
    """
    Validating string results
    """

    def validate(self, news_item: NewsItem) -> None:
        """
        Validate news_item values
        :param news_item:
        :return:
        """
        required_fields = ['title', 'summary', 'link', 'date']
        for key in required_fields:
            if key not in news_item.keys():
                raise ValueError(f'{key} is not defined')
            if news_item[key] == '':
                raise ValueError(f'Value of {key} cannot be empty')
