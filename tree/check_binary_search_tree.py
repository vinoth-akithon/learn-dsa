from tree_node import Node
from binary_tree import binary_tree
from binary_search_tree import BinarySearchTree


def is_this_binary_search_tree(root: Node, min_value, max_value) -> bool:
    if not isinstance(root, Node): return True
    elif root.value < min_value or  root.value > max_value: return False
    return (is_this_binary_search_tree(root.left_child, min_value, root.value - 1) and 
            is_this_binary_search_tree(root.right_child, root.value + 1, max_value))



print(is_this_binary_search_tree(binary_tree, float("-inf"), float("inf")))


binary_tree = BinarySearchTree()
binary_tree.insert(7)
binary_tree.insert(4)
binary_tree.insert(9)
binary_tree.insert(1)
binary_tree.insert(6)
binary_tree.insert(10)
binary_tree.insert(8)
print(is_this_binary_search_tree(binary_tree.root, float("-inf"), float("inf")))





