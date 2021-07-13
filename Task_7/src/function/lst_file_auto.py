import os
def fn_list_file_auto(path_input:str)->list:
	files_in_dir = os.listdir(path_input)
	return files_in_dir
