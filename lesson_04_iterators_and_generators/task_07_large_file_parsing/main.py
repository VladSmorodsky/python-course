import re
from typing import Generator


def get_errors_from_log_file(file_path: str) -> Generator[str, None, None]:
    """
    Get lines from file where 5** and 4** codes exists
    :param file_path:
    :return: Line with error code
    """
    with open(file_path, 'r') as rows:
        for row in rows:
            if re.search(r'\b[5|4][0-9]{2}\b', row.strip()):
                yield row


def write_error_log(error_line: str) -> None:
    """
    Write error line into error log file
    :param error_line:
    :return:
    """
    with open('error.log', 'a') as file:
        file.write(error_line)


file = get_errors_from_log_file('server_file_log.txt')
for line in file:
    write_error_log(line)
