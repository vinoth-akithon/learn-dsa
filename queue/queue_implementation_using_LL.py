"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data: int) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        new_node = Node(data)
        if self.is_empty:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self) -> int:
        if self.is_empty:
            raise Exception("Queue is Empty")
        val = self._head.data
        self._head = self._head.next
        self._size -= 1
        return val

    def peek(self) -> int:
        if self.is_empty:
            raise Exception("Queue is Empty")
        return self._head.data

    @property
    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def __repr__(self):
        return f"{self._head}"

if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    # queue.enqueue(4)
    # queue.dequeue()

    # print(queue.peek())

    print(queue.is_empty)

    # print(queue)
