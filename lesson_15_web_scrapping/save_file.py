import os
from logging import Logger
from typing import List

import pandas as pd

from parsers.abc_parser import NewsItem


def save_to_csv(news_list: List[NewsItem], logger: Logger) -> None:
    """
    Save news list to csv
    :param news_list:
    :param logger:
    :return:
    """
    try:
        if not news_list:
            logger.error('No news items to save.')
            return
        filename = os.getenv('CSV_FILE_NAME', 'file.csv')
        df = pd.DataFrame()
        if os.path.isfile(filename):
            df = pd.concat([df, pd.DataFrame(pd.read_csv(filename))], ignore_index=True).drop_duplicates()
        df = pd.concat([df, pd.DataFrame(news_list)], ignore_index=True).drop_duplicates()
        df.to_csv(filename, index=False)
    except PermissionError as error:
        logger.error(error)
    except FileNotFoundError as error:
        logger.error(error)
    except Exception as error:
        logger.error(error)