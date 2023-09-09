from heap_using_array import Heap


class PriorityQueueUsingHeap(object):
    def __init__(self) -> None:
        self.__heap = Heap()

    def __repr__(self) -> str:
        return str(self.__heap)
    
    def __len__(self) -> int:
        return self.__heap.heap_size
    
    def is_empty(self) -> bool:
        return self.__len__() == 0
    
    def enqueue(self, value: int) -> None:
        self.__heap.insert(value)
    
    def dequeue(self) -> int:
        return self.__heap.remove()



prio_queue = PriorityQueueUsingHeap()

# Enqueue operation
prio_queue.enqueue(10)
prio_queue.enqueue(5)
prio_queue.enqueue(17)
prio_queue.enqueue(4)
prio_queue.enqueue(22)
prio_queue.enqueue(23)
print(prio_queue)

# Dequeue operaion
print(prio_queue.dequeue())
print(prio_queue)

# checkig the queue is empty
# print(prio_queue.is_empty())