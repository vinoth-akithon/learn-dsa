
from __future__ import annotations

class Node:
    def __init__(self, data: int, next: Node|None = None) -> None:
        self.data = data
        self.next = next


def has_cycle(head: Node) -> bool:
    slow = fast = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False


if __name__ == "__main__":
    head = Node(3)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(-2)
    head.next.next.next.next = head.next

    print(has_cycle(head))