from stack_using_staic_array import StackUsingStaticArray


class QueueUsingStack(object):

    def __init__(self, type_code, size):
        self.__enqueue_stack = StackUsingStaticArray(type_code, size)
        self.__dequeue_stack = StackUsingStaticArray(type_code, size)

    def enqueue(self, item) -> None:
        self.__enqueue_stack.push(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        self.move_objects_from_enqueue_to_dequeue_stack()
        return self.__dequeue_stack.pop()

    def is_empty(self):
        return self.__enqueue_stack.size() == 0 and self.__dequeue_stack.size() == 0

    def size(self):
        return self.__enqueue_stack.size()

    def peek(self):
        if self.is_empty():
            raise ValueError("Queue is empty")
        
        self.move_objects_from_enqueue_to_dequeue_stack()
        return self.__dequeue_stack.peek()

    def move_objects_from_enqueue_to_dequeue_stack(self):
        if self.__dequeue_stack.is_empty:
            for _ in range(self.__enqueue_stack.size()):
                self.__dequeue_stack.push(self.__enqueue_stack.pop())

    def to_list(self):
        return self.__enqueue_stack.to_list()

    def __str__(self):
        return str(self.to_list())
        # return str(self.__enqueue_stack.__str__())


queue = QueueUsingStack("i", 3)
# print(queue)

# adding a object to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
# queue.enqueue(30)

# print(queue)

# removing a object to the queue
print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
print(queue.dequeue())
# queue.enqueue(60)

# print(queue)

# Getting first serve object from queue
# print(queue.peek())
# print(queue)

# print(queue.to_list())
