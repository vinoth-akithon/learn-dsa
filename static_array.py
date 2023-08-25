

"""
    - Create a array class
    - Should accept size and datatype
    - Implement accessibility of an element from it
    - Implement insertion of an element to it
    - Implement deletion of an element from it
    - Implement update for replacing existing element with new one
    - Enable traversal for iterating all the elemnts

    
"""


class StaticArray(object):
    """This class enables the tradition array"""

    def __init__(self, type_code: str, size: int, /) -> None:
        # check the 'type_code' is valid or not
        self.type_code = __class__.get_valid_type_code(type_code)
        # check the 'size' is integer object
        self.is_valid_integer(size, "size")
        self.array_size = size
        self.array = [None] * self.array_size

    def __str__(self) -> str:
        return str(self.array)
    
    def to_list(self):
        return self.array

    def get_valid_type_code(type_code):
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

    def traversal_items(self):
        """This method is used to iterate all the items in StaticArray obejct"""

        for item in self.array:
            print(item, end=" ")
        print('\r')

    def is_index_exist(self, index):
        """This method is used to check the index is exist in the StaticArray object"""

        # check the 'index' is integer object
        self.is_valid_integer(index, "index")
        if not ((index >= 0) and (index < len(self.array))):
            raise ValueError(
                f"The 'index' parameter should be in the range between the 0-{len(self.array) - 1}")
        return True

    def get_item(self, index):
        """This method is used to get an item from StaticArray obejct"""

        # check the requested index is exist
        if self.is_index_exist(index):
            return self.array[index]

    def update_item(self, index: int, new_item, clear_momory=False):
        """This method is used to update an item new value into StaticArray obejct"""

        if not clear_momory:
            # checking the type_code is same
            if not isinstance(new_item, self.type_code):
                raise ValueError(
                    f"The 'new_item' parameter should be '{self.type_code}' object")
        if self.is_index_exist(index):
            self.array[index] = new_item

    def delete_item(self, index: int):
        """This method is used to remove an item from StaticArray obejct"""

        # check the requested index is exist
        if self.is_index_exist(index):
            if index != len(self.array) - 1:
                deletable_item = self.array[index]
                for i in range(index, len(self.array)-1):
                    self.array[i] = self.array[i+1]
            self.array[-1] = None
            return deletable_item

    def insert_item(self, index: int, new_item):
        """This method is used to insert an item into StaticArray obejct"""

        # checking the type_code is same
        if not isinstance(new_item, self.type_code):
            raise ValueError(
                f"The 'new_item' parameter should be '{self.type_code}' object")
        if self.is_index_exist(index):
            if index != len(self.array) - 1:
                if self.array[index]:
                    for i in range(len(self.array) - 1, index, -1):
                        self.array[i] = self.array[i - 1]
            self.array[index] = new_item


# array creation flow
# array = StaticArray("s", 3)
# print(array)

# array traversal flow
# array.traversal_items()

# array access flow
# print(array.get_item(2))

#  array update flow
# array.update_item(0, "vinoth")
# array.update_item(1, "kumar")
# array.update_item(2, "aki")
# array.update_item(3, "aki")

# print(array)

# array delete flow
# array.delete_item(1)
# print(array)


# array insert flow
# array.insert_item(0, "veeram")
# array.insert_item(1, "ajith")
# print(array)
