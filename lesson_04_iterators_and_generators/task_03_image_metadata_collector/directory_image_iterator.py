import os
from typing import Union
from PIL import Image

from directory_descriptor import DirectoryDescriptor


class DirectoryImageIterator:
    """
    Class is responsible for file iteration in directory
    """
    __dir = DirectoryDescriptor()

    def __init__(self, directory: str) -> None:
        """
        Set image directory and collection files inside it.
        :param directory:
        """
        self.__dir = directory
        self.__file_path_collection = os.listdir(self.__dir)
        self.__position = 0

    def __iter__(self):
        return self

    def __next__(self) -> list[Union[str, float]]:
        """
        Returns image metadata (file name, file format and size in KB)
        :return list[Union[str, float]]:
        """
        if self.__position > len(self.__file_path_collection) - 1:
            raise StopIteration
        image_path = f"{self.__dir}/{self.__file_path_collection[self.__position]}"
        with Image.open(image_path) as img:
            img_metadata = [img.filename, img.format, round(os.path.getsize(image_path) / 1024, 2)]
        self.__position += 1
        return img_metadata
