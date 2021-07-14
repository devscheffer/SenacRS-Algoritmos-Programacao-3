from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)

from Task_7.src.process_list import cls_process_list


path_input = "Task_7/data/input"
path_output = "Task_7/data/output"
lst_file_manual = ["test.txt"]

report = cls_process_list(
	path_input      = path_input
	, path_output      = path_output
	, lst_file_manual = lst_file_manual
	, execution       = 'manual'
	)
print(report.lst_file_auto)
report.mtd_start_process()
