from array.static_array import StaticArray


class PriorityQueueUsingArray(object):

    def __init__(self, type_code, size) -> None:
        self.__static_array = StaticArray(type_code, size)
        self.__queue_size = 0

    def enqueue(self, new_item):
        if self.__queue_size == self.__static_array.array_size:
            raise AssertionError("Queue gets filled")
        if self.is_empty():
            self.__static_array.insert_item(self.__queue_size, new_item)
        else:
            for i in range(self.__queue_size - 1, -1, -1):
                print(i)
                current_item = self.__static_array.array[i]
                print(current_item)
                if current_item > new_item:
                    self.__static_array.array[i+1] = current_item
                else:
                    self.__static_array.array[i+1] = new_item
                    break
        self.__queue_size +=1

    # def dequeue(self):
    #     if self.is_empty():
    #         raise AssertionError("queue is empty")
        
    #     deletable_item = self.__static_array.array[self.__front]
    #     self.__static_array.update_item(self.__front, None, True)
    #     self.__front = (self.__front + 1) % self.__static_array.array_size
    #     self.__queue_size -=1
    #     return deletable_item

    def peek(self):
        pass

    def is_empty(self):
        return self.__queue_size == 0

    def size(self):
        pass

    def __str__(self) -> str:
        return str(self.__static_array.to_list())
        

queue = PriorityQueueUsingArray("i", 5)
# print(queue)

# enqueue operation
queue.enqueue(10)
queue.enqueue(5)
# queue.enqueue(50)
# queue.enqueue(70)

# print(queue)
# queue.enqueue(20)
print(queue)

# dequeue operation
# print(queue.dequeue())
# print(queue.dequeue())
# print(queue)

# print("-----------------")
# queue.enqueue(60)
# print(queue)


