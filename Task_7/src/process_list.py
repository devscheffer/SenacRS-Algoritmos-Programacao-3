import time
import os
from Task_7.src.create_report import cls_report

class cls_process_list:
	def __init__(
		self,
		path_input     : str       = "Task_7/data/input",
		path_output     : str       = "Task_7/data/output",
		lst_file_manual: list[str] = ["test"],
		execution      : str       = "auto"
	):
		self.path_input      = path_input
		self.path_output      = path_output
		self.lst_file_manual = lst_file_manual
		self.execution       = execution

	@property
	def path_input(self):
		return self._path_input

	@path_input.setter
	def path_input(self, value):
		self._path_input = value

	@property
	def path_output(self):
		return self._path_output

	@path_output.setter
	def path_output(self, value):
		self._path_output = value

	@property
	def lst_file_manual(self):
		return self._lst_file_manual

	@lst_file_manual.setter
	def lst_file_manual(self, value):
		self._lst_file_manual = value

	@property
	def execution(self):
		return self._execution

	@execution.setter
	def execution(self, value: str):
		lst_option = ["auto", "manual"]
		if value in (lst_option):
			self._execution = value
		else:
			raise ValueError("Opcao nao permitida para esse atributo")

	@property
	def lst_file_auto(self):
		return os.listdir(self.path_input)

	def mtd_start_process(self):
		lst_input = {
			"auto": self.lst_file_auto
			, "manual": self.lst_file_manual
			}

		for file_name in lst_input[self.execution]:
			start_time = time.time()
			lst_file_name = file_name.split('.')
			dict_file_name = {
				'name': lst_file_name[0]
				, 'extension': lst_file_name[1]
				}
			file_text = cls_report(
				file_name = dict_file_name['name'],
				path_rel_input=self.path_input,
				path_rel_output=self.path_output,
				extension= dict_file_name['extension']
				)
			file_text.mtd_create_report_file()
			end_time = time.time()
			exec_time = file_text.mtd_insert_execution_time_in_report(
				end_time - start_time
			)
			print(f'{dict_file_name["name"]} -> {exec_time}')
