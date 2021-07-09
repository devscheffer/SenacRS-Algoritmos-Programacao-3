from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.node import cls_node


class Test_binary_tree:
    def test_tree(self):
        res = cls_node(1)
        res.mtd_insert(1)
        res.mtd_insert(2)
        assert (res.left.data) == 1
