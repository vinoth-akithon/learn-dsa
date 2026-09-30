"""

"""


from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    


def optimal_approach(head: Node) -> Node:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if not head or not head.next:
        return None
    
    pre = head
    curr = head.next

    while (curr.next is not None):
        pre = curr
        curr = curr.next
    
    pre.next = None

    return head


if __name__ == "__main__":
    LL = Node(1)
    # LL.next = Node(2)
    # LL.next.next = Node(3)

    print(LL)
    print(optimal_approach(LL))
