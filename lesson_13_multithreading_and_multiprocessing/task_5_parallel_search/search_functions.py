import os
from threading import Thread


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
                    print(f'{file_path}: Found {searched_text} on line {line_number}')
    except FileNotFoundError as error:
        print(error)
    except Exception as error:
        print(error)


def search_text_in_dir(dir_path: str, searched_text: str) -> None:
    """
    Search text in directory with text files.
    :param dir_path:
    :param searched_text:
    :return:
    """
    try:
        files_in_dir = os.listdir(dir_path)
        threads = []
        for file_name in files_in_dir:
            thread = Thread(target=search_text, args=(os.path.join(dir_path, file_name), searched_text,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()
        print('Processes done.')
    except FileNotFoundError as error:
        print(error)
    except Exception as error:
        print(error)
