import json
import os
from typing import Generator, Any

from exceptions.file_extension_error import FileExtensionError


class JsonManager:
    """
    Responsible for working with json files
    """
    __ALLOWED_EXTENSIONS = ['.json']

    def read_json_file(self, json_file_path: str) -> Generator[list[str], Any, None]:
        """
        Read JSON file
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            self.__validate_file_extension(json_file_path)
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                for row in data:
                    yield row
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {json_file_path}")
            raise FileNotFoundError

    def write_json_file(self, json_file_path: str, added_data: list[dict[str, str]]) -> None:
        """
        Write into json file
        :param data:
        :return:
        """
        try:
            data = []
            try:
                for book in self.read_json_file(json_file_path):
                    data.append(book)
            except FileNotFoundError:
                print(f"New file will be created: {json_file_path}")

            for item in added_data:
                data.append(item)
            with open(json_file_path, 'w') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
        except FileExtensionError as error:
            print(error)

    def __validate_file_extension(self, json_file_path: str) -> None:
        """
        Validate if file has an allowed format
        :return:
        """
        file_extension = os.path.splitext(json_file_path)[1]
        if file_extension not in self.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {json_file_path} has not compatible extension: {file_extension}")
