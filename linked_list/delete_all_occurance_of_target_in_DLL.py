"""
"""

from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None, prev: Self|None=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

    def __str__(self) -> str:
        return f"{self.data} <-> {self.next}"

    
    def __repr__(self) -> str:
        return f"{self.data} <-> {self.next}"


def brute_force(head: Node, t: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    temp = head

    while temp:
        if temp.data == t:
            prev = temp.prev
            next_ = temp.next

            if temp is head:
                head = head.next
            elif temp.next is None:
                prev.next = None
            else:
                prev.next = next_
                next_.prev = prev

        temp = temp.next

    return head


if __name__ == "__main__":
    head = Node(1)

    head.next = Node(2, prev=head)

    head.next.next = Node(3, prev=head.next)
    head.next.next.next = Node(1, prev=head.next.next)
    head.next.next.next.next = Node(4, prev=head.next.next.next)

    print(head)

    print(brute_force(head, 1))