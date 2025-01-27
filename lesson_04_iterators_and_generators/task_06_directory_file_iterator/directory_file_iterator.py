import os

from directory_descriptor import DirectoryDescriptor
from file_meta_data import FileMetadata


class DirectoryFileIterator:
    """
    Class is responsible for file iteration in the directory.
    """
    _directory = DirectoryDescriptor()

    def __init__(self, directory: str) -> None:
        """
        :param directory: Directory with files
        """
        self._directory = directory
        self._file_path_list = os.listdir(self._directory)
        self._position = 0

    def __iter__(self):
        """
        :return:
        """
        return self

    def __next__(self) -> FileMetadata:
        """
        Returns file metadata (file name and size in kilobytes)
        :return FileMetadata:
        """
        if self._position >= len(self._file_path_list):
            raise StopIteration
        file_path = f"{self._directory}/{self._file_path_list[self._position]}"
        file_metadata = FileMetadata(os.path.basename(file_path), round(os.path.getsize(file_path) / 1024, 2))
        self._position += 1
        return file_metadata
