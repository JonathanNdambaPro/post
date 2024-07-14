import csv
import json
from pathlib import Path
from typing import Dict, List, Protocol, Union

import openpyxl


class CSVReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_csv(self) -> List[Dict[str, str]]:
        with open(self.filename, "r") as file:
            csv_reader = csv.DictReader(file)
            return list(csv_reader)


class ExcelReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_excel(self) -> List[Dict[str, str]]:
        workbook = openpyxl.load_workbook(self.filename)
        sheet = workbook.active
        data = []
        headers = [cell.value for cell in sheet[1]]
        for row in sheet.iter_rows(min_row=2, values_only=True):
            data.append(dict(zip(headers, row)))
        return data


class JSONReader:
    def __init__(self, filename: str):
        self.filename = filename

    def read_json(self) -> List[Dict[str, str]]:
        with open(self.filename, "r") as file:
            return json.load(file)


class DataReader(Protocol):
    def read_data(self) -> List[Dict[str, str]]: ...


class CSVAdapter:
    def __init__(self, reader: CSVReader):
        self.reader = reader

    def read_data(self) -> List[Dict[str, str]]:
        return self.reader.read_csv()


class ExcelAdapter:
    def __init__(self, reader: ExcelReader):
        self.reader = reader

    def read_data(self) -> List[Dict[str, str]]:
        return self.reader.read_excel()


class JSONAdapter:
    def __init__(self, reader: JSONReader):
        self.reader = reader

    def read_data(self) -> List[Dict[str, str]]:
        return self.reader.read_json()


if __name__ == "__main__":
    dict_strategy_reader: dict[str, Union[CSVReader, ExcelReader, JSONReader]] = {
        ".csv": CSVReader,
        ".xls": ExcelReader,
        ".json": JSONReader,
    }

    dict_strategy_adapter: dict[str, DataReader] = {
        ".csv": CSVAdapter,
        ".xls": ExcelAdapter,
        ".json": JSONAdapter,
    }

    path_to_file = Path("some_file.csv").resolve()

    reader_instance = dict_strategy_reader[path_to_file.suffix](path_to_file)
    adapter_instance = dict_strategy_adapter[path_to_file.suffix](reader_instance)

    adapter_instance.read_data()
