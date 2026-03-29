"""

"""

from typing import Self

class Node:
    def __init__(self, data:tuple[int, str], next: Self|None =None) -> None:
        self.data = data
        self.next = next

    def __repr__(self) -> str:
        return f"data: {self.data}"

class LL:
    def __init__(self, node: Node) -> None:
        self.head = node
        self.tail = node


class HashMap:
    def __init__(self) -> None:
        self.arr: list[LL|None] = [None] * 10

    def hash(self, key: int) -> int:
        return key % 10

    def put(self, key: int, value: str) -> None:
        index = self.hash(key)
        if self.arr[index]:
            ll: LL = self.arr[index]
            new_node = Node((key, value))
            ll.tail.next = new_node
            ll.tail = new_node
        else:
            node = Node((key, value))
            ll = LL(node)
            self.arr[index] = ll

    def get(self, key: int) -> str|None:
        node = self._get_node(key)
        if node:
            return node.data[1]
        
    def _get_node(self, key: int) -> Node|None:
        index = self.hash(key)
        ll = self.arr[index]
        if ll:
            node = ll.head
            while (node):
                if node.data[0] == key:
                    return node
                node = node.next


    def remove(self, key: int) -> None:
        index = self.hash(key)
        ll = self.arr[index]
        if ll:
            p = None
            c = ll.head
            while (c):
                if c.data[0] == key:
                    if c is ll.head:
                        ll.head = ll.head.next
                    else:
                        p.next = c.next
                    return
                p = c
                c = c.next
        raise KeyError("Key Not Found")

    # test case
    # empty -> directly handled by the array itself
    # only head -> [3] (in -> 3)
    # removing head -> [3] -> [2] -> [1] (in -> 3)
    #                   ^
    #                   |
    # removing tail -> [3] -> [2] -> [1] (in -> 1)
    #                                 ^
    #                                 |
    # removing middle -> [3] -> [2] -> [1] (in -> 2)
    #                            ^
    #                            |
    # no match found -> [3] -> [2] -> [1] (in -> 5)


if __name__ == "__main__":
    hashmap = HashMap()
    hashmap.put(1, "vinoth")
    hashmap.put(11, "aravind")
    print(hashmap.get(11))
    # print(hashmap.get(13))
    hashmap.remove(1)
    # hashmap.remove(1)
    print(hashmap.get(1))
