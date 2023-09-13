"""
Binary Tree to BST

Given a Binary Tree, convert it to Binary Search Tree 
in such a way that keeps the original structure of Binary Tree intact.

Example 1:
-----------
Input:
      1
    /   \
   2     3
Output: 
1 2 3
Explanation:
The converted BST will be 
      2
    /   \
   1     3


Example 2:
------------
Input:
          1
       /    \
     2       3
   /        
 4       
Output: 
1 2 3 4
Explanation:
The converted BST will be

        3
      /   \
    2     4
  /
 1
"""

from typing import Self

class Node:
    def __init__(self, value:int, left_child: Self|None = None, right_child:Self|None = None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return f"Node={self.value}"
    
    def __repr__(self) -> str:
        return f"Node={self.value}"
    
# Test Case 1
bst = Node(1)
bst.left_child = Node(2)
bst.right_child = Node(3)


# Test Case 2
# bst = Node(3)
# bst.left_child = Node(2)
# bst.right_child = Node(4)
# bst.left_child.left_child = Node(1)

def traverse(root: Node, array: list) -> None:
    if root:
        traverse(root.left_child, array)
        array.append(root.value)
        traverse(root.right_child, array)

def build_tree(array):
    if not array: return
    middle = len(array)//2
    root = Node(array[middle])
    root.left_child = build_tree(array[0: middle])
    root.right_child = build_tree(array[middle+1:])
    return root

def convert_bt_to_bst(root: Node):
    array = []
    traverse(root, array)
    print(array)
    array.sort()
    return build_tree(array)
    
    

lst =[]
traverse(convert_bt_to_bst(bst), lst)
print(lst)