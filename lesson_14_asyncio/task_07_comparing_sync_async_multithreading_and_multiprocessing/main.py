import asyncio
import logging
import time
from asyncio import Semaphore
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Optional

import aiohttp
import requests

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def _make_request(url: str) -> Optional[requests.Response]:
    """
    Makes a request to the given url
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.content is None:
            logging.info(f'Content is empty.')
            return None
        return response
    except requests.exceptions.HTTPError as error:
        logging.error("HTTP Error: {}".format(error))
        return None
    except Exception as error:
        logging.error(f"Page downloading failed: {error}", )
        return None


def sync_request_method() -> str:
    """
    Make request 500 times synchronous
    :return:
    """
    response = ''
    for i in range(500):
        response = _make_request(url=f'https://docs.python.org/3/')
    return response


def multi_threaded_request_method() -> None:
    """
    Make request 500 times using multithreaded method
    :return:
    """
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(_make_request, ['https://docs.python.org/3/'] * 500)


def multi_processed_request_method() -> None:
    """
    Make request 500 times using multiprocessing method
    :return:
    """
    with ProcessPoolExecutor(max_workers=10) as executor:
        executor.map(_make_request, ['https://docs.python.org/3/'] * 500)


async def async_request_method() -> None:
    """
    Make request 500 times using async method
    :return:
    """
    semaphore = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, 'https://docs.python.org/3/', semaphore) for _ in range(500)])


async def fetch(session: aiohttp.ClientSession, url: str, semaphore: Semaphore) -> Optional[str]:
    """
    Make async request
    :param session:
    :param url: Domain name (e.g. https://example.com)
    :param semaphore: Used for limiting simultaneous downloads
    :return:
    """
    try:
        async with semaphore:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except aiohttp.ClientResponseError as error:
        logging.error(error)
    except ValueError as error:
        logging.error(error)
    except ConnectionError as error:
        logging.error(error)
    except asyncio.CancelledError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


if __name__ == '__main__':
    # Multi-Threaded method
    start_time = time.time()
    multi_threaded_request_method()
    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time:.2f} seconds")

    # Multi-Processed method
    start_time = time.time()
    multi_processed_request_method()
    end_time = time.time()
    print(f"Multi-processed execution time: {end_time - start_time:.2f} seconds")

    # Async method
    start_time = time.time()
    asyncio.run(async_request_method())
    end_time = time.time()
    print(f"Asynchronous execution time: {end_time - start_time:.2f} seconds")

    # Sync method
    start_time = time.time()
    sync_request_method()
    end_time = time.time()
    print(f"Synchronous execution time: {end_time - start_time:.2f} seconds")
