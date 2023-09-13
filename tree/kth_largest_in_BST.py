"""
Kth largest element in BST

Given a Binary Search Tree. 
Your task is to complete the function which will
return the Kth largest element without doing 
any modification in Binary Search Tree.

Example 1:
------------
Input:
      4
    /   \
   2     9
k = 2 
Output: 4

Example 2:
---------------
Input:
       9
        \ 
          10
K = 1
Output: 10
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
    
# bst = Node(4)
# bst.left_child = Node(2)
# bst.right_child = Node(9)

bst = Node(9)
bst.right_child = Node(10)


def kth_largest(root: Node, k: int):
    def traverse(root: Node, array: list) -> None:
        if root:
            traverse(root.right_child, array)
            array.append(root.value)
            traverse(root.left_child, array)
    array = []
    traverse(root, array)
    return array[k-1]

print(kth_largest(bst, 1))

        