"""

"""

from typing import Any, Generic, TypeVar

T = TypeVar("T")

class ArrayQueue(Generic[T]):
    def __init__(self, capacity=1000):
        self._capacity = capacity
        self._front = 0
        self._rear = 0
        self._list: list[T|None] = [None] * self._capacity
        self._size = 0

    def enqueue(self, data: T) -> None:
        if self.is_full:
            raise Exception("Queue is Full")
        self._list[self._rear] = data
        self._rear = (self._rear + 1) % self._capacity

        self._size += 1

    def dequeue(self) -> T:
        if self.is_empty:
            raise Exception("Queue is Empty")
        # if self._list[self._front] is not None:
        data = self._list[self._front]
        self._list[self._front] = None
        self._front = (self._front + 1) % self._capacity

        self._size -= 1
        return data

    def peek(self) -> T:
        if self.is_empty:
            raise Exception("Queue is Empty")
        return self._list[self._front]

    @property
    def is_full(self) -> bool:
        return self.size == self._capacity

    @property
    def is_empty(self) -> bool:
        return self.size == 0

    def __repr__(self):
        return str(self._list)

    @property
    def size(self) -> int:
        return self._size

    
if __name__ == "__main__":
    queue = ArrayQueue[int](5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)


    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()
    # queue.dequeue()

    queue.enqueue(6)

# 

    print(queue)
