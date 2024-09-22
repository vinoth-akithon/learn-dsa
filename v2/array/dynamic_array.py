import unittest
from typing import Any
from static_array import StaticArray

class DynamicArray(StaticArray):
    """Dynamic array implementation."""

    def __init__(self, size: int=0) -> None:
        super().__init__(size)

    def resize(self):
        if self._length == self._capacity: # for growing
            self._capacity = self._capacity * 2 if self._capacity else 1
        elif self._length*2 == self._capacity: # for shirnking
            self._capacity = self._length


    def insert(self, index: int, item: Any) -> None:
        if index < 0:
            raise IndexError("Array index out of range.")
        elif self._length == self._capacity:
            self.resize()
            new_array = []
            for _ in range(self._capacity):
                new_array.append(None)
            
            for i in range(self._length):
                new_array[i] = self._array[i]
            
            self._array = new_array

        if index < self._length:
            for i in range(self._length, index, -1):
                self._array[i] = self._array[i-1]
            self._array[index] = item
        else:   
            self._array[self._length] = item
        self._length += 1

    
    def remove(self, index: int) -> Any:
        if index < 0 or index >= self._length:
            raise IndexError("Array index out of range.")
        elif index == self._length-1:
            print("Insert at end")
            self._array[index] = None
        else:
            for i in range(index, self._length-1):
                self._array[i] = self._array[i+1]
            self._array[self._length-1] = None

        self._length -= 1
        self.resize()


class TestCase(unittest.TestCase):
    def test_insert(self):
        self.assertRaises(ValueError, DynamicArray, size=-1) 

        arr = DynamicArray(0)
        self.assertEqual(arr.length, 0)
        arr.insert(1, 10)
        self.assertEqual(arr.length, 1)
        self.assertEqual(arr.get(0), 10)

        arr = DynamicArray(1)
        self.assertRaises(IndexError, arr.insert, index=-1, item=100) 

        arr.insert(0, 10)
        self.assertEqual(arr.length, 1)
        self.assertEqual(arr.get(0), 10)

        arr.insert(1, 20)
        self.assertEqual(arr.length, 2)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)

        arr.insert(1, 30)
        self.assertEqual(arr.length, 3)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 30)
        self.assertEqual(arr.get(2), 20)

        arr.insert(0, 100)
        self.assertEqual(arr.length, 4)
        self.assertEqual(arr.get(0), 100)
        self.assertEqual(arr.get(1), 10)
        self.assertEqual(arr.get(2), 30)
        self.assertEqual(arr.get(3), 20)


    def test_update(self):
        arr = DynamicArray()
        self.assertEqual(arr.length, 0)
        self.assertRaises(IndexError, arr.update, index=-1, item=100)
        self.assertRaises(IndexError, arr.update, index=0, item=100)

        arr.insert(0, 10)
        arr.update(0, 20)
        self.assertEqual(arr.length, 1)
        self.assertEqual(arr.get(0), 20)


    def test_get(self):
        arr = DynamicArray(4)
        self.assertRaises(IndexError, arr.get, index=1)
        self.assertRaises(IndexError, arr.get, index=-1)

        arr.insert(0, 10)
        arr.insert(1, 20)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertRaises(IndexError, arr.get, index=-2)
        self.assertRaises(IndexError, arr.get, index=2)


    def test_remove(self):
        arr = DynamicArray()
        self.assertRaises(IndexError, arr.remove, index=-1)
        self.assertRaises(IndexError, arr.remove, index=100)
        self.assertRaises(IndexError, arr.remove, index=0)

        arr.insert(0, 10)
        arr.insert(1, 20)
        arr.insert(2, 30)
        arr.insert(3, 40)
        arr.remove(3)
        self.assertEqual(arr.length, 3)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 20)
        self.assertEqual(arr.get(2), 30)

        arr.remove(1)
        self.assertEqual(arr.length, 2)
        self.assertEqual(arr.get(0), 10)
        self.assertEqual(arr.get(1), 30)
        self.assertEqual(arr.capacity, 2)
        

        # arr.remove(2)
        # self.assertEqual(arr.length, 2)
        # self.assertRaises(IndexError, arr.get, index=2)
        # self.assertEqual(arr.get(1), 20)


    def test_length(self):
        arr = DynamicArray()
        arr.insert(0, 10)
        arr.insert(1, 20)

        self.assertEqual(arr.length, 2)
        arr.remove(0)
        self.assertEqual(arr.length, 1)


    def test_traversal(self):
        arr = DynamicArray()
        arr.insert(0, 40)
        arr.insert(0, 30)
        arr.insert(0, 20)
        arr.insert(0, 10)

        for index, value in enumerate(arr):
            expected = [10, 20, 30, 40]
            self.assertEqual(expected[index], value)


if __name__ == "__main__":
    unittest.main()