from __future__ import annotations

class Node:
    def __init__(self, data: int, next: Node|None = None) -> None:
        self.data = data
        self.next = next


def middle_node(head: Node) -> Node:
    slow = fast = head
    while (fast and fast.next):
        slow = slow.next
        fast = fast.next.next
    return slow.data



if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print(middle_node(head))