from typing import Iterator


class ReadBackIterator:
    """Class represents iterator that starts reading from the end of the file"""

    @staticmethod
    def read_file(file_path: str) -> Iterator[str]:
        """Method reads file from the end.
        :param file_path:
        :rtype Iterator[str]
        """
        with open(file_path, 'r') as file:
            content = file.readlines()
            start_index = len(content) - 1

            while start_index >= 0:
                yield content[start_index].strip()
                start_index -= 1


for row in ReadBackIterator.read_file('task_01_file.txt'):
    print(row)
