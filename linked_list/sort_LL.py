"""

"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"


def brute_force(head: Node) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(2n + n log n)
            - Space -> O(n)
    
    """
    arr = []
    temp = head

    while temp:
        arr.append(temp.data)
        temp = temp.next

    arr.sort()
    temp = head
    
    for e in arr:
        temp.data = e
        temp = temp.next

    return head



if __name__ == "__main__":
    LL = Node(2)
    LL.next = Node(3)
    LL.next.next = Node(1)
    LL.next.next.next = Node(4)

    print(LL)
    print(brute_force(LL))
