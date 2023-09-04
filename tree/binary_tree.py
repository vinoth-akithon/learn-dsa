from typing import Any
from tree_node import Node



# Sample binary tree
#           a
#         /   \
#       b       c
#     /   \      \
#    d     e      f   




# binary_tree = Node("3")
# binary_tree.left_child = Node(")
# binary_tree.right_child = Node("c")
# binary_tree.left_child.left_child = Node("d")
# binary_tree.left_child.right_child = Node("e")
# binary_tree.right_child.right_child = Node("f")


binary_tree = Node(3)
binary_tree.left_child = Node(11)
binary_tree.right_child = Node(4)
binary_tree.left_child.left_child = Node(4)
binary_tree.left_child.right_child = Node(-2)
binary_tree.right_child.right_child = Node(1)