"""

"""
import sys
import os
from typing import TypeVar, Generic
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


from learn_dsa.queue.queue_implementation_using_array import ArrayQueue



T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self, capacity: int = 1000):
        self._capacity = capacity
        self._items = ArrayQueue(capacity)

    def push(self, data: T) -> None:
        try:
            self._items.enqueue(data)
            queue_size = self._items.size
            
            for _ in range(queue_size -1):
                self._items.enqueue(self._items.dequeue())
        except:
            raise Exception("Stack is Full")

    def pop(self) -> T:
        try:
            return self._items.dequeue()
        except:
            raise Exception("Stack is Empty")

    def top(self) -> T:
        if self.is_empty:
            raise Exception("Stack is Empty")
        return self._items.peek()
            
    @property
    def is_empty(self) -> bool:
        return self._items.size == 0

    @property
    def is_full(self) -> bool:
        return self._items.size == self._capacity

    def __repr__(self) -> None:
        return f"{self._items}"

if __name__ == "__main__":
    stack = Stack[int](5)
    # print(stack._items)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    # stack.push(6)


    print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.pop())

    print(stack.top())


    print(stack)
