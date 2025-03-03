import logging
import os
from concurrent.futures import ThreadPoolExecutor

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')


def search_text(file_path: str, searched_text: str) -> None:
    """
    Search text in a text file.
    :param file_path:
    :param searched_text:
    :return:
    """
    try:
        with open(file_path, 'r') as file:
            for line_number, line in enumerate(file, start=1):
                if searched_text.lower() in line.lower():
                    logging.info(f'{file_path}: Found {searched_text} on line {line_number}')
    except FileNotFoundError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)


def search_text_in_dir(dir_path: str, searched_text: str) -> None:
    """
    Search text in directory with text files.
    :param dir_path:
    :param searched_text:
    :return:
    """
    try:
        files_in_dir = os.listdir(dir_path)
        with ThreadPoolExecutor() as executor:
            for file_name in files_in_dir:
                executor.submit(search_text, os.path.join(dir_path, file_name), searched_text)
        logging.info(f'Processes done.')
    except FileNotFoundError as error:
        logging.error(error)
    except Exception as error:
        logging.error(error)
