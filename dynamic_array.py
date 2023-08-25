
class DynamicArray(object):
    """This class enables the tradition array"""

    def __init__(self, type_code: str, size: int, /) -> None:
        # check the 'type_code' is valid or not
        self.type_code = self.get_valid_type_code(type_code)
        # check the 'size' is integer object
        self.is_valid_integer(size, "size")
        self.array_size = size
        self.array = [None] * self.array_size
        self.filled_count = 0

    def __str__(self) -> str:
        return str(self.array[0: self.filled_count])
    
    def append_item(self, new_item) -> None:
        """This method is used to append a item into DynamicArray object"""
        # checking the type_code is same
        if not isinstance(new_item, self.type_code):
            raise ValueError(
                f"The 'new_item' parameter should be '{self.type_code}' object")
        # check the array is filled or not
        if self.filled_count == self.array_size: 
            self.array_size +=1
            self.array = self.array + [new_item]
            self.filled_count +=1
        else:
            self.array[self.filled_count] = new_item
            self.filled_count +=1
            
    def remove_item(self, index):
        """This method is used to remove a item from DynamicArray object"""
        if (index <0  or index >= self.filled_count):
            raise ValueError(f"The 'index' parameter should be in the range between the 0-{self.filled_count - 1}")
        
        if index != (self.filled_count - 1):
            for i in range(index, self.filled_count - 1):
                self.array[i] = self.array[i + 1]
        self.filled_count -= 1

    def search_item(self, item):
        """This method is used to search an item from DynamicArray object"""
        for i in range(self.filled_count):
            if self.array[i] == item:
                return 1
        return -1

    def get_valid_type_code(self, type_code):
        """This method is used to get the valid type_code object"""

        if not type_code in ("s", "i", "f"):
            raise ValueError(
                "The 'type_code' parameter should be either 's', 'i', 'f'")
        return str if type_code == "s" else int if type_code == "i" else float

    def is_valid_integer(self, value, parameter=""):
        """This methos is used to check the given object is int object."""

        if not isinstance(value, int):
            raise ValueError(
                f"The '{parameter}' parameter should be 'int' objet")


# array creation flow
array = DynamicArray("i", 3)

# append item
array.append_item(10)
array.append_item(20)
array.append_item(30)
array.append_item(40)
print(array)

# remove item
array.remove_item(3)
print(array)

# search item
print(array.search_item(200))