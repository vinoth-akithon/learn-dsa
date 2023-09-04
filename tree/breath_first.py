from tree_node import Node
from binary_tree import binary_tree

# Sample binary tree
#           a
#         /   \
#       b       c
#     /   \      \
#    d     e      f   


# Breath first traversal or level order traversal
# a -> b -> c -> d -> e -> f

def breath_first_search_using_iteration(root: Node):
    if not isinstance(root, Node): return []
    result = []
    queue = [ root ]
    while queue:
        current = queue.pop(0)
        result.append(current.value)
        if current.left_child: queue.append(current.left_child)
        if current.right_child: queue.append(current.right_child)
    return result


print(breath_first_search_using_iteration(binary_tree))