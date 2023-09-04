from tree_node import Node
from binary_tree import binary_tree

def max_path_sum_using_recursion(root: Node):
    if root is None: return float("-inf")
    if root.left_child is None and root.right_child is None: 
        return root.value
    return root.value + max(max_path_sum_using_recursion(root.left_child), \
                            max_path_sum_using_recursion(root.right_child))

print(max_path_sum_using_recursion(binary_tree))