from typing import Any
from abc import ABC, abstractmethod
import unittest


class Array(ABC):
    """ ADT for array data structure."""

    @abstractmethod
    def __init__(self, size: int) -> None:
        """Create a new array of given size."""
        self.size = size
        self.array = [None] * size
        self.item_count = 0

    @abstractmethod
    def insert(self, index:int, item: Any) -> None:
        """Insert an element into the array."""
        pass

    @abstractmethod
    def update(self, index: int, item: Any) -> None:
        """Update an item with the new value in the specified index."""
        pass

    @abstractmethod
    def get(self, index: int) -> Any:
        """Get the element at given index."""
        pass

    @abstractmethod
    def length(self):
        """Return the size of the array."""
        pass

    def remove(self, index: int) -> Any:
        """Remove item at specified index"""
        pass


class StaticArray(Array):
    """Static array implementtion"""

    def __init__(self, size: int) -> None:
        super().__init__(size)

    def print_array(self):
        for i in range(self.item_count):
            print(self.array[i])

    def remove(self, index: int) -> Any:
        if 0 <= index < self.item_count:
            pass
        else:
            raise IndexError("Array out of range.")

    def insert(self, index: int, item: Any) -> None:
        if 0 <= index < self.size and self.item_count < self.size:
            next_available_slot = [i for i in range(index, self.size) if self.array[i] is None][0]
            for j in range(next_available_slot, index, -1):
                self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
            self.array[index] = item
            self.item_count += 1           
        else:
            raise IndexError("Array out of range.")
    
    def update(self, index: int, item: Any) -> None:
        if 0 <= index < self.size:
            if self.array[index] is None:
                self.item_count += 1
            self.array[index] = item
        else:
            raise IndexError("Array out of range.")

    def get(self, index: int) -> Any:
        if 0 <= index < self.item_count:
            return self.array[index]
        raise IndexError("Array out of range.")
    
    def length(self):
        return self.item_count
    
    # def create(self, size: int, type: Any=None) -> None:
    #     self.array = [0 for _ in range(size)]
    #     self.array_capacity = size

    # def length(self):
    #     return self.array_size
    
    # def get(self, index: int) -> Any:
    #     if 0 <= index < self.array_capacity:
    #         return self.array[index]
    #     raise IndexError("array index out of range")
    
    # def set(self, index: int, value: Any) -> None:
    #     if 0 <= index < self.array_capacity:
    #         if self.array_size < self.array_capacity:
    #             previous_value = self.array[index]
    #             if previous_value == 0:
    #                 self.array[index] = value
    #                 self.array_size += 1
    #             else:
    #                 next_available_index = 0
    #                 for i in range(index+1, self.array_capacity):
    #                     if self.array[i] == 0:
    #                         next_available_index = i
    #                 for j in range(next_available_index, index, -1):
    #                     self.array[j], self.array[j-1] = self.array[j-1], self.array[j]
    #                 self.array[index] = value
    #             return
    #         else:
    #             raise IndexError("array capacity exceeds")
    #     raise IndexError("array index out of range")
    
    # def __iter__(self):
    #     return iter(self.array)
    
    # def __str__(self):
    #     return " -> ".join(self.array)


class TestCase(unittest.TestCase):
    def test_get(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.get, index=1)

        arr.update(0, 10)
        arr.update(1, 20)
        self.assertEqual(arr.get(1), 20)
        self.assertRaises(IndexError, arr.get, index=-2)
        self.assertRaises(IndexError, arr.get, index=2)


    def test_remove(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.remove, index=-1)
        self.assertRaises(IndexError, arr.remove, index=100)
        self.assertRaises(IndexError, arr.remove, index=0)




    def test_update(self):
        arr = StaticArray(4)
        self.assertEqual(arr.length(), 0)
        self.assertRaises(IndexError, arr.update, index=-1, item=100)
        self.assertRaises(IndexError, arr.update, index=4, item=100)

        arr.update(0, 10)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.length(), 1)



    def test_insert(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.insert, index=-1, item=100)
        self.assertRaises(IndexError, arr.insert, index=4, item=100)

        arr.insert(0, 10)
        arr.insert(1, 20)
        self.assertEqual(arr.get(1), 20)

        arr.insert(0, 100)
        self.assertEqual(arr.get(0), 100)
        self.assertEqual(arr.get(1), 10)
        self.assertEqual(arr.get(2), 20)
        self.assertEqual(arr.length(), 3)

        arr.insert(3, 40)
        self.assertEqual(arr.get(3), 40)






    def test_length(self):
        arr = StaticArray(4)
        arr.update(0, 10)
        arr.update(1, 20)

        self.assertEqual(arr.length(), 2)
        

        # arr = StaticArray(1)
        # self.assertEqual(arr.length(), 1)

        # arr = StaticArray(5)
        # self.assertEqual(arr.length(), 4)
    


if __name__ == "__main__":
    # arr = StaticArray(4)
    # arr.print_array()
    unittest.main()