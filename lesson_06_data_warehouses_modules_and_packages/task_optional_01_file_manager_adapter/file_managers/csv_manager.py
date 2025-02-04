import csv
import os
from typing import Generator, Any

from exceptions.file_extension_error import FileExtensionError


class CsvManager:
    """
    Responsible for working with csv files
    """
    __ALLOWED_EXTENSIONS = ['.csv']

    def read_csv_file(self, csv_file_path: str) -> Generator[list[str], Any, None]:
        """
        Read CSV file
        :param csv_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            self.__validate_file_extension(csv_file_path)
            with open(csv_file_path, 'r') as csv_file:
                data = csv.reader(csv_file)
                for row in data:
                    yield row
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {csv_file_path}")

    def write_csv_file(self, csv_file_path: str, data: list[str]) -> None:
        """
        Add student into csv file
        :param csv_file_path:
        :param data:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            self.__validate_file_extension(csv_file_path)
            with open(csv_file_path, 'w') as csv_file:
                writer = csv.writer(csv_file)
                for row in data:
                    writer.writerow(row)
            print(f"Data successfully added into {csv_file_path}")
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {csv_file_path}")

    def __validate_file_extension(self, csv_file_path: str) -> None:
        """
        Validate if file has an allowed format
        :param csv_file_path:
        :return:
        :raise FileExtensionError
        """
        file_extension = os.path.splitext(csv_file_path)[1]
        if file_extension not in self.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {csv_file_path} has not compatible extension: {file_extension}")
