from typing import Any
from tree_node import Node
from binary_tree import binary_tree



def tree_includes_using_iteration(root: Node, target: Any):
    """ Implementation using depth first(iteratation)"""
    if not root or not isinstance(root, Node): return False
    stack = [ root ]
    while stack:
        current = stack.pop()
        if current.value == target: return True
        if current.right_child: stack.append(current.right_child)
        if current.left_child: stack.append(current.left_child)
    return False


def tree_includes_using_recursion(root, target):
  """Implementation using depth first(recursion)"""
  if not root: return False
  return root.value == target or \
          tree_includes_using_recursion(root.left_child, target) or \
          tree_includes_using_recursion(root.right_child, target)
  

print(tree_includes_using_iteration(binary_tree, -2))
print(tree_includes_using_iteration(binary_tree, 20))

print(tree_includes_using_iteration(binary_tree, -2))
print(tree_includes_using_iteration(binary_tree, 20))