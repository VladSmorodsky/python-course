import csv
import os
from typing import Generator, Any

from exceptions.file_extension_error import FileExtensionError
from exceptions.student_score_exception import StudentScoreException


class CsvManager:
    """
    Class is responsible for working with CSV files.
    """
    __ALLOWED_EXTENSIONS = ['.csv']

    @classmethod
    def read_file(cls, csv_file_path: str) -> Generator[list[str], Any, None]:
        """
        Read CSV file
        :param csv_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            cls.__validate_file_extension(csv_file_path)
            with open(csv_file_path, 'r') as csv_file:
                data = csv.reader(csv_file)
                for row in data:
                    yield row
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {csv_file_path}")

    @classmethod
    def get_avg_students_value(cls, csv_file_path: str) -> float:
        """
        Returns average students score value.
        :param csv_file_path:
        :return:
        :raise (StudentScoreException, FileExtensionError, FileNotFoundError, ValueError)
        """
        students_score_list = []
        for index, row in enumerate(cls.read_file(csv_file_path)):
            if index == 0:
                continue
            if not row[2].isdigit():
                raise ValueError('Score can be digit only')
            score = 0 if row[2] == '' else int(row[2])
            students_score_list.append(score)
        students_score = sum(students_score_list)
        if len(students_score_list) == 0 or students_score <= 0:
            raise StudentScoreException(f"Students scores are incorrect. Please check csv file.")
        return round(students_score / len(students_score_list), 0)

    @classmethod
    def write_csv(cls, csv_file_path: str, student_data: list[str]) -> None:
        """
        Add student into csv file
        :param student_data:
        :param csv_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            cls.__validate_file_extension(csv_file_path)
            with open(csv_file_path, 'a') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(student_data[0:3])
            print(f"Data successfully added into {csv_file_path}")
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {csv_file_path}")

    @classmethod
    def __validate_file_extension(cls, file_path: str) -> None:
        """
        Validate if file has an allowed format
        :param file_path:
        :return:
        """
        file_extension = os.path.splitext(file_path)[1]
        if file_extension not in cls.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {file_path} has not compatible extension: {file_extension}")
