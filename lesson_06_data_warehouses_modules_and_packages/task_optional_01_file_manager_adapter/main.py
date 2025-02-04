from file_managers.csv_manager import CsvManager
from file_manager_adapter import FileManagerAdapter

# Adapter
file_adapter = FileManagerAdapter()

file_adapter.adapt_csv_to_json('book.csv')
file_adapter.adapt_json_to_csv('book.json')
file_adapter.convert_xml_to_json('book.xml')
