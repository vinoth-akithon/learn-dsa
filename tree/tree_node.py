"""This module having the tree node object"""

class Node:
    def __init__(self, value, left_child=None, right_child=None) -> None:
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self) -> str:
        return f"Node={self.value}"
    
    def __repr__(self) -> str:
        return f"Node={self.value}"