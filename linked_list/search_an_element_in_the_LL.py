"""

"""


from typing import Self

class Node:
    def __init__(self, data: int, next: Self|None = None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return f"{self.data} -> {self.next}"
    


def optimal_approach(head: Node, t: int) -> bool:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    while head:
        if head.data == t:
            return True
        head = head.next
        
    return False


if __name__ == "__main__":
    LL = Node(1)
    LL.next = Node(2)
    LL.next.next = Node(3)

    print(optimal_approach(LL, 3))
    print(optimal_approach(LL, 5))
