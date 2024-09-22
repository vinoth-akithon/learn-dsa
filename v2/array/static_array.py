from typing import Any
import unittest
from array_adt import Array


class StaticArray(Array):
    """Static array implementtion"""

    def __init__(self, size: int) -> None:
        """Create a new array of given size."""
        if size < 0:
            raise ValueError("Size should be greater than 0")
        self._capacity = size
        self._array = [None] * size
        self._length = 0

    def remove(self, index: int) -> Any:
        if index < 0 or index >= self._length:
            raise IndexError("Array out of range.")
        
        for i in range(index, self._length-1):
            self._array[i] = self._array[i+1]
        self._array[self.length-1] = None 
        self._length -= 1


    def insert(self, index: int, item: Any) -> None:
        if item is None:
            raise ValueError("Item cannot be None")
        elif index < 0:
            raise IndexError("Array out of range.")
        elif self._length == self.capacity:
            raise IndexError("Array is full.")
        elif index >= self._length:
            self._array[self._length] = item
        else:
            for j in range(self._length, index, -1):
                self._array[j]= self._array[j-1]
            self._array[index] = item
        self._length += 1
                      
    
    def update(self, index: int, item: Any) -> None:
        if index < 0 or index >= self._length:
            raise IndexError("Array out of range.")
        self._array[index] = item


    def get(self, index: int) -> Any:
        if index < 0 or index >= self._length:
            raise IndexError("Array out of range.")
        return self._array[index]

    
    @property
    def length(self):
        return self._length

    
    @property
    def capacity(self):
        return self._capacity
    
   
    def __iter__(self):
        self.current_item = 0
        return self

    def __next__(self):
        if self.current_item >= self.length:
            raise StopIteration()
        current_item = self.current_item
        self.current_item += 1
        return self._array[current_item]
    
    def __str__(self):
        result = "["
        for index, value in enumerate(self):
            if index+1 == self.length:
                result += f"{value}"
            else:
                result += f"{value}, "
        return result + "]"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return self._length

class TestCase(unittest.TestCase):
    def test_get(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.get, index=1)
        self.assertRaises(IndexError, arr.get, index=-1)

        arr.insert(0, 10)
        arr.insert(1, 20)
        self.assertEqual(arr.get(1), 20)
        self.assertRaises(IndexError, arr.get, index=-2)
        self.assertRaises(IndexError, arr.get, index=2)


    def test_remove(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.remove, index=-1)
        self.assertRaises(IndexError, arr.remove, index=100)
        self.assertRaises(IndexError, arr.remove, index=0)

        arr.insert(0, 10)
        arr.insert(1, 20)
        arr.insert(2, 30)
        arr.insert(3, 40)
        arr.remove(3)
        self.assertEqual(arr.length, 3)
        self.assertEqual(arr.get(2), 30)

        arr.remove(2)
        self.assertEqual(arr.length, 2)
        self.assertRaises(IndexError, arr.get, index=2)
        self.assertEqual(arr.get(1), 20)


    def test_update(self):
        arr = StaticArray(4)
        self.assertEqual(arr.length, 0)
        self.assertRaises(IndexError, arr.update, index=-1, item=100)
        self.assertRaises(IndexError, arr.update, index=0, item=100)

        arr.insert(0, 10)
        arr.update(0, 20)
        self.assertEqual(arr.get(0), 20)
        self.assertEqual(arr.length, 1)


    def test_insert(self):
        arr = StaticArray(4)
        self.assertRaises(IndexError, arr.insert, index=-1, item=100) 

        arr.insert(0, 20) 
        self.assertEqual(arr.length, 1)

        arr.insert(0, 10) 
        self.assertEqual(arr.length, 2)
        # self.assertEqual(arr.get(0), 10)

        arr.insert(2, 30) 
        arr.insert(3, 40) 
        self.assertRaises(IndexError, arr.insert, index=3, item=40) 
        self.assertRaises(IndexError, arr.insert, index=1, item=20) 

        # arr2 = StaticArray(2)
        # arr2.insert(100, 10) # Attempt to insert at an index greater than the capacity.

        self.assertRaises(ValueError, arr.insert, index=0, item=None)

        # arr.insert(2, 20)
        # self.assertEqual(arr.length, 2)
        # self.assertEqual(arr.get(1), 20)

        # arr.insert(0, 100)
        # arr.insert(1, 200)
        # self.assertEqual(arr.length, 4)
        # self.assertEqual(arr.get(0), 100)
        # self.assertEqual(arr.get(1), 200)
        # self.assertEqual(arr.get(2), 10)
        # self.assertEqual(arr.get(3), 20)


    def test_length(self):
        arr = StaticArray(4)
        arr.insert(0, 10)
        arr.insert(1, 20)

        self.assertEqual(arr.length, 2)

    
    def test_capacity(self):
        arr = StaticArray(4)
        self.assertEqual(arr.capacity, 4)
        

    def test_traversal(self):
        arr = StaticArray(4)
        arr.insert(0, 40)
        arr.insert(0, 30)
        arr.insert(0, 20)
        arr.insert(0, 10)

        for index, value in enumerate(arr):
            expected = [10, 20, 30, 40]
            self.assertEqual(expected[index], value)
    


if __name__ == "__main__":
    unittest.main()
