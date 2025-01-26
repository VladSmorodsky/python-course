import os
from typing import Generator


def read_log_file(file_dir_path: str) -> Generator[str]:
    """
    Read log file
    :param file_dir_path: Path to log file.
    :return:
    """
    if not os.path.exists(file_dir_path):
        raise ValueError(f"Path {file_dir_path} is not exist.")
    with open(file_dir_path, 'r') as log_file:
        for line in log_file:
            yield line.strip()


def log_errors(line: str) -> None:
    """
    Write log's line that contains 'Error' word. If not, skip this line.
    :param line:
    :return:
    """
    error_key = 'Error'

    if not error_key in line:
        return

    with open('log_error.txt', 'a') as error_log_file:
        error_log_file.write(line + "\n")


log_file = read_log_file('log_file.txt')

for line in log_file:
    log_errors(line)
