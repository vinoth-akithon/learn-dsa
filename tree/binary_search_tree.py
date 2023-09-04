
from typing import Self
from tree_node import Node


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return
        
        current_node = self.root
        while current_node:
            if value < current_node.value:
                if current_node.left_child is None:
                    current_node.left_child = new_node
                    return
                current_node = current_node.left_child
            else:
                if current_node.right_child is None:
                    current_node.right_child = new_node
                    return
                current_node = current_node.right_child
        
    def find(self, value):
        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left_child
            elif value > current_node.right_child:
                current_node = current_node.right_child
            else:
                return True
        return False
    
    def __str__(self) -> str:
        return str(self.root)
    
    def __traversal_pre_order(self, root):
        # Base condition
        if not root:
            return
        print(root.value)
        self.__traversal_pre_order(root.left_child)
        self.__traversal_pre_order(root.right_child)

    def __traversal_in_order(self, root):
        # Base condition
        if not root:
            return
        self.__traversal_in_order(root.left_child)
        print(root.value)
        self.__traversal_in_order(root.right_child)

    def __traversal_post_order(self, root):
        # Base condition
        if not root:
            return
        self.__traversal_post_order(root.left_child)
        self.__traversal_post_order(root.right_child)
        print(root.value)

    def __is_leaf(self, root):
        return (root.left_child is None) and (root.right_child is None)

    def __height(self, root):
        # base conditions
        if root is None:
            return -1
        if self.__is_leaf(root):
            return 0
        left_height = self.__height(root.left_child)
        right_height = self.__height(root.right_child)
        return 1 + max(left_height, right_height)
    
    def __min(self, root, binary_search_tree=False):
        if binary_search_tree:
            """ This algorithm for finding min value in 'binary search tree' 
            Here the time complexity gets O(log n), because we are traversing
            through only the left sub tree 
            """
            if root is None:
                raise ValueError("Empty tree found")
            current_node = root
            last = current_node
            while current_node:
                last = current_node
                current_node = current_node.left_child
            return last.value


        else:
            """ This algorithm for finding min value in 'binary tree'
            Here the time complexity gets O(n), because we are traversing
            through each node in the tree
            """
            if root is None:
                return float("inf")
            
            if self.__is_leaf(root):
                return root.value
            left_min = self.__min(root.left_child)
            right_min = self.__min(root.right_child)
            return min(min(left_min, right_min), root.value)


    def __equals(self, first, second) -> bool:
        if (first is None) and (second is None):
            return True
        elif (first is not None) and (second is not None):
            return (first.value == second.value) and \
                    self.__equals(first.left_child, second.left_child) and \
                    self.__equals(first.right_child, second.right_child)
        return False
        
    def __get_nodes_at_distance(self, root, distance: int, arr: list):
        if root is None:
            return
        
        if distance == 0:
            arr.append(root.value)
            return
        
        self.__get_nodes_at_distance(root.left_child, distance -1, arr)
        self.__get_nodes_at_distance(root.right_child, distance -1, arr)

        

    def swap_child(self):
        self.root.left_child, self.root.right_child = \
        self.root.right_child, self.root.left_child

    def traversal_pre_order(self):
        self.__traversal_pre_order(self.root)

    def traversal_in_order(self):
        self.__traversal_in_order(self.root)

    def traversal_post_order(self):
        self.__traversal_post_order(self.root)

    def traversal_level_order(self):
        for distance in range(self.height() + 1):
            for i in self.get_nodes_at_distance(distance):
                print(i)

    def height(self):
        return self.__height(self.root)
    
    def min(self):
        # return self.__min(self.root)
        return self.__min(self.root, binary_search_tree=True)
    
    def equals(self, other_tree) -> bool:
        if not isinstance(other_tree, BinarySearchTree):
            return False
        
        return self.__equals(self.root, other_tree.root)
    
    
    def get_nodes_at_distance(self, distance):
        arr = []
        self.__get_nodes_at_distance(self.root, distance, arr)
        return arr
    
# Binary tree instantiation
# tree = BinarySearchTree()

# Inserting new node
# tree.insert(7)
# tree.insert(4)
# tree.insert(9)
# tree.insert(1)
# tree.insert(6)
# tree.insert(10)
# tree.insert(8)

# print(tree.check_is_this_binary_tree())


# Checking if the node exist or not
# print(tree.find(11))


# Traversal using pre order
# tree.traversal_pre_order()
# print("----------")
# tree.traversal_in_order()
# print("----------")
# tree.traversal_post_order()

# getting the height of the tree
# print(tree.height())


# Getting the min value in the tree
# print(tree.min())
# print("")

# creating new tree for equivality checking
# tree1 = BinarySearchTree()
# tree1.insert(7)
# tree1.insert(4)
# tree1.insert(9)
# tree1.insert(1)
# tree1.insert(6)
# tree1.insert(10)
# tree1.insert(8)

# print(tree.equals(tree1))


# Checking the given binary tree is binary search tree
# print(tree.is_binary_search_tree())

# temporaly swapping the child 
# tree.swap_child()
# print(tree.is_binary_search_tree())

# getting nodes at distance 
# print(tree.get_nodes_at_distance(3))

# Traversal using level order
# tree.traversal_level_order()
# print("")