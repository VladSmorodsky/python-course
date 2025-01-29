import csv
from typing import Iterable


def write_csv(csv_file_path: str, data: Iterable):
    """
    Writes content into csv file
    :param csv_file_path:
    :param data:
    :return:
    """
    with open(csv_file_path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for data_row in data:
            writer.writerow(data_row)
