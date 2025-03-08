from asyncio import Semaphore
from logging import Logger
from typing import Optional

import aiohttp
from bs4 import BeautifulSoup


async def get_page(url: str, semaphore: Semaphore, logger: Logger, page: int = 1) -> Optional[BeautifulSoup]:
    """
    Get page content from url
    :param url: site url
    :param semaphore: used for controlling of simultaneous pages downloading
    :param page: site page number
    :param logger:
    :return:
    """
    try:
        async with semaphore:
            async with aiohttp.ClientSession() as session:
                # Sites can return 403 error if User-Agent header not defined (e.g. DOU).
                headers = {
                    'User-Agent': 'Custom User Agent'
                }
                async with session.get(f"{url}/page/{page}", headers=headers) as response:
                    response.raise_for_status()
                    response = await response.text()
                    if response == '' or response is None:
                        raise ValueError(f'Content is empty: {url}')
                    return BeautifulSoup(response, 'lxml')
    except aiohttp.ClientConnectionError as error:
        logger.error("{}: Connection Error: {}".format(url, error))
    except ValueError as error:
        logger.error("{}: ValueError: {}".format(url, error))
    except Exception as error:
        logger.error("{}: {}".format(url, error))