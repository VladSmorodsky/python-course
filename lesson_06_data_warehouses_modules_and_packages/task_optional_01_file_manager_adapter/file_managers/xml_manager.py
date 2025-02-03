import os
from typing import Generator, Any
import xml.etree.ElementTree as ET
from xml.dom.minidom import Element

from exceptions.file_extension_error import FileExtensionError


class XmlManager:
    """
    Class manages XML files
    """
    __ALLOWED_EXTENSIONS = '.xml'

    def read_file_xml(self, xml_file_path: str) -> Generator[Element, Any, None]:
        """
        Read XML file
        :param xml_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            self.__validate_file_extension(xml_file_path)
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for child in root:
                yield {child}
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {xml_file_path}")

    def __validate_file_extension(self, file_path: str) -> None:
        """
        Validate if file has
        :param file_path:
        :return:
        """
        file_extension = os.path.splitext(file_path)[1]
        if file_extension not in self.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {file_path} has not compatible extension: {file_extension}")
