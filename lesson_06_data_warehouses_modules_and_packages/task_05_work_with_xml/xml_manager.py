import os
from typing import Generator, Any
import xml.etree.ElementTree as ET

from exceptions.file_extension_error import FileExtensionError
from exceptions.insufficient_product_count_exception import InsufficientProductCountException


class XMLManager:
    """
    Class manages work with XML
    """
    __ALLOWED_EXTENSIONS = '.xml'

    @classmethod
    def read_file(cls, xml_file_path: str) -> Generator[list[str], Any, None]:
        """
        Read XML file
        :param xml_file_path:
        :return:
        :raise (FileExtensionError, FileNotFoundError)
        """
        try:
            cls.__validate_file_extension(xml_file_path)
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for product in root.findall('product'):
                yield {product.find('name').text: int(product.find('quantity').text)}
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {xml_file_path}")

    @classmethod
    def decrease_product_count(cls, xml_file_path: str, product_name: str, count: int) -> None:
        """
        Remove product count from xml file
        :param xml_file_path:
        :param product_name:
        :param count:
        :return:
        :raise InsufficientProductCountException
        """
        try:
            cls.__validate_file_extension(xml_file_path)
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for product in root.findall('product'):
                if product.find('name').text == product_name:
                    updated_quantity = int(product.find('quantity').text) - count
                    if updated_quantity < 0:
                        raise InsufficientProductCountException(
                            f"Product {product_name} has only {product.find('quantity').text} items, but {count} requested.")
                    product.find('quantity').text = str(updated_quantity)
            tree.write(xml_file_path)
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {xml_file_path}")

    @classmethod
    def increase_product_count(cls, xml_file_path: str, product_name: str, count: int) -> None:
        """
        Add products count to xml file
        :param xml_file_path:
        :param product_name:
        :param count:
        :return:
        :raise InsufficientProductCountException
        """
        try:
            cls.__validate_file_extension(xml_file_path)
            tree = ET.parse(xml_file_path)
            root = tree.getroot()
            for product in root.findall('product'):
                if product.find('name').text == product_name:
                    updated_quantity = int(product.find('quantity').text) + count
                    product.find('quantity').text = str(updated_quantity)
            tree.write(xml_file_path)
        except FileExtensionError as error:
            print(error)
        except FileNotFoundError:
            print(f"File not found: {xml_file_path}")

    @classmethod
    def __validate_file_extension(cls, file_path: str) -> None:
        """
        Validate if file has
        :param file_path:
        :return:
        """
        file_extension = os.path.splitext(file_path)[1]
        if file_extension not in cls.__ALLOWED_EXTENSIONS:
            raise FileExtensionError(f"File {file_path} has not compatible extension: {file_extension}")
