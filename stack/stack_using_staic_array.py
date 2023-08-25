from array.static_array import StaticArray


class StackUsingStaticArray(object):

    def __init__(self, type_code: str, size: int) -> None:
        self.__stack_size = 0
        self.__static_array = StaticArray(type_code, size)

    def push(self, item) -> None:
        if self.__stack_size == self.__static_array.array_size:
            raise ValueError("Stack Overflow")

        self.__static_array.insert_item(self.__stack_size, item)
        self.__stack_size += 1

    def pop(self):
        if self.__stack_size == 0:
            raise ValueError("Stack Underflow")

        # popped_obj = self.__static_array.delete_item(self.__stack_size - 1)
        popped_obj = self.__static_array.to_list()[self.__stack_size - 1]
        self.__static_array.update_item(self.__stack_size - 1, None, True)
        self.__stack_size -= 1
        return popped_obj

    def peek(self):
        if self.__static_array.array_size == 0:
            raise ValueError("Stack Underflow")
        
        return self.get_stack()[self.__stack_size - 1]

    def is_empty(self) -> bool:
        return self.__stack_size == 0
    
    def is_full(self) -> bool:
        return self.__stack_size == self.__static_array.array_size
    
    def size(self) -> int:
        return self.__stack_size
    
    def get_stack(self):
        return self.__static_array.to_list()[0: self.__stack_size]
    
    def to_list(self):
        return self.__static_array.to_list()[0: self.__stack_size]

    def __str__(self):
        return str(self.__static_array.to_list())


# stack = StackUsingStaticArray("i", 5)
# print(stack)

# pushing a object into stack
# stack.push(10)
# stack.push(20)
# stack.push(30)
# stack.push(40)
# stack.push(50)
# stack.push(60)

# print(stack)

# pop top object from stack
# print(stack.pop())
# print(stack.pop())
# stack.push(30)
# print(stack)
# get the top object without removing
# print(stack.peek())
# print(stack)

# get the size of the stack
# print(stack.size())

# check the stack is empty
# print(stack.is_empty())
