import os.path
import shutil


class BackupContextManager:
    """
    Class responsible for creating backup when important file opens and someone working with it.
    If smth goes wrong, original file will be recovered. Otherwise, it will be overridden
    """

    def __init__(self, file_path: str) -> None:
        """
        :param file_path:
        """
        self._file_path = file_path

    def __enter__(self) -> str:
        """
        Create file copy and return file path
        :return:
        """

        shutil.copy2(self._file_path, self._get_recovery_file_path())
        return self._file_path

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Override original file when changes done successfully or recover it when smth went wrong. Delete copy file.
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        if exc_type is not None:
            shutil.copy2(self._get_recovery_file_path(), self._file_path)
        os.remove(self._get_recovery_file_path())

    def _get_recovery_file_path(self) -> str:
        """
        Return recovery file name
        :return str:
        """
        file_name = os.path.basename(self._file_path)
        return f"{os.path.curdir}/copy_{file_name}"
