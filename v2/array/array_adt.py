from typing import Any
from abc import ABC, abstractmethod

class Array(ABC):
    """ ADT for array data structure."""

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

    @property
    @abstractmethod
    def length(self):
        """Return the count of filled slots of the array."""
        pass

    @property
    @abstractmethod
    def capacity(self):
        """Return the capacity of the array."""
        pass

    @abstractmethod
    def remove(self, index: int) -> Any:
        """Remove item at specified index"""
        pass
