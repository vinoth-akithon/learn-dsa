
"""
    Create a linked list and perform certain operation on them
"""


from typing import Any


class _Node(object):
    def __init__(self, value: Any) -> None:
        self.value = value
        self.next = None

    def __repr__(self) -> str:
        return f"Node={self.value}"


class LinkedList(object):
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.__size = 0
        self.size = self.__size

    def add_last(self, item: Any) -> None:
        node = _Node(item)
        if self.__is_empty():
            self.first = self.last = node
        else:
            self.last.next = node
            self.last = node
        self.__size += 1

    def add_first(self, item: Any) -> None:
        node = _Node(item)
        if self.__is_empty():
            self.first = self.last = node
        else:
            node.next = self.first
            self.first = node
        self.__size += 1

    def index_of(self, item: Any) -> int:
        index, current_node = 0, self.first
        while current_node:
            if current_node.value == item:
                return index
            else:
                current_node = current_node.next
                index += 1
        return -1

    def contains(self, item: Any) -> bool:
        return self.index_of(item) != -1

    def remove_first(self) -> None:
        if self.first:
            if self.first.next:
                second = self.first.next
                self.first.next = None
                self.first = second
            else:
                self.first = self.last = None
            self.__size -= 1

    def remove_last(self) -> None:
        if self.last:
            if self.first is self.last:
                self.first = self.last = None
            else:
                previous_node = self.__get_previous_node(self.last)
                self.last = previous_node
                previous_node.next = None
            self.__size -= 1

    def remove(self, item: Any):
        if self.first == self.last:
            if self.first.value is item:
                return item
        current_node = self.first
        while current_node:
            if current_node.value is item:
                previous_node = self.__get_previous_node(current_node)
                previous_node.next = current_node.next
                return item
            current_node = current_node.next
        return 


    def size(self) -> int:
        return self.__size

    def to_list(self) -> list:
        list_object = list()
        current_node = self.first
        while current_node:
            list_object.append(current_node.value)
            current_node = current_node.next
        return list_object

    def __get_previous_node(self, node) -> _Node:
        current_node = self.first
        while current_node:
            if current_node.next is node:
                return current_node
            current_node = current_node.next

    def __is_empty(self) -> bool:
        return False if self.first else True

    def reverse(self) -> None:
        if self.first:
            previous_node = self.first
            current_node = self.first.next
            while current_node:
                next_node = current_node.next
                current_node.next = previous_node
                previous_node = current_node
                current_node = next_node

            self.last = self.first
            self.first = previous_node
            self.last.next = None

    def get_kth_node_from_end(self, k: int) -> _Node:
        if not self.first:
            raise AssertionError("The linked list has no nodes")

        pointer_1 = pointer_2 = self.first
        for _ in range(k-1):
            pointer_2 = pointer_2.next
            if not pointer_2:
                raise ValueError(
                    f"'k' value should be less than or equal to {self.__size}")

        while pointer_2 != self.last:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next

        return pointer_1.value
    
    def __str__(self):
        return str(self.to_list())


# Instantiate LinkedList object
# linked_list = LinkedList()

# adding a node at last
# linked_list.add_last(1)
# linked_list.add_last(2)
# linked_list.add_last(3)
# linked_list.add_last(4)
# linked_list.add_last(5)


# adding a node at begining
# linked_list.add_first(11)
# linked_list.add_first(22)
# linked_list.add_first(33)

# getting the linked list size
# print(linked_list.size())


# getting the index of node
# print(linked_list.index_of(22))

# checking is the item(node) availabilty
# print(linked_list.contains(22))

# removing a node at begining
# linked_list.remove_first()

# removing a node at last
# linked_list.remove_last()

# converting LinkedList object into list object
# print(linked_list.to_list())

# reversing the linkedlist
# linked_list.reverse()
# print(linked_list.to_list())

# finding the Kth node from the end
# print(linked_list.get_kth_node_from_end(-1))
