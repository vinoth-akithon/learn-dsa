"""
Leftmost and rightmost nodes of binary tree

Given a Binary Tree of size N, Print the corner nodes 
ie- the node at the leftmost and rightmost of each level.

Example 1:               
-----------------
Input:   1                   
       /  \
     2      3
    / \    / \
   4   5  6   7  

Output: 1 2 3 4 7

Example 2:
-------------------
Input:  10
      /    \
     5     20
    / \  
   2  8

Output: 10 5 20 2 8


"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"Node={self.val}"

def printCornerNodes(root):
    if not root:
        return
    queue = [ root ]
    while queue:
        # Get the size of the current level
        level_size = len(queue)

        for i in range(level_size):
            node = queue.pop(0)

            if i == 0:
                print(node.val, end=" ")
            if level_size > 1:
                if i == level_size - 1:
                    print(node.val, end=" ")

            if node.left: queue.append(node.left)
            if node.right:queue.append(node.right)

# Example usage:
# Construct a binary tree
root = TreeNode("a")
root.left = TreeNode("b")
root.right = TreeNode("c")
root.left.left = TreeNode("d")
root.left.right = TreeNode("e")
root.right.right = TreeNode("f")

# Call the function to print corner nodes
printCornerNodes(root)
