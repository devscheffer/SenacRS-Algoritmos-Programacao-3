from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.node import cls_node


class cls_huffman_algorithm:
    # --> Contructor
    def __init__(self, inpt_text: str):
        self.__text = inpt_text

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text: str):
        self.__text = text

    # --> Method Private

    def __get_element_value(self, element) -> int:
        if isinstance(element, tuple):
            element_value = element[1]
        else:
            element_value = element.data
        return element_value

    def __get_item(self, dct_aux: dict) -> tuple:
        lst_key = list(dct_aux.keys())
        lst_key_sorted = sorted(lst_key)
        item = dct_aux[lst_key_sorted[0]].pop(0)
        if dct_aux[lst_key_sorted[0]] == []:
            dct_aux.pop(lst_key_sorted[0])
            lst_key_sorted.pop(0)
        return dct_aux, item

    def __create_binary_tree(self, pair: list, total: int) -> cls_node:
        binary_tree = cls_node(total)
        for i in range(len(pair)):
            element = pair.pop(0)
            binary_tree.mtd_insert(element)
        return binary_tree

    def __create_pair(self, dct_aux: dict) -> tuple:
        pair = []
        total = 0
        while len(pair) < 2 and dct_aux != {}:
            dct_aux, item = self.__get_item(dct_aux)
            pair.append(item)
            total += self.__get_element_value(item)
        return dct_aux, pair, total

    def __insert_tree_in_dict(self, binary_tree: cls_node, dct_aux: dict) -> dict:
        dct_aux_v2 = dct_aux
        if binary_tree.data in dct_aux:
            dct_aux_v2[binary_tree.data].append(binary_tree)
        else:
            dct_aux_v2[binary_tree.data] = [binary_tree]
        return dct_aux_v2

    # --> Method Public
    def mtd_create_frequency_table_list(self) -> dict:
        dct_frequency = {}
        for k, v in self.mtd_create_frequency_table().items():
            if v in dct_frequency:
                dct_frequency[v].append((k, v))
            else:
                dct_frequency[v] = [(k, v)]
        return dct_frequency

    def mtd_create_frequency_table(self) -> dict:
        frequency = {}
        for letter in self.text:
            if letter in frequency:
                frequency[letter] += 1
            else:
                frequency[letter] = 1
        return frequency

    def mtd_create_huffman_binary_tree(self) -> cls_node:
        dct_aux = self.mtd_create_frequency_table_list()
        while dct_aux != {}:
            dct_aux, pair, total = self.__create_pair(dct_aux)
            binary_tree = self.__create_binary_tree(pair, total)
            dct_aux = self.__insert_tree_in_dict(binary_tree, dct_aux)
            if len(dct_aux.keys()) == 1 and len(dct_aux[list(dct_aux.keys())[0]]) == 1:
                return dct_aux[list(dct_aux.keys())[0]][0]

    def mtd_create_binary_table(self) -> dict:
        root_node = self.mtd_create_huffman_binary_tree()
        dct_aux = root_node.mtd_dct_leaf_path_Preorder()
        dct_aux_v2 = {}
        for i in dct_aux:
            lst_binary = list(map(str, (dct_aux[i])))
            new_binary = "".join(lst_binary)
            element = i[0]
            frequency = i[1]
            dct_aux_v2[element] = {"binary_path": new_binary, "frequency": frequency}
        return dct_aux_v2

    def mtd_string_to_binary_normal(self) -> dict:
        lst_binary = []
        for i in bytes(self.text, "UTF-8"):
            lst_binary.append(f"{i:08b}")
        binary = "".join(lst_binary)
        res = {"binary": binary, "size": len(str(binary)), "binary_lst": lst_binary}
        return res

    def mtd_string_to_binary_huffman(self) -> dict:
        dct_aux = self.mtd_create_binary_table()
        lst_binary = []
        for i in self.text:
            element = dct_aux[i]["binary_path"]
            lst_binary.append(element)
        binary = "".join(lst_binary)
        res = {"binary": binary, "size": len(str(binary)), "binary_lst": lst_binary}
        return res

    def mtd_compression(self) -> str:
        normal = self.mtd_string_to_binary_normal()["size"]
        huffman = self.mtd_string_to_binary_huffman()["size"]
        ratio = huffman / normal
        return f"{ratio*100:.1f} %"
