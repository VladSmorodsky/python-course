import asyncio
import logging
import random
from asyncio import Semaphore
from typing import List

from validation import validate_url

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def download_page(url: str, semaphore: Semaphore) -> None:
    """
    Emulates downloading page from 1 up to 5 seconds.
    :param url: domain name of the page (e.g. http://example.com)
    :param semaphore: Used for limiting simultaneous downloads
    :return:
    """
    try:
        async with semaphore:
            validate_url(url)
            load_time = random.uniform(1, 5)
            logging.info(f'Downloading page {url}...')
            await asyncio.sleep(load_time)
            logging.info(f'Page downloaded {url}. Time elapsed: {load_time} seconds.')
    except asyncio.CancelledError as error:
        logging.error(error)
    except ValueError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


async def main(url_list: List[str]) -> None:
    """
    Process url list and download pages.
    :param url_list: List of domain names (e.g. ['http://example.com', 'www.example.com'])
    :return:
    """
    semaphore = asyncio.Semaphore(5)
    await asyncio.gather(*(download_page(url, semaphore) for url in url_list))


if __name__ == '__main__':
    urls = [
        "http://example.com/customers",
        "http://example.com/orders",
        "http://example.com/products"
    ]
    asyncio.run(main(urls))
