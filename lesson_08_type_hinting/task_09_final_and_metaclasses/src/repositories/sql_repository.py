from typing import Dict, Any

from lesson_08_type_hinting.task_09_final_and_metaclasses.src.repositories.base_repository import BaseRepository


class SQLRepository(BaseRepository):
    """
    Represents base repository implementation
    """

    def save(self, data: Dict[str, Any]) -> None:
        """
        Method represents insert SQL query
        :param data:
        :return:
        """
        data_keys: str = ''
        data_values: str = ''
        for item_index, item in enumerate(data):
            data_keys += item
            data_values += str(data[item])
            if item_index != len(data) - 1:
                data_keys += ', '
                data_values += ', '

        print(f"INSERT INTO {self.config['database_name']}.{self.config['product_table_name']} ({data_keys}) "
              f"VALUES ({data_values});")
