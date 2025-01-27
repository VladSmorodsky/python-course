"""
DirectoryDescriptor is used for field that contains directory path
and responsible for getting and setting result using validation rules.
"""

import os


class DirectoryDescriptor:
    """
    Class represents directory descriptor
    """

    def __get__(self, instance: object, owner) -> str:
        """
        Returns dir path value
        :param instance:
        :param owner:
        :return str:
        """
        return instance.__dict__['__dir']

    def __set__(self, instance: object, image_dir_path: str) -> None:
        """
        Set directory path
        :param instance:
        :param image_dir_path:
        :return:
        :raise ValueError:
        :raise NotADirectoryError:
        """
        if not os.path.exists(image_dir_path):
            raise ValueError(f"Path {image_dir_path} is not exist.")
        if not os.path.isdir(image_dir_path):
            raise NotADirectoryError(f"It's not directory item.")
        instance.__dict__['__dir'] = image_dir_path.strip()
