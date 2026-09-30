"""

"""
from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None):
        self.data = data
        self.next = next

    def __str__(self) -> str:
            return f"{self.data} -> {self.next}"
        
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"



class Stack:
    def __init__(self):
        self.head = None
        self._size = 0

    def push(self, data: int) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size += 1

    def pop(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")

        data = self.head.data
        self.head = self.head.next
        self._size -= 1
        return data

    def top(self) -> int:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Stack is Empty")

        return self.head.data

    @property
    def is_empty(self) -> bool:
        return self._size == 0


    def __repr__(self):
        return f"{self.head}"


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)

    print(stack)
    print(stack.top())
    print(stack.pop())
    # print(stack.pop())
    print(stack.top())


