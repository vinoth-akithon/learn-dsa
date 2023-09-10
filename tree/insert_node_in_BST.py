"""
Insert a node in a BST

Given a BST and a key K. If K is not present in the BST,
Insert a new Node with a value equal to K into the BST. 
If K is already present in the BST, don't modify the BST.

Example1:

Input:
    2
   /   \   
  1     3

K = 4

Output: 1 2 3 4 (In order traversal)

Example 2:
Input:
        2
      /   \
     1     3
             \
              6
K = 4
Output: 1 2 3 4 6 (In order traversl)

hint:
returns the root of the modified BST after inserting K
"""


from tree_node import Node

def insert(root, Key):
    if root is None:
        return Node(Key)
    if Key < root.value:
        root.left_child = insert(root.left_child, Key)
    elif Key > root.value:
        root.right_child = insert(root.right_child, Key)
    return root    

def traversal_in_order(root):
    # Base condition
    if root:
        traversal_in_order(root.left_child)
        print(root.value, end=" ")
        traversal_in_order(root.right_child)

# Test Case 1
# root = insert(Node(2), 1)
# root = insert(root, 3)
# root = insert(root, 4)

# Test Case 2
# root = insert(Node(2), 1)
# root = insert(root, 3)
# root = insert(root, 6)
# root = insert(root, 4)


# traversal_in_order(root)


