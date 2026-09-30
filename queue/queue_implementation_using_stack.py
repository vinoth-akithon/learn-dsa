"""
"""

from typing import TypeVar, Generic


T = TypeVar("T")

class Queue(Generic[T]):
    def __init__(self):
        self._items = []
        self._size = 0

    def enqueue(self, data: T) -> None:
        """
            - Complexity Analysis:
                - Time -> O(n)
                - Space -> O(n)
        """
        auxiliary_stack = []
        for _ in range(self._size):
            auxiliary_stack.append(self._items.pop())

        self._items.append(data)
        for _ in range(self._size):
            self._items.append(auxiliary_stack.pop())

        self._size += 1

    def dequeue(self) -> T:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Queue is Empty")
        
        self._size -= 1
        return self._items.pop()

    def peek(self) -> T:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        if self.is_empty:
            raise Exception("Queue is Empty")
        return self._items[-1]

    @property
    def is_empty(self) -> bool:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return self._size == 0

    def __repr__(self):
        return f"{self._items}"

class EfficientQueue(Generic[T]):
    def __init__(self):
        self._input_stack = []
        self._output_stack = []

    def enqueue(self, data: T) -> None:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        self._input_stack.append(data)

    def dequeue(self) -> T:
        """
            - Complexity Analysis:
                - Time -> O(n)
                - Space -> O(n)
        """
        if self.is_empty:
            raise Exception("Queue is Empty")
        
        if not self._output_stack:
            for _ in range(len(self._input_stack)):
                self._output_stack.append(self._input_stack.pop())

        return self._output_stack.pop()

    def peek(self) -> T:
        """
            - Complexity Analysis:
                - Time -> O(n)
                - Space -> O(n)
        """
        if self.is_empty:
            raise Exception("Queue is Empty")
        
        if not self._output_stack:
            for _ in range(len(self._input_stack)):
                self._output_stack.append(self._input_stack.pop())
        
        return self._output_stack[-1]

    @property
    def is_empty(self) -> bool:
        """
            - Complexity Analysis:
                - Time -> O(1)
                - Space -> O(1)
        """
        return not self._input_stack and not self._output_stack

    def __repr__(self):
        return f"{self._output_stack}"



if __name__ == "__main__":
    # queue = Queue()
    queue = EfficientQueue()


    queue.enqueue(1)
    queue.enqueue(2)
    # queue.enqueue(30)
    print(queue.peek())


    print(queue.dequeue())
    print(queue.dequeue())
    # print(queue.dequeue())
    # print(queue.dequeue())

    # print(queue.peek())


    print(queue)
