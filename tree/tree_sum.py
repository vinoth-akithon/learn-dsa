from tree_node import Node
from binary_tree import binary_tree


def tree_sum_using_iteration_depth(root: Node):
    """Implementation using depth first(iteration)"""
    if not isinstance(root, Node): return 0
    result = 0
    stack = [ root ]
    while stack:
        current = stack.pop()
        result += current.value
        if current.left_child: stack.append(current.left_child)
        if current.right_child: stack.append(current.right_child)
    return result


def tree_sum_using_iteration_breath(root: Node):
    """Implementation using breath first(iteration)"""
    if not isinstance(root, Node): return 0
    result, queue = 0, [ root ]
    while queue:
        current = queue.pop(0)
        result += current.value
        if current.left_child: queue.append(current.left_child)
        if current.right_child: queue.append(current.right_child)
    return result


def tree_sum_using_recursion(root: Node):
    """Implementation using depth first(recursion)"""
    if not root: return 0
    return root.value + tree_sum_using_recursion(root.left_child) + tree_sum_using_recursion(root.right_child)


print(tree_sum_using_iteration_depth(binary_tree))
print(tree_sum_using_iteration_breath(binary_tree))
print(tree_sum_using_recursion(binary_tree))
