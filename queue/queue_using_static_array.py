import sys, os

# Add the root directory to the Python path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)


from custom_array.static_array import StaticArray



class QueueUsingStaticArray(object):

    def __init__(self, type_code, size) -> None:
        self.__front = 0
        self.__rear = 0
        self.__queue_size = 0
        self.__static_array = StaticArray(type_code, size)

    def get_queue(self):
        return self.__static_array.to_list()[self.__front:self.__rear]

    def enqueue(self, item) -> None:
        if self.__queue_size == self.__static_array.array_size:
            raise AssertionError("Queue gets filled")
        
        self.__static_array.insert_item(self.__rear, item)
        self.__rear = (self.__rear + 1) % self.__static_array.array_size
        self.__queue_size += 1

    def dequeue(self):
        if self.__queue_size == 0:
            raise AssertionError("Queue is empty")
        
        deleted_obj = self.__static_array.get_item(self.__front)
        self.__static_array.update_item(self.__front, None, True)
        self.__front = (self.__front + 1) % self.__static_array.array_size
        self.__queue_size -= 1
        return deleted_obj

    def peek(self):
        if self.__queue_size == 0:
            raise AssertionError("Queue is empty")
        return self.__static_array.array[self.__front]

    def size(self):
        return self.__queue_size

    def is_empty(self):
        return self.__queue_size == 0
    
    def is_full(self):
        return self.__queue_size == self.__static_array.array_size

    def __str__(self):
        return str(self.__static_array.to_list())
    

# instantiate the queue object
queue = QueueUsingStaticArray("i", 5)
# print(queue)

# adding an item to the queue
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
# queue.enqueue(40)
# queue.enqueue(50)
# queue.enqueue(60)
print(queue)

# removing an item from the queue
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue.dequeue())
print(queue)
# queue.dequeue()


# peeking the first item from the queue
print(queue.peek())
print(queue)



# print(queue)