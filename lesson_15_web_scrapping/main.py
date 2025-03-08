import argparse
import asyncio
import logging
import os
from asyncio import Semaphore

from dotenv import load_dotenv

from get_page import get_page
from parse_news import parse_news
from save_file import save_to_csv
from validators.news_item_validator import NewsItemValidator
from parsers.dou_news_parser import DouNewsParser
from parsers.abc_parser import ABCParser, NewsItem

load_dotenv()

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create CLI processor
cli_processor = argparse.ArgumentParser(description="Process command-line arguments")

# Add arguments
cli_processor.add_argument("--pages", type=int, help="News site's pages count for storing", default=1)
cli_processor.add_argument("--parser", type=str, help="Select web site's parser", default='dounewsparser')


async def main():
    """
    Main function that contains application configurations (set parsers, set web site's page count for parsing)
    :return:
    """
    args = cli_processor.parse_args()
    site_url = os.getenv('SITE_URL')
    if site_url is None or site_url == '':
        raise ValueError('SITE_URL environment variable is not set')
    news_validator = NewsItemValidator()  # Create Validator instance
    dou_news_parser = DouNewsParser(news_validator, logger)  # Create DouNewsParser instance
    parser_registry = {dou_news_parser.__repr__().lower(): dou_news_parser}  # Add it into registry
    parser_name = args.parser
    if parser_name not in parser_registry:
        logging.error('Invalid parser specified: {}'.format(args.parser))
        return
    semaphore = asyncio.Semaphore(5)
    current_page = 1
    while current_page <= args.pages:
        await store_news(site_url, semaphore, parser_registry[parser_name], current_page)
        current_page += 1


async def store_news(site_url: str, semaphore: Semaphore, parser: ABCParser, page_number: int = 1) -> None:
    """
    Get and store news in the csv file
    :param site_url:
    :param semaphore:
    :param page_number:
    :param parser:
    :return:
    """
    soap_object = await get_page(site_url, semaphore, logger, page_number)
    if soap_object:
        data = parse_news(parser, soap_object, logger)
        save_to_csv(data, logger)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except ValueError as error:
        logging.error(error)
