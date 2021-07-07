from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.binary_tree.cls_node import cls_node


class Test_binary_tree:
    def test_tree(self):

