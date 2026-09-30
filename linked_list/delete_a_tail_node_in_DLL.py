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
    

def optimal_approach(head: Node) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if not head or not head.next:
        return None


    prev = head
    curr = head.next

    while (curr.next):
        prev = curr
        curr = curr.next

    curr.prev = None
    prev.next = None

    return head



if __name__ == "__main__":
    DLL = Node(1)
    DLL.next = Node(2, prev=DLL)
    DLL.next.next = Node(3, prev=DLL.next)

    print(DLL)
    print(optimal_approach(DLL))