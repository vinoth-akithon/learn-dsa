"""
AVL Tree Implementation
"""

from typing import Self

class Node:
    """AVL Tree Node"""
    def __init__(self, value, left_child: Self|None=None, right_child:Self|None=None) -> None:
         self.value = value
         self.left_child = left_child
         self.right_child = right_child
         self.height = 0

    def __repr__(self):
        return f"Node={self.value}"


class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def __height(self, node) -> int:
        return -1 if node is None else node.height
    
    def __balance_factor(self, root: Node| None) -> int:
        return 0 if root is None else \
            (self.__height(root.left_child) - self.__height(root.right_child))
    
    def __is_left_heavy(self, balance_factor: int) -> bool:
        return balance_factor > 1

    def __is_right_heavy(self, balance_factor: int) -> bool:
        return balance_factor < -1
    
    def __rotate_left(self, root: Node) -> Node:
        new_root = root.right_child
        root.right_child = new_root.left_child
        new_root.left_child = root
        
        # setting up height
        self.__set_height(root)
        self.__set_height(new_root)
        return new_root
    

    def __rotate_right(self, root: Node) -> Node:
        new_root = root.left_child
        root.left_child = new_root.right_child
        new_root.right_child = root
        
        # setting up height
        self.__set_height(root)
        self.__set_height(new_root)
        return new_root

    def __set_height(self, node: Node) -> None:
        node.height = 1 + max(self.__height(node.left_child),
                              self.__height(node.right_child))
    
    def __balance(self, root: Node) -> Node: 
        balance_factor = self.__balance_factor(root)
        if self.__is_left_heavy(balance_factor):
            if self.__balance_factor(root.left_child) < 0:
                root.left_child = self.__rotate_left(root.left_child)
            return self.__rotate_right(root)
        elif self.__is_right_heavy(balance_factor):
            if self.__balance_factor(root.right_child) > 0:
                root.right_child = self.__rotate_right(root.right_child)
            return self.__rotate_left(root)
        else:
            return root


    def __insert(self, root: Node | None, value:int) -> Node:
        """Insertion operation using recursion."""
        # Base condition
        if root is None:
            return Node(value)
        
        # recursion
        if value < root.value:
            root.left_child = self.__insert(root.left_child, value)
        else:
            root.right_child = self.__insert(root.right_child, value)
        
        # updating height of the parent nodes
        self.__set_height(root)

        # balancing
        return self.__balance(root)

    def insert(self, value):
        self.root = self.__insert(self.root, value)


avl_tree = AVLTree()

# LL rotate
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)

# RL rotate
# avl_tree.insert(10)
# avl_tree.insert(30)
# avl_tree.insert(20)

# RR rotate
# avl_tree.insert(30)
# avl_tree.insert(20)
# avl_tree.insert(10)

# LR rotate
# avl_tree.insert(30)
# avl_tree.insert(10)
# avl_tree.insert(20)

print("pass")
