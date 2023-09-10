"""
Kth largest element in BST

Given a Binary Search Tree. 
Your task is to complete the function which will return 
the Kth largest element without doing any modification in Binary Search Tree.

Example 1:

Input:
      4
    /   \
   2     9
k = 2 
Output: 4

Example 2:

Input:
    9
     \ 
      10
K = 1
Output: 10
"""

from heap_using_array import Heap

class Node:
    def __init__(self, value, left_child=None, right_child=None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return f"Node={self.value}"
    
    def __repr__(self) -> str:
        return f"Node={self.value}"


def insert(root, Key):
    if root is None:
        return Node(Key)
    if Key < root.value:
        root.left_child = insert(root.left_child, Key)
    elif Key > root.value:
        root.right_child = insert(root.right_child, Key)
    return root 


def kth_largest_in_bst(root: Node, k:int) -> int:
    heap = Heap()
    def traversal_in_order(root):
        # Base condition
        if root:
            traversal_in_order(root.left_child)
            heap.insert(root.value)
            traversal_in_order(root.right_child)
    traversal_in_order(root)

    for _ in range(k-1):
        heap.remove()

    return heap.max()


# Test Case 1
# root = insert(Node(4), 2)
# root = insert(root, 9)
# print(kth_largest_in_bst(root, 2))


# Test Case 2
root = insert(Node(9), 10)
print(kth_largest_in_bst(root, 1))