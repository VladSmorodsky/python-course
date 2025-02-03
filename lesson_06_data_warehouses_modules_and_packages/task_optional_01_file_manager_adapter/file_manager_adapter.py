import os
from typing import Any
from xml.etree.ElementTree import ElementTree, Element

from file_managers.csv_manager import CsvManager
from file_managers.json_manager import JsonManager
from file_managers.xml_manager import XmlManager


class FileManagerAdapter(CsvManager, JsonManager, XmlManager):
    """
    Class is responsible for adapting different file managers
    """

    def adapt_csv_to_json(self, csv_file_path: str) -> None:
        """
        Transform CSV file to JSON
        :param csv_file_path:
        :return:
        """
        data_for_json = []
        file_data = self.read_csv_file(csv_file_path)
        header = next(file_data)
        for row in file_data:
            json_data = {}
            for index, header_value in enumerate(header):
                json_data[header_value] = row[index]
            data_for_json.append(json_data)
        self.write_json_file(f"{os.path.splitext(csv_file_path)[0]}.json", data_for_json)

    def adapt_json_to_csv(self, json_file_path: str) -> None:
        """
        Transform JSON file to CSV
        :param json_file_path:
        :return:
        """
        data_for_csv = []
        for index, json_item in enumerate(self.read_json_file(json_file_path)):
            csv_header = []
            csv_item_data = []
            for item_index, item_key in enumerate(json_item):
                if index == 0:
                    csv_header.append(item_key)

                    if item_index == len(json_item) - 1:
                        data_for_csv.append(csv_header)
                csv_item_data.append(json_item[item_key])
            data_for_csv.append(csv_item_data)
        self.write_csv_file(f"{os.path.splitext(json_file_path)[0]}.csv", data_for_csv)

    def convert_xml_to_json(self, file_xml_path: str) -> None:
        """
        Transforms XML file to JSON
        :param file_xml_path:
        :return:
        """
        data_for_json = []
        for xml_item in self.read_file_xml(file_xml_path):
            xml_item_traversed_data = self.__traverce_xml(xml_item)
            data_for_json.append(xml_item_traversed_data)
        self.write_json_file(f"{os.path.splitext(file_xml_path)[0]}_from_xml.json", data_for_json)

    def __traverce_xml(self, element: Element) -> dict[Any, dict[Any, dict[ElementTree]]] | None | Any:
        """
        Travers whole element tree
        :param element:
        :return:
        """
        if len(element) == 0:
            return element.text.strip() if element.text else None
        element_dictionary = {}
        for child in element:
            element_dictionary[child.tag] = self.__traverce_xml(child)
        return element_dictionary
