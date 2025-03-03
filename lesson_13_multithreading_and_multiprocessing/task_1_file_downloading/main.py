import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import List
from urllib.error import HTTPError
from urllib.parse import urlparse

import requests


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def download_file(url: str) -> None:
    """
    Download file from url
    :param url:
    :return:
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        if response.content is None:
            logging.info(f'Content is empty.')
            return
        file_name = get_file_name_from_url(url)
        if os.path.exists(file_name):
            logging.info(f'File {file_name} already exists. Skip download.')
            return
        with open(file_name, 'wb') as file:
            file.write(response.content)
        logging.info(f'File {file_name} has been downloaded.')
    except HTTPError as error:
        logging.error("HTTP Error: {}".format(error))
    except Exception as error:
        logging.error(f"File downloading failed: {error}", )


def get_file_name_from_url(url: str) -> str:
    """
    Get file name from url
    :param url:
    :return:
    """
    parsed_url = urlparse(url)
    return os.path.basename(parsed_url.path)


def downloading_files_by_threads(urls: List[str]) -> None:
    """
    Download file from urls using treads
    :param urls:
    :return:
    """
    with ThreadPoolExecutor() as executor:
        for url in urls:
            executor.submit(download_file, url)


if __name__ == "__main__":
    urls = [
        'https://upload.wikimedia.org/wikipedia/commons/9/99/Unofficial_JavaScript_logo_2.svg',
        'https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg'
    ]
    downloading_files_by_threads(urls)
