"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, prev: Self|None = None, next: Self|None = None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} <-> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data}"
    

def optimal_approach(head: Node, data: int) -> Node:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """


    tail = head
    while tail.next:
        tail = tail.next
    
    new_node = Node(data, prev=tail)
    tail.next = new_node

    return head



if __name__ == "__main__":
    DLL = Node(1)
    DLL.next = Node(2, prev=DLL)
    # DLL.next.next = Node(3, prev=DLL.next)

    print(DLL)
    print(optimal_approach(DLL, 4))
