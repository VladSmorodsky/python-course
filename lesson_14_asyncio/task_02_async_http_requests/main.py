import asyncio
import logging
from typing import Optional, List
from urllib.error import HTTPError

import aiohttp

from validation import validate_url

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


async def fetch_content(url: str) -> Optional[str]:
    """
    Fetch content from url
    :param url:
    :return:
    """
    try:
        validate_url(url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()
    except HTTPError as error:
        logging.error(error)
    except ValueError as error:
        logging.error(error)
    except ConnectionError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


async def fetch_all(url_list: List[str]) -> List[str]:
    """
    Fetch content from whole url list
    :param url_list:
    :return:
    """
    return await asyncio.gather(*[fetch_content(url) for url in url_list])


async def get_contents() -> None:
    """
    Run fetch_all function and show content
    :return:
    """
    urls = [
        "https://www.python.org",
        "https://www.w3schools.com/python/default.asp",
    ]
    contents = await fetch_all(urls)
    for url, content in zip(urls, contents):
        logging.info(f"Content of {url}: {content}")


asyncio.run(get_contents())
