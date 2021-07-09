import os
import os.path
from sys import path

cwd = os.getcwd()
path.append(cwd)
from Task_7.components.huffman_algorithm import cls_huffman_algorithm
import json
import time

class cls_report:
    def __init__(
        self,
        file_name,
        path_rel_input="Task_7/data/input",
        path_rel_output="Task_7/data/output",
        extension="txt"
    ):
        self.__file_name = file_name
        self.__path_input = f"{os.getcwd()}/{path_rel_input}"
        self.__path_output = f"{os.getcwd()}/{path_rel_output}"
        self.__extension = extension

    @property
    def file_name(self):
        return self.__file_name

    @property
    def path_input(self):
        return self.__path_input

    @property
    def path_output(self):
        return self.__path_output

    @property
    def extension(self):
        return self.__extension

    @property
    def report_data(self):
        return cls_huffman_algorithm(self.mtd_read_file())

    def mtd_read_file(self) -> str:
        try:
            with open(
                f"{self.path_input}/{self.file_name}.{self.extension}", mode="r",encoding="utf-8"
            ) as file:
                f = file.readlines()
                return "".join(f)
        except FileNotFoundError:
            return "File not found"

    def mtd_create_directory(self) -> str:
        directory = f"{self.path_output}/report-{self.file_name}"
        if not os.path.exists(directory):
            os.mkdir(directory)
        return directory

    def __mtd_create_report_json(
        self, directory: str, report_name: str, report_data: dict
    ) -> None:
        with open(f"{directory}/{report_name}.json", mode="w") as file:
            json.dump(report_data, file, ensure_ascii=False)

    def mtd_create_report_file(self) -> None:
        report = self.report_data
        dct_report = {
            "1_table_frequency": report.mtd_create_frequency_table(),
            "2_table_freq_list": report.mtd_create_frequency_table_list(),
            "3_table_binary": report.mtd_create_binary_table(),
            "4_1_binary_string": {
                "binary_string_normal_size": report.mtd_string_to_binary_normal()["size"],
                "binary_string_huffman_size": report.mtd_string_to_binary_huffman()["size"],
                "compression": report.mtd_compression(),
            },
            "4_2_binary_string_detail": {
                "binary_string_normal": report.mtd_string_to_binary_normal(),
                "binary_string_huffman": report.mtd_string_to_binary_huffman(),
                "compression": report.mtd_compression(),
            },
        }
        directory = self.mtd_create_directory()
        for i in dct_report:
            report_name = i
            report_data = dct_report[i]
            self.__mtd_create_report_json(directory, report_name, report_data)

    def mtd_insert_execution_time_in_report(self,duration:float):
        directory = self.mtd_create_directory()
        report_name = '4_1_binary_string'
        with open(f'{directory}/{report_name}.json',mode='r') as file:
            report_data=json.load(file)
            key_new={"Execution_time(s)": round(duration,2)}
            report_data.update(key_new)
        self.__mtd_create_report_json(directory, report_name, report_data)
        return key_new


