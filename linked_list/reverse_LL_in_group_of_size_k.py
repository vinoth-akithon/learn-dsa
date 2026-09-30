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


def brute_force(head: Node, k: int) -> Node:
    """
        - Complexity Analysis:
            - Time -> O(n*k)
            - Space -> O(1)
    """
    dummy = dummy_tail = Node(0)
    start = tail = head
    cnt = 0

    while tail:
        cnt += 1
        if cnt != k and tail.next is None:
            dummy_tail.next = start
            tail = tail.next
        # If window not found, move forward
        elif cnt != k:
            tail = tail.next
        # If window found
        else:
            next_ = tail.next
            tail.next = None

            # Reverse the window (start -> tail)
            pre = None
            curr = start
            while curr:
                next__ = curr.next
                curr.next = pre

                pre = curr
                curr = next__

            # Add the reversed window to the dummy node
            dummy_tail.next = pre
            dummy_tail = start

            # reset to form new window
            cnt = 0
            start = tail = next_

    return dummy.next





if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(head)

    print(brute_force(head, 2))
