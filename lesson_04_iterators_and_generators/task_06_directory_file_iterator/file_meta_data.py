class FileMetadata:
    """
    Represents file's metadata.
    """

    def __init__(self, file_name: str, size: float) -> None:
        """
        :param file_name:
        :param size:
        """
        self._file_name = file_name
        self._size = size

    def __repr__(self):
        return f"(File name: {self._file_name}, File size (KB): {self._size})"
