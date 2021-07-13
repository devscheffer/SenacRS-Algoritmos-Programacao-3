import os
import os.path
from sys import path

cwd = os.getcwd()
path.append(cwd)
from Task_7.src.create_huffman_algorithm import cls_huffman_algorithm
import json

class cls_report:
	def __init__(
		self,
		file_name:str,
		path_rel_input:str="Task_7/data/input",
		path_rel_output:str="Task_7/data/output",
		extension:str="txt"
	):
		self._file_name = file_name
		self._path_input = f"{os.getcwd()}/{path_rel_input}"
		self._path_output = f"{os.getcwd()}/{path_rel_output}"
		self._extension = extension

	@property
	def file_name(self):
		return self._file_name

	@property
	def path_input(self):
		return self._path_input

	@property
	def path_output(self):
		return self._path_output

	@property
	def extension(self):
		return self._extension

	@property
	def report_data(self):
		return cls_huffman_algorithm(self.mtd_read_file())

	def mtd_read_file(self) -> str:
		try:
			with open(
				f"{self.path_input}/{self.file_name}.{self.extension}"
				, mode="r"
				,encoding="utf-8"
			) as file:
				list_lines = file.readlines()
				return "".join(list_lines)
		except FileNotFoundError:
			return "File not found"

	def mtd_create_directory(self) -> str:
		directory = f"{self.path_output}/report-{self.file_name}"
		if not os.path.exists(directory):
			os.mkdir(directory)
		return directory

	def __mtd_create_report_json(
		self
		, directory: str
		, report_name: str
		, report_data: dict
	) -> None:
		with open(f"{directory}/{report_name}.json", mode="w") as file:
			json.dump(report_data, file, ensure_ascii=False)

	def mtd_create_report_file(self) -> None:
		report = self.report_data
		dct_report = {
			"1_table_frequency": report.mtd_create_table_frequency(),
			"2_table_freq_list": report.mtd_create_table_frequency_list(),
			"3_table_binary": report.mtd_create_binary_table(),
			"4_1_binary_string": {
				"binary_string_normal_size": report.mtd_string_to_binary_normal()["size"],
				"binary_string_huffman_size": report.mtd_string_to_binary_huffman()["size"],
				"compression": report.mtd_compression(),
			},
			"4_2_binary_string_normal_full": report.mtd_string_to_binary_normal(),
			"4_3_binary_string_huffman_full": report.mtd_string_to_binary_huffman()
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


