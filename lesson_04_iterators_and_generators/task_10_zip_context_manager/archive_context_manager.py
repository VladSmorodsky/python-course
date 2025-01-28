import zipfile
from zipfile import ZipFile


class ArchiveContextManager:
    """Make a zipfile with files"""

    def __init__(self, archive_name: str):
        """
        :param archive_name: Zip file name
        """
        self._archive_name = archive_name
        self._archive = zipfile.ZipFile(f"{archive_name}.zip", mode="a")

    def __enter__(self) -> ZipFile:
        """
        Returns zip file for adding files into it.
        :return:
        """
        return self._archive

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Close archive when actions finished.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self._archive.close()
