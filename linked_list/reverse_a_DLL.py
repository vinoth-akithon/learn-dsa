"""

"""

from typing import Self, Optional

class Node:
    def __init__(self, data: int, next: Optional[Self] = None, prev: Optional[Self] = None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    
    def __repr__(self) -> str:
        return f"{self.data} -> {self.next}"
    
def brute_force(head: Node) -> Node:
    """
        - Using Auxiliary DS (stack) for copying the data of each nodes
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(n)
    """
    stack = []

    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next

    temp = head
    while temp:
        temp.data = stack.pop()
        temp = temp.next

    return head

def optimal_approach(head: Node) -> Node:
    """
        - Using Pointer manipulation
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    curr = head
    prev = None

    while curr:
        prev = curr.prev
        curr.prev, curr.next = curr.next, curr.prev
        curr = curr.prev

    if prev:
        head = prev.prev
    return head



if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)

    head.next.prev = head
    head.next.next.prev = head.next

    print(head)
    # print(brute_force(head))
    print(optimal_approach(head))
