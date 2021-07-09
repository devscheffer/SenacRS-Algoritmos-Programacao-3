
from os import getcwd,listdir
from sys import path

from numpy import str0

cwd = getcwd()
path.append(cwd)
import time
from Task_7.components.file_read import cls_report


class cls_process_list:
    def __init__(self
        ,path_input:str="Task_7/data/input"
        ,lst_file_manual:list[str]=['test']
        ,execution:str='auto'
        ):
        self.__path_input=path_input
        self.__lst_file_manual=lst_file_manual
        self.__execution=execution

    @property
    def path_input(self):
        return self.__path_input
    @property
    def lst_file_manual(self):
        return self.__lst_file_manual

    @property
    def execution(self):
        return self.__execution
    @execution.setter
    def execution(self, value:str):
        lst_option = ['auto','manual']
        if value in (lst_option):
            self.__execution = value
        else:
            raise ValueError("Opcao nao permitida para esse atributo")



    def mtd_start_process(self):
        lst_file_auto = list(map(lambda x: x.split(".")[0], listdir(self.path_input)))
        print(lst_file_auto)

        lst_input = {
            "auto": lst_file_auto
            ,"manual": self.lst_file_manual
        }

        for file_name in lst_input[self.execution]:
            start_time = time.time()
            file_text = cls_report(file_name, path_rel_input=self.path_input)
            file_text.mtd_create_report_file()
            end_time = time.time()
            exec_time=file_text.mtd_insert_execution_time_in_report(end_time-start_time)
            print(exec_time)

