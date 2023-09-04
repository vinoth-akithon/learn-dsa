from tree_node import Node
from binary_tree import binary_tree

# Sample binary tree
#           a
#         /   \
#       b       c
#     /   \      \
#    d     e      f   

# Depth first traveral   
# Pre order traversal --> a -> b -> d -> e -> c -> f
# In order traversal --> d -> b -> e -> a -> c -> f
# Post order traversal --> d -> e -> b -> f -> c -> a


def depth_first_search_using_iteration(root: Node) -> list:
    if not root or not isinstance(root, Node): return []
    result = []
    stack = [ root ]
    while stack:
        current = stack.pop()
        result.append(current.value)
        if current.right_child: stack.append(current.right_child)
        if current.left_child: stack.append(current.left_child)

    return result



def depth_first_search_using_recursion(root: Node) -> list:
    if not isinstance(root, Node): return []

    left_tree = depth_first_search_using_recursion(root.left_child)
    right_tree = depth_first_search_using_recursion(root.right_child)
    return [ root.value, *left_tree, *right_tree ] # Pre order traversal
    # return [ *left_tree, root.value, *right_tree ] # In order traversal
    # return [ *left_tree, *right_tree,  root.value ] # Post order traversal


# print(depth_first_search_using_iteration(binary_tree))
# print(depth_first_search_using_recursion(binary_tree))