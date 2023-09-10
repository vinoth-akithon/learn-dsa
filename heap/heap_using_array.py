"""
Heap Data structure implementation using array
"""


class Heap(object):
    def __init__(self):
        self.__heap_array = []

    def __repr__(self) -> str:
        return str(self.__heap_array)
    
    @property
    def heap_size(self):
        return self.__heap_array.__len__()
    
    def __is_empty(self):
        return self.heap_size == 0
    
    def __get_left_child_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return (parent_index * 2) + 2

    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2
    
    def __get_left_child_value(self, parent_index):
        return self.__heap_array[self.__get_left_child_index(parent_index)]
    
    def __get_right_child_value(self, parent_index):
            return self.__heap_array[self.__get_right_child_index(parent_index)]
        
    def __has_left_child(self, current_index):
        return self.__get_left_child_index(current_index) < self.heap_size
    
    def __has_right_child(self, current_index):
        return self.__get_right_child_index(current_index) < self.heap_size
    
    def __arrange_heap(self, first, second) -> None:
        self.__heap_array[first], self.__heap_array[second] = \
            self.__heap_array[second], self.__heap_array[first]
        
    def __bubble_up(self):
        current_index = self.heap_size - 1
        parent_index = self.__get_parent_index(current_index)
        while current_index > 0 and (self.__heap_array[current_index] > \
                                     self.__heap_array[parent_index]):
            self.__arrange_heap(current_index, parent_index)
            current_index = parent_index
            parent_index = self.__get_parent_index(current_index)

    def __bubble_down(self):
        index = 0
        while (index < self.heap_size) and \
                not self.__is_valid_parent(index):
            largest_child_index = self.__get_largest_child_index(index)
            self.__arrange_heap(largest_child_index, index)
            index = largest_child_index    

    
    def  __is_valid_parent(self, index):
        if not self.__has_left_child(index):
            return True
        
        if not self.__has_right_child(index):
            return ( self.__heap_array[index] >= self.__get_left_child_value(index) )

        return ( self.__heap_array[index] >= self.__get_left_child_value(index) ) and \
                    ( self.__heap_array[index] >= self.__get_right_child_value(index) )

    def __get_largest_child_index(self, index):
        if not self.__has_left_child(index):
            return index
        
        if not self.__has_right_child(index):
            return self.__get_left_child_index(index)
        
        if self.__get_left_child_value(index) > \
            self.__get_right_child_value(index):
            largest_child_index = self.__get_left_child_index(index)
        else:
            largest_child_index = self.__get_right_child_index(index)
        return largest_child_index
    
    def insert(self, value: int) -> None:
        # appending new value to the heap
        self.__heap_array.append(value)
        self.__bubble_up()
        
    def remove(self) -> int:
        if self.__is_empty():
            raise ValueError("Heap is Empty!")
        
        removed_value = self.__heap_array.pop(0)
        if self.heap_size:
            self.__heap_array.insert(0, self.__heap_array.pop())
            self.__bubble_down()
        return removed_value
    
    def max(self) -> int:
        """It will return max value in the heap"""
        if self.heap_size == 0:
            raise ValueError("Heap is empty!")
        return self.__heap_array[0]


# heap = Heap()
# heap.insert(10)
# heap.insert(5)
# heap.insert(17)
# heap.insert(4)
# heap.insert(22)
# heap.insert(23)

# print(f"Initail Heap: {heap}")
# print(heap.remove())
# print(f"Final Heap: {heap}")
