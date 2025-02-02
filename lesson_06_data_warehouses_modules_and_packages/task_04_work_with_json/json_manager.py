import json
import os
from typing import Generator, Any

from exceptions.file_extension_error import FileExtensionError


class JsonManager:
    """
    Class manages work with json
    """
    __ALLOWED_EXTENSIONS = '.json'

    @classmethod
    def read_file(cls, json_file_path: str) -> Generator[list[str], Any, None]:
        """
        Read JSON file
        :param json_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            cls.__validate_file_extension(json_file_path)
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                for row in data:
                    yield row
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {json_file_path}")

    @classmethod
    def get_available_book_list(cls, json_file_path: str) -> Generator[list[str], Any, None]:
        """
        Returns Generator with available books list
        :param json_file_path:
        :return:
        """
        for row in cls.read_file(json_file_path):
            if row['isAvailable']:
                yield row

    @classmethod
    def add_book(cls, json_file_path: str, book_data: dict[str, str | bool]) -> None:
        """
        Add book into json file
        :param book_data:
        :param json_file_path:
        :return:
        """
        try:
            data = []
            for book in cls.read_file(json_file_path):
                data.append(book)
            data.append(book_data)
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {json_file_path}")

    @classmethod
    def __validate_file_extension(cls, file_path: str) -> None:
        """
        Validate if file has
        :param file_path:
        :return:
        """
        file_extension = os.path.splitext(file_path)[1]
        if file_extension not in cls.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {file_path} has not compatible extension: {file_extension}")
