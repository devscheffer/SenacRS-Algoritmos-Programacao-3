from Task_7.src.create_node import cls_node


def fn_create_binary_subtree( pair: list, total: int) -> cls_node:
	binary_tree = cls_node(total)
	for i in range(len(pair)):
		element = pair.pop(0)
		binary_tree.mtd_insert(element)
	return binary_tree
