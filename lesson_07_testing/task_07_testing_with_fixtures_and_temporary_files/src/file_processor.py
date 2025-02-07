"""
FileProcessor is used for manipulating with files
"""


class FileProcessor:
    pass

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        """
        Write data into file
        :param file_path:
        :param data:
        :return:
        """
        with open(file_path, 'a') as file:
            file.write(data.strip() + "\n")

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Read from file
        :param file_path:
        :return:
        """
        with open(file_path, 'r') as file:
            return file.read()

