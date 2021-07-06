from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.binary_tree.cls_binary_tree import cls_binary_tree


class Test_binary_tree:
    def test_tree(self):
        res = cls_binary_tree(1)
        res.insert(0)
        res.insert(3)
        assert res.print_tree_preorder() == [1, 0, 3]
