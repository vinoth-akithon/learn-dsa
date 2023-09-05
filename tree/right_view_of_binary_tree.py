"""
Right View of Binary Tree

Given a Binary Tree, find Right view of it. 
Right view of a Binary Tree is set of nodes 
visible when tree is viewed from right side.

          1
       /     \
     2        3
   /   \      /    \
  4     5   6    7
    \
     8
Right view of above tree is 1 3 7 8
"""


from tree_node import Node


def right_view_binary_tree(root: Node) -> list:
    result = []
    queue = [ root ]
    while queue:
        queue_lenth = len(queue)
        for i in range(queue_lenth):
            current = queue.pop(0)
            if i == 0 :
                result.append(current.value)

            if current.right_child: queue.append(current.right_child)
            if current.left_child: queue.append(current.left_child)

    return result

# Test Case 1
# binary_tree = Node(1)
# binary_tree.left_child = Node(2)
# binary_tree.right_child = Node(3)
# binary_tree.left_child.left_child = Node(4)
# binary_tree.left_child.right_child = Node(5)  
# binary_tree.right_child.left_child = Node(6)
# binary_tree.right_child.right_child = Node(7)
# binary_tree.left_child.left_child.right_child = Node(8)

# Test Case 2
binary_tree = Node(1)
binary_tree.left_child = Node(3)
binary_tree.right_child = Node(2)


# Test Case 3
binary_tree = Node(10)
binary_tree.left_child = Node(20)
binary_tree.right_child = Node(30)
binary_tree.left_child.left_child = Node(40)
binary_tree.left_child.right_child = Node(60)

print(right_view_binary_tree(binary_tree))