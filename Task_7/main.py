from os import getcwd, listdir
from sys import path
import time
cwd = getcwd()
path.append(cwd)
from Task_7.components.file_read import cls_report


path_input = "Task_7/data/input"
lst_file_input = list(map(lambda x: x.split(".")[0], listdir(path_input)))
print(lst_file_input)

lst_file = ["test"]

for file_name in lst_file_input:
    start_time = time.time()
    file_text = cls_report(file_name, path_rel_input=path_input)
    file_text.mtd_create_report()
    end_time = time.time()
    print(f'{file_name}: {end_time-start_time} s')
