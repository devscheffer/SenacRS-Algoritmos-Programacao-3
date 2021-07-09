from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.process_list import cls_process_list


path_input = "Task_7/data/input"
lst_file_manual = ["test"]

report = cls_process_list(path_input, lst_file_manual,execution='manual')
report.mtd_start_process()
