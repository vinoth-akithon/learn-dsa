from tree_node import Node
from binary_tree import binary_tree


def tree_min_value_using_iteration_depth(root: Node):
    """Implementation using depth first(iteration)"""
    if not isinstance(root, Node): 
        raise ValueError("binary tree object is required")
    result = root.value
    stack = [ root ]
    while stack:
        current = stack.pop()
        if current.value < result:
            result = current.value
        if current.left_child: stack.append(current.left_child)
        if current.right_child: stack.append(current.right_child)
    return result


def tree_min_value_using_iteration_breath(root: Node):
    """Implementation using breath first(iteration)"""
    if not isinstance(root, Node): 
        raise ValueError("binary tree object is required")
    result = root.value
    queue = [ root ]
    while queue:
        current = queue.pop(0)
        if current.value < result:
            result = current.value

        if current.left_child: queue.append(current.left_child)
        if current.right_child: queue.append(current.right_child)
    return result


def tree_min_value_using_recursion(root: Node):
    """Implementation using depth first(recursion)"""
    if root is None: return float("inf")
    # if root.left_child is None and root.right_child is None: return root.value
    return min(root.value, min(tree_min_value_using_recursion(root.left_child), \
                                tree_min_value_using_recursion(root.right_child)))


print(tree_min_value_using_iteration_depth(binary_tree))
print(tree_min_value_using_iteration_breath(binary_tree))
print(tree_min_value_using_recursion(binary_tree))
