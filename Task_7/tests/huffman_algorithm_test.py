from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.huffman_algorithm import cls_huffman_algorithm


class Test_1_item:
    def test_binary_table_1_item(self):
        t5 = cls_huffman_algorithm("a")
        print(t5.text)
        binary_table = t5.mtd_create_binary_table()
        assert binary_table == {"a": {"binary_path": "0", "frequency": 1}}


class Test_init:
    def test_init_get(self):
        string = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
        res = cls_huffman_algorithm(string)
        assert res.text == string

    def test_init_set(self):
        string = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
        res = cls_huffman_algorithm(string)
        res.text = "ab"
        assert res.text == "ab"


class Test_dict_frequency:
    def test_dictionary(self):
        t1 = cls_huffman_algorithm("hello world")
        assert t1.mtd_create_frequency_table() == {
            "h": 1,
            "e": 1,
            "l": 3,
            "o": 2,
            " ": 1,
            "w": 1,
            "r": 1,
            "d": 1,
        }

    def test_dictionary_key(self):
        t2 = cls_huffman_algorithm("hello world")
        assert t2.mtd_create_frequency_table_list() == {
            1: [("h", 1), ("e", 1), (" ", 1), ("w", 1), ("r", 1), ("d", 1)],
            3: [("l", 3)],
            2: [("o", 2)],
        }

    def test_leaf_path(self):
        t3 = cls_huffman_algorithm(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
        )
        root_node = t3.mtd_create_huffman_binary_tree()
        bt = root_node
        assert bt.mtd_dct_leaf_path_Preorder() == {
            ("i", 12): [0, 0],
            ("s", 13): [0, 1],
            ("e", 15): [1, 0],
            ("u", 4): [1, 1, 0, 0],
            ("t", 1): [1, 1, 0, 1, 0],
            ("o", 3): [1, 1, 0, 1, 1],
            ("a", 10): [1, 1, 1],
        }

    def test_binary_table(self):
        t4 = cls_huffman_algorithm(
            "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
        )
        assert t4.mtd_create_binary_table() == {
            "i": {"binary_path": "00", "frequency": 12},
            "s": {"binary_path": "01", "frequency": 13},
            "e": {"binary_path": "10", "frequency": 15},
            "u": {"binary_path": "1100", "frequency": 4},
            "t": {"binary_path": "11010", "frequency": 1},
            "o": {"binary_path": "11011", "frequency": 3},
            "a": {"binary_path": "111", "frequency": 10},
        }


class Test_binary_table:
    def test_binary_table(self):
        res = cls_huffman_algorithm("hello world")
        answer = {
            " ": {"binary_path": "000", "frequency": 1},
            "w": {"binary_path": "001", "frequency": 1},
            "r": {"binary_path": "010", "frequency": 1},
            "d": {"binary_path": "011", "frequency": 1},
            "l": {"binary_path": "10", "frequency": 3},
            "o": {"binary_path": "110", "frequency": 2},
            "h": {"binary_path": "1110", "frequency": 1},
            "e": {"binary_path": "1111", "frequency": 1},
        }
        for k, v in res.mtd_create_binary_table().items():
            assert v == answer[k]

    def test_string_to_binary(self):
        res = cls_huffman_algorithm("a")
        assert res.mtd_string_to_binary_normal()["binary"] == "01100001"

    def test_string_huffman_binary(self):
        res = cls_huffman_algorithm("abb")
        assert (res.mtd_string_to_binary_huffman())["binary"] == "011"

    def test_compression(self):
        res = cls_huffman_algorithm("abb")
        assert (res.mtd_string_to_binary_normal()) == {
            "binary": "011000010110001001100010",
            "size": 24,
        }
        assert (res.mtd_string_to_binary_huffman()) == {"binary": "011", "size": 3}
        assert (res.mtd_compression()) == "12.5 %"
