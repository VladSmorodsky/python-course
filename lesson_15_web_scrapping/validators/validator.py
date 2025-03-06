from parsers.abc_parser import NewsItem


class Validator:
    """
    Validating string results
    """

    def validate(self, news_item: NewsItem) -> None:
        """
        Validate news_item values
        :param news_item:
        :return:
        """
        for key in news_item:
            if news_item[key] is None or news_item[key] == '':
                raise ValueError(f'Value of {key} cannot be empty')
