from typing import Any


class Array:
    """ ADT for array data structure."""

    def create(self, size: int, type: Any) -> None:
        """Create a new array of given size and data type."""
        pass

    def get(self, index: int) -> Any:
        """Get the element at given index."""
        pass

    def set(self, index: int, value: Any) -> None:
        """Set the element at givent index."""
        pass

    def length(self):
        """Return the size of the array."""
        pass


class StaticArray(Array):
    """Static array implementtion"""

    def __init__(self) -> None:
        self.array = None
        self.array_capacity = 0
        self.array_size = 0

    def create(self, size: int, type: Any=None) -> None:
        self.array = [0 for _ in range(size)]
        self.array_capacity = size

    def length(self):
        return self.array_size
    
    def get(self, index: int) -> Any:
        if 0 <= index < self.array_capacity:
            return self.array[index]
        raise IndexError("array index out of range")
    
    def set(self, index: int, value: Any) -> None:
        if 0 <= index < self.array_capacity:
            if self.array_size < self.array_capacity:
                previous_value = self.array[index]
                if previous_value == 0:
                    self.array[index] = value
                    self.array_size += 1
                else:
                    next_available_index = 0
                    for i in range(index+1, self.array_capacity):
                        if self.array[i] == 0:
                            next_available_index = i
                    for j in range(next_available_index, index, -1):
                        self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
                    self.array[index] = value
                return
            else:
                raise IndexError("array capacity exceeds")
        raise IndexError("array index out of range")
    
    def __iter__(self):
        return iter(self.array)
    
    # def __str__(self):
    #     return " -> ".join(self.array)
    


if __name__ == "__main__":
    arr = StaticArray()
    arr.create(4)
    # print(arr.length())
    # print(arr.get(1))
    # print(arr.get(10))
    for i in arr:
        print(i, end=" ")
    print()

    arr.set(0, 1)
    arr.set(1, 10)
    arr.set(2, 3)
    arr.set(0, 2)


    for i in arr:
        print(i, end=" ")
