from typing import TextIO


class ArithmeticMeanFileContextManager:
    """
    Responsible for managing file and throw exceptions when smth went wrong
    """
    def __init__(self, file_path: str):
        self._file_path = file_path
        self._file = None

    def __enter__(self) -> TextIO:
        """
        :return:
        """
        self._file = open(self._file_path, 'r')
        return self._file

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Close file and raise ValueError exception if denied symbols exists in the file
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self._file.close()
        if exc_type == ValueError:
            raise ValueError('Error: Only digits and spaces allowed.')
